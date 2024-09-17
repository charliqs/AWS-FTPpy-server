#Toda info de: https://pypi.org/project/pyftpdlib/
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user('usher', 'passHere', '.', perm='elradfmw')

handler = FTPHandler
FTPHandler.permit_foreign_addresses = True
handler.authorizer = authorizer
handler.passive_ports = range(30000, 30011)

handler.banner = "A test FTP"


address = ('0.0.0.0', 21)
server = FTPServer(address, handler)

server.max_cons = 5

server.serve_forever()