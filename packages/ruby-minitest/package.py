# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyMinitest(Package):
    """Ruby gem minitest"""

    homepage = "https://rubygems.org/gems/minitest/versions/5.13.0"
    url      = "https://rubygems.org/downloads/minitest-5.13.0.gem"

    version('5.14.1', sha256='afdc52567e32e275f8e8f825437883803efac2f9658dce0c70ea75fbb54d7f25', expand=False)
    version('5.13.0', 'b1666465cc443e41e03661e17e7e3ebfa076c9934845365a870352bdd9b92670', expand=False)
    version('5.11.3', sha256='78e18aa2c49c58e9bc53c54a0b900e87ad0a96394e92fbbfa58d3ff860a68f45', expand=False)

    extends('ruby')

    def install(self, spec, prefix):
        gem('install', 'minitest-{0}.gem'.format(self.version))



    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)
        spack_env.prepend_path('GEM_PATH', self.prefix)
