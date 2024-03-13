# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Redmine(Package):
    """Redmine wiki/bugtracker/SCM interface """

    homepage = "https://www.redmine.org/"
    url      = "http://www.redmine.org/releases/redmine-4.1.0.tar.gz"

    version("5.1.2", sha256="26c0ca0a9aaee1ceb983825bf1266c99b0850bf013c178713f5a3b0080012123", expand=False)
    version("5.0.8", sha256="1eda410840a21ab0f6965a378699a65588b6785db95eaf6494c6c9bc51b5bf6e", expand=False)
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
    variant("db_migrate", default=False, description="run rake:db_migrate")

    variant("plugin_redmine_better_gantt_chart", default=True,  description="redmine plugin better_gantt_chart")
    variant("plugin_redmine_bootstrap_kit", default=True,  description="redmine plugin bootstrap_kit")
    variant("plugin_redmine_jenkins", default=True,  description="redmine plugin jenkins")
    variant("plugin_redmine_redcarpet_viewer", default=True,  description="redmine plugin redcarpet_viewer")
    variant("plugin_redmine_sortable_table", default=True,  description="redmine plugin sortable_table")
    variant("plugin_redmine_group_assignee", default=True,  description="redmine plugin group_assignee")
    variant("plugin_simple_ci", default=True,  description="redmine plugin  simple_ci")
    variant("plugin_wiki_external_filter", default=True,  description="redmine plugin  wiki_external_filter")

    depends_on('ruby @2.7.0:3.2.99', type=('build','run'), when="@5.1:")
    depends_on('ruby @2.5.0:3.1.0', type=('build','run'), when="@5:5.0.99")
    depends_on('ruby @2.3.0:2.7.0', type=('build','run'), when="@4:4.99")
    depends_on('ruby @2.3.0:2.5.0', type=('build','run'), when="@3:3.99")
    depends_on('redmine-ruby-deps', type=('build','run'))
    depends_on('ruby-mysql2@0.4.6:', type=('build','run'), when='+mysql')
    depends_on('ruby-pg', type=('build','run'), when='+postgres')
    depends_on('ruby-sqlite3', type=('build','run'), when='+sqlite')
    depends_on('ruby-rmagick', type=('build','run'), when='+rmagick')
    depends_on('ruby-net-ldap', type=('build','run'), when='+ldap')
    depends_on('ruby-rack')
    depends_on('ruby-rake')

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
        with working_dir(prefix):
            os.system("tar xzf %s" %  self.stage.archive_file)
            os.system("mv redmine-[0-9]*/* . && rm -rf  redmine-[0-9]*")
            os.system("bundle config set --local without 'development test %s'"%  ("rmagick" if "+rmagick" in spec else ""))
            os.system("bundle install") 
        for variant in plugin_urls:
            if variant in self.spec:
                with working_dir(prefix.plugins):
                    os.system("git clone %s" %  plugin_urls[variant])
                with working_dir(prefix):
                    os.system("bundle exec rake redmine:plugins:migrate NAME=%s VERSION=0 RAILS_ENV=production" % variant.replace('+',''))
        if '+plugin-redmine-jenkins' in self.spec:
            with working_dir(prefix.plugins.redmine_jenkins):
                os.sytem("patch -p1 < %s" % os.path.join(os.path.dirname(__file__),"redmine_jenkins.patch") )
            
        if '+db_migrate' in self.spec:
            with working_dir(prefix):
                os.system("RAILS_ENV=production bundle exec rake db:migrate")
