# -*- coding: utf-8 -*-
"""Entrada mínima do addon Saile Media Center."""

from __future__ import absolute_import

import os
import sys

ADDON_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(ADDON_DIR, "resources", "lib")
if LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)

from router import run

if __name__ == "__main__":
    run(sys.argv)
