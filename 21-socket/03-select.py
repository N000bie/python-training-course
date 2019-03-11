import select, socket
HOST = ''
PORT = 50007

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
inputs = [server]
outputs = []
buffers = {}

try:
    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs
        )
        for s in readable:
            if s is server:
                conn, addr = s.accept()
                print('Connected by', addr)
                inputs.append(conn)
            else:
                data = s.recv(1024)
                print('Received', repr(data), 'from', s.getpeername())
                if data:
                    if s not in outputs:
                        outputs.append(s)
                    buffers.setdefault(s, []).append(data)
                else:
                    print('Socket', s.getpeername(), 'disconnected')
                    inputs.remove(s)
                    if s in outputs:
                        outputs.remove(s)
                    if s in buffers:
                        buffers.pop(s)
                    s.close()
        for s in writable:
            data = buffers.get(s, [])
            if data:
                s.sendall(data.pop(0))
            else:
                outputs.remove(s)
        for s in exceptional:
            print('Socket', s.getpeername(), 'encountered error')
finally:
    server.close()
