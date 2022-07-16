import requests
import json
import hashlib
import base64
import hmac
import time
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)


class LarkCustomBot(object):
    def __init__(self, webhook: str, secret: str = None) -> None:
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.webhook = webhook
        self.secret = secret
        self.time = str(int(time.time()))

    # 签名校验
    async def get_sign(self, timestamp, secret):

        # 拼接timestamp和secret
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        hmac_code = hmac.new(string_to_sign.encode(
            "utf-8"), digestmod=hashlib.sha256).digest()

        # 对结果进行base64处理
        sign = base64.b64encode(hmac_code).decode('utf-8')
        return sign

    # 封装 post 请求
    async def post(self, data):
        webhook = self.webhook
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        if self.secret != None:
            data['timestamp'] = self.time
            data['sign'] = await self.get_sign(secret=self.secret, timestamp=self.time)
        print(data)
        data = json.dumps(data)
        try:
            response = requests.post(webhook, headers=headers, data=data)
        except requests.exceptions.HTTPError as exc:
            logging.error("消息发送失败， HTTP error: %d, reason: %s" %
                          (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logging.error("消息发送失败，HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logging.error("消息发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logging.error("消息发送失败, Request Exception!")
            raise
        else:
            result = response.json()

            # 发送有错误 返回数据会携带code
            if result.get('code') is not None:
                logging.error("消息发送失败，自动通知：%s" % result)
            # 发送成功 返回数据会有StatusCode
            if result.get('StatusCode') == 0:
                logging.debug('发送成功')

    async def send_text(self, text: str, is_at_all: bool = False) -> None:
        """
        文本类型
        :param text: 消息内容（必须是字符串，如果太长自动折叠）
        :param is_at_all: 是否艾特所有人，默认关闭；False：不艾特所有人；True：艾特所有人（默认加在文字最后面）
        """
        if is_at_all:
            text = text+'<at user_id="all">所有人</at> '
        data = {"msg_type": "text", "content": {"text": text}}

        await self.post(data)

    # 发送富文本消息
    async def send_post(self, *args, title: str = None):
        """
        富文本类型
        :param *args:接受所有要发送的富文本，按照行数来，每一行都是列表 例如：
            firs_line = [content_text('wwwww'), content_a(
                href='baidu.com', text='百度')]
            second_line = [content_imag(
                'img_ecffc3b9-8f14-400f-a014-05eca1a4310g')]
            send_post(firs_line，second_line)
        :param title 标题，默认没有
        """
        content = []
        for arg in args:
            if type(arg) == list:
                content.append(arg)
        data = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": title,
                        "content": content
                    },
                }
            }
        }
        await self.post(data)

    # 发送群名片
    async def send_share_chat(self, share_chat_id: str):
        """
        分享群名片
        :param share_chat_id:群id 以 oc_开头 例：oc_f5b1a7eb27ae2c7b6adc2a74faf339ff
        """
        data = {
            "msg_type": "share_chat",
            "content": {
                "share_chat_id": share_chat_id
            }
        }
        await self.post(data)

    async def send_image(self, image_key: str):
        """
        发送图片
        :param image_key:图片key 例如：img_ecffc3b9-8f14-400f-a014-05eca1a4310g 如果想获取image_key 参考 https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/image/create#362449eb
        """
        data = {
            "msg_type": "image",
            "content": {"image_key": image_key}
        }
        await self.post(data)

    async def send_interactive(self, card):
        """
        消息卡片
        :param card:消息卡片具体构造内容 具体参考文档 https://open.feishu.cn/document/ukTMukTMukTM/uEjNwUjLxYDM14SM2ATN （由于消息卡片复杂的逻辑性，暂时无法更好的封装）
        """
        data = {
            "msg_type": "interactive",
            "card": card
        }
        await self.post(data)