#!/bin/bash

set -e

PARAMS=()

DEFAULT_DEPLOY_CONFIG="/etc/celestial/deploy_config.yml"
DEFAULT_CMDLINE_FILE="/boot/cmdline"
DEFAULT_DEV_DIRECTORY="/dev"

DEPLOY_CONFIG=${DEFAULT_DEPLOY_CONFIG}
CMDLINE_FILE=${DEFAULT_CMDLINE_FILE}
FS_FORMAT=""
DEV_DIRECTORY=${DEFAULT_DEV_DIRECTORY}

print_help () {
    echo "Celestial dual-rootfs update"
    echo "  Usage:"
    echo "    $0 [Options] rootfs_file"
    echo "  Parameters:"
    echo "    rootfs_file             -   the rootfs file to be installed"
    echo "  Options:"
    echo "    -c --deploy_config      -   the config file describing where to find the needed parameters, default is $DEFAULT_DEPLOY_CONFIG"
    echo "    -cl --cmdline_file      -   the boot partition's cmdline file, default is $DEFAULT_CMDLINE_FILE"
    echo "    -fs --fs_format         -   enforce the provided filesystem format"
    echo "    -d --dev_directory      -   the directory containing the device nodes, default is $DEFAULT_DEV_DIRECTORY"
    echo "    -h --help               -   display this help message"
}

while (( "$#" )); do
  case "$1" in
    -c|--deploy_config)
      DEPLOY_CONFIG=$2
      shift 2
      ;;
    -cl|--cmdline_file)
      CMDLINE_FILE=$2
      shift 2
      ;;
    -fs|--fs_format)
      FS_FORMAT=$2
      shift 2
      ;;
    -d|--dev_directory)
      DEV_DIRECTORY=$2
      shift 2
      ;;
    -h|--help)
      print_help
      exit 1
      ;;
    --) # end argument parsing
      shift
      break
      ;;
    -*|--*=) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      print_help
      exit 1
      ;;
    *) # preserve positional arguments
      PARAMS+=("$1")
      shift
      ;;
  esac
done

if [[ "${#PARAMS[@]}" -ne "1" ]]; then
    print_help
    exit 22
fi

