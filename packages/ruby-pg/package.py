# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyPg(Package):
    """Ruby gem pg"""

    homepage = "https://rubygems.org/gems/pg/versions/1.1.4"
    url      = "https://rubygems.org/downloads/pg-1.1.4.gem"

    version('0.18.4', sha256='62f0dce2fd0b3b0f684b2d60e09b3f515e7eb30f8f736bf5ede5b49e5425bb1d',expand=False)
    version('1.2.3', sha256='f2e71e101eb7fc297222fa9a277a89a9686729a8dfa416d46408e696b5cfae8e', expand=False)

    # version('1.1.4', '5e8a09389ee51166438c0a713097773ca398ec833c817af05bededec59f7b63a', expand=False)
    version('0.21.0', '10b7cc05782236fb840c247a4ecb859f4b77001416774e1646c911c6b1567003', expand=False)

    extends('ruby')

    depends_on('ruby-rake', type=('build','run'))
    depends_on('postgresql', type=('build','run'))
    def install(self, spec, prefix):
        gem('install', 'pg-{0}.gem'.format(self.version))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)

        spack_env.prepend_path('GEM_PATH', self.prefix)
