#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import mock_api

class ProductController(appier.Controller):

    @appier.route("/products/<int:id>", "GET")
    def show(self, id):
        product = mock_api.Product.get(id = id, map = True)
        return product

    @appier.route("/products/<int:id>.png", "GET")
    def image(self, id):
        return self.send_static("images/product%d.png" % id)
