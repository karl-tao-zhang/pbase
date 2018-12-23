# file_read_binary.py


#此示例示意以二进制模式读取mynote.txt文件

try:
    f = open("mynote.txt",'rb')    #打开模式为'rb'
    print("打开文件成功")
    b = f.read()
    print(b)
    s = b.decode('utf-8')
    print('转码后：', s)
except IOError:
    print('打开文件失败')




