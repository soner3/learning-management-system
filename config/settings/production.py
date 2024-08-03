from os import getenv, path
from dotenv import load_dotenv
from .base import *  # noqa
from .base import BASE_DIR

if path.isfile(local_env_file):
    load_dotenv(local_env_file)


SECRET_KEY = getenv("DJANGO_SECRET_KEY")


ALLOWED_HOSTS = []

ADMINS = [
    ("Soner Astan", "admin@learning-system.com"),
]
