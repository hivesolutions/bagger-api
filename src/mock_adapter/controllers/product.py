#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import models

class ProductController(appier.Controller):

    @appier.route("/categories/<category>/products.json", "GET")
    def list(self, category):
        skip = self.get_field("skip", 0, int)
        limit = self.get_field("limit", 25, int)
        products = models.Product.find(skip = skip, limit = limit)
        return products

    @appier.route("/products/<object_id>.png", "GET")
    def image(self, object_id):
        file = open("resources/images/bikini1.png", "rb")
        try: data = file.read()
        finally: file.close()
        return data
