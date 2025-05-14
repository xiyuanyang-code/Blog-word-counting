#!/bin/zsh

REPO_DIR="$HOME/Hodgepodge/Blog-word-counting"
MARKER_FILE=~/.last_push_date

if [[ ! -f "$MARKER_FILE" || $(date +%Y-%m-%d) != $(cat "$MARKER_FILE") ]]; then
    cd "$REPO_DIR" || exit 1
    # run the bash scripts, but not outputting anything
    bash src/run.sh

    if git status --porcelain | grep -q '^ M\|^M \|^A \|^D \|^\?\?'; then
        git add .
        git commit -m "Auto-commit-update: $(date +'%Y-%m-%d %H:%M:%S')"
    fi

    if git push >/dev/null 2>&1; then
        date +%Y-%m-%d >"$MARKER_FILE"
    else
        echo "[Auto-Push] Failed to push. Will retry later."
    fi
fi