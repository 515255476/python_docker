import sys
p1=sys.argv[1]



if p1=='test':
    url='测试url'
    oracle='测试数据库'
elif p1=='dev':
    url='开发url'
    oralce='开发测试库'

print(url + '' + oralce)