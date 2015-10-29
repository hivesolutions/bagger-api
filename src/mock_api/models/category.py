#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Category(base.BaggerBase):

    name = appier.field(
        index = True
    )

    image_url = appier.field(
        index = True
    )

    @classmethod
    def validate(cls):
        return super(Category, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name")
        ]

    @classmethod
    def list_names(cls):
        return ["id", "name", "image_url"]
