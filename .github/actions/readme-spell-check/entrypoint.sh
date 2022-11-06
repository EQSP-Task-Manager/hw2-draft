#!/usr/bin/env sh

echo $1
python main.py --path $1 >> $GITHUB_STEP_SUMMARY