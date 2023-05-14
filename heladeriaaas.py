print("**Bienvenido a la Heladería Fan´s Levi Live**")  
print("¡Tenemos una amplia variedad de helados! ->")
vcestrellan =500
vchamps =4000
vmeganium =2500
vdonkie =2000
cdonkie =0
cmeganium =0
cchamps=0
ccest=0
conthelado=0
op =""
helado = 0

while op != "5":
    print("***MENÚ***")
    print ("1.Cestrellan")
    print ("2.Champs")
    print ("3.Meganium")
    print ("4.Donkie")
    print ("5.Salir")
    op =input("Ingrese su opción: ")
    if op not in ("1","2","3","4","5"):
        print("***ERROR***")
        print ("Seleccione una opción válida")
    elif op == "1":
        print("____________________________________")
        print ("Usted a seleccionado un Cestrellan")
        print("Cuenta con un precio de $500")
        print(">>>>Según la edad se aplicará o no descuento")
        edad = int(input("->Ingrese edad: "))   
        if edad < 18:
                print(">>Según lo indicado eres menor de edad<<")
                print("--Se aplicará un descuento del 10%"" al Cestrellan--") 
                print("-> Descuento: $50")
                print("-> Precio final: $450 ")
                print("____________________________________")
                vcestrellan = 500-50
                helado+=vcestrellan
                ccest+=1
        elif edad >=60:
                 print(">>Según lo indicado usted es mayor de edad<<")
                 print("--Se aplicará un descuento del 10%"" al Cestrellan--") 
                 print("-> Descuento: $50")
                 print("-> Precio final: $450 ")
                 print("____________________________________")
                 vcestrellan = 500-50
                 helado+=vcestrellan
                 ccest+=1
        elif edad >=18 and edad <60:
             print(">>No se aplicará descuento<<")
             print("-> Precio final: $500 ")
             vcestrellan=500      
             helado+=vcestrellan
             ccest+=1

    elif op == "2":
        print("____________________________________")
        print ("Usted a seleccionado un Champs")
        print("Cuenta con un precio de $4000")
        print(">>>>Según la edad se aplicará un descuento")
        edad = int(input("->Ingrese edad: "))  
        if edad < 18:
                print(">>Según lo indicado eres menor de edad<<")
                print("--Se aplicará un descuento del 10%"" al Champs--") 
                print("-> Descuento: $400")
                print("-> Precio final: $3600 ")
                print("____________________________________")
                vchamps = 4000-400
                helado+=vchamps
                cchamps+=1
        elif edad >=60:
                 print(">>Según lo indicado usted es mayor de edad<<")
                 print("--Se aplicará un descuento del 10%"" al Champs--") 
                 print("-> Descuento: $400")
                 print("-> Precio final: $3600 ")
                 print("____________________________________")
                 vchamps = 4000-400
                 helado+=vchamps
                 cchamps+=1
        elif edad >=18 and edad <60:
             print(">>No se aplicará un descuento")
             print("-> Precio final: $4000 ")
             vchamps=4000
             helado+=vchamps
             cchamps+=1

    elif op == "3":
        print("____________________________________")
        print ("Usted a seleccionado un Meganium")  
        print("Cuenta con un precio de $2500")
        print(">>>>Según la edad se aplicará un descuento")
        edad = int(input("->Ingrese edad: "))         
        if edad < 18:
                print(">>Según lo indicado eres menor de edad<<")
                print("--Se aplicará un descuento del 10%"" al Meganium--")
                print("-> Descuento: $250") 
                print("-> Precio final: $2250")
                print("____________________________________")
                vmeganium = 2500-250
                helado+=vmeganium
                cmeganium+=1
        elif edad >=60:
                 print(">>Según lo indicado usted es mayor de edad<<")
                 print("--Se aplicará un descuento del 10%"" al Meganium--")
                 print("-> Descuento: $250")  
                 print ("-> Precio final: $2250")
                 print("____________________________________")
                 vmeganium = 2500-250
                 helado+=vmeganium
                 cmeganium+=1
        elif edad >=18 and edad <60:
             print(">>No se aplicará un descuento<<")
             print("-> Precio final: $2500 ")
             vmeganium=2500
             helado+=vmeganium
             cmeganium +=1

    elif op == "4":
        print("____________________________________")
        print ("Usted a seleccionado un Donkie ")
        print("Cuenta con un precio de $2000")
        print(">>>>Según la edad se aplicará un descuento")
        edad = int(input("->Ingrese edad: "))         
        if edad < 18:
                print(">>Según lo indicado eres menor de edad<<")
                print("--Se aplicará un descuento del 10%"" al Donkie--")
                print("-> Descuento: $200")  
                print("-> Precio final: $1800")
                print("____________________________________")
                vdonkie = 2000-200
                helado+=vdonkie
                cdonkie+=1
        elif edad >=60:
                 print(">>Según lo indicado usted es mayor de edad<<")
                 print("--Se aplicará un descuento del 10%"" al Donkie--") 
                 print("-> Descuento: $200") 
                 print("-> Precio final: $1800")
                 print("____________________________________")
                 vdonkie = 2000-200
                 helado+=vdonkie
                 cdonkie+=1
        elif edad >=18 and edad <60:
             print(">>No se aplicará un descuento<<")
             print("-> Precio final: $2000 ")
             vdonkie=2000
             helado+=vdonkie
             cdonkie+= 1

    elif op == "5":
        print()
        print ( "Ha salido del menú ")
        print("¡Gracias por preferirnos!")
        ventas = conthelado+helado
        print("==================================")
        print("[""Reporte helado(s) vendido(s)""]")
        print ("Cestrellan :",ccest)
        print ("Champs : ",cchamps)
        print ("Meganium: ",cmeganium)
        print ("Donkie:",cdonkie)
        print ("TOTAL VENTAS: $",ventas)
        print("==================================")
        break
        