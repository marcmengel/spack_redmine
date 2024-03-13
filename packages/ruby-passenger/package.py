# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class RubyPassenger(Package):
    """Ruby gem passenger"""

    homepage = "https://rubygems.org/gems/passenger/versions/6.0.4"
    url      = "https://rubygems.org/downloads/passenger-6.0.4.gem"

    version("6.0.20", sha256="6383431c00001d3273b1038423af0516a355c521834973773f852613ee91a393", expand=False)
    version('6.0.5', sha256='9c6f406dd00c4a7c1169a235e454fe40e82ead83c775f488e0d34e809bcb5b76', expand=False)

    version('6.0.4', sha256='298806191e4e8995dbc0f94c3791b2b1916ca50b5993e04236df6f4108bfc2af', expand=False)
    version('5.1.11', sha256='10fb4b685a3b1eae6445e49a2aa6f9deb67ce39143c5bd3771ce599063dba159', expand=False)

    extends('ruby')

    depends_on('ruby-rack', type=('build','run'))
    depends_on('ruby-rake', type=('build','run'))

    def install(self, spec, prefix):
        gem('install', 'passenger-{0}.gem'.format(self.version))
        os.system('printf "\\n\\n\\n\\n\\n" | %s/bin/passenger-install-apache2-module' % prefix)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)

        spack_env.prepend_path('GEM_PATH', self.prefix)
