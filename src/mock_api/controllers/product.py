#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import mock_api

class ProductController(appier.Controller):

    @appier.route("/products/<int:id>.json", "GET")
    def show(self, id):
        product = mock_api.Product.get(id = id, map = True)
        return product

    @appier.route("/products/<int:id>.png", "GET")
    def image(self, id):
        path = "resources/images/product%s.png" % id
        file = open(path, "rb")
        try: data = file.read()
        finally: file.close()
        return data
