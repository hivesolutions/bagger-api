#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import models

class BagController(appier.Controller):

    @appier.route("/bag", "GET")
    def me_bag(self):
        return models.Bag.get_from_session(map = True)

    @appier.route("/bag/add/<int:product_id>", "POST")
    def add_produc(self, product_id):
        quantity = self.get_field("quantity", cast = int)
        product = models.Product.get(id = product_id)
        bag = models.Bag.get_from_session()
        bag.add_product_s(product, quantity)
        return bag

    @appier.route("/bag/remove/<int:product_id>", "POST")
    def remove_product(self, product_id):
        quantity = self.get_field("quantity", cast = int)
        product = models.Product.get(id = product_id)
        bag = models.Bag.get_from_session()
        bag.remove_product_s(product, quantity)
        return bag
