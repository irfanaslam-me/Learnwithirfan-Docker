import os
import json
import time
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Connect to Redis using environment variable (set by Docker Compose)
cache = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'localhost'),
    port=int(os.environ.get('REDIS_PORT', 6379)),
    decode_responses=True
)

def cache_get(key):
    """Return cached value or None."""
    value = cache.get(key)
    return json.loads(value) if value else None

def cache_set(key, value, ttl=60):
    """Store value in cache with a TTL (seconds)."""
    cache.setex(key, ttl, json.dumps(value))


@app.route('/')
def index():
    return jsonify({
        'service': 'Flask + Redis Demo',
        'endpoints': ['/api/visits', '/api/data/users']
    })


@app.route('/api/visits')
def visits():
    """Simple visit counter stored in Redis."""
    count = cache.incr('visits')   # auto-creates key and increments
    return jsonify({'total_visits': count})


@app.route('/api/data/users')
def get_users():
    """
    Returns a list of users.
    First request: simulates a slow database query (2 seconds), stores in cache.
    Subsequent requests: returns instantly from Redis cache.
    TTL = 30 seconds.
    """
    CACHE_KEY = 'cache:users'
    cached = cache_get(CACHE_KEY)

    if cached:
        return jsonify({'source': 'cache (Redis)', 'data': cached})

    # Simulate an expensive DB query
    time.sleep(2)
    users = [
        {'id': 1, 'name': 'Irfan Aslam', 'role': 'Engineer'},
        {'id': 2, 'name': 'John Doe', 'role': 'Developer'},
        {'id': 3, 'name': 'Jane Smith', 'role': 'Designer'},
    ]

    cache_set(CACHE_KEY, users, ttl=30)
    return jsonify({'source': 'database (slow, cached for 30s)', 'data': users})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
