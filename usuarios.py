class Usuario:
    # 1. El constructor va dentro de la clase (4 espacios)
    def __init__(self, id_usuario, documento, nombre, apellido, correo, telefono, direccion):
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} {self.apellido}")
            
    # 2. Todos los métodos CRUD van a la misma altura de saludar()
    # CREATE
    def crear_usuario(self):
        lista_usuarios.append(self)
        print(f"👌 Éxito: El usuario {self.nombre} ha sido creado exitosamente.")
        
    # READ
    def ver_usuario(self): 
        print(f"ID: {self.id_usuario} | Nombre: {self.nombre} {self.apellido}")
         
    # UPDATE
    def actualizar_usuario(self, nuevo_nombre=None, nuevo_apellido=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_apellido:
            self.apellido = nuevo_apellido
        print(f"👌 Éxito: El usuario {self.nombre} ha sido actualizado exitosamente.")
            
    # DELETE
    def eliminar_usuario(self):
        if self in lista_usuarios:
            lista_usuarios.remove(self)
            print(f"👌 Éxito: El usuario {self.nombre} ha sido eliminado exitosamente.")
        else:
            print(f"❌ Error: El usuario {self.nombre} no se encuentra en la lista.")


# 3. La lista y las pruebas van totalmente a la izquierda (Fuera de la clase)
lista_usuarios = []

# Creando las instancias
usuario1 = Usuario(1, "1055312061", "Juan", "Perez", "juan.perez@example.com", "3001234567", "Calle 123 #45-67")
usuario2 = Usuario(2, "1055312062", "James", "Rodriguez", "maria.gomez@example.com", "3001234568", "Carrera 456 #78-90")

print("--- Nombres individuales ---")
print(usuario1.nombre)  # Juan
print(usuario2.nombre)  # James

print("\n--- Probando Saludos ---")
usuario1.saludar()
usuario2.saludar()

print("\n--- Métodos Crear Usuario ---")
print(f"Lista de usuarios antes: {lista_usuarios}")  # lista vacía
usuario1.crear_usuario()
usuario2.crear_usuario()

print("\n--- Verificando la Lista ---")
print(f"Usuario en posición 0: {lista_usuarios[0].nombre}")
print(f"Usuario en posición 1: {lista_usuarios[1].nombre}")

print("\n--- Leyendo Datos (READ) ---")
usuario1.ver_usuario()
usuario2.ver_usuario()