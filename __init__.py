#from .essentials import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .image import IMAGE_CLASS_MAPPINGS, IMAGE_NAME_MAPPINGS
from .mask import MASK_CLASS_MAPPINGS, MASK_NAME_MAPPINGS
from .sampling import SAMPLING_CLASS_MAPPINGS, SAMPLING_NAME_MAPPINGS
from .segmentation import SEG_CLASS_MAPPINGS, SEG_NAME_MAPPINGS
from .misc import MISC_CLASS_MAPPINGS, MISC_NAME_MAPPINGS
from .conditioning import COND_CLASS_MAPPINGS, COND_NAME_MAPPINGS
from .text import TEXT_CLASS_MAPPINGS, TEXT_NAME_MAPPINGS

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

NODE_CLASS_MAPPINGS.update(COND_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(COND_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(IMAGE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(IMAGE_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(MASK_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MASK_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(SAMPLING_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SAMPLING_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(SEG_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SEG_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(TEXT_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(TEXT_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(MISC_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MISC_NAME_MAPPINGS)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
