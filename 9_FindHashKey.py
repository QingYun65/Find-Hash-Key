import hmac

import hashlib

import base64

import struct

import sys

import binascii

import random

your_bytes_string='Li Wenjie201900180054'.encode()

match_value='sdu_cst_20220610'

round=0

while True:
    """
    随机生成长度为10的密钥
    """
    key= (''.join(random.sample(['1','2','3','4','5','6','7','8','9','0','z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))
    #key= (''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 10)))

    key=key.encode()

    """
    MD5哈希
    """
    dig = hmac.new(key, msg=your_bytes_string, digestmod=hashlib.md5).digest()

    """
    哈希值转128位二进制
    """
    tt=bin(int.from_bytes(dig, byteorder=sys.byteorder))

    tt=tt.replace('0b','')
    
    length=len(tt)

    if length<128:
        tt=tt+('0'*(128-length))

    #print(tt)

    """
    二进制转ASCII码并和match_value比较
    """
    flag=0
    length=128
    result=''
    while(flag<length):
        target=tt[flag:flag+8]              #分组为8bit一组
        target='0b'+target                   
        result=result+chr(eval(target))      #返回ascii结果
        flag=flag+8

    round=round+1

    #print(result[:1])

    if result[:3]==match_value[:3]:
        print('key:',key,'->',result)
        break
