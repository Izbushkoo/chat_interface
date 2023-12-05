import json
import os
from typing import Union
from enum import Enum
import aiohttp
from pydantic import BaseModel


class Methods(Enum):
    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"
    patch = "PATCH"


class Endpoint(BaseModel):
    uri: str
    method: str


class MapConfig:

    def __init__(self, config_file: Union[str, None] = None):
        self.config_file = config_file if config_file else '.api_config.json'
        self.config_path = self.find_config(self.config_file)
        self.data = self.read_config(self.config_path)

    @classmethod
    def find_config(cls, file_name: str):
        return os.path.join(os.getcwd(), file_name)

    @classmethod
    def read_config(cls, path):
        with open(path, 'rb') as file:
            return json.load(file)

    def _create_endpoint(self, name):
        try:
            endpoint = self.data[name]
        except KeyError:
            raise KeyError(f"""Endpoint with name '{name}' does not exists in Config""")

        return Endpoint(
            uri=endpoint['end_point'],
            method=Methods(endpoint["method"].upper()).value,
        )

    def get_endpoint_and_method_by_name(self, name: str):
        return self._create_endpoint(name)


class InterfaceAPI:

    def __init__(self,
                 api_config_file_name: Union[str, None] = None,
                 full_source_url: Union[str, None] = None,
                 source_host: str = "localhost",
                 source_port: int = 9999,
                 ):
        self.map_config = MapConfig(api_config_file_name)

        if full_source_url:
            self.source_url = full_source_url
        else:
            self.source_url = f"http://{source_host}:{source_port}"

    async def send_request(self, name: str, **kwargs):

        async with aiohttp.ClientSession(self.source_url) as session:
            endpoint = self.map_config.get_endpoint_and_method_by_name(name)
            async with session.request(
                method=endpoint.method,
                url=endpoint.uri,
                **kwargs
            ) as response:
                if response.status == 200:
                    return response

