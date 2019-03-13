# -*- encoding: utf-8 -*-
import time
from datetime import datetime, timedelta

from serial import Serial


def wait_then_read(serial: Serial, wait: float, gap: float = 0.1, poll: float = 0.1):
    buf = bytearray()
    wait_timeout = datetime.utcnow() + timedelta(seconds=wait)
    while datetime.utcnow() < wait_timeout:
        if serial.in_waiting:
            break
        time.sleep(poll)
    if not serial.in_waiting:
        return b''

    last_read = datetime.utcnow()
    while True:
        while serial.in_waiting:
            buf.extend(serial.read_all())
            last_read = datetime.utcnow()
        while not serial.in_waiting:
            time.sleep(poll)
            if (datetime.utcnow() - last_read).total_seconds() > gap:
                return bytes(buf)


with Serial('COM11', 115200, timeout=30) as com_port:
    while True:
        data = wait_then_read(com_port, 30, gap=5)
        print(data)
        if data.startswith(b'bye'):
            break
    com_port.write(b'pyserial test completed\n')
