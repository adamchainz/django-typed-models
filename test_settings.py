INSTALLED_APPS = (
    "typedmodels",
    "django.contrib.contenttypes",
    "testapp",
)
MIDDLEWARE_CLASSES = ()
DATABASES = {"default": {"NAME": ":memory:", "ENGINE": "django.db.backends.sqlite3"}}
SECRET_KEY = "abc123"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
