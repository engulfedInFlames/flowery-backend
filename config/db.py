import os
import dotenv

env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "flowery",
        "USER": os.environ.get("MYSQL_USER"),
        "PASSWORD": os.environ.get("MYSQL_PW"),
        "HOST": "127.0.0.1",
        "PORT": os.environ.get("MYSQL_PORT"),
        "OPTIONS": {
            "read_default_file": "/path/to/my.cnf",
        },
    }
}
