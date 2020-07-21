import pathlib

from ocr_tools import logger

allowed_file_ext = {".pdf", ".jpg", ".jpeg", ".png"}


def validate_input(input_file, output_file) -> bool:
    log = logger.Log.get_logger()
    log.info("Validating input file: {}".format(input_file))

    file_path = pathlib.Path(input_file)
    if file_path.exists() is False or file_path.is_file() is False:
        log.error("Input file is not exists")
        raise RuntimeError('Input file is not exists')

    if file_path.suffix.lower() not in allowed_file_ext:
        log.error("Input file is not allowed")
        raise RuntimeError('Input file is not allowed')

    return True
