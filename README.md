Simple server application written using [nanodjango](https://nanodjango.readthedocs.io/en/latest/) which is a single file approach to using Django. Rewrite of earlier project where Django project structure did not feel right.

Allows uploading and downloading files with `API_TOKEN` set in `.env` or as environment variable.

# API usage example

```
# Upload file
curl -X POST http://localhost:8000/api/upload -F 'file=@myfile.txt'

# Download file
curl -H 'Authorization: Bearer <API_TOKEN>' http://localhost:8000/api/download\?file\=myfile.txt
```

# Installing and running

Clone repository and install dependencies stated in `pyproject.toml` and run `nanodjango run server.py`. Server should start in port 8000.


Usage example with [uv](https://github.com/astral-sh/uv) which is a new Python environment manager tool by ruff team written in rust:

```
# Install uv
# curl -LsSf https://astral.sh/uv/install.sh | sh

cp .env.example .env  # and edit it or alternatively set AUTH_TOKEN env var

uv sync
uv run nanodjango run server.py
```

Documentation here is in progress and has not been tested on another machine yet.
