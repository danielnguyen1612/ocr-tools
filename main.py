import click

from ocr_tools import logger, validator, pre_processor, utils
from tesserocr import PyTessBaseAPI, OEM


@click.command()
@click.option('-i', '--input', help='Input file path', required=True)
@click.option('-o', '--output', help='Output file path', required=False)
@click.option('-v', '--verbose', help='Enable log verbose', count=True)
def recognize(input, output, verbose):
    # Initialize logger
    log = logger.Log.initialize(verbose)

    validator.validate_input(input, output)

    log.info('Opening output file: {}'.format(output))
    f = open(output, 'a')

    list_images = utils.get_images(input)
    with PyTessBaseAPI(oem=OEM.LSTM_ONLY) as api:
        for image in list_images:
            # Pre-process the image
            pre_processor.pre_processing_file(image)

            # Process OCR
            api.Clear()
            api.SetImageFile(image)

            log.info('Process OCR for image: {}'.format(image))
            text = api.GetUTF8Text()
            f.write(text)

    f.close()
    log.info('Completed to process OCR for {}'.format(input))


if __name__ == '__main__':
    recognize()
