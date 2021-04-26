# Cách chạy
# python image_pyramid.py --image images/dog.jpg
import cv2
from skimage.transform import pyramid_gaussian
from hammiu import pyramid
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
ap.add_argument("-s", "--scale", type=float, default=2, help="scale factor size")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Cách 1: Tạo image pyramid sử dụng OpenCV
for (i, resized) in enumerate(pyramid(image, scale=args["scale"])):
    cv2.imshow("Layer {}".format(i + 1), resized)
    cv2.waitKey(0)

# Cách 2: Tạo image pyramid sử dụng scikit image
# Chú ý phần này ngoài resize còn áp dụng thêm Gaussian smoothiing
for (i, resized) in enumerate(pyramid_gaussian(image, downscale=2, multichannel=True)):
    # nếu chiều nào của ảnh nhỏ hơn min thì thoát khỏi vòng lặp
    if resized.shape[0] < 30 or resized.shape[1] < 30:
        break 

    # hiển thị các ảnh đã resize
    cv2.imshow("Layer {}".format(i + 1),  resized)
    cv2.waitKey(0)

