import sys

from celestial_tools.client import dual_rootfs_update


def dual_rootfs_update_cmdline():
    """
    Runs dual_rootfs_update from the cmdline, parsing the provided sys.argv
    :return:
    """
    dual_rootfs_update(sys.argv[1:])


# Run the program when this file is executed
if __name__ == "__main__":
    dual_rootfs_update_cmdline()
