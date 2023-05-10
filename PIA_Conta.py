# Solicitamos la información
# Balance general
# **************************
print('\t\t\tBALANCE GENERAL')
print('-'*20)
# Pedimos los Activos
print('\t\t- - - Activos - - -')
print('-'*20)

efectivo = int(input("\tEfectivos: "))
clientes = int(input("\tClientes: "))
deudores = int(input("\tDeudores diversos: "))
funcionarios = int(input("\tFuncionarios y Empleados: "))
inv_mats = int(input("\tInventario de Materiales: "))
inv_ProdFin = int(input("inventario de producto terminado: $"))
tActCircu = (efectivo + clientes + deudores + funcionarios + inv_mats + inv_ProdFin)
print("Total de Activo Circulante: ", tActCircu)

print('-'*20)
terry = int(input("\tTerreno: "))
planta = int(input("\tPlanta y Equipo: "))
despAcum = int(input("\tDepreciacion acomulada: "))
tActNo = (terry + planta - despAcum)
print("Total de Activo No Circulante: ", tActNo)

print('-'*20)
act_tot=(totl_act + total_no)
print("ACTIVO TOTAL: ", tActCircu + tActNo)
print('-'*20)
# Pedimos los Pasivos

print('\t\t- - - Pasivos - - -')
print('-'*20)

proveedores = int(input("\tProveedores: "))
docx = int(input("\tDocumentos por pagar: "))
isr = int(input("ISR por pagar: "))
tPasivosCorto = (proveedores + docx + isr)
print("Total de Pasivo Corto Plazo: ", tPasivosCorto)
print('-'*20)

prestamos = int(input("\tPrestamos bancarios: "))
print("Total de Pasivos a Largo Plazo: ", prestamos)
pas_tot = (tPasivosCorto + prestamos)
print("Pasivo total: ", pas_tot)
print('-'*20)

# Pedimos Capital Contable
print('\t\t- - - Capital Contable - - -')
print('-'*20)

capital_contr = int(input("\tCapital contribuido: "))
capital_ganado = int(input("\tCapital ganado"))
tCapCont = (capital_contr + capital_ganado)
print("Capital Contable Total: ", tCapCont)

# Suma de Pasivo y Capital
sum_pasCapital = (pas_tot + tCapCont)
print("Suma del PASIVO y CAPITAL: ",sum_pasCapital)

# ***************************
# Requerimiento de materiales
# ***************************
print('-'*20)
print("\t\tRequerimientos de Materiales")
print("Material A")
matPrima_A1 = int(input("Producto CF: "))
matPrima_A2 = int(input("Producto CD: "))
matPrima_A3 = int(input("Producto CP: "))
print('-'*20)

print("Material B")
matPrima_B1 = int(input("Producto CF: "))
matPrima_B2 = int(input("Producto CD: "))
matPrima_B3 = int(input("Producto CP: "))
print('-'*20)

print("Material C")
matPrima_C1 = int(input("Producto CF: "))
matPrima_C2 = int(input("Producto CD: "))
matPrima_C3 = int(input("Producto CP: "))
print('-'*20)

print('Horas de Mano de Obra')
hrs_ManoObra_1 = int(input("Producto CF: "))
hrs_ManoObra_2 = int(input("Producto CD: "))
hrs_ManoObra_3 = int(input("Producto CP: "))
print('-'*20)

# ***************************
# Información de Inventarios
# ***************************
print('\t\t- - - Información de Invenarios - - -')
print('-'*20)

print("Inventario Inicial Primer Semestre")
matA_1s = int(input("Material A: "))
matB_1s = int(input("Material B: "))
matC_1s = int(input("Material C: "))
prodCF_1s = int(input("Producto CF: "))
prodCD_1s = int(input("Producto CD: "))
prodCP_1s = int(input("Producto CP: "))
print('-'*20)

print("Inventario Final Segundo Semestre")
matA_2s = int(input("Material A: "))
matB_2s = int(input("Material B: "))
matC_2s = int(input("Material C: "))
prodCF_2s= int(input("Producto CF: "))
prodCD_2s = int(input("Producto CF: "))
prodCP_2s = int(input("Producto CF: "))
print('-'*20)

print("Costo Primer Semestre")
matA_Costo_1s = int(input("Material A: $"))
matB_Costo_1s = int(input("Material B: $"))
matC_Costo_1s = int(input("Material C: $"))
print('-'*20)

print("Costo Segundo Semestre")
matA_Costo_2s = int(input("Material A: $"))
matB_Costo_2s = int(input("Material B: $"))
matC_Costo_2s = int(input("Material C: $"))
print('-'*20)

# ***************************
#          Productos
# ***************************
print("\t\t- - - Productos - - -")
print('-'*20)

print('Precio de Venta Primer Semestre')
cl_1s = int(input('CL: $'))
ce_1s = int(input('CE: $'))
cr_1s = int(input('CR: $'))
print('-'*20)

print('Precio de Venta Segundo Semestre')
cl_2s = int(input('CL: $'))
cl_2s = int(input('CE: $'))
cl_2s = int(input('CR: $'))
print('-'*20)

print('Ventas Planeadas Primer Semestre')
cl_ventas_1s = int(input('CL: '))
cl_ventas_1s = int(input('CE: '))
cl_ventas_1s = int(input('CR: '))
print('-'*20)

print('Ventas Planeadas Segundo Semestre')
cl_ventas_2s = int(input('CL: '))
cl_ventas_2s = int(input('CE: '))
cl_ventas_2s = int(input('CR: '))
print('-'*20)

# ***************************
# Gastos de Administración y Ventas
# ***************************
print("Gastos de Administración y Ventas:")
depreciacion_A = int(input("Depreciacion - Anuales: "))
sueldosS_A = int(input("Sueldos y salarios - Anuales: "))
comisiones = int(input("Comisiones - Porcentaje de las ventas: "))
varios_1s = int(input("Varios - Primer Semestre: "))
varios_2s = int(input("Varios - Segundo Semestre): "))
intereses_prestamo_A = int(input("Interes por Prestamo - Anuales: "))
print('-'*20)

# ***************************
# Gastos de Fabricación Indirectos
# ***************************

print("Gastos de Fabricación Indirectos")
depreciacionA_Fabricacion = int(input("Depreciacion - Anuales: "))
seguros_A = int(input("Seguros - Anuales: "))
mant_1s = int(input("Mantenimiento - Primer Semestre: "))
mant_2s = int(input("Mantenimiento - Segundo Semestre): "))
energeticos_1s = int(input("Energeticos - Primer Semestre: "))
energeticos_2s = int(input("Energeticos - Segundo Semestre): "))
varios_A = int(input("Varios - Anuales: "))
print('-'*20)

# ***************************
#        DESARROLLO
#     Presupuesto Maestro
# ***************************

print('\t\t\t- - - PRESUPUESTO MAESTRO - - -')
print('-'*20)
print('\tI. Presupuesto de Operación')
print('\t\t- - - 1. Presupuesto de Ventas- - -')
print('-'*20)
print('Producto CL')
print('Primer Semestre')

# *********
#        DESARROLLO
#     Presupuesto Maestro
#        jorge
# *********

print('\t\t\t- - - PRESUPUESTO MAESTRO - - -')
print('-'*20)
print('\tI. Presupuesto de Operación')
print('\t\t- - - 1. Presupuesto de Ventas- - -')
print('-'*20)
print('Producto CL')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {cl_ventas_1s}')
print(f'Precio de Ventas semestre1: {cl_1s}')
importe_de_venta_1ersemestre_cf = (cl_1s + cl_ventas_1s)
print(importe_de_venta_1ersemestre_cf)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {cl_ventas_2s}')
print(f'Precio de Ventas semestre2: {cl_2s}')
importe_de_venta_2dosemestre_cf = (cl_2s + cl_ventas_2s)
print(importe_de_venta_2dosemestre_cf)
#Carne diaria
print('Producto CE')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {ce_ventas_1s}')
print(f'Precio de Ventas semestre1: {ce_1s}')
importe_de_venta_1ersemestre_cd = (ce_1s + ce_ventas_1s)
print(importe_de_venta_1ersemestre_cd)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {ce_ventas_2s}')
print(f'Precio de Ventas semestre2: {ce_2s}')
importe_de_venta_2dosemestre_cd = (ce_2s + ce_ventas_2s)
print(importe_de_venta_2dosemestre_cd)
#carne pollo
print('Producto CR')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {cr_ventas_1s}')
print(f'Precio de Ventas semestre1: {cr_1s}')
importe_de_venta_1ersemestre_cp = (cr_1s + cr_ventas_1s)
print(importe_de_venta_1ersemestre_cp)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {cr_ventas_2s}')
print(f'Precio de Ventas semestre2: {cr_2s}')
importe_de_venta_2dosemestre_cp = (cr_2s + cr_ventas_2s)
print(importe_de_venta_2dosemestre_cp)
Total_de_ventas_por_1ersemestre =(importe_de_venta_1ersemestre_cf+importe_de_venta_1ersemestre_cd+importe_de_venta_1ersemestre_cp)
Total_de_ventas_por_2dosemestre =(importe_de_venta_2dosemestre_cf+importe_de_venta_2dosemestre_cd+importe_de_venta_2dosemestre_cp)
Total_de_ventas_por_semestres = (Total_de_ventas_por_1ersemestre+Total_de_ventas_por_2dosemestre)
print(f'total de venta'Total_de_ventas_por_semestres)


#***************
#2.Determinacion del saldo de clientes y flujo de entradas
#****************
print('\t\t- - - 2.Determinacion del saldo de clientes y flujo de entradas- - -')
print('-'*20)
Saldo_de_clientes_31_Dic_2022 = print(f'{clientes}')
ventas_2022 = print(f'{Total_de_ventas_por_semestres}')
Total_de_clientes2022 = (Saldo_de_clientes_31_Dic_2022+ventas_2022)
print(f"Total de clientes 2022:{Total_de_clientes2022}")
print("Entradas de efectivo:")
Por_cobranza2022 = (f'{Saldo_de_clientes_31_Dic_2022}')
Por_cobranza2023 = (ventas_2022)*(0.8)
Cobranza_final = (Por_cobranza2022+Por_cobranza2023)
print(f"cobranza final:"Cobranza_final)
Saldo_de_clientes_31_Dic_2022=(Total_de_clientes2022+Cobranza_final)