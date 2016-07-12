# -*- encoding=UTF-8 -*-
from homework3 import app
from qiniu import Auth,put_stream,put_file
import os

#需要填写你的 Access Key 和 Secret Key
access_key = app.config['QINIU_ACCESS_KEY']
secret_key = app.config['QINIU_SECRET_KEY']

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = app.config['QINIU_BUCKET_NAME']
save_dir=app.config['UPLOAD_DIR']

def qiniu_upload_file(source_file,save_file_name):
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name,save_file_name)
    source_file.save(os.path.join(save_dir, save_file_name))
    #source_file.save('D:/upload/'+save_file_name)
    ret, info =put_file(token,save_file_name,os.path.join(save_dir, save_file_name))
   # ret, info = put_stream(token,save_file_name, source_file.stream,
                          #"qiniu",source_file.stream.tell())
    print(info)

    return None