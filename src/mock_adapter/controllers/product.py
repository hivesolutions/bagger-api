#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import models

class ProductController(appier.Controller):

    @appier.route("/products/<int:id>.json", "GET")
    def show(self, id):
        product = models.Product.find(id = id)
        return product

    @appier.route("/products/<id>.png", "GET")
    def image(self, id):
        file = open("resources/images/bikini1.png", "rb")
        try: data = file.read()
        finally: file.close()
        return data