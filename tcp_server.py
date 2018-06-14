import socket
import sys


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20


def process():
  port = TCP_PORT
  if len(sys.argv) > 1:
    port = int(sys.argv[1])
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((TCP_IP, port))
  s.listen(1)
  print('Listening on TCP port %s' % port)
  print('Connect using:')
  print('telnet 127.0.0.1 %s' % port)

  conn, addr = s.accept()
  print('Connection from: %s', addr)
  while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
      break
    print('Received data: %r', data)


if __name__ == '__main__':
  process()
