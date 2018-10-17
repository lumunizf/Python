print ("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
    print ("Você venceu!")
else:
    if guess > 5:
        print ("Passou do Ponto!")
    else:
        print ("Quase lá!")
print ("Game Over!")
