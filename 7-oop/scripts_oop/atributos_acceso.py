class Acceso:
    def __init__(self):
        self.__privado = "Soy atributo privado"
        self._protegido = "Soy atributo protegido"
        self.publico = "Soy atributo publico"


class SubAcceso(Acceso):
    def print_acceso(self):
        print(self._protegido)

objetoAcceso = Acceso()
objetoSubAcceso = SubAcceso()


# objeto.__privado
print(objetoAcceso._protegido) # no hay problema. No hay protected en Python. Sólo por convención si aparece con un guión bajo
objetoSubAcceso.print_acceso()
# debe asumirse que desde aquí "no se toque"  _protegido por ser protegido -> responsabilidad del usuario.
objetoAcceso._protegido += " y es modificable desde aquí" # pero lo estoy haciendo...

print(objetoAcceso.publico) # accesible y modificable aquí por ser atributo publico "publico"
objetoAcceso.publico += " y también modificable desde aquí"
print(objetoAcceso.publico)

#objetoAcceso.__privado # da Error porque __privado es atributo privado no accesible desde fuera de clase Acceso
#objetoAcceso.__privado += " y menos modificable desde aquí" # si no es accesible desde aquí, no se podrá modificar

print(objetoAcceso.__dict__)
# cuidado porque __privado, sin embargo, puede ser acccedido con _NombreDeSuClase__privado -> ver diccionario.
# NO SE DEBE HACER lo siguiente: PSEUDOPRIVADO. UYYYY, python confía demasiado en el usuario!!!
print(objetoAcceso._Acceso__privado)