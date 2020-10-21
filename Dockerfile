FROM centos:7 AS oracle_build


WORKDIR /opt/oracle
RUN yum install -y wget unzip libaio && \
    rm -rf /var/cache/yum
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && \
    rm -f instantclient-basiclite-linuxx64.zip && \
    cd instantclient* && \
    rm -f *jdbc* *occi* *mysql* *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig


FROM python:3.7-alpine AS build
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add git gcc musl-dev libffi-dev openssl-dev make
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /requirements.txt \
    && pip --default-timeout=1000
    && mkdir -p /install/lib/python3.7/site-packages \
    && cp -rp /usr/local/lib/python3.7/site-packages /install/lib/python3.7




FROM python:3.7-alpine

COPY --from=build /install/lib /usr/local/lib
COPY --from=oracle_build /opt/oracle /usr/local/instantclient
WORKDIR /auto
COPY . /auto