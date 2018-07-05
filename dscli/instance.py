# -*- coding: utf-8 -*-
# Copyright © 2017 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from dscli.errors import TagError

class Instance(object):
    def __init__(self, tree):
        self.__xml = tree
        if tree.tag != 'INSTANCE':
            raise TagError('Root tag must be INSTANCE, not {}'.format(tree.tag))

    @property
    def xml(self):
        return self.__xml

