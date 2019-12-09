
import time
import socket

from myapp import mycelery


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


@mycelery.task
def add(x, y):
    s = x + y
    time.sleep(3)  # 模拟耗时操作
    print("主机IP11 {}: x + y = {}".format(get_host_ip(), s))
    return s

@mycelery.task
def  mul(x, y):
    # time.sleep(3)  # 模拟耗时操作
    s = x * y
    time.sleep(3)  # 模拟耗时操作
    print("主机IP {}: x * y = {}".format(get_host_ip(), s))
    return s


@mycelery.task
def  xsum(numbers):
    # time.sleep(3)  # 模拟耗时操作
    s = sum(numbers)
    time.sleep(3)  # 模拟耗时操作
    print("主机IP {}:sum(numbers)= {}".format(get_host_ip(), s))
    return s


@mycelery.task
def taskA():
    print("taskA begin...")
    print(f"主机IP {get_host_ip()}")
    time.sleep(3)
    print("taskA done.")


@mycelery.task
def taskB() -> object:
    print("taskB begin...")
    print(f"主机IP {get_host_ip()}")
    time.sleep(3)
    print("taskB done.")

@mycelery.task
def taskC() -> object:
    print("taskC begin...")
    print(f"主机IP {get_host_ip()}")
    time.sleep(3)
    print("taskC done.")