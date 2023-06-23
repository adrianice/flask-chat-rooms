class Config:
    SECRET_KEY = 'mysecretkey'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flaskchat'
    MYSQL_CHARSET = 'utf8mb4'
    MYSQL_COLLATION = 'utf8mb4_bin'
    SESSION_TYPE = 'filesystem'

config = {
    'development': DevelopmentConfig
}