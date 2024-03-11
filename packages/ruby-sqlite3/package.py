# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubySqlite3(Package):
    """Ruby gem sqlite3"""

    homepage = "https://rubygems.org/gems/sqlite3/versions/1.4.2"
    url      = "https://rubygems.org/downloads/sqlite3-1.4.2.gem"

    version('1.4.2', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', expand=False)

    extends('ruby')

    depends_on('ruby-minitest', type=('build','run'))
    depends_on('ruby-rake', type=('build','run'))
    depends_on('sqlite', type=('build','run'))
    def install(self, spec, prefix):
        gem('install', 'sqlite3-{0}.gem'.format(self.version))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)
        spack_env.prepend_path('GEM_PATH', self.prefix)
