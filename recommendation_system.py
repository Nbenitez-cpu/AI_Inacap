# Sistema de Recomendación Inicial

# Lista de productos disponibles
productos = {
    1: {"nombre": "Laptop", "categoria": "Electrónica", "precio": 1200},
    2: {"nombre": "Mouse", "categoria": "Accesorios", "precio": 25},
    3: {"nombre": "Teclado", "categoria": "Accesorios", "precio": 80},
    4: {"nombre": "Monitor", "categoria": "Electrónica", "precio": 350},
    5: {"nombre": "Auriculares", "categoria": "Accesorios", "precio": 150},
}

# Simulación de preferencias de usuario
preferencias_usuario = {
    "usuario_1": ["Electrónica", "Accesorios"],
    "usuario_2": ["Accesorios"],
    "usuario_3": ["Electrónica"],
}

def obtener_recomendaciones(usuario_id):
    """
    Retorna productos recomendados basados en las preferencias del usuario.
    """
    if usuario_id not in preferencias_usuario:
        return []
    
    categorias_preferidas = preferencias_usuario[usuario_id]
    recomendaciones = []
    
    for producto_id, producto in productos.items():
        if producto["categoria"] in categorias_preferidas:
            recomendaciones.append(producto)
    
    return recomendaciones

# Prueba del sistema
if __name__ == "__main__":
    print("=== Sistema de Recomendación ===\n")
    
    for usuario_id in preferencias_usuario.keys():
        print(f"Recomendaciones para {usuario_id}:")
        recomendaciones = obtener_recomendaciones(usuario_id)
        
        for producto in recomendaciones:
            print(f"  - {producto['nombre']} (${producto['precio']})")
        print()
