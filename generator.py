from layer import Layer

import yaml

def load_assets():
    PATH = 'assets'

    try:
        assets = read_config()
    except:
        print("An exception occured reading the configuration file.")
    finally:
        print("Configuration successfully read.")


def read_config():
    config = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
    return [Layer(**data) for data in config['ASSETS']]

def main():
    load_assets()

if __name__ == "__main__":
    main()