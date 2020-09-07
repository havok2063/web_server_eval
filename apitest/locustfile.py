# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Filename: locustfile.py
# Project: apitest
# Author: Brian Cherinka
# Created: Thursday, 2nd April 2020 10:34:01 am
# License: BSD 3-clause "New" or "Revised" License
# Copyright (c) 2020 Brian Cherinka
# Last Modified: Thursday, 2nd April 2020 10:43:20 am
# Modified By: Brian Cherinka


from __future__ import print_function, division, absolute_import
from locust import HttpUser, TaskSet, task, between


class UserBehaviour(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    tasks = {UserBehaviour: 2}
    wait_time = between(5, 9)
