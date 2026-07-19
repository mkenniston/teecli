#! /usr/bin/env bash

FAILS=0
for CMD in shellcheck racket python ruff; do
  if RES=$(command -v $CMD); then
    echo "found $RES"
  else
    echo "Tool \"$CMD\" is not found.  It must be installed."
    FAILS=1
  fi
done

if [ $FAILS -eq 0 ]; then
  echo "All tools found, all required packages are present."
fi
exit $FAILS

