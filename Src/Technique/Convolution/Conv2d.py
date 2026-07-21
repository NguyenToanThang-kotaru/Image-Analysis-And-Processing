import cv2 as cv
import numpy as np

class Conv2D:
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int) -> None:
        # Init the input channel, output channel (feature map) and kernel size
        # Ex inputChannel is RGB -> 3x3. 
        # If number of filtermap is 16 then out_channels is 16
        # The size of filter map expected is 3x3 so kernelSize is 3 too
        
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        
                
        # Initialize WEIGHTS
        # Each filter has the shape: (kernel_size, kernel_size, in_channels)
        # Stacking 'out_channels' filters results in a 4D weight tensor:
        # Shape: (out_channels, kernel_size, kernel_size, in_channels)
        # We use np.random.randn for random initialization to break symmetry, 
        # allowing the CNN to learn diverse features.
        self.filters = np.random.randn(out_channels, kernel_size, kernel_size, in_channels) * 0.1
        
        # Bias: Each filter has a bias term added to its output.
        self.bias = np.random.randn(out_channels) * 0.1
    def set_edge_detection_filter(self):
        """
        THÊM MỚI: Thiết lập thủ công Filter số 0 thành bộ lọc phát hiện cạnh (Edge Detection).
        Mục đích: Để dễ dàng thấy kết quả tích chập hình ảnh thay vì nhiễu ngẫu nhiên.
        """
        assert self.kernel_size == 3, "Hàm này giả định kernel size là 3x3"
        
        # Ma trận 3x3 dùng để phát hiện cạnh ngang (dạng Sobel/Prewitt)
        # Các trọng số này giúp làm nổi bật sự thay đổi cường độ sáng theo chiều dọc
        edge_kernel = np.array([
            [-1, -1, -1],
            [ 0,  0,  0],
            [ 1,  1,  1]
        ])
        
        # Áp dụng bộ lọc này cho cả 3 channel RGB (Màu Đỏ, Xanh lục, Xanh lam)
        # Filter thứ 0 sẽ chứa ma trận này
        for c in range(self.in_channels):
            self.filters[0, :, :, c] = edge_kernel
            
        self.bias[0] = 0.0 # Bỏ bias đi để thấy rõ viền
        
        print("Đã thiết lập Filter 0 thành bộ lọc phát hiện cạnh ngang.")
    def forward(self, input_image: np.ndarray) -> np.ndarray:
        """
            Implement the convolution throught image
            input_image: The input data (H,W,C)
        """
        H,W,C = input_image.shape
        if C != self.in_channels:
            return (f"Error, conv2d Require {self.in_channels} but argument just have {C} channel")
        
        K = self.kernel_size
        
        out_H = H - K + 1
        out_W = W - K + 1
        
        output = np.zeros((out_H, out_W, self.out_channels))
        print(f"Performing convolution... The window will slide across {out_H}x{out_W} positions.") 
        for h in range(out_H):
            for w in range(out_W):
                
                # Trích xuất một khối (patch) từ ảnh đầu vào tại vị trí hiện tại
                # Khối này có chiều sâu bằng toàn bộ số channel của đầu vào (Ví dụ: 3x3x3)
                image_patch = input_image[h:h+K, w:w+K, :]
                
                # Tính toán giá trị cho từng filter (từng feature map đầu ra)
                for f in range(self.out_channels):
                    # Nhân chập: Lấy patch ảnh nhân (element-wise) với filter thứ f
                    # Sau đó cộng tổng tất cả lại (np.sum) và cộng thêm bias
                    conv_value = np.sum(image_patch * self.filters[f]) + self.bias[f]
                    
                    # Ghi giá trị duy nhất này vào đúng pixel tương ứng của feature map thứ f
                    output[h, w, f] = conv_value
                    
        return output
