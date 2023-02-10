""" Manager for clip interrogator module. """
import logging
from typing import Optional
from config import config

from PIL import Image
from clip_interrogator import Interrogator, Config

logger = logging.getLogger('uvicorn.default')


class ClipInterrogatorManager:
    """ Manager for clip interrogator module. """

    def __init__(self):
        self.interrogator: Optional[Interrogator] = None

    def setup_interrogator(self):
        """ Set up interrogator for use. """
        logger.info('Setting up interrogator')
        self.interrogator = Interrogator(Config(clip_model_name='ViT-L-14/openai'))

    def interrogate(self, image: Image, mode: str = 'normal'):
        """ Perform interrogation. """
        if not self.interrogator:
            raise ValueError('Interrogator not set up')
        mode = config.ai.generator_mode_override if config.ai.generator_mode_override else mode
        if mode == 'normal':
            return self.interrogator.interrogate(image)
        if mode == 'fast':
            return self.interrogator.interrogate_fast(image)
        if mode == 'classic':
            return self.interrogator.interrogate_classic(image)
        raise ValueError(f'Invalid mode {mode}. Supported modes: normal, fast, classic')
