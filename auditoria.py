# ============================================================
#  AUDITORÍA DE INVENTARIO - Sistema de Reabastecimiento
# ============================================================

# --- MATRIZ DE INVENTARIO ---
# Estructura: [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    ["A001", "Teclado Mecánico",      12,  20],
    ["A002", "Monitor 24 pulgadas",    5,   5],
    ["A003", "Mouse Inalámbrico",      3,  15],
    ["A004", "Auriculares USB",        0,  10],
    ["A005", "Silla Ergonómica",       8,   6],
    ["A006", "Webcam Full HD",         2,  12],
    ["A007", "Disco Duro Externo 1TB", 7,   4],
]

# --- MÓDULO: Calcular cantidad a pedir ---
def calcular_pedido(stock_actual, stock_minimo):
    
    """
    Determina la cantidad exacta a pedir para un artículo.
    - Si stock actual < mínimo requerido → pedir la diferencia
    - Si stock actual >= mínimo requerido → no pedir (retorna 0)
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


# --- LÓGICA PRINCIPAL ---
def auditar_inventario(inventario):
    """Recorre el inventario y genera la lista de pedidos."""
    pedidos = []

    for articulo in inventario:
        codigo      = articulo[0]
        nombre      = articulo[1]
        stock_actual  = articulo[2]
        stock_minimo  = articulo[3]

        cantidad_pedido = calcular_pedido(stock_actual, stock_minimo)

        if cantidad_pedido > 0:
            pedidos.append({
                "codigo":   codigo,
                "nombre":   nombre,
                "stock_actual": stock_actual,
                "stock_minimo": stock_minimo,
                "cantidad": cantidad_pedido,
            })

    return pedidos


# --- SALIDA ---
def imprimir_reporte(pedidos):
    """Imprime el reporte de pedidos de forma clara y legible."""
    separador = "=" * 58

    print(separador)
    print("       REPORTE DE REABASTECIMIENTO DE INVENTARIO")
    print(separador)

    if not pedidos:
        print("  Todo el inventario está en niveles optimos. No hay pedidos.")
    else:
        print(f"  {'Código':<8} {'Artículo':<25} {'Actual':>6} {'Mínimo':>7} {'Pedir':>6}")
        print("-" * 58)
        total_articulos = 0
        for p in pedidos:
            print(f"  {p['codigo']:<8} {p['nombre']:<25} {p['stock_actual']:>6} {p['stock_minimo']:>7} {p['cantidad']:>6}")
            total_articulos += 1
        print("-" * 58)
        print(f"  Total de artículos a reabastecer: {total_articulos}")

    print(separador)


# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    pedidos = auditar_inventario(inventario)
    imprimir_reporte(pedidos)