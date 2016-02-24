#!该程序用于打包需要备份的数据
# coding:utf-8
# Filename:
import os
import time
import zipfile

source = ['e:\\test_a', 'e:\\test_b']

# 目标目录
# 1.创建日期文件夹
# 2.以时间为文件名的压缩包
target_dir = 'e:\\back'
target = target_dir + os.sep + time.strftime('%Y%m%d')
# zip_name = time.strftime('%H%M%S') + '.zip'
# 判断目录是否存在
for _dir in source:
    if not os.path.exists(_dir):
        print("it is not exists that path", _dir)


def init_file(*dir):
    for __dir in dir:
        if not os.path.exists(__dir):
            os.mkdir(__dir)
            print('create ', __dir)

init_file(target_dir, target)


def getdir(comment):
    global target_zip
    result = target + os.sep + time.strftime('%H%M%S') + comment + '.zip'
    return result


# 打包目录下的文件
# * 使用命令行来实现打包，当操作系统不支持时会失败
# zip_command = 'zip -qr {0} {1}'.format(target_zip, ' '.join(source))
# zip_command = 'a'
# if os.system(zip_command) == 0:
#     print("success")
# else:
#     print("fail")
# * 使用zipfile来进行打包
if __name__ == '__main__':
    str = input('input the comment for the zip:')
    if len(str) == 0:
        target_zip = getdir()
    else:
        target_zip = getdir(str)
    z = zipfile.ZipFile(target_zip, 'w')
    for s_dir in source:
        if os.path.isdir(s_dir):
            z.write(s_dir)
            print('add :', s_dir)
    z.close()


