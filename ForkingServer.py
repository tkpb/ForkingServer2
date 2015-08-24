import os
import socket
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 9000
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'
DEFAULT_ENCODING = 'ascii'


class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s: %s' % (current_process_id, data)
        print("Server sending response [current_process_id: data] = [%s]" % response)
        self.request.send(response)
        return


class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    """Nothing to add here, inherited everything necessary from parents"""
    pass


def main():
        # Launch server
        server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
        ip, port = server.server_address  # Retrieve the port number
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.setDaemon(True)  # don't hang on exit
        server_thread.start()
        print('Server loop running PID: %s' % os.getpid())

        # Clean them up
        server.shutdown()
        server.socket.close()

if __name__ == '__main__':
    main()
