#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from flask import Blueprint, render_template, render_template_string
from flask_login import current_user, login_required
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    return render_template_string(
        """{% extends "base.html" %}{% block content %}<h1 class="title"> Welcome, {{username}}!</h1>{% endblock %}""",
        username=current_user.name
    )
