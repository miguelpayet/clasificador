from eecc import EECC
from eecc_credito_visa import EECCCreditoVisa
from grabador import Grabador
from seccion import Seccion
import re


class EECCCreditoVisaLegacy(EECCCreditoVisa):

    def __init__(self):
        super().__init__()
        self.nombre = 'Estado de Cuenta Tarjeta Visa'
        self.regex_fecha = r'.*Del\s+Al\s\(día de cierre\)\n(\d{2})\/(\d{2})\/(\d{2})\s+(\d{2})\/(\d{2})\/(\d{2})\n'
