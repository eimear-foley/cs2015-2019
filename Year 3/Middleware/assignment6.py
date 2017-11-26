class QueueManager:
    # Manages the DEMAND and the REQUEST queue of messages
    def __init__(self):
        self._directory = {} # maintains reference to all servers

    def registerService(self, server):
        # registers all servers and their services in self._directory
        print("Service '%s' on Server %i registered with Queue Manager" % 
        (server._name, server._id))
        self._directory[server._name] = server

    def checkDemandQueue(self, client, item):
        # checks Demand queue for required service
        for server in self._directory:
            if server == client._request and self._directory[server]._busy == False:
                print("Required service '%s' found...\n" % client._request)
                # If required service found checks request queue
                self.checkRequestQueue(client, self._directory[server], item)
                return
        print("No service '%s' found..." % client._request)

    def checkRequestQueue(self, client, server, requested):
        # calls results from required service
        result = server.sendService(requested)
        client._request = ""
        client._currentService = server._name
        request.dequeue()
        print("Client %i now using service '%s'. Answer obtained: %s. \n" % 
        (client._id, server._name, result))

class Client:
    def __init__(self, ip):
        self._id = ip
        self._request = ""
        self._currentService = None

    def requestService(self, request, item):
        self._request = request
        print("Client %i demanding requested service '%s'.\n" % (self._id, self._request)) 
        # Enqeues client request to DEMAND queue
        demand.enqueue([self._id, self._request, item])
        # Queue Manager checks for service
        directory.checkDemandQueue(self, item)

class Server:
    # SUPER CLASS
    def __init__(self, ip, name):
        self._id = ip
        self._busy = False
        self._name = name
        directory.registerService(self)

    def sendService(self, requested):
        print("Server %i adding service '%s' to request queue...\n" % (self._id, self._name))
        self._busy = True

class Sorter(Server):
    # SUB CLASS of 'Server'
    def __init__(self, ip, name):
        super(Sorter, self).__init__(ip, name)

    def sendService(self, requested):
        # Carries out requested service - sorting
        super(Sorter, self).sendService(requested)
        results = sorted(requested)
        request.enqueue([self._id, self._name, results])
        return results

class Adder(Server):
    # SUB CLASS of 'Server'
    def __init__(self,ip, name):
        super(Adder, self).__init__(ip, name)

    def sendService(self, requested):
        # Carries out requested service - addition
        super(Adder, self).sendService(requested)
        results = requested[0] + requested[1]
        request.enqueue([self._id, self._name, results])
        return results

class Subtractor(Server):
    # SUB CLASS of 'Server'
    def __init__(self,ip, name):
        super(Subtractor, self).__init__(ip, name)

    def sendService(self, requested):
        # Carries out requested service - subtraction
        super(Subtractor, self).sendService(requested)
        results = requested[0] - requested[1]
        request.enqueue([self._id, self._name, results])
        return results

class FIFOQueue:
    def __init__(self):
        self._body = [] # queue body
        self._head = 0 # queue head
        self._empty = True
        self._lock = False # lock set to True when queue in use

    def is_empty(self):
        # returns True or False
        if self.length() != 0:
            self._empty = False
        return self._empty

    def enqueue(self, message):
        # client can add message to queue
        print("Adding message '%s'" % (message))
        self._body.append(message)

    def dequeue(self):
        # client can remove message from queue
        if self.length == 0:
            return None
        message = self._body[self._head]
        self._body[self._head] = None
        self._head += 1
        return message

    def length(self):
        # returns length of queue
        print("Length: %i" % (len(self._body) - self._head))
        return len(self._body) - self._head

    def first(self):
        # returns top of queue
        if self.length == 0:
            return None
        return ("First: %s" % (self._body[self._head]))

if __name__ == "__main__":
    directory = QueueManager()
    demand = FIFOQueue()
    request = FIFOQueue()
    s1 = Sorter(1, 'list sorter')
    s2 = Adder(2, 'adder')
    s3 = Subtractor(3, 'subtractor')
    c1 = Client(1)
    c1.requestService("list sorter", [3,2,1])
    c2 = Client(2)
    c2.requestService("adder", [8,3])
    c3 = Client(3)
    c3.requestService("subtractor", [56, 7])
