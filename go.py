# coding: utf-8

import yaml
from check import check_and_buy

def get_config():
    with open('config.yaml', 'r') as f:
        config = yaml.load(f, yaml.SafeLoader)
        print(config)
        return config


if __name__ == '__main__':
    config = get_config()
    check_and_buy(config)
