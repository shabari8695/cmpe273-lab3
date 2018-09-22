from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echo(DatagramProtocol):

    def datagramReceived(self, data, address):
        print("received %r from %s" % (data.decode('utf-8'), address))
        self.transport.write(data, address)

reactor.listenUDP(1234, Echo())
reactor.run()