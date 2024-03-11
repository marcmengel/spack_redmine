# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Redmine(Package):
    """Redmine wiki/bugtracker/SCM interface """

    homepage = "https://www.redmine.org/"
    url      = "http://www.redmine.org/releases/redmine-4.1.0.tar.gz"

    version('4.1.1', sha256='05faafe764330f2d77b0aacddf9d8ddce579c3d26bb8e03a7d6e7ff461f1cdda', expand=False)
    version('4.1.0',  '32c7b9ce4c419092da439b540cbc1dbf', expand=False)
    version('4.0.6',  '897bfcaa4a49539b10d0529ce103f919', expand=False)
    version('3.4.13', '5f17b35dfe73118067f63fb535332cfb', expand=False)
    version('3.4.11', sha256='19c09eedbe970fc5a20de96c2f1107a186072a69dc512c501a5638979a3e2891', expand=False)



    variant('sqlite',default=False, description="include sqlite database access")
    variant('mysql',default=False, description="include sqlite database access")

    variant('postgres',default=True, description="include postgres database access")
    variant('ldap',default=True, description="include sqlite database access")
    variant('markdown', default=True, description="include markdown support")
    variant('rmagick', default=True, description="include rmagick support")
    variant('passenger', default=True, description="include passenger")
    variant("db_migrate", default=False, description="run rake:db_migrate")

    variant("plugin_redmine_better_gantt_chart", default=True,  description="redmine plugin better_gantt_chart")
    variant("plugin_redmine_bootstrap_kit", default=True,  description="redmine plugin bootstrap_kit")
    variant("plugin_redmine_jenkins", default=True,  description="redmine plugin jenkins")
    variant("plugin_redmine_redcarpet_viewer", default=True,  description="redmine plugin redcarpet_viewer")
    variant("plugin_redmine_sortable_table", default=True,  description="redmine plugin sortable_table")
    variant("plugin_redmine_group_assignee", default=True,  description="redmine plugin group_assignee")
    variant("plugin_simple_ci", default=True,  description="redmine plugin  simple_ci")
    variant("plugin_wiki_external_filter", default=True,  description="redmine plugin  wiki_external_filter")

    depends_on('ruby', type=('build','run'))
    depends_on('redmine-ruby-deps', type=('build','run'))
    depends_on('ruby-mysql2@0.4.6:', type=('build','run'), when='+mysql')
    depends_on('ruby-pg', type=('build','run'), when='+postgres')
    depends_on('ruby-sqlite3', type=('build','run'), when='+sqlite')
    depends_on('ruby-rmagick', type=('build','run'), when='+rmagick')
    depends_on('ruby-net-ldap', type=('build','run'), when='+ldap')

    def install(self, spec, prefix):
        import os
        plugin_urls =  {
            "+plugin_redmine_better_gantt_chart": "https://github.com/kulesa/redmine_better_gantt_chart.git",
            "+plugin_redmine_bootstrap_kit": "https://github.com/jbox-web/redmine_bootstrap_kit.git",
            "+plugin_redmine_jenkins": "https://github.com/jbox-web/redmine_jenkins.git",
            "+plugin_redmine_redcarpet_viewer": "https://github.com/ngyuki/redmine_redcarpet_viewer.git",
            "+plugin_redmine_sortable_table": "https://github.com/AstraSerg/redmine_sortable_table.git",
            "+plugin_redmine_group_assignee": "git@github.com:marcmengel/redmine_group_assignee.git",
            "+plugin_simple_ci": "git@github.com:marcmengel/simple_ci.git",
            "+plugin_wiki_external_filter": "git@github.com:marcmengel/wiki_external_filter.git",

        }
        os.system("cd %s && tar xzf %s" % (prefix, self.stage.archive_file))
        os.system("cd %s && mv redmine-[0-9]*/* . && rm -rf  redmine-[0-9]*" % prefix )
        os.system("cd %s && patch -p1 < %s" % (prefix, os.path.join(os.path.dirname(__file__),"patch_3.4.11")))
        os.system("cd %s && bundle install --local --without development test %s" % (prefix, ("rmagick" if "+rmagick" in spec else "")))
        for variant in plugin_urls:
            if variant in self.spec:
                os.system("cd %s/plugins && git clone %s" % (prefix, plugin_urls[variant]))
                os.system(" cd %s && bundle exec rake redmine:plugins:migrate NAME=%s VERSION=0 RAILS_ENV=production" % (prefix, variant.replace('+','')))
        if '+db_migrate' in self.spec:
            os.system("cd %s && RAILS_ENV=production bundle exec rake db:migrate" % prefix)

