'''
1 读入视频文件
2 抽帧,提取声音
3 按帧混合叠加（控制频率、亮度等）
4 组合视频
5 组合声音
'''

import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from moviepy.editor import CompositeAudioClip, VideoFileClip, AudioFileClip
import cv2
import os
import moviepy.editor as mpe


#
# # 获取音频
# prevideo = VideoFileClip('video.mp4')  # 视频所在路径
# audio = prevideo.audio
# audio.write_audiofile('video.mp3')  # 音频所在路径
#
# # # 获取fps:25
# # (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
# # if int(major_ver) < 3:
# #     fps1 = video.get(cv2.cv.CV_CAP_PROP_FPS)
# #     fps2 = tool_video.get(cv2.cv.CV_CAP_PROP_FPS)
# # else:
# #     fps1 = video.get(cv2.CAP_PROP_FPS)
# #     fps2 = tool_video.get(cv2.CAP_PROP_FPS)
#
#
# if __name__ == "__main__":
#     print(cv2)
#     video = cv2.VideoCapture('video.mp4')  # 读取需要处理的视频
#     tool_video = cv2.VideoCapture('tool_video.mp4')
#
#     if video.isOpened() and tool_video.isOpened():  # 判读视频是否正常打开
#         print("打开ok")
#     else:
#         print("打开失败，程序退出")
#         exit(-1)  # 如果不能正常打开则自动结束程序
#
#     savedpath = 'result/'  # 将生成的图片保存在result文件夹下面
#     isExists = os.path.exists(savedpath)  # 判断该存储图片的文件夹是否存在
#     if not isExists:  # 如果路径不存在则创建文件夹，否则提示文件夹已存在
#         os.makedirs(savedpath)
#         print("创建存储路径")
#     else:
#         print("路径已经存在")
#     c = 1  # 设置抽帧图片的名称
#
#     while True:
#         # 得到两帧
#         ok1, frame1 = video.read()  # 按帧读取视频，返回两个数值，第一个布尔值，False为读取到结尾，第二个是每帧图像 <class 'numpy.ndarray'> (1080, 1920, 3)
#         ok2, frame2 = tool_video.read()  # 按帧读取视频，返回两个数值，第一个布尔值，False为读取到结尾，第二个是每帧图像 <class 'numpy.ndarray'> (1080, 1920, 3)
#
#         if ok1 and ok2:  # 如果能正常读取
#             a = 0.9
#             new_frame = frame1 * a + frame2 * (1 - a)
#             cv2.imwrite(savedpath + str(c) + '.jpg', new_frame)  # 保存图像，路径 加图像
#             print('完成第' + str(c) + '张图片的保存')  # 打印已保存的图片数量
#             c = c + 1  # 每次命名加1
#         else:
#             print("读取完成")  # 否则读取失败
#             break
#
#     print("结束")  # 结束视频处理
#     video.release()  # 需要释放
#     tool_video.release()  # 需要释放
#
#
# # 生成视频
# # 完成写入对象的创建，第一个参数是合成之后的视频的名称，第二个参数是可以使用的编码器，第三个参数是帧率即每秒钟展示多少张图片，第四个参数是图片大小信息
# fps = 25
# size = (1920, 1080)
#
# videowriter = cv2.VideoWriter("test.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
# path = r'result/'
#
# for filename in [r'result/{0}.jpg'.format(i+1) for i in range(250)]:
#     print(filename)
#     img = cv2.imread(filename)
#     videowriter.write(img)
#
# print('end!')


# 添加音乐
videoFile = 'test.avi'  # 视频文件
video = VideoFileClip(videoFile)
videos = video.set_audio(AudioFileClip('video.mp3'))  # 音频文件
videos.write_videofile('compose.mp4', audio_codec='aac')  # 保存合成视频，注意加上参数audio_codec='aac'，否则音频无声音