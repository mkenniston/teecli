#! /usr/bin/env bash

if ! ruff check; then
  exit 1
fi
cat tools/runtimes.tee tools/framework.tee \
    | racket -t tools/compiler.rkt \
    | targets/Python/runner.py

