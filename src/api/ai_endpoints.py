""" Endpoints for ai processing. """
import logging
from io import BytesIO
from typing import Union

import requests

from PIL import Image, UnidentifiedImageError
from fastapi import APIRouter, HTTPException

from ai.clip_interrogator_manager import ClipInterrogatorManager
from api.dtos import GeneratePromptRequestBody, GeneratePromptResponseBody

ai_router = APIRouter(prefix='/ai')

clip_interrogator_manager = ClipInterrogatorManager()
clip_interrogator_manager.setup_interrogator()

logger = logging.getLogger('uvicorn.default')


@ai_router.post("/generate_prompt")
async def generate_prompt(prompt_request_body: GeneratePromptRequestBody) -> GeneratePromptResponseBody:
    """ Generate a prompt from an image, given as a URL. """
    logger.info(f'POST received in /ai/generate_prompt')
    response = requests.get(prompt_request_body.url)
    try:
        pil_image = Image.open(BytesIO(response.content)).convert('RGB')
    except UnidentifiedImageError:
        raise HTTPException(status_code=422, detail='Doesn\'t exist or not a valid image')
    logger.info('Image loaded, generating prompt')
    prompt = clip_interrogator_manager.interrogate(pil_image, mode=prompt_request_body.mode)
    logger.info('Done generating, sending response')
    return GeneratePromptResponseBody(message=prompt)
