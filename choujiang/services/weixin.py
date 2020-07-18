from choujiang import utils

"""
获取access_token

curl "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=23_ygOnBsu-lCsLVuOj8l-TnFsVmbnICaQphSxWJ2bCpidV9CwwW0NWbk-r9yRGkfFa8rpnxrHB-UYEb_lS1qlUlM3dCZSoM12TW8iZbXOZO4x-fYb7_dQepAm_pK55xe6bU0JrO7P7evgzUaj4SHXjAIAETJ&type=TYPE" -F media=@monitor.png -F  description='{"title":VIDEO_TITLE, "introduction":INTRODUCTION}'
{"media_id":"YmLCB7QxFaxZlzViH5XW8CVs6ra2npgYCq-oKV5-_j8","url":"http:\/\/mmbiz.qpic.cn\/mmbiz_png\/cWjdTREJep0OjbvmgdrKQK3MDibzZ8uuOKcjomV9dRyobNVnIMQrJic1AozmXRD5OJBf1sWfj9TYmc1AiaAiasMjyg\/0?wx_fmt=png"}%
"""


class WeiXin:

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app


    def access_token(self):
        pass

    def update_image(self):
        # 上传图片素材
        pass

    def delete_image(self):
        # 删除图片素材
        pass


weixin = WeiXin()
