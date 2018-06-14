import select
import socket
import sys


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20


def process():
  port = TCP_PORT
  if len(sys.argv) > 1:
    port = int(sys.argv[1])
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setblocking(0)
  server.bind((TCP_IP, port))
  server.listen(1)
  inputs = [server]
  print('Listening on TCP port %s' % port)
  print('Connect using:')
  print('telnet 127.0.0.1 %s' % port)
  while True:
    readable, writable, exceptional = select.select(inputs, [], [])
    for s in readable:
      if s is server:
        conn, addr = s.accept()
        print('Connection from: %s' % (addr, ))
        conn.setblocking(0)
        inputs.append(conn)
      else:
        data = s.recv(BUFFER_SIZE)
        if data:
          print('Received data: %r' % (data, ))


if __name__ == '__main__':
  process()
