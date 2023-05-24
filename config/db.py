import os
import dotenv

env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "flowery",  # 연동할 mysql connection 이름
        "USER": os.environ.get("MYSQL_USER"),  # mysql 계정 유저네임
        "PASSWORD": os.environ.get("MYSQL_PW"),  # mysql 계정 비밀번호
        "HOST": "127.0.0.1",
        "PORT": os.environ.get("MYSQL_PORT"),
    }
}
