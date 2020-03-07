from behave import *
from celestial_tools.client.dual_rootfs_update import dual_rootfs_update


@when("the rootfs_update command line script is run")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    args = [
        "--cmdline", context.sample_cmdline_file,
        "--format", context.rootfs_format,
        "--node1", context.rootfs_device_node_1,
        "--node2", context.rootfs_device_node_2,
        context.rootfs_file
    ]
    context.rootfs_update_retval = dual_rootfs_update(args)


@step("the rootfs_update command line script returns {value}")
def step_impl(context, value):
    """
    :type context: behave.runner.Context
    """
    assert context.rootfs_update_retval == int(value)
