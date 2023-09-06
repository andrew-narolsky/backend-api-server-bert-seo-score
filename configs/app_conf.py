from os import getenv


class AppConfig:
    API_URL_PREFIX = '/api/v1'
    API_KEY = getenv('API_KEY')
