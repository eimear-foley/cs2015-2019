class Directory:
    # Discovery Server
    # Stores the registered services in a hash map where service ID's are keys
    def __init__(self):
        self._discover = {}

    def lookUp(self, request, ip):
        # 'lookUp' function that searches for requested service
        for i in self._discover:
            service = self._discover[i]
            if service["name"] == request or service["quality"] == request:
                print("Found requested service.")
                if service["state"] == "ready":
                    print("Joining Client %i to requested service '%s'." % (ip, service["name"]))
                    self.join(ip, service)
                    return
                elif service["state"] == "running":
                    print("Service '%s' is unavailable on this thread. Creating a thread for service '%s'" % (service["name"], service["name"]))
                    self.join(ip, service)
                    return
        print("No service '%s' found." % request)
        return

    def join(self, ip, service):
        # 'join' function that connects requested service to the client
        service["state"] = "running"
        print("Client IP:%i has joined to service '%s' with ID:%i from server IP:%i on Port %i.\n" % (ip, service["name"], service["ID"], service["IP"], service["port"]))
        return True

class Client:
    # Requests services from the Discovery Service either by name or preferred quality
    def __init__(self, ip):
        self._ip = ip
        self._request = ""
        self._directory = directory
        self._current_service = None

    def requestService(self, request):
        self._request = request
        print("Discovering requested service '%s'." % self._request) 
        service = self._directory.lookUp(self._request, self._ip)
        if service:
            self._current_service = self._request

class Server:
    # Creates service definitions
    # Registers services with the Discovery Server
    def __init__(self, ip):
        self._ip = ip
        self._directory = directory

    def createService(self, name, service_id, port_num, quality):
        service = {"name": name, "ID": service_id, "port": port_num, "state": "ready", "IP": self._ip, "quality": quality}
        if self.registerService(service):
            print("Service '%s' created and registered." % (service["name"]))

    def registerService(self, service):
        self._directory._discover[service["ID"]] = service
        if service["ID"] in self._directory._discover:
            return True

if __name__ == "__main__":
    directory = Directory()
    client1 = Client(1)
    client2 = Client(2)
    server1 = Server(3)
    server2 = Server(4)
    print("\n***CREATING SERVICES***\n")
    server1.createService("printer", 45, 9100, "low power")
    server1.createService("calculator", 65, 5001, "efficient")
    server2.createService("email", 101, 25, "high speed")
    server2.createService("printer", 92, 9100, "efficient")
    print("\n***SERVICE REQUESTS***")
    print("\nClient 1 request\n")
    client1.requestService("email")
    print("\nClient 2 request\n")
    client2.requestService("printer")
    print("\nClient 1 request\n")
    client1.requestService("printer")
    print("\nClient 2 request\n")
    client2.requestService("calculator")
    print("\nClient 2 request\n")
    client2.requestService("email")