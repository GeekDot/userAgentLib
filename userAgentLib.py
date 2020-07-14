#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import json
import random


class UserAgentLib(object):

    def __init__(self):

        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '0.1.11')

        self.fake_data = []
        self._read_file()

    def _read_file(self):

        with open(self.path, 'r') as f:
            json_data = json.loads(f.read())
            dict_data = json_data['browsers']

        for k in dict_data:
            self.fake_data.extend(dict_data[k])

    @property
    def get(self):
        return random.choice(self.fake_data)


ua = UserAgentLib()
