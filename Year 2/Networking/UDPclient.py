from socket import *
hostname = gethostname()
server_address = (hostname, 6789)
sock = socket(AF_INET, SOCK_DGRAM)
 
try:
    # Send data
    data = 'message from client'
    print('sending "%s"' % data)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendto(data.encode(), (server_address))
 
    # Look for the response
    amount_received = 0
    amount_expected = len(data)
     
    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        received_data, address = sock.recvfrom(1024)
        received_data = received_data.decode()
        amount_received += len(received_data)
        print('received "%s"' % received_data)
finally:
    sock.close()
