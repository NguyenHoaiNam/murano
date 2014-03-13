#    Copyright (c) 2014 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from muranoapi.engine import classes
from muranoapi.engine import helpers


@classes.classname('com.mirantis.murano.Object')
class SysObject(object):
    def setAttr(self, _context, name, value, owner=None):
        if owner is None:
            owner = helpers.get_type(helpers.get_caller_context(_context))
        if not isinstance(owner, classes.MuranoClass):
            raise TypeError()

        attribute_store = helpers.get_attribute_store(_context)
        attribute_store.set(self, owner, name, value)

    def getAttr(self, _context, name, owner=None):
        if owner is None:
            owner = helpers.get_type(helpers.get_caller_context(_context))
        if not isinstance(owner, classes.MuranoClass):
            raise TypeError()

        attribute_store = helpers.get_attribute_store(_context)
        return attribute_store.get(self, owner, name)
