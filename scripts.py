import requests
import re
import os
from mitmproxy.http import HTTPFlow


def response(flow:HTTPFlow):
    dirname = 'E:\python-study\python\spiders\Vedio'
    pattern = r'http://v\d+-dy[-\w]*\.ixigua\.com/'
    regex = re.compile(pattern)
    matcher = regex.match(flow.request.url)
    if matcher:
        resp = requests.get(flow.request.url, headers=flow.request.headers, stream=True)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filename = os.path.join(dirname, '{}.mp4'.format(1))
        with open(filename, 'wb', encoding='utf8') as f:
            for i in resp.iter_content():
                f.write(i)
    # global num
    # 经测试发现视频url前缀主要是3个
    # target_urls = ['http://v1-dy.ixigua.com/', 'http://v9-dy.ixigua.com/','http://v3-dy-y.ixigua.com/', 'http://v3-dy-z.ixigua.com/'
    #                'http://v3-dy-x.ixigua.com/', 'https://v3-dy.ixigua.com/', 'http://v6-dy.ixigua.com/']
    # for url in target_urls:
    #     # 过滤掉不需要的url
    #     if flow.request.url.startswith(url):
    #         # 设置视频名
    #         filename = path + str(num) + '.mp4'
    #         # 使用request获取视频url的内容
    #         # stream=True作用是推迟下载响应体直到访问Response.content属性
    #         res = requests.get(flow.request.url, stream=True)
    #         # 将视频写入文件夹
    #         with open(filename, 'ab') as f:
    #             f.write(res.content)
    #             f.flush()
    #             print(filename + '下载完成')
    #         num += 1