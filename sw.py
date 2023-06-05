from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pix2txt2pix import  recognize_image

class ImageChooser:
    def __init__(self, master):
        self.master = master
        self.master.title('图搜图')
        self.path = ''

        # 定义布局
        self.btn_open = Button(master, text='打开图片文件', command=self.open_file)
        self.btn_open.pack(padx=10, pady=10)

        self.btn_open = Button(master, text='搜索', command=self.search_pix)
        self.btn_open.pack(padx=10, pady=10)

        self.label_img = Label(master)
        self.label_img.pack(padx=10, pady=10)

    # 打开文件对话框，选择要打开的图片文件
    def open_file(self):
        path = filedialog.askopenfilename(title='选择一张图片', filetypes=[('Image files', '*.jpg;*.png;*.jpeg')])
        if path is not None and path != '':
            self.path = path
            self.load_image()

    # 加载图片文件，并将其显示到界面上
    def load_image(self):
        image = Image.open(self.path)
        image = ImageTk.PhotoImage(image)  # 将PIL图像转换为Tkinter可以显示的格式
        self.label_img.configure(image=image)
        self.label_img.image = image  # 更新引用防止图片被垃圾回收清除

    def search_pix(self):
        recognize_image(self.path,
                        "models/")


if __name__ == '__main__':
    print("...Loading...")
    print("...耐心等待一下，生成完图片，会自动打开文件夹的哦~...")
    root = Tk()
    ImageChooser(root)
    root.mainloop()