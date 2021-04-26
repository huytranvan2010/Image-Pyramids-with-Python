import imutils

def pyramid(image, scale=1.5, minSize=(30, 30)):    # minSize là (width, height)
    """ Tạo image pyramid bằng OpenCV """
    # xuất ra ảnh gốc
    yield image     # dùng yield xuất xong ảnh gốc khi gọi đến nó tiếp nó sẽ chạy xuống dưới

    while True:
        # tính size mới và resize ảnh
        w = int(image.shape[1] / scale)     # thay đổi width này
        image = imutils.resize(image, width=w)

        # nếu kích thước ảnh nhỏ hơn minimum size yêu cầu (theo bất cứ chiều nào) thì dừng, thoát luôn
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break 

        # xuất ra ảnh tiếp theo với size nhỏ hơn
        yield image