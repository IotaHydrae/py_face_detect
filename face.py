# encoding:utf-8
from tkinter import *
import requests
import base64
import get_token
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        # 使用网格布局
        self.grid()
        self.create_widgets()
        
    def openfile(self):
        print('opening')
        self.label_file.delete("0", END)
        file_url = filedialog.askopenfilename(title='选择图片文件', filetypes=[('JPG', '*.jpg'), ('PNG', '*.png')])
        self.label_file.insert(END, file_url)
        
    def create_widgets(self):
        self.button_open = Button(self, text='打开', command=self.openfile)
        self.button_open.grid(row=0, column=0)
        self.label_file = Entry(self)
        self.label_file.grid(row=0, column=1)
        self.button_detect = Button(self, text='识别', command=self.detect)
        self.button_detect.grid(row=1)
    def detect(self):
        file_url = self.label_file.get()
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        # 二进制方式打开图片文件
        f = open(file_url, 'rb')
        img = base64.b64encode(f.read())
        
        img_url ='https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=15d6a6b676899e51788e3d127a9cbe0e/902397dda144ad3479aef2ccdda20cf431ad8563.jpg'
        
        params = {"image":img,"image_type":'BASE64'}
        access_token = get_token.get_token()
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        result = face_num = response.json()['result']
        face_num = result['face_num']
        face_list = result['face_list']
        # 66edab90d929f6d4c2a75feb8f85bf82
        # print(face_list)
        img2 = Image.open(file_url)
        img2.show()
        draw = ImageDraw.Draw(img2)
        location = face_list[0]['location']
        left = location['left']
        top = location['top']
        width = location['width']+left
        height = location['height']+top
        right = left+width
        bottom = top+height
        
        face_probability = face_list[0]['face_probability']
        xy = [left,top,width,height]
        print(xy)
        draw.text((left, top-10), 'face', fill=(255,0,0))
        draw.rectangle(xy, outline=(255,0,0), width=2)
        plt.imshow(img2)
        plt.show()
        print('Confidence: ',face_probability*100,'%')
        
if __name__ == "__main__":
    root = Tk()
    root.title('人脸检测')
    root.geometry('250x100')
    app = Application(root)
    app.mainloop()  