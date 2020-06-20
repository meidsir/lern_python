import sys
import time


def bar(num, total=100):
    """
    进度条
    :param num:
    :param total:
    :return:
    """
    rate = num / total
    rate_num = int(rate * 100)
    s = '\r[%s%s]%s%%' % ('=' * num, ' ' * (100 - num), rate_num)
    sys.stdout.write(s)
    sys.stdout.flush()
    print("打印测试")


if __name__ == '__main__':
    for i in range(101):
        time.sleep(0.1)
        bar(i)


# for index,arg in enumerate(sys.argv):
#     print(sys.argv)
#     print('第%s个参数是: %s' % (index,arg))
