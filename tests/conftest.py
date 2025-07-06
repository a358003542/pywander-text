#!/usr/bin/env python
# -*-coding:utf-8-*-

import pytest
import os
import tempfile
import shutil


@pytest.fixture
def sample_config():
    return {'a': 1}


