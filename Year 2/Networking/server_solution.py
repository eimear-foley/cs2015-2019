# from the socket module import all
from socket import *
from time import gmtime, strftime
 
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# set value for host using 'gethostname()' - meaning this machine and port number 10000
hostname = gethostname()
# set value for IP using 'gethostbyname()' and by passing the hostname as a parameter
IP = gethostbyname(hostname) #IPv4 format
server_address = (hostname, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
print("Domain name: %s, IP address: %s" % (hostname, IP))
# Bind the socket to the host and port
sock.bind(server_address)
 
# Listen for one incoming connections to the server
sock.listen(1)
 
# we want the server to run all the time, so set up a forever true while loop
while True:
 
    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
     
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
 
        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            if data:
                # open a filehandle for the log file
                filehandle = open('logfile.txt', 'a')
 
                # time logged for the data in string format in GMT time
                time_logged = strftime("%Y-%m-%d %H:%M:%S", gmtime())
 
                # write data and time logged to log file
                filehandle.write("Data received: " + data + "\nTime Logged: " + time_logged + "\n")
 
                # output to terminated data received and time logged
                print('received "%s", logged at %s' % (data, time_logged))
                print('sending data back to the client')
 
                # concatenate time logged to data to send back to client
                data = "Data: " + data + ", Time logged: " + time_logged
                connection.sendall(data.encode())
            else:
                print('no more data from', client_address)
                break
             
    finally:
        # Clean up the connection
        connection.close()
 
# now close the socket
sock.close();
