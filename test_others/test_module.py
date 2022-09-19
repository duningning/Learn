# _*_coding:utf-8_*_
# 作者:duningning.ming
# 创建时间: 2022/7/5 17:52
# 文件   : module_test.py
# IDE   : PyCharm
# save this as app.py
import logging
import os

import pytest
from time import sleep
# import random
#
import time
import paramiko


def test_upload_package(self):  # 上传包到远程环境
    #logger.info('Upload package to remote test environment')

    try:
        transport_x86 = paramiko.Transport('172.17.21.2', 22)
        transport_x86.connect(username='ubunt', password='ubuntu')
    except Exception as e:
        #self.logger.error(repr(e))
        pass
# 如果连接需要密钥，则要加上一个参数，hostkey="密钥"
    #self.logger.info('Connect to x86 test environment')
    sftp_x86 = paramiko.SFTPClient.from_transport(transport_x86)

    packages = os.listdir(ccb_path)
    for package in packages:
        if 'aarch' in package:
            pass
            # self.logger.info('Upload arm test package')
            # bag_dir = self.ccb_path + package
            # sftp_arm.put(bag_dir, '/home/admin/dnn/' + package)  # 将本地的文件上传至服务器/root/Windows.txt
            # self.logger.info('Arm test package upload completed')
        elif 'x86' in package:
            self.logger.info('Upload x86 test package')
            bag_dir = self.ccb_path + package
            sftp_x86.put(bag_dir, '/home/ubuntu/zza/' + package)  # 将本地的文件上传至服务器/root/Windows.txt
            self.logger.info('X86 test package upload completed')
        else:
            self.logger.debug('There is no package to upload,or the package name does not match')
    # sftp_arm.close()
    sftp_x86.close()
    self.logger.info('Upload completed,environment disconnected')

def test_remote_control_arm():
    strs = 'abbacabb'
    print(strs.strip('ab'))
    print(11111)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(hostname='172.17.31.2', username='root', password='On1shiuva4')

    # 执行命令
    # packages = os.listdir(ccb_path)
    # for package in packages:
    #     if 'aarch' in package:
    #        print(package)
            # 测试前清理多余文件夹
    print(11111)
    stdin, stdout, stderr = ssh_client.exec_command('bash --login -c "python -V"')
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    print(result.decode())
    for line in iter(stdout.readline, ""):
        print(line, end="")
    ssh_client.close()
if __name__ == '__main__':

    pytest.main(['-xvs','./test_module.py::test_remote_control_arm'])
    #print(time.strftime('%Y-%m-%d', time.localtime(int(time.time()))))

    # res, err = stdout.read(), stderr.read()
    # result = res if res else err
    # print(result.decode())


# # 定义一个类，表示一台远端linux主机
# class Linux(object):
#     # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
#     def __init__(self, ip, username, password, timeout=30):
#         self.ip = ip
#         self.username = username
#         self.password = password
#         self.timeout = timeout
#         # transport和chanel
#         self.t = ''
#         self.chan = ''
#         # 链接失败的重试次数
#         self.try_times = 3
#
#     # 调用该方法连接远程主机
#     def connect(self):
#         while True:
#             # 连接过程中可能会抛出异常，比如网络不通、链接超时
#             try:
#                 self.t = paramiko.Transport(sock=(self.ip, 22))
#                 self.t.connect(username=self.username, password=self.password)
#                 self.chan = self.t.open_session()
#                 self.chan.settimeout(self.timeout)
#                 self.chan.get_pty()
#                 self.chan.invoke_shell()
#                 # 如果没有抛出异常说明连接成功，直接返回
#                 print('连接%s成功' % self.ip)
#                 # 接收到的网络数据解码为str
#                 print(self.chan.recv(65535).decode('utf-8'))
#                 return
#             # 这里不对可能的异常如socket.error, socket.timeout细化，直接一网打尽
#             except Exception as e1:
#                 if self.try_times != 0:
#                     print('连接%s失败，进行重试' % self.ip)
#                     self.try_times -= 1
#                 else:
#                     print('重试3次失败，结束程序')
#                     exit(1)
#
#     # 断开连接
#     def close(self):
#         self.chan.close()
#         self.t.close()
#
#     # 发送要执行的命令
#     def send(self, cmd):
#         cmd += '\r'
#         result = ''
#         # 发送要执行的命令
#         self.chan.send(cmd)
#         # 回显很长的命令可能执行较久，通过循环分批次取回回显,执行成功返回true,失败返回false
#         while True:
#             sleep(0.5)
#             ret = self.chan.recv(65535)
#             ret = ret.decode('utf-8')
#             result += ret
#             return result
#
#     '''
#     发送文件
#     @:param upload_files上传文件路径 例如：/tmp/test.py
#     @:param upload_path 上传到目标路径 例如：/tmp/test_new.py
#     '''
#
#     # def upload_file(self, upload_files, upload_path):
#     #     try:
#     #         tran = paramiko.Transport(sock=(self.ip, self.port))
#     #         tran.connect(username=self.username, password=self.password)
#     #         sftp = paramiko.SFTPClient.from_transport(tran)
#     #         result = sftp.put(upload_files, upload_path)
#     #         return True if result else False
#     #     except Exception as ex:
#     #         print(ex)
#     #         tran.close()
#     #     finally:
#     #         tran.close()
#
#
# # 连接正常的情况
# if __name__ == '__main__':
#     host = Linux('172.17.31.2', 'root', 'On1shiuva4')  # 传入Ip，用户名，密码
#     host.connect()
#
#
#     # result = host.send('ls') # 发送一个查看ip的命令
#     def input_cmd(str):
#         return input(str)
#
#
#     tishi_msg = "输入命令："
#     while True:
#         msg = input(tishi_msg)
#         if msg == "exit":
#             host.close()
#             break
#         else:
#             res = host.send(msg)
#             data = res.replace(res.split("\n")[-1], "")
#             tishi_msg = res.split("\n")[-1]
#             print(res.split("\n")[-1] + data.strip("\n"))

# def test_demo1():
#     assert True
#
#
# def test_demo2():
#     a=random.randint(1,5)
#     assert a==3
#
#
# def test_demo3():
#     assert True

# from datetime import datetime, timedelta
# import time
#
# def test_loger():
#     # logger = logging.getLogger('public.sub')
#     # logger.info("this is another module using logging\n")
#     # logger.warning('另一个模块打印的警告\n')
#     #print(asctime)
#     print(datetime.now())
# import os
# from tqdm import tqdm,trange
#
# # /Users/duningning/Downloads/
# file_names = ["deh5_atlas_aarch64_cb.zip", "deh5_atlas_x86_64_cb.zip"]
# # for file_name in file_nam
# file_name ="霍格沃斯学院"
# download_path = "/Users/duningning/Downloads/"
# #print(os.path)
# if file_name in os.listdir(download_path):
#     i = ">>>"
#     while True:
#         first_size = os.path.getsize(download_path+file_name)
#         time.sleep(5)
#         after_size = os.path.getsize(download_path+file_name)
#         if  first_size !=after_size:
#             print("文件下载中  "+i)
#             i= i+">>>"
#         else:
#             print("文件下载完成")
#             break
#
#
#
#
#
#
#
#
# def test_dnn_tqdm():
#     print(1111)
#     for i in trange(100,position=0, leave=True):
#         time.sleep(0.05)
#
#
# def test_www_a():
#     print(1111)
#     for i in trange(100):
#         time.sleep(0.05)


    # def test_getbag_for_ui(self):
    #     # option = webdriver.ChromeOptions()
    #     # option.add_argument('headless')  # 设置option
    #     #登录gitlab
    #     self.driver = webdriver.Chrome('/Users/duningning/Downloads/chromedriver/103/chromedriver')
    #     #self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #     self.driver.get("http://172.17.0.5/DEH5/DEH5CI/-/pipelines/")
    #     self.driver.find_element_by_id("user_login").send_keys("duningning")
    #     self.driver.find_element_by_id("user_password").send_keys("ming6932058F")
    #     self.driver.find_element_by_name("commit").click()
    #     self.driver.implicitly_wait(5)
    #     # #下载x86
    #     # self.driver.find_element_by_xpath('//*/tr[1]/td[7]//*/button').click()
    #     # self.driver.find_element_by_link_text("deh5_atlas_x86_64_cb:archive").click()
    #     # #下载arm
    #     # self.driver.find_element_by_xpath('//*/tr[1]/td[7]//*/button').click()
    #     # #self.driver.find_element_by_xpath("//*/tr[1]/td[7]//*/li[4]/a/div/p").click()
    #     # self.driver.find_element_by_link_text("deh5_atlas_aarch64_cb:archive").click()
    #     self.file_names = ["deh5_atlas_aarch64_cb.zip", "deh5_atlas_x86_64_cb.zip"]
    #     self.download_path = "/Users/duningning/Downloads/"
    #     #判断包是否下载
    #     for file_name in self.file_names:
    #         self.driver.find_element_by_xpath('//*/tr[1]/td[7]//*/button').click()
    #         self.driver.find_element_by_link_text(file_name).click()
    #         if file_name in os.listdir(self.download_path):
    #             i = ">>>"
    #             while True:
    #                 first_size = os.path.getsize(self.download_path + file_name)
    #                 time.sleep(5)
    #                 after_size = os.path.getsize(self.download_path + file_name)
    #                 if first_size != after_size:
    #                     print("文件下载中  " + i)
    #                     i = i + ">>>"
    #                 else:
    #                     print("文件下载完成")
    #                     break
    #     self.driver.quit()

    # def remote_run(self):#后面整,暂时搞不定
    #     ssh_client = paramiko.SSHClient()
    #     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    #     ssh_client.connect(hostname='172.17.21.3', username='admin', password='On1shiuva4')
    #     stdin, stdout, stderr = ssh_client.exec_command('cd /home/admin/dnn;ls;sudo su;python3 start.py')
    #
    #     res, err = stdout.read(), stderr.read()
    #     result = res if res else err
    #     print(result.decode())

    # def download_sh(self):
    #     localFile = open("下载后的文件路径", "wb")
    #     # 创建本地文件，注意是下载二进制文件，比如zip包，需要加上参数b，即binary模式，默认是t模式，即text文本模式。
    #     # 示例：localFile=open("/Users/devnn/Desktop/test.zip","wb")
    #
    #     conn.retrieveFile("共享文件夹名称", "文件所在路径", localFile)
    #     # 从smb服务器下载文件到本地,默认超时30秒，可以修改:timeout=xx。“文件所在路径”是相对共享文件夹的路径，不需要加"/".
    #     # 示例：conn.retrieveFile("test","test1/test2/test3.zip",localFile)
    #
    #     localFile.close()
    #     # 关闭
    #     print("下载成功")