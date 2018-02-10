cadena_ejemplo="Cadena para prueba de join y split"

print (cadena_ejemplo.split())
print ("otra-prueba".split("-"))

con_lista=["Cadena2", "de", "prueba", "de", "join"]

#print (con_lista.join()) # ERROR!
print("".join(con_lista))
print(",".join(con_lista))
