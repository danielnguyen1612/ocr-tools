# OCR Tool
This tool help to recognize text based on TesseractOCR

## Installation guide
1. Install [poetry](https://python-poetry.org/)
2. Install dependencies by poetry following command
```bash
poetry install
```
3. Run the main program following command
```bash
poetry run python main.py -i [INPUT] -o [OUTPUT]
```
More details can get from help menu
```bash
Usage: main.py [OPTIONS]

Options:
  -i, --input TEXT   Input file path  [required]
  -o, --output TEXT  Output file path
  -v, --verbose      Enable log verbose
  --help             Show this message and exit.
```
