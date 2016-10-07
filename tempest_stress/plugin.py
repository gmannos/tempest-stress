# Copyright 2015 Intel
# All Rights Reserved.
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


import os

from tempest import config
from tempest.test_discover import plugins

from tempest_stress import config as config_opts


class TempestStressPlugin(plugins.TempestPlugin):
    def load_tests(self):
        return {}

    def register_opts(self, conf):
        config.register_opt_group(conf,
                                  config_opts.stress_group,
                                  config_opts.StressGroup)

    def get_opt_lists(self):
        return [
            (config_opts.stress_group.name,
             config_opts.StressGroup)
        ]