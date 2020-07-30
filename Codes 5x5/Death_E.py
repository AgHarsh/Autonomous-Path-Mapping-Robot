import numpy as np
import cv2


def dabba():
    im = cv2.imread("arena_Kmeans.jpg")     # Image for thresholding
    showCrosshair = False
    fromCenter = False
    hoc_bg = np.zeros([5, 5], dtype=int)
    shape = im.shape
    hoc_bg[0][0] = 1
    hoc_bg[4][0] = 1
    hoc_bg[0][4] = 1
    hoc_bg[4][4] = 1

    """r = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # first time color selection
    imcrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    r1 = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # second time color selection
    imcrop1 = im[int(r1[1]):int(r1[1] + r1[3]), int(r1[0]):int(r1[0] + r1[2])]

    imcropmin = [imcrop[:, :, 0].min(), imcrop[:, :, 1].min(), imcrop[:, :, 2].min()]
    imcropmax = [imcrop[:, :, 0].max(), imcrop[:, :, 1].max(), imcrop[:, :, 2].max()]
    imcrop1min = [imcrop1[:, :, 0].min(), imcrop1[:, :, 1].min(), imcrop1[:, :, 2].min()]
    imcrop1max = [imcrop1[:, :, 0].max(), imcrop1[:, :, 1].max(), imcrop1[:, :, 2].max()]

    thresh = 5  # for having corr0ect range of colors
    minBGR = np.array([min(imcropmin[0], imcrop1min[0]) - thresh, min(imcropmin[1], imcrop1min[1]) - thresh,
                       min(imcropmin[2], imcrop1min[2]) - thresh])
    maxBGR = np.array([max(imcropmax[0], imcrop1max[0]) + thresh, max(imcropmax[1], imcrop1max[1]) + thresh,
                       max(imcropmax[2], imcrop1max[2]) + thresh])
    maskBGR = cv2.inRange(im, minBGR, maxBGR)
    kernel = np.ones((5, 5), np.uint8)
    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('erode_mask', maskBGR)
    for cnt in contours:
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        if area > 1500:
            cv2.drawContours(im, [cnt], 0, 0, 3)
            cv2.imshow("image", im)
            cx = int((int(M['m10'] / M['m00']) / shape[0]) * 5)
            cy = int((int(M['m01'] / M['m00']) / shape[1]) * 5)
            hoc_bg[cy][cx] = 1
    cv2.destroyAllWindows()"""
    death_e = np.zeros([5, 5], dtype=int)
    weapons = np.zeros([5, 5], dtype=int)

    r = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # first time color selection
    imcrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    r1 = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # second time color selection
    imcrop1 = im[int(r1[1]):int(r1[1] + r1[3]), int(r1[0]):int(r1[0] + r1[2])]

    imcropmin = [imcrop[:, :, 0].min(), imcrop[:, :, 1].min(), imcrop[:, :, 2].min()]
    imcropmax = [imcrop[:, :, 0].max(), imcrop[:, :, 1].max(), imcrop[:, :, 2].max()]
    imcrop1min = [imcrop1[:, :, 0].min(), imcrop1[:, :, 1].min(), imcrop1[:, :, 2].min()]
    imcrop1max = [imcrop1[:, :, 0].max(), imcrop1[:, :, 1].max(), imcrop1[:, :, 2].max()]

    thresh = 10  # for having correct range of colors
    minBGR = np.array([min(imcropmin[0], imcrop1min[0]) - thresh, min(imcropmin[1], imcrop1min[1]) - thresh,
                       min(imcropmin[2], imcrop1min[2]) - thresh])
    maxBGR = np.array([max(imcropmax[0], imcrop1max[0]) + thresh, max(imcropmax[1], imcrop1max[1]) + thresh,
                       max(imcropmax[2], imcrop1max[2]) + thresh])
    maskBGR = cv2.inRange(im, minBGR, maxBGR)
    kernel = np.ones((5, 5), np.uint8)
    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('erode_mask', maskBGR)
    for cnt in contours:
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(im, [cnt], 0, 0, 3)
            cv2.imshow("image", im)
            cx = int((int(M['m10'] / M['m00']) / shape[0]) * 5)
            cy = int((int(M['m01'] / M['m00']) / shape[1]) * 5)
            weapons[cy][cx] = 1
            if weapons[cy][cx] == hoc_bg[cy][cx]:
                death_e[cy][cx] = 1
    weapons = weapons - death_e
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    np.save("death_e", death_e)
    np.save("weapons", weapons)
    np.save("true_hoc", hoc_bg)
    return death_e, weapons, hoc_bg
