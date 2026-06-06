# Docker Complete Learning Series

A complete, step-by-step Docker series — from zero to production ready.

## Learning Path

| # | Topic | File |
|---|-------|------|
| 01 | What is Docker & Why Use It | [01. Overview of Docker.md](01.%20Overview%20of%20Docker.md) |
| 02 | Install Docker on Windows | [02. Install Docker on Windows.md](02.%20Install%20Docker%20on%20Windows.md) |
| 03 | Docker Architecture | [03. Docker Architecture.md](03.%20Docker%20Architecture.md) |
| 04 | Docker Images | [04. Docker Images.md](04.%20Docker%20Images.md) |
| 05 | Docker Containers | [05. Docker Containers.md](05.%20Docker%20Containers.md) |
| 06 | Dockerfile | [06. Dockerfile.md](06.%20Dockerfile.md) |
| 07 | Docker Volumes | [07. Docker Volumes.md](07.%20Docker%20Volumes.md) |
| 08 | Docker Networks | [08. Docker Networks.md](08.%20Docker%20Networks.md) |
| 09 | Docker Compose | [09. Docker Compose.md](09.%20Docker%20Compose.md) |
| 10 | Docker Hub & Registry | [10. Docker Hub and Registry.md](10.%20Docker%20Hub%20and%20Registry.md) |
| 11 | System & Cleanup Commands | [11. Docker System and Cleanup.md](11.%20Docker%20System%20and%20Cleanup.md) |
| 12 | Logs & Debugging | [12. Docker Logs and Debugging.md](12.%20Docker%20Logs%20and%20Debugging.md) |
| 13 | Environment Variables | [13. Docker Environment Variables.md](13.%20Docker%20Environment%20Variables.md) |
| 14 | Resource Management | [14. Docker Resource Management.md](14.%20Docker%20Resource%20Management.md) |
| 15 | Security Best Practices | [15. Docker Security Best Practices.md](15.%20Docker%20Security%20Best%20Practices.md) |
| 16 | Multi-Stage Builds | [16. Docker Multi-Stage Builds.md](16.%20Docker%20Multi-Stage%20Builds.md) |

## What You Will Learn

- What Docker is and how it solves real problems
- How to install and configure Docker on Windows
- Docker's internal architecture (Daemon, Client, Registry)
- Build, tag, push, and pull Docker Images
- Run, manage, inspect, and debug Containers
- Write Dockerfiles from scratch
- Persist data with Volumes and Bind Mounts
- Connect containers with Docker Networks
- Orchestrate multi-container apps with Docker Compose
- Push images to Docker Hub
- Monitor, clean, and secure Docker environments
- Optimize builds with Multi-Stage Builds

## Quick Reference

```bash
# Pull and run your first container
docker run hello-world

# Run nginx web server
docker run -d -p 8080:80 --name my-web nginx

# List running containers
docker ps

# List all images
docker images

# Build from Dockerfile
docker build -t my-app:1.0 .

# Run Docker Compose
docker compose up -d
```

---

> Start with [01. Overview of Docker.md](01.%20Overview%20of%20Docker.md)
