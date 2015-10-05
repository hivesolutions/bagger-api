#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import models

class BagController(appier.Controller):

	@appier.route("/bags/me", "GET")
	@appier.ensure(token = "base")
	def me_bag(self):
		key = self.session.sid
	  	bag = models.Product.find(bag = key)
	   	return bag

	@appier.route("/bags/<int:id>/add/<int:product_id>", "POST")
	@appier.ensure(token = "base")
	def add_to_bag(self, id, product_id):
		size = self.get_field("size", "s", unicode)
		quantity = self.get_field("quantity", 0, int)
		products = models.Product.find(id = id)
		if products.count:
			product = products[0]
			product.size = size
			product.quantity = quantity
			product.bag = self.session.sid
			product.save()
		return product