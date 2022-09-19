# _*_coding:utf-8_*_
# 作者:duningning.ming
# 创建时间: 2022/7/11 14:32
# 文件   : test_threading.py
# IDE   : PyCharm
# 线程使用的方式一
import threading
import time
import os
os.system('md5sum -h')


# 需要多线程运行的函数
# def fun(args):
#     print("我是线程%s" % args)
#     time.sleep(5)
#     print("线程%s运行结束" % args)
#
#
# # 创建线程
# t1 = threading.Thread(target=fun, args=(1,))
# t2 = threading.Thread(target=fun, args=(2,))
# start_time = time.time()
# t1.start()
# t2.start()
# end_time = time.time()
# print("两个线程一共的运行时间为：", end_time-start_time)
# print("主线程结束")



bag_name = "deh5_atlas_x86_64_l4ab:archive"
bag_name = bag_name.split(':')[1]
print(bag_name)

# def get_md5sum(bags):
#
#     #print("md5sum生成"+bags)
#     local_path = "/Users/duningning/Desktop/bag/ccb/"+bags
#     #print(local_path)
#     os.system(f"cd /Users/duningning/Desktop/bag/ccb/;md5sum {bags}")
#     #print(os.system('ls'))
#     #os.system(f"md5sum '{local_path}'")
#
# # if __name__ == '__main__':
#     print("111111")
#     bags = os.listdir("/Users/duningning/Desktop/bag/ccb")
#     start_time = time.time()
#     for bag in bags:
#         t = threading.Thread(target=get_md5sum,args=[bag,])
#         #t.setDaemon(True)
#         t.start()
#         t.join()
#     end_time = time.time()
#     print("两个线程一共的运行时间为：", end_time-start_time)