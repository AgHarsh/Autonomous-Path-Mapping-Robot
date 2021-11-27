import numpy as np
import cv2
from sklearn.cluster import KMeans


def refine_image():
    # Resizing the main arena
    img = cv2.imread("arena.jpg")
    roiData = cv2.selectROI("Image", img, fromCenter=False, showCrosshair=False)
    np.save("roi_data", roiData)
    cv2.destroyAllWindows()

    # Applying KMeans for clustering multiple RGB values of same color
    img = img[int(roiData[1]):int(roiData[1] + roiData[3]), int(roiData[0]):int(roiData[0] + roiData[2])]
    img_size = img.shape
    X = img.reshape(img_size[0] * img_size[1], img_size[2])
    km = KMeans(n_clusters=12)
    km.fit(X)
    X_compressed = km.cluster_centers_[km.labels_]
    X_compressed = np.clip(X_compressed.astype('uint8'), 0, 255)
    new_img = X_compressed.reshape(img_size[0], img_size[1], img_size[2])
    cv2.imwrite('arena_KMeans.jpg', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return roiData
