#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base
from . import category

class Product(base.BaggerBase):

    name = appier.field(
        index = True
    )

    size = appier.field(
        index = True
    )

    price = appier.field(
        type = float,
        index = True
    )

    image_url = appier.field(
        index = True,
        meta = "url"
    )

    image_urls = appier.field(
        type = list
    )

    category_name = appier.field()

    category = appier.field(
        type = appier.reference(
            category.Category
        )
    )

    @classmethod
    def validate(cls):
        return super(Product, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name")
        ]

    @classmethod
    def list_names(cls):
        return ["id", "name", "price", "image_url", "category_name"]

    def pre_save(self):
        base.BaggerBase.pre_save(self)

        self.category_name = self.category.name
