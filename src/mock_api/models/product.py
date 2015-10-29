#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base
from . import category

class Product(base.BaggerBase):

    name = appier.field(
        type = unicode,
        index = True
    )

    size = appier.field(
        type = unicode,
        index = True
    )

    price = appier.field(
        type = float,
        index = True
    )

    image_url = appier.field(
        type = unicode,
        index = True
    )

    image_urls = appier.field(
        type = list
    )

    category = appier.field(
        type = appier.reference(
            category.Category
        )
    )

    category_name = appier.field(
        type = unicode
    )

    def pre_save(self):
        base.BaggerBase.pre_save(self)

        self.category_name = self.category.name
