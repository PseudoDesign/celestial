import argparse
import sys

from celestial_tools.client import rootfs


def dual_rootfs_update(args: [str]) -> int:
    """
    Runs a commandline program for updating a dual rootfs
    :type args: an array of strings dictating the commandline parameters
    :return: 0 on success, else a linux error code
    """
    parser = argparse.ArgumentParser(description="Install/verify a dual-rootfs update")
    parser.add_argument("--cmdline", type=str, default="/boot/cmdline", help="The boot partition's cmdline parameters file.")
    parser.add_argument("--format",
                        type=str, default=None, help="The type of filesystem used on this system.  Examples: ext2, ext4")
    parser.add_argument("--node1",
                        type=str, default="/dev/mmcblk0p1", help="rootfs1's partition device node")
    parser.add_argument("--node2",
                        type=str, default="/dev/mmcblk0p2", help="rootfs2's partition device node")
    parser.add_argument("new_rootfs", help="the new rootfs to install")
    parsed_args = parser.parse_args(args)
    rootfs.dual_boot_update(
        parsed_args.new_rootfs, parsed_args.node1, parsed_args.node2, parsed_args.cmdline, parsed_args.format
    )

    return 0


def dual_rootfs_update_cmdline():
    """
    Runs dual_rootfs_update from the cmdline, parsing the provided sys.argv
    :return:
    """
    dual_rootfs_update(sys.argv[1:])


# Run the program when this file is executed
if __name__ == "__main__":
    dual_rootfs_update_cmdline()
