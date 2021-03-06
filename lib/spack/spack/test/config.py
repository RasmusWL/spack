##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://scalability-llnl.github.io/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
import unittest
import shutil
import os
from tempfile import mkdtemp

from spack.config import *


class ConfigTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.tmp_dir = mkdtemp('.tmp', 'spack-config-test-')


    @classmethod
    def tearDown(cls):
        shutil.rmtree(cls.tmp_dir, True)


    def get_path(self):
        return os.path.join(ConfigTest.tmp_dir, "spackconfig")


    def test_write_key(self):
        config = SpackConfigParser(self.get_path())
        config.set_value('compiler.cc',  'a')
        config.set_value('compiler.cxx', 'b')
        config.set_value('compiler', 'gcc@4.7.3', 'cc',  'c')
        config.set_value('compiler', 'gcc@4.7.3', 'cxx', 'd')
        config.write()

        config = SpackConfigParser(self.get_path())

        self.assertEqual(config.get_value('compiler.cc'),  'a')
        self.assertEqual(config.get_value('compiler.cxx'), 'b')
        self.assertEqual(config.get_value('compiler', 'gcc@4.7.3', 'cc'), 'c')
        self.assertEqual(config.get_value('compiler', 'gcc@4.7.3', 'cxx'), 'd')

        self.assertEqual(config.get_value('compiler', None, 'cc'),  'a')
        self.assertEqual(config.get_value('compiler', None, 'cxx'), 'b')
        self.assertEqual(config.get_value('compiler.gcc@4.7.3.cc'), 'c')
        self.assertEqual(config.get_value('compiler.gcc@4.7.3.cxx'), 'd')

        self.assertRaises(NoOptionError, config.get_value, 'compiler', None, 'fc')
