# -*- encoding: utf-8 -*-

from serial import Serial

with Serial('COM11', 115200, timeout=10) as com_port:
    print(com_port.read(100))
    com_port.write(b'pyserial test completed\n')


