#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Category(base.BaggerBase):

    name = appier.field(
        type = unicode,
        index = True
    )

    image_url = appier.field(
        type = unicode,
        index = True
    )
