#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import models

class BagController(appier.Controller):

    @appier.route("/bags/me", "GET")
    def me_bag(self):
        session_id = 1
        bag = models.Bag.find(session_id = session_id)
        return bag

    @appier.route("/bags/<int:id>/add/<int:product_id>", "POST")
    def add_to_bag(self, id, product_id):
        quantity = self.get_field("quantity", cast = int)
        session_id = 1
        product = models.Product.find(id = product_id)[0]
        bag = models.Bag.find(session_id = id)[0]
        bag.add_product_s(product, quantity)
        return bag

    @appier.route("/bags/<int:id>/remove/<int:product_id>", "POST")
    def remove_product(self, id, product_id):
        quantity = self.get_field("quantity", cast = int)
        session_id = 1
        product = models.Product.find(id = product_id)[0]
        bag = models.Bag.find(session_id = id)[0]
        bag.remove_product_s(product, quantity)
        return bag
