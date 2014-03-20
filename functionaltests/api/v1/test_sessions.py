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

from tempest import exceptions
from tempest.test import attr

from functionaltests.api import base


class TestSessions(base.TestCase):

    @attr(type='smoke')
    def test_create_session(self):
        _, env = self.client.create_environment('test')
        self.environments.append(env)

        resp, sess = self.client.create_session(env['id'])

        self.assertEqual(resp.status, 200)
        self.assertEqual(env['id'], sess['environment_id'])

    @attr(type='negative')
    def test_create_session_before_env(self):
        self.assertRaises(exceptions.NotFound,
                          self.client.create_session,
                          None)

    @attr(type='smoke')
    def test_delete_session(self):
        _, env = self.client.create_environment('test')
        self.environments.append(env)

        _, sess = self.client.create_session(env['id'])

        resp, _ = self.client.delete_session(env['id'], sess['id'])

        self.assertEqual(resp.status, 200)

    @attr(type='negative')
    def test_delete_session_without_env_id(self):
        _, env = self.client.create_environment('test')
        self.environments.append(env)

        _, sess = self.client.create_session(env['id'])

        self.assertRaises(exceptions.NotFound,
                          self.client.delete_session,
                          None,
                          sess['id'])

    @attr(type='smoke')
    def test_get_session(self):
        _, env = self.client.create_environment('test')
        self.environments.append(env)

        _, sess = self.client.create_session(env['id'])

        resp, session = self.client.get_session(env['id'], sess['id'])

        self.assertEqual(resp.status, 200)
        self.assertEqual(session, sess)

    @attr(type='negative')
    def test_get_session_without_env_id(self):
        _, env = self.client.create_environment('test')
        self.environments.append(env)

        _, sess = self.client.create_session(env['id'])

        self.assertRaises(exceptions.NotFound,
                          self.client.get_session,
                          None,
                          sess['id'])

    @attr(type='negative')
    def test_get_session_after_delete_env(self):
        _, env = self.client.create_environment('test')
        self.environments.append(env)

        _, sess = self.client.create_session(env['id'])

        self.client.delete_environment(env['id'])

        self.assertRaises(exceptions.NotFound,
                          self.client.get_session,
                          env['id'],
                          sess['id'])

    @attr(type='negative')
    def test_double_delete_session(self):
        _, env = self.client.create_environment('test')
        self.environments.append(env)

        _, sess = self.client.create_session(env['id'])

        self.client.delete_session(env['id'], sess['id'])

        self.assertRaises(exceptions.NotFound,
                          self.client.delete_session,
                          env['id'],
                          sess['id'])
