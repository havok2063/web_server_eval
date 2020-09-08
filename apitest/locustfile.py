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

    @task(2)
    def header(self):
        self.client.get("/header")

    @task(2)
    def async_header(self):
        self.client.get("/aheader")

    @task(2)
    def flux_ext(self):
        self.client.get("/file/flux")

    @task(2)
    def wave_ext(self):
        self.client.get("/file/wave")

    @task(2)
    def download_image(self):
        self.client.get("/dlimage")


class WebsiteUser(HttpUser):
    tasks = {UserBehaviour: 2}
    wait_time = between(5, 9)
