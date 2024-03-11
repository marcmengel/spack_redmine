# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyMysql2(Package):
    """Ruby gem mysql2"""

    homepage = "https://rubygems.org/gems/mysql2/versions/0.5.3"
    url      = "https://rubygems.org/downloads/mysql2-0.5.3.gem"

    version('0.5.3', '5ca2d97d9c25fa27dc67eca77dd8d73f12576c4cd4f6f6c18b12925a3cbb2434', expand=False)

    extends('ruby')

    depends_on('mariadb', type=('build','run'))
    def install(self, spec, prefix):
        gem('install', 'mysql2-{0}.gem'.format(self.version))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)
        spack_env.prepend_path('GEM_PATH', self.prefix)
