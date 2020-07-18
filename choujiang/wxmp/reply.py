# -*- coding: utf-8 -*-

"""
参考：https://github.com/whtsky/WeRoBot/blob/develop/werobot/replies.py
"""

import time


class Reply(object):
    def __init__(self, message, **kwargs):

        if message and "source" not in kwargs:
            kwargs["source"] = message.target

        if message and "target" not in kwargs:
            kwargs["target"] = message.source

        if 'time' not in kwargs:
            kwargs["time"] = int(time.time())
        self._args = kwargs

    def render(self):
        return self.TEMPLATE.format(**self._args)


class TextReply(Reply):
    TEMPLATE = u"""
                <xml>
                <ToUserName><![CDATA[{target}]]></ToUserName>
                <FromUserName><![CDATA[{source}]]></FromUserName>
                <CreateTime>{time}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{content}]]></Content>
                </xml>
                """


class ImageReply(Reply):
    TEMPLATE = u"""
                <xml>
                <ToUserName><![CDATA[{target}]]></ToUserName>
                <FromUserName><![CDATA[{source}]]></FromUserName>
                <CreateTime>{time}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{media_id}]]></MediaId>
                </Image>
                </xml>
                """


class VoiceReply(Reply):
    TEMPLATE = u"""
                <xml>
                <ToUserName><![CDATA[{target}]]></ToUserName>
                <FromUserName><![CDATA[{source}]]></FromUserName>
                <CreateTime>{time}</CreateTime>
                <MsgType><![CDATA[voice]]></MsgType>
                <Voice>
                <MediaId><![CDATA[{media_id}]]></MediaId>
                </Voice>
                </xml>
                """


class ArticleReply(Reply):
    TEMPLATE = u"""
                <xml>
                <ToUserName><![CDATA[{target}]]></ToUserName>
                <FromUserName><![CDATA[{source}]]></FromUserName>
                <CreateTime>{time}</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>1</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[{title}]]></Title>
                <Description><![CDATA[{description}]]></Description>
                <PicUrl><![CDATA[{picurl}]]></PicUrl>
                <Url><![CDATA[{url}]]></Url>
                </item>
                </Articles>
                </xml>
                """


class SuccessReply(Reply):
    def render(self):
        return "success"
