from behave import *
import subprocess
from features import utils
import os

script = os.path.join(utils.SCRIPTS_DIR, "rootfs_update.sh")


@when("we run the rootfs_update.sh console script")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.celestial_rootfs_install_result = subprocess.run([
            "/bin/bash",
            "-c",
            script +
            ' --deploy_config {}'.format(context.sample_deploy_config_file) +
            ' --cmdline_file {}'.format(context.sample_cmdline_file) +
            ' --dev_directory {}'.format(context.rootfs_device_node_dir) +
            ' --fs_format {}'.format(context.rootfs_format) +
            " " + context.rootfs_file,
        ])
    except ValueError as e:
        context.celestial_rootfs_install_result = e
    return


@when("we run the rootfs_update.sh console script with {num_params} random parameters")
def step_impl(context, num_params):
    """
    :type context: behave.runner.Context
    :type num_params: str
    """
    params = ""
    for i in range(int(num_params)):
        params += " fake_param_{}".format(i)
    try:
        context.celestial_rootfs_install_result = subprocess.run([
            "/bin/bash",
            "-c",
            script +
            params,
        ])
    except ValueError as e:
        context.celestial_rootfs_install_result = e
    return


@step("the rootfs_update.sh script exits with return code {return_code}")
def step_impl(context, return_code):
    """
    :type context: behave.runner.Context
    :param return_code:
    """
    assert context.celestial_rootfs_install_result.returncode == int(return_code)
