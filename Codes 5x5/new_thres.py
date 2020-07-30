import cv2
import numpy as np
import time
from sklearn.cluster import KMeans


def give_shape(cap, arena, w_pos, r):
    ret, frame = cap.read()
    cv2.imwrite("new_a.jpg", frame)
    frame = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    shape = frame.shape
    print(shape)
    y = int(w_pos / 5)
    x = w_pos % 5
    print(y, x)

    nr = [(shape[0]/5) * x, (shape[1]/5) * y, (shape[0]/5) * (x+1), (shape[1]/5) * (y+1)]
    print(nr)
    frame = frame[int(nr[1]):int(nr[3]), int(nr[0]):int(nr[2])]

    img_size = frame.shape
    X = frame.reshape(img_size[0] * img_size[1], img_size[2])
    km = KMeans(n_clusters=12)
    km.fit(X)
    X_compressed = km.cluster_centers_[km.labels_]
    X_compressed = np.clip(X_compressed.astype('uint8'), 0, 255)
    new_img = X_compressed.reshape(img_size[0], img_size[1], img_size[2])
    red_range = np.load("Red_Range.npy")
    yellow_range = np.load("Yellow_Range.npy")
    maskBGR = cv2.inRange(new_img, red_range[0], red_range[1])
    kernel = np.ones((5, 5), np.uint8)

    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    cv2.imshow("kernel", maskBGR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            rect_area = w * h
            extent = float(area) / rect_area
            # red circle is 1 red square is 2 yellow circle is 3 and yellow square is 4
            if extent < 0.8:  # circle
                num = 1
            elif extent >= 0.8:  # square
                num = 2
    maskBGR = cv2.inRange(new_img, yellow_range[0], yellow_range[1])
    kernel = np.ones((5, 5), np.uint8)
    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    cv2.imshow("kernel", maskBGR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            rect_area = w * h
            extent = float(area) / rect_area
            # red circle is 1 red square is 2 yellow circle is 3 and yellow square is 4
            if extent < 0.8:  # circle
                num = 3
            elif extent >= 0.8:  # square
                num = 4
    print(num)
    return num

