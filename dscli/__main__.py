#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2017 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from dscli import __version__

import argparse
import locale
import sys

def alarm():
    locale.setlocale(locale.LC_ALL, '')
    parser = argparse.ArgumentParser(description='Run a dscli session and return a bunch of alarms')
    parser.add_argument('-V', '--version', action='version', version=__version__)
    parser.add_argument('cli', help='The full dscli command to use, when '
            'executed on the shell, this same command line should show the user '
            '\'dscli> \'')

    args = parser.parse_args()

    return 0

if __name__ == '__main__':
    sys.exit(alarm())