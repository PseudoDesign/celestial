import argparse

from . import rootfs


def dual_rootfs_update_cmdline():
    """
    Runs a commandline program for updating a dual rootfs
    :return:
    """
    parser = argparse.ArgumentParser(description="Install/verify a dual-rootfs update")
    parser.add_argument()
