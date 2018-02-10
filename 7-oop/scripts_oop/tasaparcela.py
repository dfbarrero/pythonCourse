import claseparcela


miparcela = claseparcela.Parcela("RM", 100000)

# una vez creada una instancia, se pueden usar
# las propiedades y metodos del objeto
print ("Uso del suelo: ", miparcela.uso_suelo)
mitasa = miparcela.valoracion()
print (mitasa)