import socket
import os

SERVER_HOST = 'localhost'
SERVER_PORT = 9000
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'
DEFAULT_ENCODING = 'ascii'


class ForkedClient:
    """ A client to test forking server"""
    def __init__(self, ip, port):
        # Create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        self.sock.connect((ip, port))

    def run(self):
        """ Client playing with the server"""

        # Send the data to server
        current_process_id = os.getpid()
        print('PID %s Sending echo message to the server : "%s"' % (current_process_id, ECHO_MSG))
        sent_data_length = self.sock.send(ECHO_MSG.encode(DEFAULT_ENCODING))
        print("Sent: %d characters, so far..." % sent_data_length)

        # Display server response
        response = self.sock.recv(BUF_SIZE)
        print("PID %s received: %s" % (current_process_id, response[5:]))

    def shutdown(self):
        """ Cleanup the client socket """
        self.sock.close()


def main():
    print('hey')
    client = ForkedClient(SERVER_HOST, SERVER_PORT)
    client.run()
    client.shutdown()

if __name__ == '__main__':
    main()
