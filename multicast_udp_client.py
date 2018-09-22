from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        self.transport.write('Client: Ping'.encode('utf-8'), ("228.0.0.5", 8005))

    def datagramReceived(self, datagram, address):
        print("client::Datagram %s received from %s" % (repr(datagram.decode("utf-8")), repr(address)))


reactor.listenMulticast(8005, MulticastPingClient(), listenMultiple=True)
reactor.run()