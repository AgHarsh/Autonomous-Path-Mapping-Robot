import numpy as np
import Aruco_Webcam
import Path_mom
import numpy.linalg as la
import Signal
import time


def bot_vec(r, ser, cap):
    corners = Aruco_Webcam.photu_de(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners[0, 0, :, :]
    mu = (corners[0, :] + corners[1, :]) / 2
    md = (corners[2, :] + corners[3, :]) / 2
    mid = (mu + md) / 2
    print("mu:", mu, "md:", md, "mid:", mid)
    return mu, md, mid


def mover(n, r, src, end, ser, cap, index):
    path_x, path_y = Path_mom.path_vec(n, src, end, index)
    last_x = path_x[-1]
    last_y = path_y[-1]
    for i in range(len(path_x) - 1):
        mu, md, mid = bot_vec(r, ser, cap)
        pv = [path_x[i + 1] - mid[0], path_y[i + 1] - mid[1]]
        pv = np.asarray(pv)
        bv = mu - md
        angle = np.angle(complex(bv[0], bv[1]) / complex(pv[0], pv[1]), deg=True)
        print("new pv:", pv, "midf:", mid)
        while (la.norm(np.asarray([path_x[i + 1] - mid[0], path_y[i + 1] - mid[1]])) > 20 and (
                path_x[i + 1] != last_x or path_y[i + 1] != last_y)) or angle > 5 or angle < -5:
            print("new distance:", la.norm(np.asarray([path_x[i + 1] - mid[0], path_y[i + 1] - mid[1]])))
            bv = mu - md
            # print(bv, pv)
            # angle = ((np.cross(bv, pv)) / (la.norm(bv) * la.norm(pv))) * 180 / np.pi
            angle = np.angle(complex(bv[0], bv[1]) / complex(pv[0], pv[1]), deg=True)
            m = 0.01
            m1 = 0.003
            c = 0.08
            c1 = 0.02
            print("angle", angle)
            if angle > 5:
                Signal.left(ser)
                time.sleep(m1 * angle + c1)
                Signal.stop(ser)
            elif angle < -5:
                Signal.right(ser)
                time.sleep(-1 * m1 * angle + c1)
                Signal.stop(ser)
            elif la.norm(np.asarray([path_x[i + 1] - mid[0], path_y[i + 1] - mid[1]])) > 20 and (
                    path_x[i + 1] != last_x or path_y[i + 1] != last_y):
                Signal.fwd(ser)
                time.sleep(m * (la.norm(np.asarray([path_x[i + 1] - mid[0], path_y[i + 1] - mid[1]]))) + c)
                Signal.stop(ser)
            Signal.stop(ser)
            time.sleep(0.03)
            mu, md, mid = bot_vec(r, ser, cap)


"""
import serial
cap = cv2.VideoCapture(1)
time.sleep(2)
ser = serial.Serial('COM4', 9600)
time.sleep(2)
ser.write(b'S')
print("All done")
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite("arena.jpg", frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
cv2.destroyAllWindows()
r = np.load("roi_data.npy")
index = []
mover(9, r, 2, 20, ser, cap, index)
"""
