# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyRack(Package):
    """Ruby gem rack"""

    homepage = "https://rubygems.org/gems/rack/versions/2.0.8"
    url      = "https://rubygems.org/downloads/rack-2.0.8.gem"

    version("3.0.9.1", sha256="5426d7fe733a1e646b0249b6f9ada0f2792b6336a3bb5f0fc5af1af8c558e6d4", expand=False)
    version('2.0.8', 'f98171fb30e104950abe1e9fb97c177d8bb5643dd649bc2ed837864eb596a0c5', expand=False)
    version('2.0.7', sha256='5158fb64313c17fb2535c8e5def3de7e8b38baf2ab9e4c90155ebed5a9db207d', expand=False)
    version('1.6.11', sha256='ee2016b1ddf820f6e5ee437d10a85319506b60c0d493da1d15815361a91129bd', expand=False)

    extends('ruby')

    def install(self, spec, prefix):
        gem('install', 'rack-{0}.gem'.format(self.version))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)
        spack_env.prepend_path('GEM_PATH', self.prefix)
