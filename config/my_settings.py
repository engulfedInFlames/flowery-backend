import os
import dotenv
env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flowery',  # 연동할 mysql db 이름
        'USER': os.environ.get("MYSQL_USER"),  # db 접속 계정명
        'PASSWORD': os.environ.get("MYSQL_PW"),  # 해당 계정 비밀번호
        'HOST': '127.0.0.1',
        'PORT': os.environ.get("MYSQL_PORT"),
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
