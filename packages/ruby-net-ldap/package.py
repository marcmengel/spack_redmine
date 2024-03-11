# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyNetLdap(Package):
    """Ruby gem net-ldap"""

    homepage = "https://rubygems.org/gems/net-ldap/versions/0.16.2"
    url      = "https://rubygems.org/downloads/net-ldap-0.16.2.gem"

    version('0.16.2', 'af9f05383fedd4eb081a644de21377462d86c78bfd583a61313865277784eeef', expand=False)
    version('0.12.1', sha256='864ce59bc51ab5a83a344a477a07def3b9691dd8a2b11f52dca3af45e707327c', expand=False)

    extends('ruby')

    def install(self, spec, prefix):
        gem('install', 'net-ldap-{0}.gem'.format(self.version))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)
        spack_env.prepend_path('GEM_PATH', self.prefix)
