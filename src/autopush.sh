#!/bin/bash

REPO_DIR="$HOME/Hodgepodge/Blog-word-counting"
MARKER_FILE=~/.last_push_date

if [[ ! -f "$MARKER_FILE" || $(date +%Y-%m-%d) != $(cat "$MARKER_FILE") ]]; then
    cd "$REPO_DIR" || exit 1

    # Run the bash script silently
    bash src/run.sh &> /dev/null

    # Check for changes and commit silently
    if git status --porcelain | grep -q '^ M\|^M \|^A \|^D \|^\?\?'; then
        git add . &> /dev/null
        git commit -m "Auto-commit-update: $(date +'%Y-%m-%d %H:%M:%S')" &> /dev/null
    fi

    # Push changes silently
    if git push &> /dev/null; then
        date +%Y-%m-%d >"$MARKER_FILE"
    else
        # Suppress echo output
        : # Do nothing (silent failure)
    fi
fi