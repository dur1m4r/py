def einsum(u,v):
    final = (u+v)/(1+(u*v/299792.458**2))
    return final

totalSpeed = 0
body1 = float(input("The speed of the first body with respect to the observer is: "))
body2 = float(input("The speed of the second body with respect to the first is: "))
body3 = float(input("The speed of the third body with respect to the second is: "))
body4 = float(input("The speed of the fourth body with respect to the third is: "))
totalSpeed += einsum(body1, body2)
totalSpeed += einsum(body2, body3)
totalSpeed += einsum(body3, body4)

print ("Sum of speeds is "+str(totalSpeed)+" km/s")
              
