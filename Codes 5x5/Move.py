import numpy as np
import numpy.linalg as la
import time
import Aruco_Webcam
import Path_mom
import Signal


def bot_vec(r, ser, cap):
    corners = Aruco_Webcam.capture(r, ser, cap)
    corners = np.asarray(corners)
    corners = corners[0, 0, :, :]
    mu = (corners[0, :] + corners[1, :])/2
    md = (corners[2, :] + corners[3, :])/2
    mid = (mu + md)/2
    print("mu:", mu, "md:", md, "mid:", mid)
    return mu, md, mid


def move_bot(r, src, end, ser, cap, index):
    path_x, path_y = Path_mom.path_vec(src, end, index)
    last_x = path_x[-1]
    last_y = path_y[-1]
    for i in range(len(path_x)-1):
        mu, md, mid = bot_vec(r, ser, cap)
        pv = [path_x[i + 1] - mid[0], path_y[i + 1] - mid[1]]
        pv = np.asarray(pv)
        bv = mu - md
        angle = np.angle(complex(bv[0], bv[1]) / complex(pv[0], pv[1]), deg=True)
        while (la.norm(np.asarray([path_x[i+1] - mid[0], path_y[i+1] - mid[1]])) > 2 and (path_x[i+1] != last_x or path_y[i+1] != last_y)) or angle > 5 or angle < -5:
            bv = mu - md
            angle = np.angle(complex(bv[0], bv[1])/complex(pv[0], pv[1]), deg=True)
            m = 0.01
            m1 = 0.003
            c = 0.08
            c1 = 0.02
            if angle > 5:
                Signal.left(ser)
                time.sleep(m1*angle + c1)
                Signal.stop(ser)
            elif angle < -5:
                Signal.right(ser)
                time.sleep(-1*m1*angle + c1)
                Signal.stop(ser)
            elif la.norm(np.asarray([path_x[i+1] - mid[0], path_y[i+1] - mid[1]])) > 2 and (path_x[i+1] != last_x or path_y[i+1] != last_y):
                Signal.fwd(ser)
                time.sleep(m*(la.norm(np.asarray([path_x[i+1] - mid[0], path_y[i+1] - mid[1]]))) + c)
                Signal.stop(ser)
            mu, md, mid = bot_vec(r, ser, cap)
