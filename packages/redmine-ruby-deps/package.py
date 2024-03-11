# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RedmineRubyDeps(BundlePackage):
    """Rather than define dozens of ruby packages, we just make one GEM_HOME bundle and
       stuff them all in here..."""

    homepage = "https://www.example.com"

    maintainers("marcmengel")

    version("1.0")

    # FIXME: Add dependencies if required.
    depends_on("ruby")

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("GEM_HOME", self.prefix.gems)
        env.prepend("GEM_PATH", self.prefix.gems)

    def setup_run_environment(self, env, dependent_spec):
        env.set("GEM_HOME", self.prefix.gems)
        env.prepend("GEM_PATH", self.prefix.gems)
