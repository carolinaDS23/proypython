from abb import ArbolBinarioBusqueda
from ciberoteca import *
# --- TESTS CLASE CIBEROTECA ---

#Creacion de una instrancia de Ciberoteca
biblioteca = Ciberoteca()

# Test para verificar si el arbol esta vacio
assert biblioteca.cantidad_usuario() == 0
assert biblioteca.cantidad_libro() == 0

assert biblioteca.usuarios.raiz == None
assert biblioteca.usuarios.tamano == 0

#assert biblioteca == None

# Test crear usuario y contiene usuario

usuario_1 = biblioteca.crear_objeto_usuario(33331261, "carogaray@gmail.com","Carolina","Garay","04/06/1990","Caro_23", "1234")
usuario_2 = biblioteca.crear_objeto_usuario(13231261, "sofiamartinez@gmail.com","Sofia","Martinez","14/11/1490","Sofi_w.w", "lovelycomplex")
usuario_3 = biblioteca.crear_objeto_usuario(44331261, "marcosgaray@gmail.com","Marcos","Garay","21/11/2100","marcos_-.-", "3471")

assert biblioteca.contiene_usuario(33331261) == True
assert biblioteca.contiene_usuario(11331261) == False
assert biblioteca.cantidad_usuario() ==  3
assert biblioteca.cantidad_usuario() !=  10

# Test crear usuario y contiene usuario
libro_1 = biblioteca.crear_objeto_libro(1, "enredados", "Carolina Garaycoechea", "romantica","tienda mia", 2000)
libro_2 = biblioteca.crear_objeto_libro(2, "La chica del tren", "Paula Hawkins", "romantica","Planeta", 2015)
assert biblioteca.cantidad_libro() ==  2
assert biblioteca.cantidad_libro() !=  0

# Test buscar usuario
test_buscar = biblioteca.buscar_usuario(30331261)
assert test_buscar == None

test_buscar = biblioteca.buscar_usuario(13231261)
#print (test_buscar)
assert test_buscar.dni == 13231261

# Test dar de baja un usuario
eliminar= biblioteca.baja_usuario(13231261)
assert eliminar == None

biblioteca.mostrar_usuario()
biblioteca.mostrar_libro()

biblioteca.modificar_titulo_libro(libro_1.id, "Enredados")
titulo_libro = biblioteca.buscar_libro(libro_1.id).titulo

# Test modificacion de titulo en un libro
assert titulo_libro == "Enredados"  
assert titulo_libro != "Bajo la misma estrella"  

biblioteca.modificar_anio_libro(libro_1.id, 2001)
nuevo_anio_libro = biblioteca.buscar_libro(libro_1.id).anio_publicado

# Test modificacion del año en un libro
assert nuevo_anio_libro == 2001  
assert nuevo_anio_libro != 2021 

#modificar_editorial_libro(self,id,editorial_nueva)
biblioteca.modificar_editorial_libro(libro_1.id, "Planeta")
nueva_editorial_libro = biblioteca.buscar_libro(libro_1.id).editorial

# Test modificacion del año en un libro
assert nueva_editorial_libro == "Planeta"  
assert nueva_editorial_libro != "tienda mia"