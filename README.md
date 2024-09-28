# Installing and running
Clone repository and install dependencies stated in `pyproject.toml` and run `nanodjango run server.py`.

Usage example with [uv](https://github.com/astral-sh/uv) which is a new Python environment manager tool by ruff team written in rust.

```
# Install uv
# curl -LsSf https://astral.sh/uv/install.sh | sh

cp .env.example .env  # and edit it or alternatively set AUTH_TOKEN env var

uv sync
uv run nanodjango run server.py
```

# API usage example

```
# Upload file
curl -X POST http://localhost:8000/api/upload -F 'file=@myfile.txt'

# Download file
curl -H 'Authorization: Bearer <API_TOKEN>' http://localhost:8000/api/download\?file\=myfile.txt
```
