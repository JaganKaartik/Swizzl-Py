#!/usr/bin/env python3
from swizzl import app
from flask_celery import make_celery


if __name__ == '__main__':
    app.run(debug=True)
 