# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyPowerAssert(Package):
    """Ruby gem power_assert"""

    homepage = "https://rubygems.org/gems/power_assert/versions/1.1.5"
    url      = "https://rubygems.org/downloads/power_assert-1.1.5.gem"

    version('1.2.0', sha256='41fab3d9ca46bad37f59729e9bbec3fd745d2f263d1b3068bc6f21863b56b06a', expand=False)

    version('1.1.5', '1a04cdc7bd051154408c167f0065ae0da0447ea01f8895a6465502e5260731b6', expand=False)
    version('0.4.1', sha256='8d2bf80d28a9f8bc4c6c7eb162780971896d0a27fa0540093a0f125157aa6b7f', expand=False)

    extends('ruby')

    def install(self, spec, prefix):
        gem('install', 'power_assert-{0}.gem'.format(self.version))



    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)
        spack_env.prepend_path('GEM_PATH', self.prefix)
