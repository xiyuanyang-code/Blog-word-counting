#!/bin/bash
cd ../Blog-word-counting
python ./src/main.py
cat ./total.json | tail -5 | head -3
echo "Done!"

# add a simple version of auto-push
git add .
git commit -m "Upd: $(date '+%Y-%m-%d %H:%M:%S')"
git push

cd -
