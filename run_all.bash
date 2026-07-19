#! /usr/bin/env bash

for TARGET in `ls targets`
do
  ./run_one.bash $TARGET
done

