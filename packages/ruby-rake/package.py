# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyRake(Package):
    """Ruby gem rake"""

    homepage = "https://rubygems.org/gems/rake/versions/13.0.1"
    url      = "https://rubygems.org/downloads/rake-13.0.1.gem"

    version("13.1.0", sha256="be6a3e1aa7f66e6c65fa57555234eb75ce4cf4ada077658449207205474199c6", expand=False)
    version("13.0.1", sha256="292a08eb3064e972e3e07e4c297d54a93433439ff429e58a403ae05584fad870", expand=False)
    version("12.3.3", sha256="f7694adb4fe638da35452300cee6c545e9c377a0e3190018ac04d590b3c26ab3", expand=False)
    version("12.1.0", sha256="5cbb774dfd1c31c4ef19e365728b8a9ecb8b0b74349496c32e3a993aee7dd855", expand=False)

    extends('ruby')

    depends_on('ruby-minitest', type=('build','run'))
    def install(self, spec, prefix):
        gem('install', 'rake-{0}.gem'.format(self.version))

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)

        spack_env.prepend_path('GEM_PATH', self.prefix)
