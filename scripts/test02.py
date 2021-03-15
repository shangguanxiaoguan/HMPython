# coding=utf-8

"""
   1.多线程应用
"""
from time import sleep


def say(name):
    print("你好，%s" % name)
    sleep(5)


def sing(name):
    print("%s 在唱歌" % name)
    sleep(5)

# 导包
import threading

# 实例化线程1 线程2
t1 = threading.Thread(target=say, args=('张三',))
t2 = threading.Thread(target=sing, args=('李四',))

"""
【注意点】target参数值为函数引用名而非调用
        正确：target=fun
        错误：target=fun()
"""

# 启动线程
t1.start()
t2.start()