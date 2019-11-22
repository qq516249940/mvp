# backend/tancho/config/config.yml

from motor.motor_asyncio import AsyncIOMotorClient
import yaml


def load_config() -> dict:
    conf = {}
    try:
        with open('config/config.yml') as yaml_file:
            conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    except FileNotFoundError:
        with open('config/config.ci.yml') as yaml_file:
            conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    return conf


CONF = load_config()

if CONF.get("databases", {}).get("default", {}).get("USER", False) and\
        CONF.get("databases", {}).get("default", {}).get("PASSWORD", False):
    client_conf = {
        "host": CONF.get(
            "databases", {}).get("default", {}).get("HOST", "127.0.0.1"),
        "port": CONF.get(
            "databases", {}).get("default", {}).get("PORT", 27017),
        "username": CONF.get(
            "databases", {}).get("default", {}).get("USER", ""),
        "password": CONF.get(
            "databases", {}).get("default", {}).get("PASSWORD", ""),
    }
else:
    client_conf = {
        "host": CONF.get(
            "databases", {}).get("default", {}).get("HOST", "127.0.0.1"),
        "port": CONF.get(
            "databases", {}).get("default", {}).get("PORT", 27017),
    }

DB_CLIENT = AsyncIOMotorClient(**client_conf)

DB = DB_CLIENT[
    CONF.get("databases", {}).get("default", {}).get("NAME", "test_db")
]


def close_db_client():
    DB_CLIENT.close()
