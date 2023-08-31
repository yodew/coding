import yaml

from app.common.constants.env_constants import CONF_CONSUL_HOST, CONF_CONSUL_PORT
from app.common.constants.path_constants import BASE_CONF_YAML_PATH


def base_config():
    with open(BASE_CONF_YAML_PATH, encoding="utf-8") as f:
        yaml_conf = yaml.load(f, Loader=yaml.FullLoader)
        if yaml_conf:
            # 从环境变量中更新consul客户端参数
            if "CONSUL" in yaml_conf and CONF_CONSUL_HOST and CONF_CONSUL_PORT:
                yaml_conf["CONSUL"].update(HOST=CONF_CONSUL_HOST, PORT=CONF_CONSUL_PORT)
            return yaml_conf
    return {}


base_config = base_config()

if __name__ == "__main__":
    print(base_config)