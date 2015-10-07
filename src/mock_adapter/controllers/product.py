#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class ProductController(appier.Controller):

    @appier.route("/products/<int:id>.json", "GET")
    def show(self, id):
        product = models.Product.find(id = id)
        return product

    @appier.route("/products/<int:id>.png", "GET")
    def image(self, id):
        path = "resources/images/product%s.png" % id
        file = open(path, "rb")
        try: data = file.read()
        finally: file.close()
        return data
