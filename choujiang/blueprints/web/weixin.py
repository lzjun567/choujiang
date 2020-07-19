# -*- coding:utf-8 -*-

from hashlib import sha1

from flask import request
from ...wxmp import SubscribeEvent
from ...wxmp import TextMessage
from ...wxmp import TextReply
from ...wxmp import parser

from choujiang.blueprints.web import web_bp
from ...models import Award

"""
微信签名校验和事件接收
"""


@web_bp.route('/wx', methods=["GET", "POST"])
def weixin_signature():
    """
    签名校验校验及消息处理
    """
    if request.method == "GET":
        return sign_check()
    else:
        xml = request.get_data()
        openid = request.args.get("openid")
        msg = parser.process_message(parser.parse_xml(xml))
        if isinstance(msg, TextMessage):
            # 处理文本消息
            content = msg.content.strip()
            if "抽奖" in content:
                # 总参与次数
                count = Award.visit_count()
                # 当前用户参与次数
                visit = Award.visit_count(openid)
                # 当前用户剩余参与次数
                remain = 5-visit
                remain = remain if remain > 0 else 0
                if visit <= 5:
                    # 获取抽奖号码
                    award = Award.get_number(openid)
                    if award:
                        if visit == 4:
                            content = f"已为您生成抽奖号码：{award.number} \n\n" \
                                      f"回复 “t” 查询中奖结果\n\n" \
                                      f"邀请微信好友参与还可额外获取1次抽奖机会"
                        else:
                            content = f"已为您生成抽奖号码：{award.number} \n\n" \
                                      f"回复 “t” 查询中奖结果\n\n"\
                                      f"还剩 {remain-1} 次抽奖机会\n\n"\
                                      f"中奖后凭此号码和截图兑换奖品\n\n" \
                                      f"当前已参与人次：{count}\n\n" \

                    else:
                        content = "当前参与人数爆棚，客官您来晚啦"
                else:
                    content = f"您的抽奖机会已经全部用完啦，谢谢参与！ 当前已参与人次：{count}"

            elif content in ("t", "T"):
                result = Award.is_hit(openid)
                if result:
                    content = "恭喜您获得图书一本，请微信联系 lzjun567，凭中奖号码和截图兑换奖品"
                else:
                    content = "有点小遗憾哦，您本次未中奖，再接再厉"
        elif isinstance(msg, SubscribeEvent):
            content = "欢迎！回复'抽奖'可参与抽奖"
        else:
            content = "success"
        return TextReply(msg, content=content).render()


def sign_check():
    """
    微信服务器接口校验
    """
    signature = request.args.get("signature", None)
    echostr = request.args.get("echostr", None)
    timestamp = request.args.get("timestamp", None)
    nonce = request.args.get("nonce", None)
    sign = ["supersoft", timestamp, nonce]
    sign.sort()
    sign = "".join(sign).encode("utf-8")
    sign = sha1(sign).hexdigest()
    if sign == signature:
        # 微信校验成功
        return echostr
    else:
        return 'fail'
