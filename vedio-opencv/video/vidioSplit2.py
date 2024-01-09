import cv2

cap = cv2.VideoCapture("./query_video/0001设备管理.wmv")
c = 1
timeRate = 10  # 截取视频帧的时间间隔（这里是每隔10秒截取一帧）

while (True):
    ret, frame = cap.read()
    FPS = cap.get(5)
    if ret:
        # 因为cap.get(5)获取的帧数不是整数，所以需要取整一下（向下取整用int，四舍五入用round，向上取整需要用math模块的ceil()方法）
        frameRate = int(FPS) * timeRate
        if (c % frameRate == 0):
            print("开始截取视频第：" + str(c) + " 帧")
            # 这里就可以做一些操作了：显示截取的帧图片、保存截取帧到本地
            # 这里是将截取的图像保存在本地
            cv2.imwrite("./capture_image2/" + str(c) + '.jpg', frame)
        c += 1
        cv2.waitKey(0)
    else:
        print("所有帧都已经保存完成")
        break
cap.release()