# 图搜图
本项目实现以图搜类似图片的效果


<VER：1.0>
---------------------
2023-06-05 更新
图搜图版本

---------------------
## 简介：
🥇目前认知的能力在于模型本身，图片的生成考虑到生成时间和存储空间成本。舍弃了传统本地图像数据集和扩散模型生成
针对当前普通版的说明：
会继续维护普通版，对传入的图像，会生成6张类似的风格图片。识别的类别会在根目录创建一个识别文件夹，内含6张类似图片

----------------------
## 特别声明：
本项目只在Github发布和更新，如有问题，联系邮箱  2474842866@buaa.edu.cn

-----------------------
## 使用介绍：

1. 安装python配置环境，如requirement.txt文件中所示
pip install -r requirement.txt

2. 打开命令行到根目录，执行sw.py文件
python sw.py

3. 选择图片，选择完毕，程序框会出现图片
![image](https://github.com/haimianxing/pic_search_pic/assets/64762650/58c5b674-a49b-4fe4-98a4-c6448190b4e6)


4. 点击搜索
程序会分析所选图片，在网络上寻找同类似的图片，下载到本地。
耐心等待，会根据图片复杂度影响到速度。因为是单线程所写，程序可能会短暂失去响应，属于正常现象。
搜索完毕，会打开文件夹，看到类似搜索的图片
![image](https://github.com/haimianxing/pic_search_pic/assets/64762650/4a6a804c-0e7f-4e17-a9f9-66cc094e22f3)


-------------------------
# pic_search_pic
This project realizes the effect of searching similar graphs with graphs


---------------------

##Introduction:

🥇 At present, the ability of cognition lies in the model itself. The generation of pictures takes into account the cost of generation time and storage space. Traditional local image dataset and diffusion model generation are abandoned

Description for the current normal version:

The normal version will continue to be maintained. For the incoming images, 6 similar style images will be generated. The identified category will create an identification folder in the root directory, containing 6 similar pictures

-----------------------------
##Introduction to use:



1. install the python configuration environment, as shown in the requirement.txt file

PIP install -r requirement.txt



2. open the command line to the root directory and execute the sw.py file

Python sw.py

3. select a picture. After selection, the picture will appear in the program box

4. Click Search

The program will analyze the selected pictures, find similar pictures on the network, and download them locally.

Waiting patiently will affect the speed according to the complexity of the picture. Because it is written by a single thread, the program may lose response temporarily, which is a normal phenomenon.

After the search, the folder will be opened and a picture similar to the search will be displayed
