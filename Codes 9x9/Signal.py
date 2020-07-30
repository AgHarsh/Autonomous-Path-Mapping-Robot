def fwd(ser):
    ser.write(b'F')
    print("F")


def rev(ser):
    ser.write(b'B')
    print("b")


def left(ser):
    ser.write(b'L')
    print("l")


def right(ser):
    ser.write(b'R')
    print("r")


def stop(ser):
    ser.write(b'S')
    print("s")


def up(ser):
    ser.write(b'U')
    print("u")


def down(ser):
    ser.write(b'D')
    print("d")
