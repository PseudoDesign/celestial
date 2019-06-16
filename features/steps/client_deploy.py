from behave import *
import subprocess
from features import utils
import os

use_step_matcher("re")


@when("we run the rootfs_update.sh console script")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    script = os.path.join(utils.SCRIPTS_DIR, "rootfs_update.sh")
    try:
        context.celestial_rootfs_install_result = subprocess.run([
            "/bin/bash",
            "-c",
            script,
            '--deploy_config {}'.format(context.sample_deploy_config_file),
            '--cmdline {}'.format(context.sample_cmdline_file),
            '--dev {}'.format(context.rootfs_device_node_dir),
            '--fs_format {}'.format(context.rootfs_format),
            context.rootfs_file,
        ])
    except ValueError as e:
        context.celestial_rootfs_install_result = e
