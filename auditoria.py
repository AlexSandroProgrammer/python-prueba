# MATRIZ DE DE AUDITORIA DE INVENTARIO

# importación de la data
from data_inventario import inventario

#* --- Funcion Calcular cantidad a pedir validando si el stock es menor al mínimo ---
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0
 
 
# --- LÓGICA PRINCIPAL ---
def auditar_inventario(inventario):
    
    # creamos un arreglo para ingresar los pedidos que se necesitan hacer para reabastecer el inventario
    pedidos = []
 
    # Entramos a consultar cada uno de los articulos 
    for articulo in inventario:
        cantidad_pedido = calcular_pedido(articulo["stock_actual"],articulo["stock_minimo"])
 
        if cantidad_pedido > 0:
            pedidos.append({
                "codigo":       articulo["codigo"],
                "nombre":       articulo["nombre"],
                "stock_actual": articulo["stock_actual"],
                "stock_minimo": articulo["stock_minimo"],
                "cantidad":     cantidad_pedido,
            })
 
    return pedidos
 
 
#* --- Funcion para imprimir el reporte ---
def imprimir_reporte(pedidos):
    separador = "=" * 58
 
    print(separador)
    print("REPORTE DE REABASTECIMIENTO DE INVENTARIO")
    print(separador)
 
    if not pedidos:
        print("  Todo el inventario está en niveles óptimos.")
    else:
        print(f"  {'Código':<8} {'Artículo':<25} {'Actual':>6} {'Mínimo':>7} {'Pedir':>6}")
        print("-" * 58)
        for p in pedidos:
            print(f"  {p['codigo']:<8} {p['nombre']:<25} {p['stock_actual']:>6} {p['stock_minimo']:>7} {p['cantidad']:>6}")
        print("-" * 58)
        print(f"  Total de artículos a reabastecer: {len(pedidos)}")
 
    print(separador)
 
 
# --- Funcion index que se ejecuta mediante la linea de comandos ---
if __name__ == "__main__":
    pedidos = auditar_inventario(inventario)
    imprimir_reporte(pedidos)