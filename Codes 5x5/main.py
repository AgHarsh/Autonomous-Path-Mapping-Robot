import numpy as np
import cv2
import time
import serial

import KMeans
import Arena_Gen
import Death_E
import Signal
import Aruco_Webcam
import Move
import New_shape

cap = cv2.VideoCapture(1)
time.sleep(2)
ser = serial.Serial('COM4', 9600)
time.sleep(2)
ser.write(b'S')
print("Setup Done!")

# Initial Arena Capture
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite("arena.jpg", frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
cv2.destroyAllWindows()

# Refining Image
r = KMeans.refine_image()

# Generating all shapes and colors along with position of different blocks
arena, shape = Arena_Gen.generate_arena()
death_e, weapons = Death_E.generate_deatheater()

# Start moving bot
d_pos = []
for i in range(5):
    for j in range(5):
        if death_e[i][j]:
            d_pos.append(5*i + j)
Signal.up(ser)
time.sleep(4)
for i in d_pos:
    index = []
    for j in range(5):
        for k in range(5):
            if arena[j][k] == 4:
                index.append(5*j + k)
    corners = Aruco_Webcam.capture(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * 5 / shape[0])
    cy = int(int(mid[1]) * 5 / shape[1])
    a_pos = 5 * cy + cx
    print(a_pos)
    Move.move_bot(r, a_pos, i, ser, cap, index)
    print("Death Eater Reached")
    Signal.stop(ser)
    time.sleep(1)
    Signal.down(ser)    # servo motor function
    time.sleep(1)
    corners = Aruco_Webcam.capture(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * 5 / shape[0])
    cy = int(int(mid[1]) * 5 / shape[1])
    a_pos = 5 * cy + cx
    print(a_pos)
    Move.move_bot(r, a_pos, 2, ser, cap, index)
    Signal.stop(ser)
    time.sleep(1)
    Signal.up(ser)  # servo motor function
    time.sleep(1)

w_pos = []
for i in range(5):
    for j in range(5):
        if weapons[i][j]:
            w_pos.append(5*i + j)
for i in w_pos:
    index = []
    for j in range(5):
        for k in range(5):
            if arena[j][k] == 4:
                index.append(5*j + k)
    corners = Aruco_Webcam.capture(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * 5 / shape[0])
    cy = int(int(mid[1]) * 5 / shape[1])
    a_pos = 5 * cy + cx
    print(a_pos)
    Move.move_bot(r, a_pos, i, ser, cap, index)
    print("Weapon Reached")
    Signal.stop(ser)
    time.sleep(1)
    Signal.down(ser)  # servo motor function
    time.sleep(1)
    Signal.right(ser)
    time.sleep(1)
    Signal.stop(ser)
    time.sleep(2)
    num = New_shape.give_shape(cap, i, r)
    index = []
    for j in range(5):
        for k in range(5):
            if arena[j][k] == num:
                index.append(5 * j + k)
    print(index)
    corners = Aruco_Webcam.capture(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * 5 / shape[0])
    cy = int(int(mid[1]) * 5 / shape[1])
    a_pos = 5 * cy + cx
    print(a_pos)
    Move.move_bot(r, a_pos, d_pos[0], ser, cap, index)
    Signal.stop(ser)
    time.sleep(1)
    Signal.up(ser)  # servo motor function
    time.sleep(1)
