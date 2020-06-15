from batou.component import Component
from batou.lib.buildout import Buildout
from batou.lib.mercurial import Clone
from batou.lib.supervisor import Program


class App(Component):

    def configure(self):
        self += Clone('ssh://hg@bitbucket.org/ctheune/zwicky',
                      target='zwicky',
                      branch='default')

        # XXX hack, hack, hack
        w = self.workdir
        self.workdir += '/zwicky'
        self += Buildout(python='2.7',
                         version='2.3.1',
                         setuptools='12.0.5')
        self.workdir = w

        self += Program(
            'app',
            priority=20,
            options=dict(startsecs=10),
            command='zwicky/bin/web')
