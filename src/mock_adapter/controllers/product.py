#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class ProductController(appier.Controller):

    @appier.route("/products/<id>.png", "GET")
    def image(self, id):
        file = open("resources/images/bikini1.png", "rb")
        try: data = file.read()
        finally: file.close()
        return data
