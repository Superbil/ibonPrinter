#!/usr/bin/env python3

from setuptools import setup

import ibon


setup(setup_cfg=True,
entry_points = {
    'console_scripts': ['ibonprinter=ibon.cli:main']
})
