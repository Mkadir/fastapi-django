"""
ASGI config for democore project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.staticfiles import StaticFiles

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "democore.settings")
apps.populate(settings.INSTALLED_APPS)
from demoapi.views import app as demo_router

application = get_wsgi_application()


def get_application() -> FastAPI:
    # Main Fast API application
    fast_app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)  # To disable docs: docs_url=None,
    # redoc_url=None
    fast_app.mount('/static', StaticFiles(directory='static'), name='static')

    # Set all CORS enabled origins
    fast_app.add_middleware(CORSMiddleware, allow_origins=[str(origin) for origin in settings.ALLOWED_HOSTS] or ["*"],
                            allow_credentials=True, allow_methods=["*"], allow_headers=["*"], )

    # Include all api endpoints

    # Mounts an independent web URL for Django WSGI application
    fast_app.mount(f"{settings.WSGI_APP_URL}", WSGIMiddleware(application))

    fast_app.include_router(demo_router)
    return fast_app


app = get_application()
