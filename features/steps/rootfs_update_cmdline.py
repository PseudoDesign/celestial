from behave import *
from celestial_tools.client import dual_rootfs_update_cmdline


@when("the rootfs_update command line script is run")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    args = [
        "-c", context.sample_cmdline_file,
        "-f", context.rootfs_format,
        "-n1", context.rootfs_device_node_1,
        "-n2", context.rootfs_device_node_2,
    ]
    context.rootfs_update_retval = dual_rootfs_update_cmdline(args)
