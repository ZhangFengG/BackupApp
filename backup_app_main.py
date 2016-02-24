#!该程序用于打包需要备份的数据
# coding:utf-8
# Filename:
import os
import time
import zipfile
import xml.dom.minidom as Mdom

source_dirs = []
source_path = 'source_path'
target_path = 'target_path'
# 将xml文件转换为节点
dom = Mdom.parse('config.xml')
# 获取当前元素,解析，获取对应路径
elements = dom.getElementsByTagName(source_path)
for element in elements:
    source_dirs.append(element.firstChild.data)
elements = dom.getElementsByTagName(target_path)
target_dir = elements[0].firstChild.data

# 目标目录
# 1.创建日期文件夹
# 2.以时间为文件名的压缩包
target = target_dir + os.sep + time.strftime('%Y%m%d')
# zip_name = time.strftime('%H%M%S') + '.zip'
# 判断目录是否存在
for _dir in source_dirs:
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
        target_zip = getdir('')
    else:
        target_zip = getdir(str)
    z = zipfile.ZipFile(target_zip, 'w')
    for s_dir in source_dirs:
        for dirpath, dirnames, filenames in os.walk(s_dir):
            for filename in filenames:
                str = os.path.join(dirpath, filename)
                print('压缩：', str)
                z.write(str)
    z.close()


