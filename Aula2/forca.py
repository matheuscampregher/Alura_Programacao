def jogar():
    print("----------------------")
    print("Bem-vindo ao Jogo da Forca")
    print("----------------------")
    
    palavra_secreta = "Python"
    
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra: ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(f"Encontrei a letra {letra} na posição {index}")
        print("Jogando...")

    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()
