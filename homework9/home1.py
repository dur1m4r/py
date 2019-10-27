def boys_and_girls(list):
    output = [0,0]
    for i in list:
        i = i.split(" ")
        if i[len(i)-1] == "G":
            output[1] +=1
        elif i[len(i)-1] == "B":
            output[0] += 1
    return output


print(boys_and_girls(['Mark B', 'Ella G', 'Robert Hugo B', 'Ralf B', 'Veronika G']))

