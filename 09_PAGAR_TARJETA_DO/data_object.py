from dataclasses import dataclass

@dataclass
class DataUser:
    tarjeta:str
    expiracion:str
    cvv:str