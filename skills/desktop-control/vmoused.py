#!/usr/bin/env python3
# Persistent virtual mouse on /dev/uinput (raw ioctls, no python-evdev needed).
# Reads one command per line from the FIFO given as argv[1]:
#   move DX DY | press BTN | release BTN | wheel N | quit      (BTN: left, right, middle)
# One long-lived device is required: a device created for each action loses its first events.
import fcntl, os, struct, sys, time

UI_SET_EVBIT, UI_SET_KEYBIT, UI_SET_RELBIT = 0x40045564, 0x40045565, 0x40045566
UI_DEV_SETUP, UI_DEV_CREATE, UI_DEV_DESTROY = 0x405C5503, 0x5501, 0x5502
EV_SYN, EV_KEY, EV_REL = 0, 1, 2
REL_X, REL_Y, REL_WHEEL, REL_WHEEL_HI_RES = 0, 1, 8, 11
BUTTONS = {"left": 0x110, "right": 0x111, "middle": 0x112}

fd = os.open("/dev/uinput", os.O_WRONLY | os.O_NONBLOCK)
fcntl.ioctl(fd, UI_SET_EVBIT, EV_KEY)
for code in BUTTONS.values():
    fcntl.ioctl(fd, UI_SET_KEYBIT, code)
fcntl.ioctl(fd, UI_SET_EVBIT, EV_REL)
for code in (REL_X, REL_Y, REL_WHEEL, REL_WHEEL_HI_RES):
    fcntl.ioctl(fd, UI_SET_RELBIT, code)
fcntl.ioctl(fd, UI_DEV_SETUP, struct.pack("HHHH80sI", 3, 0x1234, 0x5678, 1, b"claude-desk-mouse", 0))
fcntl.ioctl(fd, UI_DEV_CREATE)


def emit(kind, code, value):
    os.write(fd, struct.pack("llHHi", 0, 0, kind, code, value))


def sync():
    emit(EV_SYN, 0, 0)


while True:
    with open(sys.argv[1]) as fifo:
        for line in fifo:
            cmd = line.split()
            if not cmd:
                continue
            if cmd[0] == "quit":
                fcntl.ioctl(fd, UI_DEV_DESTROY)
                sys.exit(0)
            elif cmd[0] == "move":
                emit(EV_REL, REL_X, int(cmd[1])); emit(EV_REL, REL_Y, int(cmd[2])); sync()
            elif cmd[0] in ("press", "release"):
                emit(EV_KEY, BUTTONS[cmd[1]], 1 if cmd[0] == "press" else 0); sync()
            elif cmd[0] == "wheel":   # raw: positive = physical wheel up
                n = int(cmd[1]); step = 1 if n > 0 else -1
                for _ in range(abs(n)):
                    emit(EV_REL, REL_WHEEL_HI_RES, 120 * step); emit(EV_REL, REL_WHEEL, step); sync()
                    time.sleep(0.06)
