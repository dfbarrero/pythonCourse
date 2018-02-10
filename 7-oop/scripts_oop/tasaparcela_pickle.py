import pickle
import claseparcela

miparcela = claseparcela.Parcela("RM", 100000)
mitasa = miparcela.valoracion()
print (mitasa)

print("Serializamos el objeto: \n", miparcela)
fout = open("parcelas.db", 'wb')
pickle.dump(miparcela, fout)
fout.close()

fout = open("parcelas.db", 'rb')
miparcelaout = pickle.load(fout)
fout.close()

print("Objeto leido: \n", miparcelaout)
print ("Uso del suelo: ", miparcelaout.uso_suelo)
mitasa2 = miparcelaout.valoracion()
print (mitasa2)