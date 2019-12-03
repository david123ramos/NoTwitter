from ibge import *
import json
from pyUFbr.baseuf import ufbr



m = Municipios()
n = m.getId()

f = open("regioes.txt", "w")


for i in n:
    municipio = Municipio(i)
    regiao = municipio.getRegiao()
    dic = {i: regiao}
    f.write(json.dumps(dic))
    f.write("\n")