import cv2 as cv
import numpy as np
import os
from Conv2d import Conv2D

BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, "..", "..", "..", "Images", "lena_std.tif")

image = cv.imread(image_path)
if __name__ == "__main__":
    # Load ảnh theo đường dẫn của bạn
    
    # Tạo một ảnh numpy giả nếu không tìm thấy file thật để code vẫn chạy được
    if not os.path.exists(image_path):
        print(f"Không tìm thấy ảnh tại {image_path}. Khởi tạo ảnh giả ngẫu nhiên 320x320x3 để test...")
        image = np.random.randint(0, 256, (320, 320, 3), dtype=np.uint8)
    else:
        image = cv.imread(image_path)
    
    # Tiền xử lý chuẩn Deep Learning: Đưa giá trị pixel về dải [0, 1] để tính toán ổn định
    image_normalized = image.astype('float32') / 255.0
    
    # Resize nhỏ lại một chút (ví dụ 100x100) để code Python thuần chạy nhanh hơn. 
    # (Vì vòng lặp for lồng nhau trong Python khá chậm so với GPU/C++)
    image_resized = cv.resize(image_normalized, (100, 100))
    
    print("Thông số đầu vào:")
    print(f"- Kích thước ảnh gốc: {image.shape}")
    print(f"- Kích thước ảnh sau resize đưa vào CNN: {image_resized.shape}")
    print("-" * 40)
    
    # ---------------------------------------------------------
    # BƯỚC QUAN TRỌNG: KHỞI TẠO LAYER VÀ THIẾT LẬP KERNEL
    # ---------------------------------------------------------
    
    # Khởi tạo layer
    conv_layer = Conv2D(in_channels=3, out_channels=16, kernel_size=3)
    
    # Ép filter 0 thành bộ lọc có cấu trúc rõ ràng (thay vì nhiễu ngẫu nhiên)
    # conv_layer.set_edge_detection_filter()
    
    # Quét ảnh qua layer Convolution
    feature_maps = conv_layer.forward(image_resized)
    
    print("-" * 40)
    print("Kết quả sau tích chập:")
    print(f"- Kích thước Feature Maps: {feature_maps.shape}")
    
    # ---------------------------------------------------------
    # TRỰC QUAN HÓA (Tùy chọn: Lưu Feature Map đầu tiên ra xem)
    # ---------------------------------------------------------
    # Lấy ra Feature Map số 0 (trong số 16 cái)
    fm_0 = feature_maps[:, :, 0]
    
    # Lấy trị tuyệt đối vì phát hiện cạnh có thể sinh số âm (chuyển đổi từ sáng sang tối)
    fm_0_abs = np.abs(fm_0)
    
    # Chuyển đổi lại về dải màu [0, 255] để lưu ảnh bằng OpenCV
    fm_0_normalized = cv.normalize(fm_0_abs, None, 0, 255, cv.NORM_MINMAX)
    fm_0_img = fm_0_normalized.astype(np.uint8)
    
    output_path = os.path.join(BASE_DIR, "feature_map_edge.jpg")
    cv.imwrite(output_path, fm_0_img)
    print(f"- Đã lưu Feature Map phát hiện cạnh ra ảnh tại: {output_path}")