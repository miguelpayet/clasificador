from eecc import EECC
from eecc_credito_visa import EECCCreditoVisa
from grabador import Grabador
from seccion import Seccion
import re


class EECCCreditoAmex(EECCCreditoVisa):

    def __init__(self):
        super().__init__()
        self.cuenta = 37
        self.nombre = 'Estado de Cuenta Tarjeta American Express'
