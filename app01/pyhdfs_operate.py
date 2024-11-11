import pyhdfs


#hdfs地址
client = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='root')

# 查看当前文件状态
def state(hdfs_path):
    path = client.list_status(hdfs_path)
    print(path)


# 在hdfs系统中创建目录
def set_dir(hdfs_path):
    client.mkdirs(hdfs_path)


# 删除hdfs文件
def delete_file(hdfs_path):
    client.delete(hdfs_path, recursive=True)


# 从本地上传文件到hdfs
def upload_file(local_path, hdfs_path):
    client.copy_from_local(local_path, hdfs_path, cleanup=True)


# 从hdfs获取文件到本地
def download_file(local_path, hdfs_path):
    client.copy_to_local(local_path, hdfs_path, overwrite=False)


# 追加数据到hdfs文件
def append_file(hdfs_path, data):
    client.append(hdfs_path, data, overwrite=False, append=True)


# 查看数据文件
def open_file(file_path):
    response = client.open(file_path)
    print(response.read())


# 返回目录下的文件
def list(hdfs_path):
    return client.listdir(hdfs_path, status=False)


class FileManager(object):

    # upload file to HDFS from lacal file system
    def file_upload(self, host, user_name, local_path, hdfs_path):
        print('File upload begin !')
        fs = pyhdfs.HdfsClient(hosts=host, user_name=user_name)
        print(fs.listdir('/file'))
        fs.copy_from_local(local_path, hdfs_path)
        print('File upload finished !')

    def file_down(self, host, user_name, local_path, hdfs_path):

        print('File download start !')
        fs = pyhdfs.HdfsClient(hosts=host, user_name=user_name)
        fs.copy_from_local(hdfs_path, local_path)
        print('File download finished !')


if __name__ == '__main__':

    file_manager = FileManager()
    file_manager.file_upload('localhost:50070', 'root', u'', 'hdfs_file')
    file_manager.file_down('localhost:50070', 'root', u'', 'hdfs_file')
