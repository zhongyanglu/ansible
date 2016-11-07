# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy

class Attribute:

    def __init__(
            self,
            isa=None,
            private=False,
            default=None,
            required=False,
            listof=None,
            priority=0,
            class_type=None,
            always_post_validate=False,
            inherit=True,
            force_parent=False,
        ):

        # the type of the field (string, bool, int, etc.)
        self.isa = isa
        # whether the value of the attribute is private
        self.private = private
        # the default value of the attribute, if not specified in the YAML
        self.default = default
        # if required and not set, an error will be raised
        self.required = required
        # if isa == 'list', this field can be used to control the types
        # of each element in the list for validation purposes
        self.listof = listof
        # the loading priority of the attribute
        self.priority = priority
        # the class type of the attribute when isa == 'class'
        self.class_type = class_type
        # whether or not the attribute should be post validated
        self.always_post_validate = always_post_validate
        # whether or not the attribute should be inherited from the parent
        self.inherit = inherit
        # force inheritence from the parent, even if _get_parent_attribute
        # is not found in the class
        self.force_parent = force_parent

        if default is not None and self.isa in ('list', 'dict', 'set'):
            self.default = deepcopy(default)
        else:
            self.default = default

    def __eq__(self, other):
        return other.priority == self.priority

    def __ne__(self, other):
        return other.priority != self.priority

    # NB: higher priority numbers sort first

    def __lt__(self, other):
        return other.priority < self.priority

    def __gt__(self, other):
        return other.priority > self.priority

    def __le__(self, other):
        return other.priority <= self.priority

    def __ge__(self, other):
        return other.priority >= self.priority


class FieldAttribute(Attribute):
    pass
