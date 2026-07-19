#! /usr/bin/env bash

if ! shellcheck ./*.bash ./*/*.bash ./*/*/*.bash; then
  exit 1
fi

ALL_TARGETS=$(ls targets)
for TARGET in $ALL_TARGETS; do
  ./run_one.bash "$TARGET"
done

