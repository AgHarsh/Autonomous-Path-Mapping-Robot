import numpy as np
import cv2
import time
import serial
import KMeans
import Arena_Gen
import Death_E
import jail_manage
import Aruco_Webcam
import move
import Signal
import new_thres

print("Enter arena size")
print("----------------")
n = 9   # dimensions of the arena
print(n)

cap = cv2.VideoCapture(1)   # For starting camera
# cap.set(3, 1280)
# cap.set(4, 960)
time.sleep(2)
ser = serial.Serial('COM4', 9600)   # Starting Arduino Signal
time.sleep(2)
ser.write(b'S')
print("Setup All Done")

while True:     # For taking first pic
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite("arena.jpg", frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
cv2.destroyAllWindows()

r = KMeans.get_simplified_photo()   # For applying ML on the arena.jpg
arena, arena_mom_x, arena_mom_y, shape = Arena_Gen.thresholding(n)   # For recognizing shapes of red and yellow figures
death_e, weapons, hoc_bg, jail = Death_E.dabba(n)    # For recognizing death eater, weapons, jail and real hocruxes

jail_pos = jail_manage.jails(n, jail, death_e)
jailer = 0

d_pos = []
for i in range(n):
    for j in range(n):
        if death_e[i][j]:
            d_pos.append(n*i + j)
Signal.up(ser)
time.sleep(5)
for i in d_pos:
    index = []
    for j in range(9):
        for k in range(9):
            if arena[j][k] == 4:
                index.append(9*j + k)
    corners = Aruco_Webcam.photu_de(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * n / shape[0])
    cy = int(int(mid[1]) * n / shape[1])
    a_pos = n * cy + cx
    print(a_pos)
    move.mover(n, r, a_pos, i, ser, cap, index)
    print("Death Eater Reached")
    Signal.fwd(ser)
    time.sleep(0.4)
    Signal.stop(ser)
    time.sleep(1)
    Signal.down(ser)    # servo motor function
    time.sleep(1)

    corners = Aruco_Webcam.photu_de(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * n / shape[0])
    cy = int(int(mid[1]) * n / shape[1])
    a_pos = n * cy + cx
    print(a_pos)
    move.mover(n, r, a_pos, jail_pos[jailer], ser, cap, index)
    jailer += 1
    print("Death Eater at Azkabban")
    Signal.stop(ser)
    time.sleep(1)
    Signal.up(ser)  # servo motor function
    time.sleep(1)
    # num = new_thres.give_shape(n, cap, arena, i, r)


w_pos = []
for i in range(n):
    for j in range(n):
        if weapons[i][j]:
            w_pos.append(n*i + j)
for i in w_pos:
    index = []
    for j in range(n):
        for k in range(n):
            if arena[j][k] == 4:
                index.append(n*j + k)
    corners = Aruco_Webcam.photu_de(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * n / shape[0])
    cy = int(int(mid[1]) * n / shape[1])
    a_pos = n * cy + cx
    print(a_pos)
    move.mover(n, r, a_pos, i, ser, cap, index)
    print("Weapon Reached")
    Signal.stop(ser)
    time.sleep(1)
    Signal.down(ser)  # servo motor function
    time.sleep(1)
    Signal.right(ser)
    time.sleep(1)
    Signal.stop(ser)
    time.sleep(2)
    num = new_thres.give_shape(n, cap, arena, i, r)
    index = []
    for j in range(n):
        for k in range(n):
            if arena[j][k] == num:
                index.append(n * j + k)
    print(index)
    corners = Aruco_Webcam.photu_de(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners.reshape(4, 2)
    mid = 0
    for j in range(4):
        mid = mid + corners[j]
    mid = mid / 4
    cx = int(int(mid[0]) * n / shape[0])
    cy = int(int(mid[1]) * n / shape[1])
    a_pos = n * cy + cx
    print(a_pos)
    move.mover(n, r, a_pos, d_pos[0], ser, cap, index)
    Signal.stop(ser)
    time.sleep(1)
    Signal.up(ser)  # servo motor function
    time.sleep(1)
