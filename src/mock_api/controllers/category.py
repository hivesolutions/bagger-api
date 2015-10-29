#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import mock_api

class CategoryController(appier.Controller):

    @appier.route("/categories", "GET")
    def list(self):
        object = appier.get_object(alias = True, find = True)
        categories = mock_api.Category.find(map = True, **object)
        return categories

    @appier.route("/categories/<int:id>.png", "GET")
    def image(self, id):
        return self.send_static("images/category%d.png" % id)

    @appier.route("/categories/<int:category>/products", "GET")
    def list_products(self, category):
        object = appier.get_object(alias = True, find = True)
        products = mock_api.Product.find(category = category, **object)
        return products
