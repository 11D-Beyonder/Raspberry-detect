from picamera import PiCamera

camera = PiCamera() #得到摄像头实例

camera.resolution = (1024, 768) # 设置分辨率
camera.rotation = 180 # 控制摄像头旋转180度

def capture():
    camera.capture('./data/state.jpg') #拍摄并保存图片到当前目录
