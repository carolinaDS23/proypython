# Ciberoteca

Este proyecto consta de una biblioteca virtual qué almacena libros (formato PDF) (página de internet con información qué brindan usuarios de la red), qué aportan los usuarios y permiten compartirse de manera gratuita en la comunidad.
Los usuarios podrán acceder a la biblioteca de manera online y gratuita a través de un registro; se podrán leer de manera online y descargar, la manera de buscarlos es por orden id: “número asignado”. Este consta de un conjunto de productos catalogados por nombre, editorial, autor, y año de publicación. la búsqueda será  interna “botón de búsqueda” como externa a través de la plataforma de búsqueda “google, opera, etc”

Para el funcionamiento del programa se implementan diferentes métodos y se realizan los testeos correspondientes para su correcto funcionamiento, la organizacion  es dividirlos archivos separados que estaran dentro de una carpeta, estos contienen: 

- archivo de  estructuras de datos de arboles binarios de busqueda (estos permiten la busqueda y ordenacion del los nodos)

- archivo de clases: 

                - clase Ciberoteca 
                - clase usuarios 
                - clase libros 

- menu de opciones para acceder desde la consola 
- archivos con test implementados y previamente probados en la ejecucion 



## Ofrece un Servicio: 

Consta de Registro de usuario en el sistema, para la posterior lectura y descarga de libros de interes general o especifico, tiene como limite tres descargas por usuarios. 
En la cuarta descarga se cobra un aporte por descarga y lectura del mismo.

### Contextualizando el problema: 
Se presta un servicio que quien adquiera el producto o este interesado se benefiaciara monetariamente de formra pasiva en los cuales los usuarios abonaran un monto para la descarga de libros y lectura siendo usuarios previamente resgistrados en la plataforma diriamos que funciona como una biblioteca virtual de la racopilacion y actualizacion de libros para los interesados. 

## Descripcion: 
usuarios: 

        id 
        gmail
        nombre
        apellido
        fecha_nacimiento
        alias
        contraseña

libros: 

         id
         nombre
         autor
         genero
         editorial
         anio_publicado 

## Funcionalidad: 

El sistema posee las siguientes funcionalidades mas relevantes:

- dar de alta un usuario y libro
- se guarda y lee a traves de la  libreria pickle despues de haber creado el mismo
- buscar libro 
- modificar por una nueva edicion, titulo o año de publicacion
- ABM se implementa un alta, baja, modificaciones y eliminacion del dato o datos ingresados 

## Funcionamiento: 
### abb= Arboles Binarios de Busqueda




Nuestro proyecto consiste en dar altas a usuarios y libros, estas son clases definidas asi como tambien la clase ciberoteca, las primeras  funcionan pasando los parametros para guardarlos y luego inicializarlos.- en cuanto a la clase ciberoteca se crea para reutilizar clase libro y usuario, tambien utilizaremos los Arboles Binarios de Busquedas que nos ayudaran a tener una busqueda mas eficiente y ordenada, se incorpora un menu de opciones el cual cada que vez que ingresemos datos podremos guardarlos en un archivo generadno una base de datos de los elementos guardados gracias a las funcionalidades de la libreria de Pickle.-

Explicamos un poco como es el procedimiento para el uso de clases y abb: 
Una vez creadas las clases mencionadas anteriormente a estas le incorporamos metodos para su utilizacion nuestra biblioteca, tambien utilizamos abb por ejemplo: 

```Python
class Ciberoteca():
    def __init__(self):
        self.usuarios =  ArbolBinarioBusqueda()
        self.libros = ArbolBinarioBusqueda()
 ```
En la clase ciberoteca tenemos los atributos de usuarios y libros que serian instancias de clases, cada nodo del arbol puede tener informacion de estas siendo la estructura del arbol para una busqueda eficiente de la informacion,

```Python
def alta_nuevo_usuario(self,usuario)-> None:
        self.usuarios.agregar(usuario.dni,usuario)
 ```
En esta funcion definida como alta nuevo usuario implementamos abb agregar este toma a la clase usuario accede al dni de usuario 


```Python
def crear_objeto_libro (self, id, titulo, autor, genero, editorial, anio_publicado)-> "Libro":
       libro = Libro(id, titulo, autor, genero, editorial, anio_publicado)
       self.alta_nuevo_libro(libro) #crea el objeto libro y lo agrega al arbol
 ```
La función crear objeto nuevo libro recibe los parámetros id, título, autor, género, editorial y el año publicado para cargarlo en la clase “Libro”  mediante la función “alta_nuevo_libro(libro)” en donde crea el objeto y lo agrega al árbol.



```Python
 def buscar_usuario(self,dni)-> "Usuario":
        return self.usuarios.obtener(dni)
 ```
Contiene usuario devuelve un true si el dni que recibe como parámetro está guardado como clave de algún nodo del abb self.usuarios (es por eso que utilizando el método obtener con el dni como parámetro chequeamos que sea diferente a none) y devuelve un false en caso contrario.


```Python
def contiene_usuario(self,dni)-> bool:
        if self.usuarios.obtener(dni) != None:
          return True
        else:
            return False
 ```
Contiene usuario devuelve un true si el dni que recibe como parámetro está guardado como clave de algún nodo del abb self.usuarios (es por eso que utilizando el método obtener con el dni como parámetro chequeamos que sea diferente a none) y devuelve un false en caso contrario.

```Python
def mostrar_libro(self)-> None:
        self.usuarios.inorden()def modificar_anio_libro(self,id,edicion_nueva)-> None:
        libro_modificado = self.buscar_libro(id)
        if libro_modificado != None:
            libro_modificado.anio_publicado = edicion_nueva
        else:
            print("El año del libro que quiere modificar no existe")
 ```
La función mostrar libro recibe una ciberoteca e imprime todos los nodos dentro de ésta a través del método inorden, el cual modificamos para que en lugar de mostrar las claves de los nodos, muestre las cargas útiles (id, título, autor, género, editorial, año publicado)


```Python
 def cantidad_usuario(self) -> int:
       return self.usuarios.longitud()
 ```
La función cantidad de usuarios permite saber cuántos nodos tengo dentro de la clase ciberoteca,  devuelve un entero(int) para saber cuántos usuarios tengo almacenado en mi clase ciberoteca usuario self.usuarios accediendo al método longitud() de la clase abb que nos brinda el tamaño(cuántos nodos tengo almacenado en el abb usuario)  

```Python
def modificar_anio_libro(self,id,edicion_nueva)-> None:
        libro_modificado = self.buscar_libro(id)
        if libro_modificado != None:
            libro_modificado.anio_publicado = edicion_nueva
        else:
            print("El año del libro que quiere modificar no existe")
 ```
La funcion modificar año de libro nos toma de la clase ciberoteca para luego devolver una edicion nueva mediante una variable buscamos el libro con un id para facilitar su busqueda a traves la funcion bsucar librocuando ingresa en el if si el libro es modificado es distinto de none me lo cambiara por una edicion nueva sino no esta el libro a modificar no existe. 

```Python
def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self,arbol):
        if arbol != None:
            self._inorden(arbol.hijoIzquierdo)
            print(arbol.cargaUtil)
            self._inorden(arbol.hijoDerecho)
 ```
Este metodo inorden define dos métodos relacionados con el recorrido en orden de un árbol binario de búsqueda. El recorrido ordenado es un tipo de recorrido de árboles que sigue el orden izquierda-raíz-derecha.

```Python
def eliminar(self,clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')
 ```
Este metodo de arbol binario de busqueda sirve para eliminar un nodo con una clave especifica de arbol su utilizacioon fue muy importante porque nos ayuda a la hora de eliminar un usuario a traves de un nodo especifico
Si el arbol no tiene nodo o la clave no coincide este emite un mensaje de error. este fue implementado en dar de baja un usuario

### Metodos especiales: 
isdigit: verifica si todos los caracteres son numericos sin espacios 
isalpha: verifica que todos los caracteres sean alfa-numericos 
isalnum: verifica que contenga caracteres alfanumericos por ejemplo el alias que debera contener solo caracteres alfanumericos 
```Python
if opcion == 1:  # Alta nuevo usuario
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
                                usuario = Ciberoteca.crear_objeto_usuario(dni, gmail, nombre, apellido, fecha_nacimiento, alias, contraseña)
                                print("El usuario se agrego")


 ```



## Ejecutando las pruebas ⚙️

### --- TESTS CLASE CIBEROTECA ---

``` Python
usuario_1 = biblioteca.crear_objeto_usuario(33331261, "carogaray@gmail.com","Carolina","Garay","04/06/1990","Caro_23", "1234")
usuario_2 = biblioteca.crear_objeto_usuario(13231261, "sofiamartinez@gmail.com","Sofia","Martinez","14/11/1490","Sofi_w.w", "lovelycomplex")
usuario_3 = biblioteca.crear_objeto_usuario(44331261, "marcosgaray@gmail.com","Marcos","Garay","21/11/2100","marcos_-.-", "3471")

assert biblioteca.contiene_usuario(33331261) == True
assert biblioteca.contiene_usuario(11331261) == False
assert biblioteca.cantidad_usuario() ==  3
assert biblioteca.cantidad_usuario() !=  10
```
En este assert creamos un objeto para poder comprobar si estan correctos le pasamos 3 objetos a los cuales es == 3 que nos devuelve la cantidad de usuarios comprobando que el assert es correcto realizamos lo mismo  para en caso contrario le pasaremos un valor diferente al valor de los datos reales pasara. 


## Autores ✒️

# _Lara Gimenez , Carolina Garaycoechea , Laura Ibaceta_


## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`




---
⌨️ con ❤️ por [ciberotaca.com] 😊