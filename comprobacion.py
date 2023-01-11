import re
from datetime import datetime

def emailValidator(e_mail):

  if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', e_mail):
    return True
  else:
    return False
def dateValidator(fechaNac):
  try:
    datetime.strptime(fechaNac,'%d/%m/%Y')
    return True
  except:
    return False
def nombreValidator(nombre):
  if re.match(r'^[a-zA-Z\s]+$',nombre) and len(nombre)>=3:
    return True
  else:
    return False
  