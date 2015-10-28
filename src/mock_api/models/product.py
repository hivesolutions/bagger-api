#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from .category import Category

class Product(appier_extras.admin.Base):

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

    category_id = appier.field(
        type = appier.reference(
            "Category"
        )
    )
    
    category_name = appier.field(
        type = unicode,
        index = True
    )
    
    def pre_save(self):
        appier_extras.admin.Base.pre_save(self)
        
        # sets the category name
        description = str(self.category_id)
        category = Category.get(description = description)
        self.category_name = category.name
