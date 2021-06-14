#!/bin/csh

set SCRIPT=`basename $0`
set ROOT=$1

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

set CASE=$ROOT/case
set ENV=$ROOT/env
set LIB=$ROOT/lib
set SIM=$ROOT/sim
set SRC=$ROOT/src
set TOOL=$ROOT/tool

function check_directory() {
	set DIR=$1
	if [ ! -d $DIR ]; then
		echo "$DIR must exist!"
		exit 1
	fi
}

check_directory $CASE
check_directory $ENV
check_directory $LIB
check_directory $SIM
check_directory $SRC
check_directory $TOOL
