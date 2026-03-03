ventas_mañana = float(input("Escribe las ventas de la Mañana "))

ventas_tarde = float(input("Escribe las ventas de la Tarde "))

ventas_noche = float(input("Escribe las ventas de la Noche "))

ventas_totales = ventas_mañana + ventas_tarde + ventas_noche

if ventas_totales >= 150000:
    print("Meta Alcanzada: ", f"${ventas_totales:,.0f}" , " de ventas")
else:
    print("Meta no Alcanzada: ", f"${ventas_totales:,.0f}", " de ventas")