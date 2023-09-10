from dotenv import dotenv_values

config = dotenv_values(".env")

api_token = config["api_token"]
