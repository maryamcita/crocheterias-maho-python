# Este archivo contiene el análisis de los datos del proyecto
"""
Script Principal de Análisis de Datos — Crocheterias Maho
Carga los archivos de datos (productos.csv y pedidos.csv), aplica las funciones de preprocesamiento,
combina los dataframes (merge) y responde a las preguntas clave de análisis de negocio en consola.
"""

import preprocesamiento as prep


def main():
    print("=" * 70)
    print(" CROCHETERIAS MAHO - MODULO DE ANALISIS DE DATOS (MOMENTO 2) ")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # 1. CARGA DE DATOS
    # -------------------------------------------------------------------------
    print("\n[1] CARGANDO DATASETS...")
    df_productos_raw = prep.cargar_datos("data/productos.csv")
    df_pedidos_raw = prep.cargar_datos("data/pedidos.csv")

    # -------------------------------------------------------------------------
    # 2. PREPROCESAMIENTO Y LIMPIEZA DE DATOS
    # -------------------------------------------------------------------------
    print("\n[2] APLICANDO LIMPIEZA Y PREPROCESAMIENTO...")

    # Limpieza de productos
    df_prod = prep.limpiar_moneda(df_productos_raw, "precio_cop")
    df_prod = prep.manejar_nulos(df_prod, estrategia="eliminar", columnas=["precio_cop"])
    df_prod = prep.estandarizar_texto(df_prod, columnas=["nombre", "categoria"], formato="titulo")

    # Limpieza de pedidos
    df_ped = prep.manejar_nulos(df_pedidos_raw, estrategia="eliminar")
    df_ped = prep.estandarizar_texto(df_ped, columnas=["estado_pedido"], formato="mayusculas")
    df_ped = prep.estandarizar_texto(df_ped, columnas=["ciudad_envio"], formato="titulo")

    # -------------------------------------------------------------------------
    # 3. COMBINACIÓN DE DATAFRAMES (MERGE)
    # -------------------------------------------------------------------------
    print("\n[3] COMBINANDO DATAFRAMES (MERGE por id_producto)...")
    df_merged = df_ped.merge(df_prod, on="id_producto", how="inner")
    
    # Calcular subtotal de cada pedido (cantidad * precio_cop)
    df_merged["subtotal_cop"] = df_merged["cantidad"] * df_merged["precio_cop"]

    print(f"[OK] DataFrames combinados exitosamente: {len(df_merged)} transacciones emparejadas.\n")

    # -------------------------------------------------------------------------
    # 4. PREGUNTAS DE ANÁLISIS DE NEGOCIO
    # -------------------------------------------------------------------------
    print("=" * 70)
    print(" RESULTADOS DEL ANALISIS DE DATOS ")
    print("=" * 70)

    # --- PREGUNTA 1: Análisis de Frecuencia ---
    print("\n---> PREGUNTA 1: Analisis de Frecuencia")
    print("Cual es el producto con la mayor cantidad de registros o transacciones de venta?")
    
    frecuencia_productos = (
        df_merged.groupby("nombre")
        .agg(total_transacciones=("id_pedido", "count"), total_unidades=("cantidad", "sum"))
        .sort_values(by="total_transacciones", ascending=False)
    )
    
    producto_top = frecuencia_productos.index[0]
    num_transacciones = int(frecuencia_productos.iloc[0]["total_transacciones"])
    unidades_top = int(frecuencia_productos.iloc[0]["total_unidades"])

    print(f"   * Producto estrella mas vendido: '{producto_top}'")
    print(f"   * Total de transacciones: {num_transacciones} pedidos")
    print(f"   * Total de unidades vendidas: {unidades_top} unidades")

    # --- PREGUNTA 2: Análisis de Agregación ---
    print("\n---> PREGUNTA 2: Analisis de Agregacion")
    print("Calcular el total de ingresos (COP) y unidades vendidas agrupadas por Categoria de producto.")
    
    agregacion_categoria = (
        df_merged.groupby("categoria")
        .agg(
            total_unidades=("cantidad", "sum"),
            ingresos_totales=("subtotal_cop", "sum"),
            precio_promedio=("precio_cop", "mean")
        )
        .reset_index()
    )
    
    agregacion_categoria["ingresos_formateados"] = agregacion_categoria["ingresos_totales"].apply(lambda x: f"${x:,.0f} COP")
    agregacion_categoria["precio_prom_formateado"] = agregacion_categoria["precio_promedio"].apply(lambda x: f"${x:,.0f} COP")

    print("\nResumen por Categoria:")
    print(agregacion_categoria[["categoria", "total_unidades", "ingresos_formateados", "precio_prom_formateado"]].to_string(index=False))

    # --- PREGUNTA 3: Análisis con Filtrado y Conteo ---
    print("\n---> PREGUNTA 3: Analisis con Filtrado y Conteo")
    print("Segmentar pedidos y contar cuantos cumplen condiciones especificas de negocio.")
    
    # Condición A: Pedidos en proceso de producción artesanal ("TEJIENDO")
    pedidos_tejiendo = df_merged[df_merged["estado_pedido"] == "TEJIENDO"]
    unidades_tejiendo = int(pedidos_tejiendo["cantidad"].sum())
    print(f"   * Pedidos actualmente en fase 'TEJIENDO': {len(pedidos_tejiendo)} pedidos ({unidades_tejiendo} productos en confeccion).")

    # Condición B: Pedidos enviados a la ciudad de Medellín
    pedidos_medellin = df_merged[df_merged["ciudad_envio"] == "Medellin"]
    print(f"   * Pedidos registrados con destino 'Medellin': {len(pedidos_medellin)} envios.")

    # Condición C: Pedidos al por mayor (cantidad >= 5 unidades)
    pedidos_al_por_mayor = df_merged[df_merged["cantidad"] >= 5]
    print(f"   * Pedidos al por mayor (>= 5 unidades): {len(pedidos_al_por_mayor)} ordenes.")

    print("\n" + "=" * 70)
    print(" ANALISIS COMPLETADO EXITOSAMENTE ")
    print("=" * 70)


if __name__ == "__main__":
    main()
