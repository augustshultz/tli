from dotenv import dotenv_values


def api_token() -> str:
    config = dotenv_values(".env")
    return config["api_token"]
