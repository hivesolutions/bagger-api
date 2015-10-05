#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

import models

class BaggerApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(
            self,
            parts = (
                appier_extras.AdminPart,
            )
        )

BaggerApp().serve()
