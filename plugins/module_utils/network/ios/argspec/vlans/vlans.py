#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the ios_vlans module
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


class VlansArgs(object):
    """The arg spec for the ios_vlans module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "name": {"type": "str"},
                "vlan_id": {"required": True, "type": "int"},
                "mtu": {"type": "int"},
                "remote_span": {"type": "bool"},
                "state": {"type": "str", "choices": ["active", "suspend"]},
                "shutdown": {
                    "type": "str",
                    "choices": ["enabled", "disabled"],
                },
                "private_vlan": {
                    "type": "dict",
                    "options": {
                        "type": {
                            "type": "str",
                            "choices": ["primary", "community", "isolated"],
                        },
                        "associated": {
                            "type": "list",
                            "elements": "int",
                        },
                    },
                },
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "rendered",
                "parsed",
                "gathered",
            ],
            "default": "merged",
            "type": "str",
        },
    }
