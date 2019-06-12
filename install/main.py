#coding:utf-8
#This script will auto install SecKMS 2.11.0

import os
import subprocess
import mode

#获取当前目录
InstallPath = os.getcwd()
SrcPath='/usr/local/src'

#获取系统Selinux 状态
Selinux_status = subprocess.Popen(["getenforce"],stdout=subprocess.PIPE,shell=True)
(selinux_out,err)= Selinux_status.communicate()


if selinux_out.strip() != 'Disabled':
    print("Warning:Please close selinux")

