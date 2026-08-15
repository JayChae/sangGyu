#!/bin/bash
# Local preview: ./serve.sh [port]   (default 8000)
cd "$(dirname "$0")"
exec python3 scripts/serve.py "$@"
