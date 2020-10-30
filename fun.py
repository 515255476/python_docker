import sys
p1=sys.argv[1]

class fun():
    def fun_1(self):
        if p1 == 'test':
            url = '测试url'
            oracle = '测试数据库'
        elif p1 == 'dev':
            url = '开发url'
            oracle = '开发测试库'
        return url,oracle