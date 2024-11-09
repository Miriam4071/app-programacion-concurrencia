from dataclasses import dataclass

@dataclass
class DataUser:
    nombre:str
    email:str
    password:str

#class DataUser:
 #   def __init__(self, nombre, email, password)->None:
  #      self.nombre=nombre
   #     self.email=email
    #    self.password=password