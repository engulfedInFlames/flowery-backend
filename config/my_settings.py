

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flowery',  # 연동할 mysql db 이름
        'USER': 'root',  # db 접속 계정명
        'PASSWORD': 'gP5fls2qkr3!m',  # 해당 계정 비밀번호
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
