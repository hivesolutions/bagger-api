#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Bag(base.BaggerBase):

    session_id = appier.field(
        type = int,
        index = True
    )

    lines = appier.field(
        type = dict
    )

    @classmethod
    def get_from_session(cls, **kwargs):
        session_id = cls.get_session_id()
        bag = cls.get(session_id = session_id, raise_e = False)
        if not bag:
            bag = Bag.new()
            bag.session_id = session_id
            bag.save()
        return cls.get(session_id = session_id, **kwargs)

    def add_product_s(self, product_id, quantity = 1):
        product_id = str(product_id)
        _quantity = self.lines.get(product_id, 0)
        _quantity += quantity
        self.lines[product_id] = _quantity
        self.save()

    def remove_product_s(self, product_id):
        product_id = str(product_id)
        _quantity = self.lines.get(product_id, None)
        if not _quantity: return
        self.update_product_s(product_id, quantity = _quantity * -1)      

    def update_product_s(self, product_id, quantity = 1):
        product_id = str(product_id)
        _quantity = self.lines.get(product_id, None)
        if not _quantity: return
        _quantity += quantity
        self.lines[product_id] = _quantity
        if _quantity < 1: del self.lines[product_id]
        self.save()
        