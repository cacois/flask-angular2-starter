"""Entry point for the server application."""

import json
import logging
from . import create_app

logger = logging.getLogger(__name__)

app = create_app()

def run():
    """Isolated entry point of the app, if not using manage.py"""
    try:
        app.run('0.0.0.0', 8081)

    except Exception as exc:
        logger.error(exc.message)
    finally:
        # get last entry and insert build appended if not completed
        # Do something here
        pass
