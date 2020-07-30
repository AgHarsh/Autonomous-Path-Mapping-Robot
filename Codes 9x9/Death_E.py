import numpy as np
import cv2


def dabba(n):
    print("Running Death_E.dabba")
    im = cv2.imread("arena_KMeans.jpg")     # Image for thresholding
    showCrosshair = False
    fromCenter = False
    hoc_bg = np.zeros([n, n], dtype=int)
    hoc_bg[0][3] = 1
    hoc_bg[0][5] = 1
    hoc_bg[4][2] = 1
    hoc_bg[4][6] = 1
    print("Select Green Background")

    shape = im.shape
    """
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
    kernel = np.ones((n, n), np.uint8)
    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        print(area)
        if area > 300:
            print(area)
            cv2.drawContours(im, [cnt], 0, 0, 3)
            cv2.imshow("image", im)
            cx = int((int(M['m10'] / M['m00']) / shape[0]) * n)
            cy = int((int(M['m01'] / M['m00']) / shape[1]) * n)
            hoc_bg[cy][cx] = 1
    cv2.destroyAllWindows()
"""
    print("Select Blue Region")
    jail = np.zeros([n, n], dtype=int)
    """
    r = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # first time color selection
    imcrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    r1 = cv2.selectROI("Image", im, fromCenter, showCrosshair)  # second time color selection
    imcrop1 = im[int(r1[1]):int(r1[1] + r1[3]), int(r1[0]):int(r1[0] + r1[2])]
    imcropmin = [imcrop[:, :, 0].min(), imcrop[:, :, 1].min(), imcrop[:, :, 2].min()]
    imcropmax = [imcrop[:, :, 0].max(), imcrop[:, :, 1].max(), imcrop[:, :, 2].max()]
    imcrop1min = [imcrop1[:, :, 0].min(), imcrop1[:, :, 1].min(), imcrop1[:, :, 2].min()]
    imcrop1max = [imcrop1[:, :, 0].max(), imcrop1[:, :, 1].max(), imcrop1[:, :, 2].max()]
    thresh = 15  # for having corr0ect range of colors
    minBGR = np.array([min(imcropmin[0], imcrop1min[0]) - thresh, min(imcropmin[1], imcrop1min[1]) - thresh,
                       min(imcropmin[2], imcrop1min[2]) - thresh])
    maxBGR = np.array([max(imcropmax[0], imcrop1max[0]) + thresh, max(imcropmax[1], imcrop1max[1]) + thresh,
                       max(imcropmax[2], imcrop1max[2]) + thresh])
    maskBGR = cv2.inRange(im, minBGR, maxBGR)
    kernel = np.ones((n, n), np.uint8)
    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        if area > 300:
            cv2.drawContours(im, [cnt], 0, 0, 3)
            cx = int((int(M['m10'] / M['m00']) / shape[0]) * n)
            cy = int((int(M['m01'] / M['m00']) / shape[1]) * n)
            x, y, w, h = cv2.boundingRect(cnt)
            print(cy,cx)
            jail[cy][cx] = 1
            if area > 700:
                if w > 2*h:
                    jail[cy][cx - 1] = 10
                    jail[cy][cx + 1] = 10
                elif h > 2*w:
                    jail[cy - 1][cx] = 10
                    jail[cy + 1][cx] = 10
    cv2.destroyAllWindows()
    """
    jail[8][3] = -1
    jail[8][4] = 1
    jail[8][5] = -1
    jail[4][4] = 1
    print("Select White")
    death_e = np.zeros([n, n], dtype=int)
    weapons = np.zeros([n, n], dtype=int)
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
    kernel = np.ones((n, n), np.uint8)
    maskBGR = cv2.erode(maskBGR, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(maskBGR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('erode_mask', maskBGR)
    for cnt in contours:
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(im, [cnt], 0, 0, 3)
            cv2.imshow("image", im)
            cx = int((int(M['m10'] / M['m00']) / shape[0]) * n)
            cy = int((int(M['m01'] / M['m00']) / shape[1]) * n)
            weapons[cy][cx] = 1
            if weapons[cy][cx] == hoc_bg[cy][cx]:
                weapons[cy][cx] = 0
                death_e[cy][cx] = 1
            elif jail[cy][cx] == -1:
                weapons[cy][cx] = 0
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    np.save("death_e", death_e)
    np.save("weapons", weapons)
    np.save("true_hoc", hoc_bg)
    np.save("jail", jail)
    print("Death Eaters:\n", death_e, "\nWeapons:\n", weapons, "\nTrue Hocruxes Backgrounds:\n", hoc_bg, "\nJails:\n", jail)
    return death_e, weapons, hoc_bg, jail
