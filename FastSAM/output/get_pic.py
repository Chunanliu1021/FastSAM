import cv2

# 指定照片的路徑
image_path = './dogs.jpg'

# 使用cv2讀取照片
image = cv2.imread(image_path)

# 檢查照片是否成功讀取
if image is not None:
    # 顯示照片
    cv2.imshow('Image', image)
    
    # 等待用戶按下任意鍵後關閉視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"無法讀取照片: {image_path}")
