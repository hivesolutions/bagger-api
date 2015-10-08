#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class Bag(appier_extras.admin.Base):

    lines = appier.field(
        type = dict
    )

    session_id = appier.field(
        type = int
    )
    
    @classmethod
    def get_from_session(cls, **kwargs):
        session_id = 1
        return cls.get(session_id = session_id, **kwargs)
        
    def add_product_s(self, product, quantity):
        if not hasattr(self, "lines"): self.lines = {}
        product_id = "%s" % product.id
        _quantity = self.lines.get(product_id, 0)
        _quantity += quantity
        self.lines[product_id] = _quantity
        self.save()

    def remove_product_s(self, product, quantity):
        if not hasattr(self, "lines"): return
        product_id = "%s" % product.id
        _quantity = self.lines.get(product_id)
        if not _quantity: return
        _quantity -= quantity
        self.lines[product_id] = _quantity
        if _quantity < 1: del self.lines[product_id]
        self.save()
