from typing import Literal

from pydantic import BaseModel, HttpUrl


class ImagePromptRequestBody(BaseModel):
    """ Model for image prompt post request body """
    url: HttpUrl
    mode: Literal['normal', 'fast', 'classic'] = 'fast'
