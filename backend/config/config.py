# backend/tancho/config/config.yml

from motor.motor_asyncio import AsyncIOMotorClient
import yaml


def load_config() -> dict:
    with open('config/config.yml') as yaml_file:
        conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    return conf


CONF = load_config()

DB_CLIENT = AsyncIOMotorClient(
    host=CONF.get("databases", {}).get("default", {}).get("HOST", ""),
    port=CONF.get("databases", {}).get("default", {}).get("PORT", 0),
    username=CONF.get("databases", {}).get("default", {}).get("USER", ""),
    password=CONF.get("databases", {}).get("default", {}).get("PASSWORD", ""),
)

DB = DB_CLIENT[CONF.get("databases", {}).get("default", {}).get("NAME")]


def close_db_client():
    DB_CLIENT.close()
