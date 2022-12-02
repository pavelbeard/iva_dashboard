import os
import threading

import yaml

CONFIG = {}


def startup():
    with open(os.path.join(os.getcwd(), 'agent-config.yml'), 'r') as config:
        global CONFIG
        CONFIG = yaml.safe_load(config).get('hosts')


def gen(key: str, i: int):
    import random
    print(random.random().hex(), f"[{key}] - [{i}]")


if __name__ == '__main__':
    startup()

    for each, i in zip(CONFIG.keys(), range(len(CONFIG.keys()))):
        thread = threading.Thread(target=gen, args=(each, i))
        thread.run()
