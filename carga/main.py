"""Programa de entrada del extractor de estados de cuenta."""

import argparse
import camelot
from pdfminer.high_level import extract_text
from init import init
import properties
import logging

def identificar_lector(data, archivo):
    text = extract_text(archivo, password=properties.properties.passwordpdf, page_numbers=[0])
    for lector in data['lectores']:
        if lector.es_lector(text):
            lector.inicializar(text)
            return lector
    return None


def main(archivo):

    logging.getLogger("requests").setLevel(logging.CRITICAL)
    data = init(archivo)
    print(data['base_archivo'])
    
    lector = identificar_lector(data, archivo)
    if lector:
        print(lector.nombre)
        tables = camelot.read_pdf(archivo, password=properties.properties.passwordpdf, pages='all')
        for tabla in tables:
            lector.leer_tabla(tabla)
        lector.grabar(properties.properties)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('simple_example')
    parser.add_argument('archivo', help='Nombre de archivo a leer.')
    args = parser.parse_args()
    main(args.archivo)
