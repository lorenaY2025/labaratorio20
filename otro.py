database=[]


def create():
    iden=len(database)+1
    nombre=input("nombre: ")
    edad=int(input("edad "))
    tel=input("telefono: ")
    registro={
        "id":iden,
        "nombre":nombre,
        "edad":edad,
        "tel":tel
        
        }
    database.append(registro)
    
    
def read():
    if len(database)==0:
        print("sin contactos...")
    else:
        for registro in database:
            print(f"ID: {registro["id"]} nombre:{registro["nombre"]} edad :{registro["edad"]} tel: {registro["tel"]}")
            print("------------------------------------------")
def find():
    read()
    if len(database)==0:
        print("no hay registro para buscar...")
    else: idbus=int(input("digite el ID a buscar"))  
    enc=0

    for registro in database:
        if persona["id"]==idbus:
            enc=1
            print("-----------------------------------------")
            print(f"ID: {registro["id"]} nombre:{registro["nombre"]} edad :{registro["edad"]} tel: {registro["tel"]}")
            print("------------------------------------------")


def update():
    if len(datebase)==00:
        print("base de datos vacia")
        read()
        idmod=int(input("IDa modificar:"))
        nombre=input("nombre modificado")
        edad=int(iput("edad modificada"))
        tel=input("telefono modificado:")
        
    personaMod={
        "id":idmod,
        "nombre":nombre,
        "edad":edad,
        "tel" :tel,
    
    }
    for i,registro in enmerate(database):
        if registro["id"]==idmod:
            database[i]=personaMod
def delete():
    if len(databasee)==0:
        print("no hay registros...")
    else:
        read()
        idDel=int(input("ingrese el ID a eleminar:"))
        for i,registro in enumerate(database):
            if registro["id"]==idDel:
                database.pop(i)
      
        
def menu():
    while  True:
        print("lista de contactos")
        print("1. crear contactos")
        print("2. ver contactos")
        print("3. buscar contactos")
        print("4. actualizar contactos")
        print("5. eliminar contactos")
        print("6. salir")
        op=input("ingrese una opcion:")
        if op=="1":
           create()
        elif op=="2":
            read()
        elif op =="3":
            print("estas en la opcion 3.")
        elif op=="4":
            print("estas en la opcion 4.")
        elif op =="5":
            print("estas en la opcion 5.")
        elif op=="6":
            print("estas en la opcion 6.")
            break
        else:
            print("opcion invalida")
menu()
                
                
                