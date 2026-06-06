# Docker — Complete Learning Series

> A structured, in-depth series covering Docker from first principles to production-ready patterns.
> Written for engineers who want to understand not just *how* but *why*.

---

## Repository Structure

```
Docker/
├── Docker Guide/       ← Step-by-step learning series (17 files)
├── Docker Projects/    ← Real-world project examples
└── README.md           ← This file
```

---

## Prerequisites

| Requirement | Why |
|-------------|-----|
| Windows 10 / 11 | This series targets Windows-based setup |
| Basic command-line familiarity | You will type commands in PowerShell / terminal |
| Understanding of what an application is | No Docker experience required |

No prior knowledge of containers, Linux, or DevOps is assumed.

---

## Learning Series — Docker Guide

| # | Topic | What You Will Learn |
|---|-------|---------------------|
| [01](Docker%20Guide/01.%20Overview%20of%20Docker.md) | Overview of Docker | What Docker is, the problem it solves, containers vs VMs, the OS directory misconception, Docker on Windows vs Linux |
| [02](Docker%20Guide/02.%20Install%20Docker%20on%20Windows.md) | Install Docker on Windows | Docker Desktop setup, WSL 2, first container, troubleshooting |
| [03](Docker%20Guide/03.%20Docker%20Architecture.md) | Docker Architecture | Client, Daemon, Registry, how they communicate, Linux namespaces and cgroups |
| [04](Docker%20Guide/04.%20Docker%20Images.md) | Docker Images | Image layers, all image commands (`pull`, `build`, `tag`, `push`, `save`, `load`, `inspect`, `history`, `prune`) |
| [05](Docker%20Guide/05.%20Docker%20Containers.md) | Docker Containers | Full container lifecycle, every container command (`run`, `exec`, `logs`, `inspect`, `stats`, `cp`, `commit`, `update`) |
| [06](Docker%20Guide/06.%20Dockerfile.md) | Dockerfile | Every instruction (`FROM`, `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, `ADD`, `ENV`, `ARG`, `EXPOSE`, `WORKDIR`, `USER`, `VOLUME`, `LABEL`, `HEALTHCHECK`, `SHELL`, `ONBUILD`), `.dockerignore`, real-world examples |
| [07](Docker%20Guide/07.%20Docker%20Volumes.md) | Docker Volumes | Named volumes, bind mounts, tmpfs, backup and restore, Compose integration |
| [08](Docker%20Guide/08.%20Docker%20Networks.md) | Docker Networks | Bridge, host, none, overlay, macvlan, all network commands, DNS, port mapping |
| [09](Docker%20Guide/09.%20Docker%20Compose.md) | Docker Compose | Full `compose.yml` reference, all compose commands, `.env` files, multi-file overrides |
| [10](Docker%20Guide/10.%20Docker%20Hub%20and%20Registry.md) | Docker Hub & Registry | `login`, `push`, `pull`, `tag`, `search`, private registry setup |
| [11](Docker%20Guide/11.%20Docker%20System%20and%20Cleanup.md) | System & Cleanup | `system df`, `system prune`, `system info`, `system events`, builder cache, full disk cleanup |
| [12](Docker%20Guide/12.%20Docker%20Logs%20and%20Debugging.md) | Logs & Debugging | `logs`, `inspect`, `exec`, `stats`, `events`, debugging crash scenarios, logging drivers |
| [13](Docker%20Guide/13.%20Docker%20Environment%20Variables.md) | Environment Variables | `-e`, `--env-file`, `ENV` vs `ARG`, Compose env methods, secrets, best practices |
| [14](Docker%20Guide/14.%20Docker%20Resource%20Management.md) | Resource Management | CPU limits (`--cpus`, `--cpu-shares`, `--cpuset-cpus`), memory limits, OOM behavior, live monitoring |
| [15](Docker%20Guide/15.%20Docker%20Security%20Best%20Practices.md) | Security Best Practices | Non-root user, read-only filesystem, capability dropping, secrets, image scanning, seccomp |
| [16](Docker%20Guide/16.%20Docker%20Multi-Stage%20Builds.md) | Multi-Stage Builds | Build stages, `COPY --from`, size optimization, Node/Go/Python/React examples, build cache |
| [17](Docker%20Guide/17.%20Docker%20Commands%20Reference.md) | Commands Reference | Every command explained — why the name, what it does, every flag, examples, visualizations, quick decision guide |

---

## Real-World Projects — Docker Projects

Hands-on projects that apply the concepts from the guide.

| # | Project | Stack | Concepts Covered |
|---|---------|-------|-----------------|
| [01](Docker%20Projects/01.%20Node.js%20API%20%2B%20MySQL/) | Node.js REST API + MySQL | Node.js, Express, MySQL | Compose, custom network, volumes, env vars, health checks |
| [02](Docker%20Projects/02.%20Python%20Flask%20%2B%20Redis/) | Python Flask API + Redis | Python, Flask, Redis | Compose, caching pattern, depends_on, named volumes |
| [03](Docker%20Projects/03.%20React%20%2B%20Node.js%20%2B%20MongoDB/) | Full Stack Web App | React, Node.js, MongoDB | Multi-stage build, three-tier architecture, networks |
| [04](Docker%20Projects/04.%20WordPress%20%2B%20MySQL/) | WordPress Blog | WordPress, MySQL, Nginx | Bind mounts, production-ready setup, reverse proxy |
| [05](Docker%20Projects/05.%20Nginx%20Reverse%20Proxy/) | Nginx Reverse Proxy | Nginx, Node.js × 3 | Load balancing, upstream, scaling with Compose |

---

## Key Concepts at a Glance

```mermaid
flowchart LR
    DF["📄 Dockerfile\n(recipe)"]
    IMG["🖼️ Image\n(mold)"]
    C1["📦 Container 1\n(running)"]
    C2["📦 Container 2\n(running)"]
    HUB[("☁️ Docker Hub\n(registry)")]

    DF -->|docker build| IMG
    IMG -->|docker run| C1
    IMG -->|docker run| C2
    IMG -->|docker push| HUB
    HUB -->|docker pull| IMG
```

| Term | One-Line Definition |
|------|---------------------|
| **Image** | A read-only, layered template for creating containers |
| **Container** | A running instance of an image — isolated, lightweight process |
| **Dockerfile** | Instructions for building a custom image |
| **Volume** | Persistent storage that survives container deletion |
| **Network** | How containers communicate with each other and the outside world |
| **Compose** | Tool to define and run multi-container applications from a single file |
| **Registry** | A server that stores and distributes images (e.g., Docker Hub) |

---

## Quick Command Reference

```bash
# ── Images ────────────────────────────────────────────────────
docker pull nginx:alpine              # Download an image
docker images                         # List all local images
docker rmi nginx                      # Remove an image
docker build -t my-app:1.0 .          # Build from Dockerfile

# ── Containers ────────────────────────────────────────────────
docker run -d -p 8080:80 --name web nginx   # Run in background
docker run -it ubuntu bash                  # Run interactive shell
docker ps                                   # List running containers
docker ps -a                                # List all containers
docker stop web                             # Stop a container
docker rm web                               # Remove a container
docker exec -it web bash                    # Open shell in container
docker logs -f web                          # Follow container logs

# ── Compose ───────────────────────────────────────────────────
docker compose up -d                  # Start all services
docker compose down                   # Stop and remove
docker compose logs -f                # Follow all logs

# ── Cleanup ───────────────────────────────────────────────────
docker system prune -a --volumes -f   # Remove all unused resources
docker system df                      # Show disk usage
```

---

## How to Use This Series

1. Read **Docker Guide** files in order — concepts build on each other
2. Run every command yourself — reading is not enough
3. Build each **Docker Project** after completing the related guide sections
4. Use [17. Docker Commands Reference](Docker%20Guide/17.%20Docker%20Commands%20Reference.md) as your daily lookup guide

---

## Resources & Links

| Resource | Link |
|----------|------|
| Docker Official Docs | [docs.docker.com](https://docs.docker.com) |
| Docker Hub | [hub.docker.com](https://hub.docker.com) |
| Chocolatey Setup | [docs.chocolatey.org/en-us/choco/setup](https://docs.chocolatey.org/en-us/choco/setup/) |
| Learn With Irfan | [learnwithirfan.com](https://learnwithirfan.com) |
| VisitToMe | [visittome.com](https://visittome.com) |

---

> Start here → [01. Overview of Docker](Docker%20Guide/01.%20Overview%20of%20Docker.md)
