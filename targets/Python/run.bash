#! /usr/bin/env bash

cat tools/runtimes.tee tools/framework.tee \
    | racket -t tools/compiler.rkt \
    | targets/Python/runner.py

