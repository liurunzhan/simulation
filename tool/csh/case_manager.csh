#!/bin/csh

set SCRIPT=`basename $0`
set ACTION=$1
set CASE_ROOT=$2
set MODULE=$3
set CASE=$4

if [ -z $ACTION ]; then
	echo "$SCRIPT only supports at least one command line arguments"
	echo "use '$SCRIPT help' to get all help document"
	exit 1
fi

create_new_case(){
	case_dir=$1
	module_name=$2
	case_name=$3
	if [ -z $case_name ]; then
	  echo "empty case name is given"
		exit 0
	fi
	echo "create a new case $case_name in module $module_name of directory $case_dir"
}

clean_new_case(){
	case_dir=$1
	module_name=$2
	case_name=$3
	if [ -z $case_name ]; then
	  echo "empty case name is given"
		exit 0
	fi
	echo "clean a case $case_name in module $modul_name of directory $case_dir"
}

if [ "create" = "$ACTION" ]; then
	create_new_case $CASE_ROOT $MODULE $CASE
elif [ "clean" = "$ACTION" ]; then
	clean_new_case $CASE_ROOT $MODULE $CASE
elif [ "help" = "$ACTION" ]; then
	echo "$SCRIPT [options]"
	echo "option : "
	echo "create :"
	echo "clean : "
	exit 0
fi
