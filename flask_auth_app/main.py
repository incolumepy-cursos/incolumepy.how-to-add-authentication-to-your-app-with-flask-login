#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from flask import Blueprint
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Index"


@main.route("/profile")
def profile():
    return "Profile"
