# Created by Adam at 6/5/2019
Feature: celestial_client_deploy
  Tests for the celestial client deploy container

  Scenario Outline: test dual_rootfs_update
    Given the sample deploy_config file test_config.yml
    And the sample cmdline file mmcblk0p1
    And a rootfs file formatted with ext3
    And the boot rootfs device is set to <boot_device_node>
    And the rootfs device nodes are named mmcblk0p1 and mmcblk0p2
    When we run the rootfs_update console script
    Then the rootfs file is burned into <expected_device_node>
    And the reported boot rootfs device is <expected_device_node>

    Examples:
    | boot_device_node | expected_device_node |
    | mmcblk0p1        | mmcblk0p2            |
    | mmcblk0p2        | mmcblk0p1            |
