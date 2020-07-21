import pathlib
import tempfile

from os import path
from typing import Set
from pdf2image import convert_from_path
from ocr_tools import logger


def get_images(input_file) -> Set[str]:
    list_images: Set[str] = set({})
    file_path = pathlib.Path(input_file)
    log = logger.Log.get_logger()

    if file_path.suffix.lower() == '.pdf':
        log.info('Input file is PDF then need to convert to images')
        images = convert_from_path(input_file)
        for idx, image in enumerate(images):
            image_name = '{}-{}.jpg'.format(file_path.stem, str(idx))
            log.info('Convert PDF page: %d into image: %s'.format(
                idx, image_name))
            temp_file = path.join(tempfile.gettempdir(), image_name)

            list_images.add(temp_file)
            image.save(temp_file, 'JPEG')
    else:
        list_images.add(input_file)

    return list_images
