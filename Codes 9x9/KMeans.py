import numpy as np
import cv2
from sklearn.cluster import KMeans


def get_simplified_photo():
    print("Select the arena for display")
    fromCenter = False
    showCrosshair = False
    img = cv2.imread("arena.jpg")
    r = cv2.selectROI("Image", img, fromCenter, showCrosshair)
    np.save("roi_data", r)
    cv2.destroyAllWindows()
    img = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    img_size = img.shape
    print("Applying KMeans")
    X = img.reshape(img_size[0] * img_size[1], img_size[2])
    km = KMeans(n_clusters=12)
    km.fit(X)
    X_compressed = km.cluster_centers_[km.labels_]
    X_compressed = np.clip(X_compressed.astype('uint8'), 0, 255)
    new_img = X_compressed.reshape(img_size[0], img_size[1], img_size[2])
    cv2.imwrite('arena_KMeans.jpg', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return r
