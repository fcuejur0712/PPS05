from decouple import Config

config = Config()

API_KEY = config.get('API_KEY')
