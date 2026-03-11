import tli.config as config
from tli.api import Api

if __name__ == "__main__":
    projects = Api(api_token=config.api_token()).projects()
    for project in projects:
        print(project)
