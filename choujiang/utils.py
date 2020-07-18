import datetime
import hashlib
import random
import xmltodict
from flask.json import JSONEncoder
from choujiang.models.base import BaseModel


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime.datetime):
                return obj.isoformat()
            elif isinstance(obj, BaseModel):
                return obj.to_dict()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def sha(content):
    sha1obj = hashlib.sha1()
    if isinstance(content, str):
        sha1obj.update(content.encode("utf8"))
    digest = sha1obj.hexdigest()
    return digest


def str_to_datetime(s, format="%Y-%m-%d %H:%M:%S"):
    """
    字符串转日期
    """
    try:
        if isinstance(s, datetime.datetime):
            return s
        return datetime.datetime.strptime(s, format)
    except:
        pass


def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


def generate_order_num():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "".join(random.sample("0123456789", 6))


def format_num(number):
    if number and number > 100000:
        return "10w+"
    else:
        return number


def json_default_decode(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")


def short_url(url):
    m = hashlib.md5()
    m.update(url.encode())
    return m.hexdigest()





def parse_xml(text):
    xml_dict = xmltodict.parse(text)["xml"]
    xml_dict["raw"] = text
    return xml_dict

