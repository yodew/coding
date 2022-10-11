import os

import yaml

from app.common.constants.path_constants import YAML_DIR
from app.common.enums.base_enum import EnvEnum


def get_config() -> dict:
    config_item = dict()
    if os.environ.get("APP_ENV") == EnvEnum.DEV.value:
        files = [f for f in YAML_DIR.iterdir() if f.name.endswith(".yml")]
        for yml_file in files:
            with yml_file.open(encoding="utf-8") as f:
                yaml_conf = yaml.load(f, Loader=yaml.FullLoader)
                if yaml_conf:
                    config_item.update(yaml_conf)
    else:

        pass
    return config_item


all_config = get_config()
