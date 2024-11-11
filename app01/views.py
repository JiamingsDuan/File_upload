from django.shortcuts import render
from pyhdfs import HdfsClient

import os


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')

    elif request.method == 'POST':
        obj = request.FILES.get('file-5[]')
        # print(obj, type(obj), obj.name)
        f = open(os.path.join('File', obj.name), 'wb+')
        for line in obj.chunks():
            f.write(line)

        f.close()
        # 获取本地文件路径 文件名 文件路径拼接
        local_path = os.path.join('./File/', obj.name)
        # 定义hdfs文件路径
        hadoop_path = os.path.join('/py_upload/', obj.name)
        print(local_path, hadoop_path)
        # 开始上传
        fs = HdfsClient(hosts='210.30.12.137,50070', user_name='flink')
        if not fs.exists('/py_upload/'):
            fs.mkdirs('/py_upload/')
        print(fs.listdir('/py_upload/'))
        fs.copy_from_local(local_path, hadoop_path)
        # 上传结束
        return render(request, 'success.html')
