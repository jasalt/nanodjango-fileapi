Simple server application written using [nanodjango](https://nanodjango.readthedocs.io/en/latest/) which is a single file approach to using Django. Rewrite of an earlier project where full Django project structure did not feel right.

Application allows uploading and downloading files with authentication by `API_TOKEN` set in `.env` or as environment variable.

Original use case was to allow transferring CSV files from machine behind firewall to a public endpoint accessible by [Grafana Cloud Infinity Data Source](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/) to make it available on a dashboard.

# API usage example

```
# Upload file
curl -X POST http://localhost:8000/api/upload -F 'file=@myfile.txt'

# Download file
curl -H 'Authorization: Bearer <API_TOKEN>' http://localhost:8000/api/download\?file\=myfile.txt
```

# Installing and running

Clone repository and install dependencies stated in `pyproject.toml` and run `nanodjango run server.py`. Server should start listening on port 8000.

Usage example with [uv](https://github.com/astral-sh/uv) which is a new Python environment manager tool by ruff team written in rust:

```
# Install uv
# curl -LsSf https://astral.sh/uv/install.sh | sh

cp .env.example .env  # and edit it or alternatively set AUTH_TOKEN env var

uv sync
uv run nanodjango run server.py
```

Documentation here is in progress and has not been tested on another machine yet..

# TODO

- [ ] Test on another machine (may require adding `/static` dir to repo as is) and finish installation docs
- [ ] [Container with uv](https://docs.astral.sh/uv/guides/integration/docker/)
- [ ] [Caddy](https://caddyserver.com/) deployment
- [ ] [Coolify](https://coolify.io/) deployment as Dockerfile

# Known issues and used workarounds

Code violates PEP8 ([related django-ninja issue](https://github.com/vitalik/django-ninja/issues/1169)) and includes ignore rules for Ruff.
