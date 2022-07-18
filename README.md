## 一、飞书自定义机器人介绍

飞书机器人是飞书群的一个高级扩展功能，但使用起来却非常简单，只需要注册一个飞书账号，就可以将第三方服务信息聚合到飞书群中，实现信息的自动同步。

## 二、常见的使用场景：

1、~~聚合 Github、Gitlab 等源码管理服务，实现源码更新同步；~~

2、~~聚合 Trello、JIRA 等项目协调服务，实现项目信息同步；~~

3、机器人支持 Webhook 自定义接入，就可以实现更多可能性，例如：将运维报警、自动化测试结果报告、工作&生活日程安排（上班打卡、下班吃饭、健身、读书、生日、纪念日...）的提醒；

目前自定义机器人支持文本（text）、富文本（post）、群名片（share_chat）、图片（image）、消息卡片（interactive）五种消息格式，五种消息类型，详细信息请参考自定义机器人官方文档

## 三、如何使用

### 安装库

```cmd
pip install feishuapi
```

### 使用

```python
import asyncio
from
from feishuapi import LarkCustomBot

webhook = '飞书自定义机器人的 webhook 链接'
# 初始化机器人
feishu = LarkCustomBot(webhook=webhook)

# 如果你给机器人设置了签名：
secret = '你给机器人设置的签名'
feishu = LarkCustomBot(webhook=webhook，secret=secret)

# 发送文本消息并艾特全体（默认加在文本最后）：
asyncio.run(feishu.send_text(text="text content", is_at_all=True))

# 发送文本消息不艾特全体(is_at_all=False 可以不写，默认是关闭艾特全体的)：
asyncio.run(feishu.send_text(text="text content", is_at_all=False))

# 发送富文本消息
# content_text 文本  content_a 超链接 content_image 图片 content_at 艾特某人 title 富文本标题，默认不填
# 代表第一行要发送的内容，以列表形式体现
first_line = [post.content_text('测试'), post.content_a(
    href='baidu.com', text='百度')]
# 第二行，以此类推
second_line = [post.content_imag(
    'img_ecffc3b9-8f14-400f-a014-05eca1a4310g')]

asyncio.run(feishu.send_post(first_line, second_line,title='测试'))
```
