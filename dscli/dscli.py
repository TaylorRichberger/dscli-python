#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2017 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from six.moves import cStringIO as StringIO
import re

import pexpect

def runcommand(child, command):
    '''Set the logfile, run the command, wait until the prompt, trim the prompt,
    and return the result.'''
    with StringIO() as string:
        child.logfile_read = string
        child.sendline(command)
        child.expect('dscli> ')
        child.logfile_read = None
        string.flush()
        return re.sub(r'\ndscli> ', '', string.getvalue())
        

class DSCLI(object):
    def __init__(self, command):
        child = pexpect.spawnu(command)
        child.setwinsize(500, 500)
        child.setecho(False)
        child.expect('dscli> ')
        runcommand('setoutput -p off -bnr off -hdr off -fmt xml')
        lssi = runcommand('lssi')

        print('####{}####'.format(lssi))

        runcommand('exit')
