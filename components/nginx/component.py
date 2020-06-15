from batou.component import Component
from batou.lib.file import File
from batou.utils import Address


class Nginx(Component):

    frontend_name = 'localhost'

    def configure(self):
        self.address = Address(self.frontend_name, 80)
        self += File('/etc/nginx/local/zwicky.conf',
                     source='zwicky.conf')
