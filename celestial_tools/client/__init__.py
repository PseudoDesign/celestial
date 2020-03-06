import argparse

from . import rootfs


def dual_rootfs_update_cmdline(args: [str]) -> int:
    """
    Runs a commandline program for updating a dual rootfs
    :type args: an array of strings dictating the commandline parameters
    :return: 0 on success, else a linux error code
    """
    parser = argparse.ArgumentParser(description="Install/verify a dual-rootfs update")
    parser.add_argument()
