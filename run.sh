#!/usr/bin/env bash
#
# Script name : run.sh
# Description : Sets up the virtualenv for running a flask development service
#               and starts the server

# Quit if anything fails
set -e

cd "$(dirname $0)"

f_RequireCmd() {
    local -r arg_cmd="$1"

    if ! command -v "$arg_cmd" &>/dev/null; then
        echo "Missing dependency: $arg_cmd" >&2
        exit 1
    fi
}

# Check dependencies
f_RequireCmd python3
f_RequireCmd pip3
f_RequireCmd virtualenv

echo "Activating virtualenv"
# Load or set up virtualenv
if [[ -f venv/bin/activate ]]; then
    source venv/bin/activate
else
    virtualenv -p python3 venv
    source venv/bin/activate
    pip3 install -r requirements.txt
fi

# Start the development server
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port 5000
