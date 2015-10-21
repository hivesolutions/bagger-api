#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class Bag(appier_extras.admin.Base):

    session_id = appier.field(
        type = int
    )

    lines = appier.field(
        type = dict
    )

    @classmethod
    def get_from_session(cls, **kwargs):
        bag = cls.get(session_id = 1, raise_e = False)
        if not bag:
            bag = Bag.new()
            bag.session_id = 1
            bag.save()
        return cls.get(session_id = 1, **kwargs)

    def add_product_s(self, product, quantity):
        if not hasattr(self, "lines"): self.lines = {}
        product_id = str(product.id)
        _quantity = self.lines.get(product_id, 0)
        _quantity += quantity
        self.lines[product_id] = _quantity
        self.save()

    def remove_product_s(self, product, quantity):
        if not hasattr(self, "lines"): return
        product_id = str(product.id)
        _quantity = self.lines.get(product_id)
        if not _quantity: return
        _quantity -= quantity
        self.lines[product_id] = _quantity
        if _quantity < 1: del self.lines[product_id]
        self.save()
