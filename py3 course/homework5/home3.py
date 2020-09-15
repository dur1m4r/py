dragons = int(input("Nubmer of dragons: "))
snakes = int(input("Nubmer of snakes: "))
dinosaurs = int(input("Nubmer of dinosaurs: "))
days = 0
while True:
    if dragons < 1:
        pass
    else:
        snakes = snakes - dragons
    print("Zmei ",snakes)
    if snakes < 1:
        pass
    else:
        dinosaurs = dinosaurs - snakes
    print("Dino ",dinosaurs)
    if dinosaurs < 1:
        pass
    else:
        dragons = dragons - dinosaurs
    print ("Drakoshi ",dragons)
    days +=1
    print ("Dni ",days)
    if dragons < 1 and dinosaurs < 1:
        print ("The last meal will be on day",days)
        print ("There will be",snakes,"snakes left")
        break
    if dragons < 1 and snakes < 1:
        print ("The last meal will be on day",days)
        print ("There will be",dinosaurs,"dinosaurs left")
        break
    if dinosaurs < 1 and snakes < 1:
        print ("The last meal will be on day",days)
        print ("There will be",dragons,"dragons left")
        break
