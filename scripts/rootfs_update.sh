#!/bin/bash
echo 1
PARAMS=""

while (( "$#" )); do
  echo "derp"
  case "$1" in
    -c|--deploy_config)
      DEPLOY_CONFIG=$2
      echo $DEPLOY_CONFIG
      shift 2
      ;;
    --) # end argument parsing
      shift
      break
      ;;
    -*|--*=) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      exit 1
      ;;
    *) # preserve positional arguments
      PARAMS="$PARAMS $1"
      shift
      ;;
  esac
done