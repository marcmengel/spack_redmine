# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyTestUnit(Package):
    """Ruby gem test-unit"""

    homepage = "https://rubygems.org/gems/test-unit/versions/3.3.4"
    url      = "https://rubygems.org/downloads/test-unit-3.3.4.gem"

    version('3.3.5', sha256='3e87e91f1f9604d3b99e9ce62089b211f9421b9baf29b2ffd241992594c1a949', expand=False)

    version('3.3.4', 'df3c6011c7d66fe37557bd6cb1f69ab57a3201118aa909c8099a81cfcdba3357', expand=False)
    version('3.2.3', sha256='fe125f1418b223b9d84ea12c2557d87ccc98d2c4ae5b7ef63c75611dc4edcfce', expand=False)

    extends('ruby')

    depends_on('ruby-power_assert', type=('build','run'))
    def install(self, spec, prefix):
        gem('install', 'test-unit-{0}.gem'.format(self.version))



    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)

        spack_env.prepend_path('GEM_PATH', self.prefix)
