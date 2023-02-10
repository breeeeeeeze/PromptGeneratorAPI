from typing import Literal

from pydantic import BaseModel, HttpUrl


class GeneratePromptRequestBody(BaseModel):
    """ Model for image prompt post request body. """
    url: HttpUrl
    mode: Literal['normal', 'fast', 'classic'] = 'fast'


class GeneratePromptResponseBody(BaseModel):
    """" Model for generate prompt response body. """
    message: str
