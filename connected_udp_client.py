from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 1234

        self.transport.connect(host, port)
        print("now we can only send to host %s port %d" % (host, port))
        self.transport.write("Hello World".encode('utf-8')) # no need for address

    def datagramReceived(self, data, address):
        print("received %r from %s" % (data, address))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(0, Helloer())
reactor.run()