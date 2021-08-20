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

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# formatter = logging.Formatter(json.dumps(json_format))
formatter = logging.Formatter("%(levelname)s - %(message)s")
file_handler = logging.FileHandler(f"logger_basic_{datetime.date.today()}.log")
file_handler.setFormatter(formatter)

file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)

class T:
    def __init__(self, name, age):
        logger.info(f"init object")
        self.name = name
        self.age = age

    def __str__(self):
        logger.info(f"call print")
        return f"{self.name} is {self.age} years old"

    def avail(self, num):
        try:
            num = int(num)
        except:
            logger.exception("not int")


t = T("唐僧", 18)
print(t)
t.avail("a")