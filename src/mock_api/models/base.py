#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier_extras

class BaggerBase(appier_extras.admin.Base):

    @classmethod
    def get_session_id(cls):
        return 1
