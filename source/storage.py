import datetime
from abc import ABC
from typing import Union, List


from source.types import MessageTypes


class Storage(ABC):
    def save_message(self, message: str, type_: MessageTypes):
        ...

    def get_history(self):
        ...

    def clear_history(self):
        ...

    def delete_message(self):
        ...

    def get_first_visit(self, key: str):
        ...

    def set_first_visit(self, key: str, value: Union[str, bool, List, int, float]):
        ...


class ClientStorage(Storage):

    def __init__(self, client_storage):
        self.storage = client_storage

    def save_message(self, message: str, type_: MessageTypes):
        self.storage.set(f"history.{datetime.datetime.utcnow().timestamp()}", f"{type_.value}__{message}")
        return {"status": 200}

    def get_history(self):
        keys = self.storage.get_keys("history.")
        if keys:
            if len(keys) > 20:
                keys = keys[-20:]
            final_messages = list()
            for key in keys:
                splited = self.storage.get(key).split("__")
                final_messages.append(
                    (splited[0], splited[1], datetime.datetime.fromtimestamp(int(key.split(".")[1])))
                )
            return final_messages
        else:
            return []

    def clear_history(self):
        keys = self.storage.get_keys("history.")
        for key in keys:
            self.storage.remove(key)

    def get_first_visit(self, key: str):
        return self.storage.get(key)

    def set_first_visit(self, key: str, value):
        self.storage.set(key, value)


class APIStorage(Storage):

    def __init__(self):
        ...




