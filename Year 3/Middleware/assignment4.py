class DiscoveryServer:
    # Discovery Server
    # Stores the registered services in a hash map where service ID's are keys
    def __init__(self):
        self._discover = {}

    def lookUp(self, client):
        # 'lookUp' function that searches for requested service
        for i in self._discover:
            service = self._discover[i]
            if service["name"] == client._request or service["quality"] == client._request:
                print("Found requested service.")
                if service["state"] == "ready":
                    print("Joining Client %i to requested service '%s'." % (client._ip, service["name"]))
                    self.join(client, service)
                    return
                elif service["state"] == "running":
                    print("Service '%s' is unavailable on this thread. Creating a thread for service '%s'" % (service["name"], service["name"]))
                    self.join(client, service)
                    return
        print("No service '%s' found." % client._request)
        return

    def join(self, client, service):
        # 'join' function that connects requested service to the client
        service["state"] = "running"
        print("Client IP:%i has joined to service '%s' with ID:%i from server IP:%i on Port %i." % (client._ip, service["name"], service["ID"], service["IP"], service["port"]))
        notification_mngr.manageClients(client, service)
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
        service = self._directory.lookUp(self)
        if service:
            self._current_service = self._request

    def cancelService(self, service):
        print("Cancelling '%s'. Error level greater than 5." % service["name"])
        notification_mngr.removeService(self, service)

    def errorReceived(self, service, errorEvent):
        if errorEvent._errorLevel > 5:
            print("Error ID %i: '%s'. Error level greater than five." % (errorEvent._id, errorEvent._message))
            self.cancelService(service)
        else:
            print("Error ID %i: '%s'. Error level less than five. Fixing error..." %(errorEvent._id, errorEvent._message))
            print("Error resolved. Process continued.")

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
        notification_mngr.manageService(service)
        if service["ID"] in self._directory._discover:
            return True

    def errorOccuring(self, ID, message, errorLevel):
        error = ErrorEvent(ID, message, errorLevel)
        print("\nError occurring on server ID: %i" % self._ip)
        print("Notifying clients...")
        for service in self._directory._discover.values():
            notification_mngr.sendNotifications(error, service)


class ErrorEvent:
    # Error event
    # Defined by an ID, an error message and an error level
    # Created on a 'Server'
    def __init__(self, ID, message, errorLevel):
        self._id = ID
        self._message = message
        self._errorLevel = errorLevel

    def setErrorMessage(self, message):
        self._message = ("%s" % message)
        
    def getErrorMessage(self):
        if self._message == "":
            return "No error."
        else:
            return ("%s" % self._message)

class NotificationManager:
    # Notification manager for services
    # Notifies clients of errors 
    def __init__(self):
        self._services = {}

    def manageService(self, service):
        self._services[service["name"]] = []

    def manageClients(self, client, service):
        if self._services[service["name"]] == []:
            self._services[service["name"]] = [client]
        else:
            self._services[service["name"]].append(client)

    def sendNotifications(self, errorEvent, service):
        found = False
        for client in self._services[service["name"]]:
            found = True
            print("\nNotifiying client ID: %i..." % client._ip)
            client.errorReceived(service, errorEvent)
        if not found:
            print("\nNo clients to '%s'." % service["name"])

    def removeService(self, client, service):
        self._services[service["name"]].remove(client)

if __name__ == "__main__":
    notification_mngr = NotificationManager()
    directory = DiscoveryServer()
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
    server1.errorOccuring(1, 'Load overbalancing', 7)
    server2.errorOccuring(1, 'Zero Division Error', 3)