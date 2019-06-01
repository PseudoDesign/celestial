from behave import *
import celestial


@when("we query the boot rootfs device")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.boot_rootfs_device_result = celestial.client.rootfs.get_boot_device(
        cmdline_file=context.sample_cmdline_file
    )


@then("the reported boot rootfs device is {expected_result}")
def step_impl(context, expected_result):
    """
    :param expected_result:
    :type context: behave.runner.Context
    """
    assert context.boot_rootfs_device_result == expected_result
