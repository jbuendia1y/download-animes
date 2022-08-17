import os
import pymysql

config = {
    "host": os.environ.get("localhost", "localhost"),
    "user": os.environ.get("user", "root"),
    "password": os.environ.get("password", "joaquin$1"),
    "port": int(os.environ.get("port", "3306")),
    "database": "my_animes"
}


def connection():
    """ Return database client """
    c = next(connection_generator())
    return c


def connection_generator():
    c = pymysql.connect(**config)
    yield c
    c.close()
