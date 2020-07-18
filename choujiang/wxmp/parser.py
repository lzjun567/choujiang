# -*- coding: utf-8 -*-
import xmltodict

from .message.events import EventMetaClass, UnknownEvent
from .message.messages import MessageMetaClass, UnknownMessage


def parse_xml(text):
    xml_dict = xmltodict.parse(text)["xml"]
    xml_dict["raw"] = text
    return xml_dict


def process_message(message):
    """
    Process a message dict and return a Message Object
    :param message: Message dict returned by `parse_xml` function
    :return: Message Object
    """
    message["type"] = message.pop("MsgType").lower()
    if message["type"] == 'event':
        message["type"] = str(message.pop("Event")).lower() + '_event'
        message_type = EventMetaClass.TYPES.get(message["type"], UnknownEvent)
    else:
        message_type = MessageMetaClass.TYPES.get(message["type"], UnknownMessage)
    return message_type(message)


if __name__ == '__main__':
    xml = """
        <xml><ToUserName><![CDATA[gh_1c5732e1a6a4]]></ToUserName>
        <FromUserName><![CDATA[oNY0rwd8LzIOHu_orRQc6onh5BIk]]></FromUserName>
        <CreateTime>1495533973</CreateTime>
        <MsgType><![CDATA[event]]></MsgType>
        <Event><![CDATA[subscribe]]></Event>
        <EventKey><![CDATA[]]></EventKey>
        </xml>
    """
    import json

    print(json.dumps(parse_xml(xml)))
