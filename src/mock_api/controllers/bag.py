#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import mock_api

class BagController(appier.Controller):

    @appier.route("/bag", "GET")
    def bag(self):
        return mock_api.Bag.get_from_session(map = True)

    @appier.route("/bag/add", "POST")
    def add_product(self):
        product_id = self.field("product_id", cast = int)
        quantity = self.field("quantity", 1, cast = int)
        bag = mock_api.Bag.get_from_session()
        bag.add_product_s(product_id, quantity = quantity)
        return bag

    @appier.route("/bag/<int:product_id>", "DELETE")
    def remove_product(self, product_id):
        bag = mock_api.Bag.get_from_session()
        bag.remove_product_s(product_id)
        return bag

    @appier.route("/bag/<int:product_id>", "PUT")
    def update_product(self, product_id):
        quantity = self.field("quantity", 1, cast = int)
        bag = mock_api.Bag.get_from_session()
        bag.update_product_s(product_id, quantity = quantity)
        return bag
