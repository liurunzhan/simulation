#!/bin/sh

SCRIPT=`basename $0`
ROOT=$1

if [ "-help" = "$ROOT" ] || [ "-h" = "$ROOT" ] || [ "--help" = "$ROOT" ] || [ "--h" = "$ROOT" ]; then
  echo "$SCRIPT supports one or none command line argument"
	echo "use '$SCRIPT root_dir' to check whether current project structure matches the needs or not"
	echo "if no root_dir is given, the checked directory is the current one"
	exit 0
elif [ "-" = "${ROOT:0:1}" ]; then
	echo "no other optional command line arguments are supported"
	echo "use '$SCRIPT -help/-h/--help/--h' to get document of $SCRIPT"
	exit 1
elif [ -z $ROOT ]; then
	ROOT=.
fi

CASE=$ROOT/case
ENV=$ROOT/env
LIB=$ROOT/lib
SIM=$ROOT/sim
SRC=$ROOT/src
