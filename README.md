# Sales Agent

Lightweight AI agent demo using FastAPI microservices and PostgreSQL. This repository contains an "agent" web service and a supporting Postgres MCP service.

## Repo structure

- `docker-compose.yml` - top-level compose for local services.
- `app/` - main agent service
  - `main.py` - FastAPI entrypoint
  - `api/` - API routes and models
  - `services/agent/` - agent service logic, prompts and assets
  - `google-credentials.json` - (optional) Google credentials used by the agent, if needed
  - `requirements.txt` - Python dependencies for the agent
- `mcp/` - minimal Postgres helper service and tooling
  - `postgres/` - postgres helper code
  - `requirements.txt` - Python dependencies for MCP tools
- `postgres/` - local DB init assets
  - `init.sql` - initialization SQL
  - `data.csv` - sample data used by init scripts

## Requirements

- Docker & Docker Compose (v2) installed
- Python 3.10+ (only required if running services locally without Docker)

## Quickstart (Docker)

Start both the agent and database services with Docker Compose:

```bash
# from project root
docker compose up --build
```

To run just the agent (if compose services are separated in your setup):

```bash
docker compose up agent
```

Logs and ports are defined in `docker-compose.yml`. The FastAPI agent typically exposes an HTTP API (see `app/main.py` and `app/api`).

## Local development (Python)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies for the agent service:

```bash
pip install -r app/requirements.txt
```

3. Run the agent locally:

```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. Start Postgres (if not using Docker) and ensure `init.sql` is applied.

## Configuration

- `app/google-credentials.json`: If the agent uses Google APIs, place your credentials file here and ensure the container mounts it (check `docker-compose.yml`).
- Database connection info is configured in `mcp/postgres/constants.py` and/or environment variables used in `docker-compose.yml`.

## Useful files

- [app/main.py](app/main.py) - application entrypoint
- [app/api/agent/routes.py](app/api/agent/routes.py) - agent API endpoints
- [app/services/agent/agent.py](app/services/agent/agent.py) - core agent logic and prompt handling
- [mcp/postgres/init.sql](postgres/init.sql) - SQL used to initialize DB

## Troubleshooting

- If containers fail to start, run `docker compose logs` and inspect the failing service:

```bash
docker compose logs agent
docker compose logs db
```

- If the agent cannot access Google APIs, confirm `google-credentials.json` is present and mounted into the container.

- If DB init fails, check `postgres/init.sql` and `mcp/postgres/constants.py` for connection parameters.

## Contributing

- Open issues for bugs or feature requests.
- For code changes, create a feature branch, add tests if appropriate, and open a PR.

## License

This repository contains example/demo code; add a LICENSE file to indicate terms if you plan to publish or reuse this project.

---

If you want, I can expand sections (API examples, endpoints list, environment variables) or add a minimal `Makefile` and a health-check example. Let me know which extras you'd like.