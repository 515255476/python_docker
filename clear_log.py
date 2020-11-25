# ! /usr/bin/python
# -*- coding: utf-8 -*
import os.path, time, datetime

logdir = "/Users/Pingpig/PycharmProjects/test/python_docker/log"

for parent, dirnames, filenames in os.walk(logdir):
    for filename in filenames:
        fullname = parent + "/" + filename  # 文件全称
        createTime = int(os.path.getctime(fullname))  # 文件创建时间
        time.ctime(createTime)
        nDayAgo = (datetime.datetime.now() - datetime.timedelta(days=0))  # 当前时间的n天前的时间
        timeStamp = int(time.mktime(nDayAgo.timetuple()))
        if createTime < timeStamp:  # 创建时间在n天前的文件删除
            os.remove(os.path.join(parent, filename))





# crontab -e 编辑
# crontab -l