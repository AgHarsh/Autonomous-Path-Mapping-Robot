import cv2
import numpy as np
from sklearn.cluster import KMeans


def give_shape(n, arena, w_pos, r):
    ret, frame = cap.read()
    cv2.imwrite("new_a.jpg", frame)
    # frame = cv2.imread("new_a.jpg")
    frame = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    shape = frame.shape
    print(shape)
    y_pos = int(w_pos / n)
    x_pos = w_pos % n
    print(y_pos, x_pos)

    nr = [(shape[0] / n) * x_pos, (shape[1] / n) * y_pos, (shape[0] / n) * (x_pos + 1), (shape[1] / n) * (y_pos + 1)]
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
    kernel = np.ones((n, n), np.uint8)

    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    # cv2.imshow("kernel", maskBGR)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    num = 0
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
    kernel = np.ones((n, n), np.uint8)
    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    # cv2.imshow("kernel", maskBGR)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
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
    arena[y_pos][x_pos] = num
    print(num)
    return num


"""arena = [[3, 4, 1, 0, 3, 0, 1, 4, 3],
         [4, 2, 2, 3, 1, 2, 1, 2, 4],
         [3, 1, 1, 3, 3, 3, 3, 2, 1],
         [0, 4, 4, 4, 1, 1, 2, 2, 0],
         [3, 2, 0, 3, 0, 2, 0, 4, 1],
         [0, 1, 4, 2, 4, 4, 3, 3, 0],
         [3, 1, 2, 1, 1, 4, 1, 4, 1],
         [4, 2, 2, 4, 2, 3, 2, 2, 4],
         [3, 4, 1, 0, 0, 0, 1, 4, 3]]
r = np.load("roi_data.npy")
give_shape(9, arena, 3, r)"""
