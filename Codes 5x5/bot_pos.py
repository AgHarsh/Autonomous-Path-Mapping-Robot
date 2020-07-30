import Aruco_Webcam


def pos_de():
    corners = Aruco_Webcam.photu_de()
    mid = 0
    for i in range(3):
        mid = mid + corners[i, :]
    mid = mid / 4
    cx = int((int(mid[0]) / shape[0]) * 5)
    cy = int((int(mid[1]) / shape[1]) * 5)
    pos = 5 * cy + cx
    return pos
