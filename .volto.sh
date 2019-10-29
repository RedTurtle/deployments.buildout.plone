#!/bin/bash
# we want to exit on errors
set -e

VIRTUALENV_BIN=$(command -v virtualenv-2.7 || command -v virtualenv)
PYTHON=$(command -v python3.7 || command -v python)
"$VIRTUALENV_BIN" --no-site-packages -p "$PYTHON" .

# Let's enter the virtualenv
. bin/activate
./bin/pip install -r requirements.txt

# Now we have
echo -e "Please enter installation type ["dev" or "prod"]: \c"
read version

PYTHON=$(command -v python3.7 || command -v python)

if [ $version == "dev" ]; then
    ln -s profiles/development.cfg buildout.cfg
else
    ln -s profiles/production.cfg buildout.cfg
fi

VOLTO=VOLTO ./bin/buildout
