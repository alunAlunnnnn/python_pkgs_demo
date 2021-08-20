import logging
import datetime
import json

json_format = {
    "level": "%(levelname)s",
    "time": "%(asctime)s",
    "funcname": "%(funcName)s",
    "message": "%(message)s",
    "line_no": "%(lineno)d",
    "logger_name": "%(name)s",
}

logging.basicConfig(
    filename=f"basic_use_{datetime.date.today()}.log",
    format=json.dumps(json_format),
    level=logging.INFO,
    filemode="w",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class T:
    def __init__(self, name, age):
        logging.info(f"init object")
        self.name = name
        self.age = age

    def __str__(self):
        logging.info(f"call print")
        return f"{self.name} is {self.age} years old"

    def avail(self, num):
        if not isinstance(num, int):
            logging.exception("not int")
        logging.exception("is int")

t = T("唐僧", 18)
print(t)
t.avail("a")