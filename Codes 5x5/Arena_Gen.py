import numpy as np
import cv2


def generate_arena():
    im = cv2.imread("arena_KMeans.jpg")     # Image for thresholding

    showCrosshair = False
    fromCenter = False
    arena = np.zeros([5, 5], dtype=int)
    arena_mom_x = np.zeros([5, 5], dtype=float)
    arena_mom_y = np.zeros([5, 5], dtype=float)
    shape = im.shape

    for i in range(2):  # 0 for red and 1 for yellow
        r = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # first time color selection
        imcrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        r1 = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # second time color selection
        imcrop1 = im[int(r1[1]):int(r1[1] + r1[3]), int(r1[0]):int(r1[0] + r1[2])]
        imcropmin = [imcrop[:, :, 0].min(), imcrop[:, :, 1].min(), imcrop[:, :, 2].min()]
        imcropmax = [imcrop[:, :, 0].max(), imcrop[:, :, 1].max(), imcrop[:, :, 2].max()]
        imcrop1min = [imcrop1[:, :, 0].min(), imcrop1[:, :, 1].min(), imcrop1[:, :, 2].min()]
        imcrop1max = [imcrop1[:, :, 0].max(), imcrop1[:, :, 1].max(), imcrop1[:, :, 2].max()]
        cv2.destroyAllWindows()
        thresh = 25  # for having correct range of colors
        minBGR = np.array([min(imcropmin[0], imcrop1min[0]) - thresh, min(imcropmin[1], imcrop1min[1]) - thresh,
                           min(imcropmin[2], imcrop1min[2]) - thresh])
        maxBGR = np.array([max(imcropmax[0], imcrop1max[0]) + thresh, max(imcropmax[1], imcrop1max[1]) + thresh,
                           max(imcropmax[2], imcrop1max[2]) + thresh])
        if i == 0:
            np.save("Red_Range", [minBGR, maxBGR])
        elif i == 1:
            np.save("Yellow_Range", [minBGR, maxBGR])

        maskBGR = cv2.inRange(im, minBGR, maxBGR)
        kernel = np.ones((5, 5), np.uint8)
        maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
        contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            M = cv2.moments(cnt)
            area = cv2.contourArea(cnt)
            if area > 100:
                cv2.drawContours(im, [cnt], 0, 0, 3)
                x, y, w, h = cv2.boundingRect(cnt)
                rect_area = w * h
                extent = float(area) / rect_area
                cx = int((int(M['m10'] / M['m00']) / shape[0]) * 5)
                cy = int((int(M['m01'] / M['m00']) / shape[1]) * 5)

                # red circle is 1 red square is 2 yellow circle is 3 and yellow square is 4
                if extent < 0.8:  # circle
                    if i == 0:
                        j = 1
                    else:
                        j = 3
                elif extent >= 0.8:  # square
                    if i == 0:
                        j = 2
                    else:
                        j = 4
                arena[cy][cx] = j
                arena_mom_x[cy][cx] = M['m10'] / M['m00']
                arena_mom_y[cy][cx] = M['m01'] / M['m00']
    cv2.imshow("Arena", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    np.save("arena_mom_x", arena_mom_x)
    np.save("arena_mom_y", arena_mom_y)
    return arena, shape
