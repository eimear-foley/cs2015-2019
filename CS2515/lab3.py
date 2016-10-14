from queuesRevised import Queue

def reverseQueue(queue):
	
	#A function which, when given a queue as input, will return a new queue with all the elements in reverse order

    r_queue = []

    if len(queue) == 0:
        return None

    i = len(queue) - 1
    while i >= 0:
        r_queue += [queue[i]]
        i -= 1
    return r_queue

def shrinkQueue(self):

	#Class method to be used when the number of queue elements drops to below 25% of the reserved list space
	#Will shrink queue to half its current size
	
    oldbody = self.body
    oldpos = self.head
    if (self.size/len(self.body)) < 0.25:
        self.body = [None] * (0.5*len(oldbody))
        pos = 0
        if self.head < self.tail:     #data is not wrapped around in list
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
        else:                         #data is wrapped around
            while oldpos < len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
            oldpos = 0
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
        self.head = 0
        self.tail = self.size

def modularEnqueue(self, item):

	#Wrap-around implementation of the Queue using modular arithmetic
	
    if self.size == 0:
        self.body[0] = item      #assumes an empty queue has head at 0
        self.size = 1
    else:
        if self.size == len(self.body):
            self.grow()
        elif (self.head + self.size) % len(self.body) == len(self.body)-1:
            self.body[self.body[self.head] - self.size] = item
        else:
            self.body[self.head + self.size] = item
        self.size += 1


#### INTERNET SIMULATOR ####

#Implement classes to represent clients, routers and packets

class Client(object):

	"""A class to represent an internet client. 
	Each client has an queue of packets to send. 
	It should have a method send(), which simply removes the first packet from the queue, 
	removes the first router from the packet's path, and enqueues the packet at that router. 
	It should also have a method receive(), which takes a packet from a router and, in this case, 
	prints a message to the command line stating that the client has received the packet, displaying its contents. """

    def __init__(self, packets):
        self._packets = packets

    def send(self):
        packet = self._packets.dequeue()
        router = packet._path.dequeue()
        router._packets.enqueue(packet)

    def receive(self, packet):
        print("Client has received packet!")
        print("Contents: %s" %  packet._content)


class Packets(object):

	"""A class to represent a simple internet packet. Each packet has content, which will be a string; 
	an address, which will be a reference to a client object; a sender, which will also be a reference to a client object; 
	and a path, which will be a queue of router objects. """
    
	def __init__(self, content, address, sender, path):
        self._content = content
        self._address = address
        self._sender = sender
        self._path = path

class Routers(object):

	"""A class to represent a simple internet router. 
	Each router has a queue of packets. It also has a process() method, which removes the first packet from its queue, 
	removes the first router from the packet's queue, and then adds that packet into the queue for the selected router. 
	If there was no router in the packet's queue, then pass the packet straight to the client in the packet's address 
	using the client's receive() method. """
	
    def __init__(self, packets):
        self._packets = packets

    def process(self):
        packets = self._packets.dequeue()
        if not (packets._path).is_empty():
            router = packets._path.dequeue()
            router._packets.enqueue(packets)
        else:
            client = packets._address
            client.receive(packets)

def main():

	"""Test function to test your internet simulation. 
	Create two clients, two routers, and then create three packets to be sent from the first client to the second, 
	via the two routers. For each packet, you will need to add the routers into the path queue. 
	Method should repeatedly cycle through the four nodes (2 clients and 2 routers) until nobody has 
	any packets left in their queue.  """

    r1 = Routers(Queue())
    r2 = Routers(Queue())
	
	p1 = Queue()
    p1.enqueue(r1)
    p1.enqueue(r2)

    p2 = Queue()
    p2.enqueue(r1)
    p2.enqueue(r2)

    p3 = Queue()
    p3.enqueue(r1)
    p3.enqueue(r2)

    c2 = Client(Queue())
    pack1 = Packets("craic", c2, "c1", p1)
    pack2 = Packets("happens", c2, "c1", p2)
    pack3 = Packets("done", c2, "c1", p3)

    clq = Queue()
    clq.enqueue(pack1)
    clq.enqueue(pack2)
    clq.enqueue(pack3)
    c1 = Client(clq)

    for i in range(3):
        c1.send()
        r1.process()
        r2.process()


if __name__ == "__main__":
    main()
