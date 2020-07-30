import cv2
import cv2.aruco as aruco
import Signal
import time


def photu_de(r, ser, cap):
    count = 0
    while True:
        ret, frame = cap.read()
        frame = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters = aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        if corners:
            return corners
        count += 1
        Signal.stop(ser)
        if count > 20:
            Signal.rev(ser)
            time.sleep(0.5)
            Signal.right(ser)
            time.sleep(0.5)
            Signal.left(ser)
            time.sleep(0.4)
            Signal.stop(ser)
        gray = aruco.drawDetectedMarkers(gray, corners)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
