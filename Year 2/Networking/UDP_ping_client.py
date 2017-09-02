from socket import *
import time
server_address = ('localhost', 12000)
total_pings = 0
seq_num = 0

while total_pings < 10:
    # create datagram socket
    sock = socket(AF_INET, SOCK_DGRAM)
    # set timeout
    sock.settimeout(1)
    total_pings += 1
    seq_num += 1
    start_time = time.time()
    # ping consisting of sequence number and current time
    ping = ("%i %s" % (seq_num, start_time))
    try:
        print('\nSending "%s"' % ping)
        # encode() function returns bytes object
        # send ping to server using sock.sendto()
        sock.sendto(ping.encode(), (server_address))
     
        # Look for the response
        amount_received = 0
        amount_expected = len(ping)    
        while amount_received < amount_expected:
            # data is read from the connection with recv()
            received_data, address = sock.recvfrom(1024)
            # round trip time in seconds = current time - start time * 1000
            rtt = ((time.time() - start_time) * 1000)
            # decode() function returns string object
            received_data = received_data.decode()
            amount_received += len(received_data)
            print('Received PING "%s"' % received_data)
            print("Round trip time: %f" % rtt)
    except timeout:
        # if timeout print message to client and close socket
        print("Request timed out")
        sock.close()
