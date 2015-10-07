#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import models

class BagController(appier.Controller):

    @appier.route("/bags/me", "GET")
    def me_bag(self):
        session_id = 1
        bag = models.Bag.get(session_id = session_id, map = True)
        return bag

    @appier.route("/bags/<int:id>/add/<int:product_id>", "POST")
    def add_to_bag(self, id, product_id):
        quantity = self.get_field("quantity", cast = int)
        session_id = 1
        product = models.Product.get(id = product_id)
        bag = models.Bag.get(session_id = id)
        bag.add_product_s(product, quantity)
        return bag

    @appier.route("/bags/<int:id>/remove/<int:product_id>", "POST")
    def remove_product(self, id, product_id):
        quantity = self.get_field("quantity", cast = int)
        session_id = 1
        product = models.Product.get(id = product_id)
        bag = models.Bag.get(session_id = id)
        bag.remove_product_s(product, quantity)
        return bag
