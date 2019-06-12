#coding:utf-8
import os
import subprocess

class KMS_MODE():
    def __init__(self):
        pass

    def Check_Selinux(self):
        Selinux_status = subprocess.Popen(["getenforce"], stdout=subprocess.PIPE, shell=True)
        (selinux_out, err) = Selinux_status.communicate()

        if selinux_out.strip() != 'Disabled':
            print("Warning:Please set selinux=disabled and reboot")
            exit(101)
    def Update_Yum(self):
        os.mkdir('/etc/yum.repo.d/bak')

    def KMS_Install(self):
        pass