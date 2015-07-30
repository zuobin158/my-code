# -*- coding: utf-8 -*-

import os
import sys
from .settings import *


CONFIG_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

env_path = CONFIG_ROOT + "/cms_env.json"

with open(env_path) as env_file:
    ENV_TOKENS = json.load(env_file)

DATABASES = ENV_TOKENS['DATABASES']

CACHES = ENV_TOKENS['CACHES']

STATIC_SERVER = ENV_TOKENS['STATIC_SERVER']

