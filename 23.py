
a=[1,1,1,2,1,1,1]


for i in a:
    try:
        assert i==1
        print("判断正确，等于1")

    except Exception as e:

        print("判断错误，抛出异常")
        raise



    212