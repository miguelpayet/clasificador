from eecc_ahorro import EECCAhorro
from eecc_credito_visa import EECCCreditoVisa
from eecc_credito_visa_legacy import EECCCreditoVisaLegacy
from eecc_credito_amex import EECCCreditoAmex
from numbers_parser import Document
from pathlib import Path
import math
import os


def init(archivo):

    stat = os.stat(archivo)
    fecha = stat.st_birthtime
    base_archivo = Path(archivo).stem

    lectores = [EECCAhorro(), EECCCreditoVisa(), EECCCreditoVisaLegacy(), EECCCreditoAmex()]

    return {"fecha": fecha, "base_archivo": base_archivo, "lectores": lectores}
