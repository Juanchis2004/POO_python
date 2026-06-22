from abc import ABC, abstractmethod

# -----------------------------------------------
# PILAR 1: ABSTRACCIÓN 
# -----------------------------------------------
# Definimos 'Producto' como una clase abstracta heredando de ABC.
# Sigue funcionando como un molde conceptual del que no se pueden crear objetos directos.
class Producto(ABC):
    
    # -----------------------------------------------
    # PILAR 2: ENCAPSAMIENTO (Métodos tradicionales Get y Set)
    # -----------------------------------------------
    # Usamos dos guiones bajos (__nombre) para hacer los atributos estrictamente PRIVADOS.
    def __init__(self, nombre: str, precio: float, codigo: str):
        self.__nombre = nombre
        self.__precio = precio
        self.__codigo = codigo

    # --- Métodos Get y Set tradicionales para Nombre ---
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self.__nombre = nuevo_nombre
        else:
            print("❌ Error: El nombre no puede estar vacío.")

    # --- Métodos Get y Set tradicionales para Precio (Con filtro de seguridad) ---
    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("❌ Error de Encapsulamiento: El precio no puede ser negativo.")

    # --- Método Get tradicional para Código (No tiene Set porque nunca cambia) ---
    def get_codigo(self):
        return self.__codigo

    # -----------------------------------------------
    # PILAR 3: POLIMORFISMO (Método abstracto obligatorio)
    # -----------------------------------------------
    @abstractmethod
    def calcular_descuento(self) -> float:
        pass

    # Método común que aprovecha los getters internos para mostrar la info
    def mostrar_info(self):
        return f"Código: {self.__codigo} | {self.__nombre} | Precio Base: ${self.__precio:.2f}"


# ------------------------------------------------------
# PILAR 4: HERENCIA (Clases Hijas)
# ------------------------------------------------------

# --- CLASE HIJA: ALIMENTO ---
class Alimento(Producto):
    def __init__(self, nombre: str, precio: float, codigo: str, fecha_vencimiento: str):
        # Invocamos al constructor padre
        super().__init__(nombre, precio, codigo)
        # Atributo específico de Alimento
        self.__fecha_vencimiento = fecha_vencimiento

    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento

    def set_fecha_vencimiento(self, nueva_fecha):
        self.__fecha_vencimiento = nueva_fecha

    # REESCRITURA POLIMÓRFICA: Descuento del 10% usando el método get_precio() de la base
    def calcular_descuento(self) -> float:
        return self.get_precio() * 0.10


# --- CLASE HIJA: ELECTRODOMÉSTICO ---
class Electrodomestico(Producto):
    def __init__(self, nombre: str, precio: float, codigo: str, garantia: str):
        # Invocamos al constructor padre
        super().__init__(nombre, precio, codigo)
        # Atributo específico de Electrodomestico
        self.__garantia = garantia

    def get_garantia(self):
        return self.__garantia

    def set_garantia(self, nueva_garantia):
        self.__garantia = nueva_garantia

    # REESCRITURA POLIMÓRFICA: Descuento del 20% usando el método get_precio() de la base
    def calcular_descuento(self) -> float:
        return self.get_precio() * 0.20


# ------------------------------------------------------
# EL SISTEMA CRUD
# ------------------------------------------------------
class Supermercado:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        # Atributo privado que contiene la lista de productos
        self.__inventario = []

    # -----------------------------------------------------------------
    # OPERACIÓN CRUD: CREATE (Crear / Añadir)
    # -----------------------------------------------------------------
    def agregar_producto(self, producto: Producto):
        for p in self.__inventario:
            # Validamos usando el método get_codigo()
            if p.get_codigo() == producto.get_codigo():
                print(f"⚠️ CRUD [Create]: El código {producto.get_codigo()} ya existe.")
                return False
        
        self.__inventario.append(producto)
        print(f"✅ CRUD [Create]: '{producto.get_nombre()}' agregado exitosamente.")
        return True

    # -----------------------------------------------------------------
    # OPERACIÓN CRUD: READ (Leer / Mostrar)
    # -----------------------------------------------------------------
    def mostrar_inventario(self):
        print(f"\n--- 📋 CRUD [Read]: INVENTARIO ACTUAL DE {self.nombre.upper()} ---")
        if not self.__inventario:
            print("El inventario se encuentra vacío.")
            print("-" * 50)
            return

        for p in self.__inventario:
            # Polimorfismo puro ejecutándose mediante llamadas de métodos estándar
            descuento = p.calcular_descuento()
            precio_final = p.get_precio() - descuento
            info_general = p.mostrar_info()
            
            if isinstance(p, Alimento):
                detalles_especificos = f" | Vence: {p.get_fecha_vencimiento()}"
            elif isinstance(p, Electrodomestico):
                detalles_especificos = f" | Garantía: {p.get_garantia()}"
            
            print(f"{info_general}{detalles_especificos} | Descuento: ${descuento:.2f} -> Total Neto: ${precio_final:.2f}")
        print("-" * 60)

    # -----------------------------------------------------------------
    # OPERACIÓN CRUD: UPDATE (Actualizar / Modificar)
    # -----------------------------------------------------------------
    def actualizar_producto(self, codigo: str, nuevo_nombre: str = None, nuevo_precio: float = None):
        for p in self.__inventario:
            if p.get_codigo() == codigo:
                if nuevo_nombre:
                    p.set_nombre(nuevo_nombre)  # Llama al método set
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)  # Llama al método set con validación
                print(f"🔄 CRUD [Update]: Producto con código {codigo} modificado con éxito.")
                return True
        print(f"❌ CRUD [Update]: No se encontró el código {codigo} para actualizar.")
        return False

    # -----------------------------------------------------------------
    # OPERACIÓN CRUD: DELETE (Eliminar / Borrar)
    # -----------------------------------------------------------------
    def eliminar_producto(self, codigo: str):
        for p in self.__inventario:
            if p.get_codigo() == codigo:
                self.__inventario.remove(p)
                print(f"🗑️ CRUD [Delete]: Producto '{p.get_nombre()}' removido del inventario.")
                return True
        print(f"❌ CRUD [Delete]: No se pudo eliminar. El código {codigo} no existe.")
        return False


# -----------------------------------------------
# CONCEPTO: INSTANCIAS Y PRUEBA DE OPERACIONES
# -----------------------------------------------
if __name__ == "__main__":
    
    print("=== INICIANDO SIMULACIÓN DE SISTEMA DE SUPERMERCADO ===")
    
    mi_super = Supermercado("Supermercado Central", "Calle Principal #123")

    print("\n--- 1. PROBANDO INSTANCIAS (Creación de Objetos Reales) ---")
    alimento_1 = Alimento("Leche", 3000, "A123", "20/06/2026")
    electro_1 = Electrodomestico("Licuadora", 150000, "E456", "2 años")
    print(f"Objeto Alimento Creado -> {alimento_1.get_nombre()} ({alimento_1.get_codigo()})")
    print(f"Objeto Electrodoméstico Creado -> {electro_1.get_nombre()} ({electro_1.get_codigo()})")

    print("\n--- 2. PROBANDO CRUD: CREATE ---")
    mi_super.agregar_producto(alimento_1)
    mi_super.agregar_producto(electro_1)

    print("\n--- 3. PROBANDO CRUD: READ ---")
    mi_super.mostrar_inventario()

    print("\n--- 4. PROBANDO CRUD: UPDATE ---")
    mi_super.actualizar_producto("A123", nuevo_precio=3500)
    mi_super.mostrar_inventario()

    print("\n--- 5. PROBANDO COMPORTAMIENTO DE ENCAPSULAMIENTO ---")
    print("Intentando asignar un precio erróneo de -500 a la leche por medio de set_precio()...")
    alimento_1.set_precio(-500)  # Disparará la advertencia de validación sin alterar el valor real

    print("\n--- 6. PROBANDO CRUD: DELETE ---")
    mi_super.eliminar_producto("E456")

    print("\n--- 7. VERIFICACIÓN FINAL DEL INVENTARIO ---")
    mi_super.mostrar_inventario()