import random
import string
import pprint

def couponRandCode(size = 8):
    '''return a string of X lengths, default is eight.'''
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

def couponJudegNum(input_set, num = 200):
    '''Judge a set is it up to num,there default is 200'''
    judgeSet = set(input_set)
    if len(judgeSet) >= num:
        return True
    else:
        return False

#变量定义
size = 15
num = 200
i = 0
allStr = len(string.ascii_uppercase + string.digits)
a_coupon = list()
coupons = set()

#防止所有的激活码达不到输出数量，比如要求输出37个激活码，而size错误的输入为1，最大只能输出36个不一样的激活码
if (allStr ** size) < num:
    print('size or num input error.')
    quit()
a_file = open('out_coupon.txt','wt')
while True:
    i+=1
    a_coupon.append(couponRandCode(size))   #往列表中添加一个激活码
    coupons = set(a_coupon)                 #将列表转为集合，因为集合中没有重复的元素
    if couponJudegNum(coupons, num):        #判断激活码是否达到指定个数
        break

print('循环次数：', i)
pprint.pprint(coupons)  #控制台打印
print('\n'.join(coupons),file = a_file)     #输出到文件