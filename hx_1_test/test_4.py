
class Test3():
    def test_3(self):
        data1 = {"name": "yang", "funcode": "003003"}
        data2 = {"funcode": "234556"}
        data_new = dict(data2, **data1)
        print(data_new)

Test3().test_3()
