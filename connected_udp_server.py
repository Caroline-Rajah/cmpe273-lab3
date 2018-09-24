from twisted.internet.protocol import DatagramProtocol

from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def datagramReceived(self, data,address):
        print (f"received {data.decode('utf-8')} from {address}")
        self.transport.write(bytes("hello back", 'utf-8'),address)

reactor.listenUDP(1234,Helloer())

reactor.run()