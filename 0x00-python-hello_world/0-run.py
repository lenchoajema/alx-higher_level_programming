#!/bin/bash

# Check if the PYFILE environment variable is set
if [ -z "$PYFILE" ]; then
    echo "Error: PYFILE environment variable is not set."
    exit 1
fi

# Check if the specified Python file exists
if [ ! -f "$PYFILE" ]; then
    echo "Error: Specified Python file '$PYFILE' does not exist."
    exit 1
fi

# Run the Python script
python "$PYFILE"
