#! /usr/bin/env bash

ruff check
if [ $? -ne 0 ]
then
  exit 1
fi
cat tools/runtimes.tee tools/framework.tee \
    | racket -t tools/compiler.rkt \
    | targets/Python/runner.py

