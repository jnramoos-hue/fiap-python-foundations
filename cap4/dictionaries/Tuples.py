usuarios = {}
emails = ["xpto@xyz.com","xkcd@phd.com"]

tupla = list(enumerate(emails))

for chave in range(0,len(tuple)):
    print ("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome"), input("Digite o nível.")]

    for chave, dado in usuarios.items():
        print("Usuario.: ",dado[0])
        print("Email...: ",dado[1])
        print("Nome....: ",dado[0])
        print("Nível...: ",dado[1])