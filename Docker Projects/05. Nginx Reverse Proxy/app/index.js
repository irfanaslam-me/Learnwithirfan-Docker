const express = require('express');
const os = require('os');

const app = express();

app.get('/', (req, res) => {
  res.json({
    message: 'Hello from Docker Load Balancer demo!',
    // hostname is the container ID — proves which instance handled this request
    handled_by: os.hostname(),
    timestamp: new Date().toISOString(),
    client_ip: req.headers['x-forwarded-for'] || req.socket.remoteAddress,
  });
});

app.get('/health', (req, res) => res.json({ status: 'ok', instance: os.hostname() }));

app.listen(3000, () => console.log(`Instance ${os.hostname()} listening on port 3000`));
