#!/usr/bin/env sh

cat $1
python /main.py --path $1 >> $GITHUB_STEP_SUMMARY
echo $$GITHUB_STEP_SUMMARY