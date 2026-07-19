#! /usr/bin/env bash

if [ $# -ne 1 ]
then
  echo "usage: $0 <target>"
  exit 1
fi

TARGET=$1
echo "running: $TARGET"
./targets/$TARGET/run.bash

