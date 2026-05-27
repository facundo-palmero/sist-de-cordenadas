coordenadas = [[i for i in range(4)]for j in range(4)]
while True:
    user_rta1 = int(input("ingresa un num de lista o escribe -10 para salir: "))
    if user_rta1 == -10:
        break
    elif user_rta1 > 3:
        print("se pasa de los limites")
        continue
    else:
        user_rta2 = int(input("ok ahora escribe un num: "))
        if user_rta2 > 3:
            print("se pasas de los limites")
            continue
        total = cordenadas[user_rta1][user_rta2]
        print(total)
print("gracias por usar el sist de cordenadas")