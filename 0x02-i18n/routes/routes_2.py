#!/usr/bin/env python3
"""Basic route 1_app."""
from flask import Blueprint, render_template

app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/', methods=["GET"], strict_slashes=False)
def home():
    """ Home page """
    return render_template('2-index.html')
