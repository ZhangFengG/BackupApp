#!该程序用于打包需要备份的数据
# Filename:

import os
import time

source = ['e:\\code_a', 'e:\\code_b']

# 目标目录
target_dir = 'e:\\back'
target = target_dir + os.sep + time.strftime('%Y%m%d') + '.zip'
# 判断目录是否存在
for _dir in source:
    if not os.path.exists(_dir):
        print("it is not exists that path", _dir)

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('create ', target_dir)
# 打包目录下的文件
zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print("success")
else:
    print("fail")
