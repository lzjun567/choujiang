from choujiang.extensions import db
from .base import BaseModel

from sqlalchemy import func


class Award(BaseModel):
    number = db.Column(db.String(10), unique=True)
    open_id = db.Column(db.String(50), nullable=True, default=None)
    valid = db.Column(db.Boolean, default=False, comment="是否为中奖号码")

    @classmethod
    def get_number(cls, open_id):
        """
        分配一个抽奖号码
        :param open_id:
        """
        award = cls.query.filter(cls.open_id.is_(None)).order_by(func.rand()).first()
        if award:
            award.open_id = open_id
            db.commit()
        return award

    @classmethod
    def visit_count(cls, open_id=None):
        if open_id is None:
            return cls.query.filter(cls.open_id.isnot(None)).count()
        else:
            return cls.query.filter(cls.open_id == open_id).count()

    @classmethod
    def is_hit(cls, open_id):
        return cls.query.filter(cls.open_id == open_id).filter(cls.valid.is_(True)).all()
