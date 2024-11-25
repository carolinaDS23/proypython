from abb import ArbolBinarioBusqueda
import pickle #libreria para guardar y recuperar informacion

class Usuario():
    def __init__(self, dni, gmail, nombre, apellido, fecha_nacimiento, alias, contraseña) -> None:
        self.dni = dni
        self.gmail = gmail
        self.nombre = nombre
        self.apellido = apellido
        self.genero = None
        self.fecha_nacimiento = fecha_nacimiento
        self.alias = alias
        self.contraseña = contraseña

    def __str__(self)-> str:
        return "DNI: {0}\nGmail: {1}\nNombre: {2}\nApellido: {3}\nGenero: {4}\nFecha de nacimiento: {5}\nAlias: {6}\nContraseña: {7}\n" \
            .format(self.dni,self.gmail,self.nombre,self.apellido,self.genero,self.fecha_nacimiento,self.alias, self.contraseña)

class Libro():
    def __init__(self, id, titulo, autor, genero, editorial, anio_publicado)-> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.anio_publicado = anio_publicado

    def __str__(self)-> str:
        return "ID: {0}\nTitulo: {1}\nAutor: {2}\nGenero: {3}\nEditorial: {4}\nAnio publicado: {5}\n" \
            .format(self.id,self.titulo,self.autor,self.genero,self.editorial,self.anio_publicado)

class Ciberoteca():
    def __init__(self):
        self.usuarios =  ArbolBinarioBusqueda()
        self.libros = ArbolBinarioBusqueda()

    def alta_nuevo_usuario(self,usuario)-> None:
        self.usuarios.agregar(usuario.dni,usuario)

    def crear_objeto_usuario (self, dni, gmail, nombre, apellido, fecha_nacimiento, alias, contraseña)-> "Usuario": 
        usuario = Usuario(dni, gmail, nombre, apellido, fecha_nacimiento, alias, contraseña)
        self.alta_nuevo_usuario(usuario) #crea el objeto libro y lo agrega al arbol
        return usuario

    def buscar_usuario(self,dni)-> "Usuario":
        return self.usuarios.obtener(dni)

    def contiene_usuario(self,dni)-> bool:
        if self.usuarios.obtener(dni) != None:
          return True
        else:
            return False

    def baja_usuario(self,dni)-> None:
        self.usuarios.eliminar(dni)

    def mostrar_usuario(self)-> None:
        self.usuarios.inorden()

    def cantidad_usuario(self) -> int:
        return self.usuarios.longitud()
    
    #agrega un nuevo libro
    def alta_nuevo_libro(self,libro)-> None: 
        self.libros.agregar(libro.id, libro)

    def crear_objeto_libro (self, id, titulo, autor, genero, editorial, anio_publicado)-> "Libro": 
        libro = Libro(id, titulo, autor, genero, editorial, anio_publicado)
        self.alta_nuevo_libro(libro) #crea el objeto libro y lo agrega al arbol
        return libro

    def buscar_libro(self,id)->"Libro":
        return self.libros.obtener(id)
    
    def contiene_libro(self,id) -> bool:
        if self.libros.obtener(id) != None:
          return True
        else:
            return False

    def cantidad_libro(self)-> int: # metodo cantidad que trabaja con la ciberoteca
        return self.libros.longitud()

    def baja_libro(self,id)-> None:
        self.usuarios.eliminar(id)

    def mostrar_libro(self) -> None:
        self.libros.inorden()

    def modificar_anio_libro(self,id,edicion_nueva)-> None: 
        libro_modificado = self.buscar_libro(id)
        if libro_modificado != None:
            libro_modificado.anio_publicado = edicion_nueva
        else:
            print("El año del libro que quiere modificar no existe")

    def modificar_titulo_libro(self,id,titulo_nuevo)-> None: 
        libro_modificado = self.buscar_libro(id)
        if libro_modificado != None:
            libro_modificado.titulo = titulo_nuevo
        else:
            print("El titulo del libro que quiere modificar no existe")

    def modificar_editorial_libro(self,id,editorial_nueva)-> None: 
        libro_modificado = self.buscar_libro(id)
        if libro_modificado != None:
            libro_modificado.editorial = editorial_nueva
        else:
            print("El titulo del libro que quiere modificar no existe")

    def guardar_archivo(self,archivo="video.pickle") -> None:
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="video.pickle")-> None:
        pickle_file = open(archivo,'rb')
        biblio = pickle.load(pickle_file)
        self.usuarios = biblio.usuarios
        self.libros = biblio.libros
        pickle_file.close()

def es_letras_y_espacios(cadena):
    return all(caracter.isalpha() or caracter.isspace() for caracter in cadena)

def menu():
    opcion = 0
    while opcion < 1 or opcion > 16:
        print("--")
        print("1) Dar de alta nuevo usuario")
        print("2) Buscar usuario")
        print("3) Mostrar usuarios")
        print("4) Verificar si usuario existe")
        print("5) Baja usuario")
        print("6) Alta a nuevo libro")
        print("7) Buscar libro") 
        print("8) Verificar si libro existe")
        print("9) Mostrar libros")
        print("10) Modificar titulo del libro")
        print("11) Modificar año del libro")
        print("12) Modificar editorial del libro")
        print("13) Baja libro")
        print("14) Guardar archivo")
        print("15) Leer archivo")
        print("16) Salir")
        print("--")
        opcion = int(input("Elija una opcion: "))
        print("--")
            
    return opcion

def run(ciberoteca):
    opcion = 0
    while opcion != 16:
        opcion = menu()

        if opcion == 1:  #alta:nuevo_usuario
            dni = input("Dni: ")
            if not dni.isdigit():
                print("El dni debe contener solo numeros :)")
            elif ciberoteca.contiene_usuario(dni):
                print("El dni ya existe")
            else:
                gmail = input("Gmail: ")
                nombre = input("Nombre: ")
                if not nombre.isalpha():
                    print("El nombre debe contener solo letras.")
                else:
                    apellido = input("apellido: ")
                    if not apellido.isalpha():
                        print("El apellido debe contener solo letras.")
                    else:
                        fecha_nacimiento = input("Fecha de nacimiento: ")
                        alias = input ("Ingrese el nombre de alias: ") 
                        if not alias.isalnum():
                            print("El alias debe contener solo letras y numeros.")
                        else:
                            contraseña = input ("contraseña: ")
                            if not contraseña.isalnum():
                                print("La contraseña debe contener solo letras y numeros.")
                            else:
                                usuario = Usuario (dni, gmail, nombre, apellido, fecha_nacimiento, alias, contraseña)
                                ciberoteca.alta_nuevo_usuario(usuario)
                                print("El usuario se agrego")

        if opcion == 2:   #buscar usuario
            dni = input("DNI: ")
            if not dni.isdigit():
                print("El dni debe contener solo numeros :)")
            else:
                if ciberoteca.buscar_usuario(usuario.dni):  # distinto de None
                    print("El usuario ya existe")
                else:
                    ciberoteca.alta_nuevo_usuario(usuario)
                    print("usuario agregado")

        if opcion == 3:  # Mostrar usuarios
            if ciberoteca.cantidad_usuario() != 0:
                print("Usuarios: ")
                ciberoteca.mostrar_usuario()
            else:
                print("No hay usuarios almacenados") 

        if opcion == 4:  # Verificar si usuario existe
            dni = input("DNI del usuario a verificar: ")
            if not dni.isdigit():
                print("El dni debe contener solo numeros :)")
            else:
                if ciberoteca.contiene_usuario(dni):
                    print("El usuario existe en la ciberoteca.")
                else:
                    print("El usuario no existe en la ciberoteca.")

        if opcion == 5:  #baja usuario
            dni = input("Ingrese el Dni:")
            if not dni.isdigit():
                print("El dni debe contener solo numeros :)")
            else:
                if ciberoteca.contiene_usuario(dni):
                    print("El usuario no existe")
                else:
                    ciberoteca.baja_usuario(usuario)
                    print("Usuario dado de baja")

        if opcion == 6:  #alta:nuevo_libro CAMBIAR DATOS
            id = input("Ingrese el ID del libro: ")
            if not id.isdigit():
                print("El id ingresado debe ser un numero :)")
            else:
                if ciberoteca.contiene_libro(id):
                    print("El libro ya existe")
                else:
                    titulo = input("Ingrese el titulo: ")
                    if not titulo.isalpha():
                        print("El titulo debe contener solo letras.")
                    else:
                        autor = input("Ingrese el autor: ")
                        if not autor.isalpha():
                            print("El autor debe contener solo letras.")
                        else:
                            genero = input("Ingrese el genero: ")
                            if not genero.isalpha():
                                print("El genero debe contener solo letras.")
                            else:
                                editorial = input("Ingrese la editorial: ")
                                if not es_letras_y_espacios(editorial):
                                    print("El nombre de la editorial debe contener solo letras.")
                                else:
                                    anio_publicado = input("Ingrese el año publicado: ")
                                    libro = Libro(id, titulo, autor, genero, editorial, anio_publicado)
                                    ciberoteca.alta_nuevo_libro(libro)
                                    print("Libro Agregado")       

        if opcion == 7:   #CONSULTAR buscar EL LIBRO
            id = input("Ingrese el id del libro: ")
            if not id.isdigit():
                print("El id ingresado debe ser un numero :)")
            else:
                if not ciberoteca.contiene_libro(id):
                    print("El libro no existe")
                else:
                    libro = ciberoteca.buscar_libro(id)
                    print ("Titulo: {0}\n" .format(libro.titulo))

        if opcion == 8:  # Verificar si libro existe
            id_libro = input("ID del libro a verificar: ")
            if not id.isdigit():
                print("El id ingresado debe ser un numero :)")
            else:
                if ciberoteca.contiene_libro(id_libro):
                    print("El libro existe en la ciberoteca.")
                else:
                    print("El libro no existe en la ciberoteca.")

        if opcion == 9:  # Mostrar libros
            if ciberoteca.cantidad_libro() != 0:
                print("Libros: ")
                ciberoteca.mostrar_libro()
            else:
                print("No hay libros almacenados") 

        if opcion == 10:  #MODIFICAR TITULO DE LIBRO
            id = input("Ingrese el id del libro: ")
            if not id.isdigit():
                print("El id ingresado debe ser un numero :)")
            else:
                if ciberoteca.contiene_libro(id):
                    nuevo_titulo = input("Ingrese el titulo nuevo: ")
                    ciberoteca.modificar_titulo_libro(id,nuevo_titulo)
                    print("El titulo del libro ha sido modificado")
                else:
                    print ("El id del libro que quiere modificar no existe")

        if opcion == 11:  #MODIFICAR AÑO DE LIBRO
            id = input("Ingrese el id del libro: ")
            if not id.isdigit():
                print("El id ingresado debe ser un numero :)")
            else:
                if ciberoteca.contiene_libro(id):
                    anio = input("Ingrese el año actualizado: ")
                    ciberoteca.modificar_anio_libro(id, anio)
                    print("El año del libro ha sido modificado")
                else:
                    print ("El año que quiere modificar no existe")

        if opcion == 12:  #MODIFICAR EDITORIAL DE LIBRO
            id = input("Ingrese el id del libro: ")
            if not id.isdigit():
                print("El id ingresado debe ser un numero :)")
            else:
                if ciberoteca.contiene_libro(id):
                    editorial = input("Ingrese la editorial actualizada del libro: ")
                    ciberoteca.modificar_editorial_libro(id,editorial)
                    print("La editorial del libro ha sido modificada")
                else:
                    print ("La editorial que quiere modificar no existe")

        if opcion == 13:      #BAJA LIBRO
            id = input("Ingrese el titulo:")
            if not id.isdigit():
                print("El id ingresado debe ser un numero :)")
            else:
                if ciberoteca.contiene_libro(id):
                    print("El libro no existe")
                else:
                    ciberoteca.baja_libro(libro)
                    print("El libro ha sido dado de baja")

        if opcion == 14:
            ciberoteca.guardar_archivo()

        if opcion == 15:
            ciberoteca.leer_archivo()
        print("usuarios: ", ciberoteca.cantidad_usuario())
        print("libros: ", ciberoteca.cantidad_libro())
        input("Presiona Enter para volver al menú...")

if __name__ == "__main__":
        ciberoteca = Ciberoteca()
        run(ciberoteca)
        print("Saliendo del programa. ¡Hasta luego!")