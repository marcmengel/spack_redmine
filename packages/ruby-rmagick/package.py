# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class RubyRmagick(Package):
    """Ruby gem rmagick"""

    homepage = "https://rubygems.org/gems/rmagick/versions/2.6.0"
    url      = "https://rubygems.org/downloads/rmagick-2.6.0.gem"

    version('4.1.2', sha256='4551d9c67d9fceb18e65093e343aaac3f7f2ae00f6e8fc4b1f1026a7a332562a', expand=False)

    version('2.16.0', sha256='06d3c969889d31065127e90a612904c575785293420f6d044a8b4dda58093d55', expand=False)
    version('2.6.0', '4c22e0d2824ea7f1a367c592901419ee4e1a34396cbb03ed56452d120d3a7679', expand=False)


    extends('ruby')

    depends_on('ruby-rake', type=('build','run'))
    depends_on('ruby-test-unit', type=('build','run'))
    depends_on('imagemagick', type=('build','run'))

    def install(self, spec, prefix):
        gem('install', 'rmagick-{0}.gem'.format(self.version))

    def setup_build_environment(self, env):
        env.set('LD_FLAGS', "-L%s" % self.spec['imagemagick'].prefix.lib )
        env.set('CPPFLAGS', "-I%s/ImageMagick-7" % self.spec['imagemagick'].prefix.include)


    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('GEM_PATH', self.prefix)


    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('GEM_PATH', self.prefix)

        spack_env.prepend_path('GEM_PATH', self.prefix)
