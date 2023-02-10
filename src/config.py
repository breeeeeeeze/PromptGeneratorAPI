import os
from dataclasses import dataclass
from typing import Union

from utils.config_reader import read_config
from utils.path_ops import get_parent


@dataclass
class AiConfig:
    generator_mode_override: Union[str, None]


@dataclass
class ApiConfig:
    port: int
    reload: bool


@dataclass
class Config:
    ai: AiConfig
    api: ApiConfig


config_dict = read_config(get_parent(__file__) / f'config.{os.environ.get("PYTHON_ENV")}.json')
api_config = ApiConfig(**config_dict['api'])
ai_config = AiConfig(**config_dict['ai'])
config = Config(ai=ai_config, api=api_config)
