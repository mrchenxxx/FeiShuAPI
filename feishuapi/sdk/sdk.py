from doctest import FAIL_FAST
import requests
from requests_toolbelt import MultipartEncoder


def uploadImage(path,tenant_access_token):
    """
    上传图片
    ：param path 图片路径地址
    ：param tenant_access_token 自建应用机器人的token
    """
    url = "https://open.feishu.cn/open-apis/im/v1/images"
    form = {'image_type': 'message',
            'image': (open(path, 'rb'))} 
    multi_form = MultipartEncoder(form)
    headers = {
        'Authorization': f'Bearer {tenant_access_token}',
    }
    headers['Content-Type'] = multi_form.content_type
    response = requests.request("POST", url, headers=headers, data=multi_form)
    print(response.headers['X-Tt-Logid'])  # for debug or oncall
    print(response.content)  # Print Response

