texto = 'Hola me llamo juan'
textonuevo = ''
for i in range(len(texto)):
    textonuevo += texto[len(texto-1-i)]
    
print(textonuevo)