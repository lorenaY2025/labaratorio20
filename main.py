database=[]

def create():
    iden=len(database)+1
    nombre=input("Nombre: ")
    edad=int(input("Edad: "))
    tel=input("Telefono: ")
    
    persona={
        "id":iden,
        "nombre":nombre,
        "edad":edad,
        "tel":tel
    }
    
    database.append(persona)
    
def read():
    if len(database)==0:
        print("Sin Contactos...")
    else:
        print("----------------------------------")
        for persona in database:
            print(f"ID: {persona["id"]} Nombre: {persona["nombre"]} Edad:{persona["edad"]} Tel: {persona["tel"]} ")
            print("----------------------------------")
    
def find():
    if len(database)==0:
        print("No hay Registros para Buscar...")
    else:
        idbus=int(input("Digite el ID a Buscar: "))
        enc=0
        for persona in database:
            if persona["id"]==idbus:
                 enc=1
                 print("----------------------------------")
                 print(f"ID: {persona["id"]} Nombre: {persona["nombre"]} Edad:{persona["edad"]} Tel: {persona["tel"]} ")
                 print("----------------------------------")
        if enc==0:
            print("El ID no Existe")
                
                
def update():
    if len(database)==0:
        print("Base de Datos Vacia")
    else:
        read()
        idmod=int(input("ID a Modificar: "))
        nombre=input("Nombre Modificado: ")
        edad=int(input("Edad Modificada: "))
        tel=input("Telefono Modificado: ")
        
        personaMod={
        "id":idmod,
        "nombre":nombre,
        "edad":edad,
        "tel":tel
        }
        
        for i,persona in enumerate(database):
            if persona["id"]==idmod:
                database[i]=personaMod
        
def delete():
    if len(database)==0:
        print("No hay Registros...")
    else:
        read()
        idDel=int(input("Ingrese el ID a Eliminar: "))
        for i,persona in enumerate(database):
            if persona["id"]==idDel:
                database.pop(i)

def menu():
    while True:
        print("Lista de Contactos")
        print("1. Crear Contacto")
        print("2. Ver Contactos")
        print("3. Buscar Contacto")
        print("4. Actualizar Contacto")
        print("5. Eliminar Contacto")
        print("6. Salir")
        
        op=input("Ingrese una Opcion: ")
        
        if op=="1":
            create()
        elif op=="2":
            read()
        elif op=="3":
            find()
        elif op=="4":
            update()
        elif op=="5":
            delete()
        elif op=="6":
            print("Saliendo....")
            break
        else:
            print("Ingrese una opcion valida")
            
menu()
