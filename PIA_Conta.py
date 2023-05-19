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

# Error de calculo de la 21 a la 29
print('-'*20)
terry = int(input("\tTerreno: "))
planta = int(input("\tPlanta y Equipo: "))
despAcum = int(input("\tDepreciacion acomulada: "))
tActNo = (terry + planta) - (despAcum)
print("Total de Activo No Circulante: ", tActNo)

print('-'*20)
act_tot=(tActCircu + tActNo)
print("ACTIVO TOTAL: ", act_tot)
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
matPrima_A1 = float(input("Producto CF: "))
matPrima_A2 = float(input("Producto CD: "))
matPrima_A3 = float(input("Producto CP: "))
print('-'*20)

print("Material B")
matPrima_B1 = float(input("Producto CF: "))
matPrima_B2 = float(input("Producto CD: "))
matPrima_B3 = float(input("Producto CP: "))
print('-'*20)

print("Material C")
matPrima_C1 = float(input("Producto CF: "))
matPrima_C2 = float(input("Producto CD: "))
matPrima_C3 = float(input("Producto CP: "))
print('-'*20)

print('Horas de Mano de Obra')
hrs_ManoObra_1 = float(input("Producto CF: "))
hrs_ManoObra_2 = float(input("Producto CD: "))
hrs_ManoObra_3 = float(input("Producto CP: "))
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
ce_2s = int(input('CE: $'))
cr_2s = int(input('CR: $'))
print('-'*20)

print('Ventas Planeadas Primer Semestre')
cl_ventas_1s = int(input('CL: '))
ce_ventas_1s = int(input('CE: '))
cr_ventas_1s = int(input('CR: '))
print('-'*20)

print('Ventas Planeadas Segundo Semestre')
cl_ventas_2s = int(input('CL: '))
ce_ventas_2s = int(input('CE: '))
cr_ventas_2s = int(input('CR: '))
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
print('\tProducto CL')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {cl_ventas_1s}')
print(f'Precio de Ventas semestre1: {cl_1s}')
importe_de_venta_1ersemestre_cf = (cl_1s * cl_ventas_1s)
print(importe_de_venta_1ersemestre_cf)
print('-'*20)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {cl_ventas_2s}')
print(f'Precio de Ventas semestre2: {cl_2s}')
importe_de_venta_2dosemestre_cf = (cl_2s * cl_ventas_2s)
print(importe_de_venta_2dosemestre_cf)
print('-'*20)
#Carne diaria
print('\tProducto CE')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {ce_ventas_1s}')
print(f'Precio de Ventas semestre1: {ce_1s}')
importe_de_venta_1ersemestre_cd = (ce_1s * ce_ventas_1s)
print(importe_de_venta_1ersemestre_cd)
print('-'*20)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {ce_ventas_2s}')
print(f'Precio de Ventas semestre2: {ce_2s}')
importe_de_venta_2dosemestre_cd = (ce_2s * ce_ventas_2s)
print(importe_de_venta_2dosemestre_cd)
print('-'*20)
#carne pollo
print('\tProducto CR')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {cr_ventas_1s}')
print(f'Precio de Ventas semestre1: {cr_1s}')
importe_de_venta_1ersemestre_cp = (cr_1s * cr_ventas_1s)
print(importe_de_venta_1ersemestre_cp)
print('-'*20)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {cr_ventas_2s}')
print(f'Precio de Ventas semestre2: {cr_2s}')
importe_de_venta_2dosemestre_cp = (cr_2s * cr_ventas_2s)
print(importe_de_venta_2dosemestre_cp)
print('-'*20)
Total_de_ventas_por_1ersemestre =(importe_de_venta_1ersemestre_cf+importe_de_venta_1ersemestre_cd+importe_de_venta_1ersemestre_cp)
Total_de_ventas_por_2dosemestre =(importe_de_venta_2dosemestre_cf+importe_de_venta_2dosemestre_cd+importe_de_venta_2dosemestre_cp)
Total_de_ventas_por_semestres = (Total_de_ventas_por_1ersemestre+Total_de_ventas_por_2dosemestre)
print(f'total de venta{Total_de_ventas_por_semestres}')
print('-'*20)

#***************
#2.Determinacion del saldo de clientes y flujo de entradas
#****************
print('\t\t- - - 2.Determinacion del saldo de clientes y flujo de entradas- - -')
print('-'*20)
print(f'\tTotal')
Saldo_de_clientes_31_Dic_2022 = clientes
print(f'Saldo de Clientes 31-Dic-2022: {Saldo_de_clientes_31_Dic_2022}')
ventas_2022 = Total_de_ventas_por_semestres 
print(f'Ventas 2022: {ventas_2022}')
Total_de_clientes2022 = (Saldo_de_clientes_31_Dic_2022+ventas_2022) # ERROR EN ESTA LÍNEA -> CREO QUE LO CORREGÍ
print(f"Total de clientes 2022:{Total_de_clientes2022}")
print('-'*20)
print('\tImporte')
print("\tEntradas de efectivo:")
Por_cobranza2022 = Saldo_de_clientes_31_Dic_2022
print(f'Por cobranza 2022: {Por_cobranza2022}')
Por_cobranza2023 = (ventas_2022)*(0.8)
print(f'Por cobranza 2023: {Por_cobranza2023}')
Cobranza_final = (Por_cobranza2022+Por_cobranza2023)
print(f"cobranza final:{Cobranza_final}")
Saldo_de_clientesfinal=(Total_de_clientes2022+Cobranza_final)
print(f'Saldo de Clientes Final: {Saldo_de_clientesfinal}')
print('-'*20)

#****************************
#3. Presupuesto de Producción
#*****************************
#Producto CF
print('\t\t- - -3. Presupuesto de Producción - - -')
print('-'*20)
print('\tProducto CF')
print("\tPrimer semestre")
unidades_a_vender_1ersemestre = cl_ventas_1s
print(f'unidades a vender{unidades_a_vender_1ersemestre}')
inventario_inicial=prodCF_1s 
inventario_final= inventario_inicial
print(f'inventario final{inventario_final}')
total_unidades=(unidades_a_vender_1ersemestre+inventario_final)
print(f'total de unidades{total_unidades}')
Unidades_a_producir_1ersemestre = (total_unidades-inventario_inicial)
print('-'*20)

print("\tSegundo semestre")
unidades_a_vender_2dosemestre = cl_ventas_2s
print(f'unidades a vender{unidades_a_vender_2dosemestre}')
inventario_inicial_2dosemestre= cl_ventas_2s
inventario_final_2dosemestre= inventario_inicial_2dosemestre
print(f'inventario final{inventario_final_2dosemestre}')
total_unidades_2dosemestre=(unidades_a_vender_2dosemestre+inventario_final_2dosemestre)
print(f'total de unidades{total_unidades_2dosemestre}')
inverario_inicial_2dosemestre=prodCF_2s
Unidades_a_producir_2dosemestre = (total_unidades_2dosemestre-inverario_inicial_2dosemestre)
print(f"Unidades a producir en el segundo semestre{Unidades_a_producir_2dosemestre}")
print('-'*20)

total_unidades_aventa2023=(unidades_a_vender_1ersemestre+unidades_a_vender_2dosemestre)
print(f'total de unidades a vender:{total_unidades_aventa2023}')
total_inventarioFinal2023=(inventario_final+inventario_final_2dosemestre)
print(f'total inventario final:{total_inventarioFinal2023}')
total_deUnidades2023=(total_unidades+total_unidades_2dosemestre)
print(f'total de unidades:{total_deUnidades2023}')
total_inventarioInicial2023=(inventario_inicial+inverario_inicial_2dosemestre)
print(f'total de inventario inicial:{total_inventarioInicial2023}')
total_unidades_aProducir2023=(Unidades_a_producir_1ersemestre+Unidades_a_producir_2dosemestre)
print(f'total de unidades a producir:{total_unidades_aProducir2023}')
print('-'*20)

#Producto CD
print('\tProducto CD')
print("\tPrimer semestre")
unidades_a_vender_1ersemestreCD = ce_ventas_1s
print(f'unidades a vender CD {unidades_a_vender_1ersemestreCD}')
inventario_inicialCD=prodCD_1s
inventario_finalCD= inventario_inicialCD
print(f'inventario final CD {inventario_finalCD}')
total_unidadesCD=(unidades_a_vender_1ersemestreCD+inventario_finalCD)
print(f'Total de unidades CD {total_unidadesCD}')
Unidades_a_producir_1ersemestreCD = (total_unidadesCD-inventario_inicialCD)
print('-'*20)

print("\tSegundo semestre")
unidades_a_vender_2dosemestreCD = ce_ventas_2s
print(f'Unidades a vender CD{unidades_a_vender_2dosemestreCD}')
inventario_inicial_2dosemestreCD = prodCD_2s
inventario_final_2dosemestreCD= inventario_inicial_2dosemestreCD
print(f'Inventario final CD {inventario_final_2dosemestreCD}')
total_unidades_2dosemestreCD=(unidades_a_vender_2dosemestreCD+inventario_final_2dosemestreCD)
print(f'Total de unidades CD{total_unidades_2dosemestreCD}')
inverario_inicial_2dosemestreCD=prodCD_2s
Unidades_a_producir_2dosemestreCD = (total_unidades_2dosemestreCD-inverario_inicial_2dosemestreCD)
print(f"Unidades a producir en el segundo semestre CD{Unidades_a_producir_2dosemestreCD}")
print('-'*20)

total_unidades_aventa2023CD=(unidades_a_vender_1ersemestreCD+unidades_a_vender_2dosemestreCD)
print(f'Total de unidades a vender CD:{total_unidades_aventa2023CD}')
total_inventarioFinal2023CD=(inventario_finalCD+inventario_final_2dosemestreCD)
print(f'Total inventario final CD:{total_inventarioFinal2023CD}')
total_deUnidades2023CD=(total_unidadesCD+total_unidades_2dosemestreCD)
print(f'Total de unidades CD:{total_deUnidades2023CD}')
total_inventarioInicial2023CD=(inventario_inicialCD+inverario_inicial_2dosemestreCD)
print(f'Total de inventario inicial CD:{total_inventarioInicial2023CD}')
total_unidades_aProducir2023CD=(Unidades_a_producir_1ersemestreCD+Unidades_a_producir_2dosemestreCD)
print(f'Total de unidades a producir CD:{total_unidades_aProducir2023CD}')
print('-'*20)

#Producto CP
print('\tProducto CP')
print("\tPrimer semestre")
unidades_a_vender_1ersemestreCP = cr_ventas_1s
print(f'Unidades a vender CP{unidades_a_vender_1ersemestreCP}')
inventario_inicialCP=prodCD_1s 
inventario_finalCP= inventario_inicialCP
print(f'Inventario final CP:{inventario_finalCP}')
total_unidadesCP=(unidades_a_vender_1ersemestreCP+inventario_finalCP)
print(f'Total de unidades CP:{total_unidadesCP}')
Unidades_a_producir_1ersemestreCP = (total_unidadesCP-inventario_inicialCP)
print('-'*20)

print("\tSegundo semestre")
unidades_a_vender_2dosemestreCP = ce_ventas_2s
print(f'Unidades a vender CP:{unidades_a_vender_2dosemestreCP}')
inventario_inicial_2dosemestreCP= ce_ventas_2s
inventario_final_2dosemestreCP= inventario_inicial_2dosemestreCP
print(f'Inventario final CP:{inventario_final_2dosemestreCP}')
total_unidades_2dosemestreCP=(unidades_a_vender_2dosemestreCP+inventario_final_2dosemestreCP)
print(f'Total de unidades CP:{total_unidades_2dosemestreCP}')
inverario_inicial_2dosemestreCP=prodCP_2s
Unidades_a_producir_2dosemestreCP = (total_unidades_2dosemestreCP-inverario_inicial_2dosemestreCP)
print(f"Unidades a producir en el segundo semestre CP:{Unidades_a_producir_2dosemestreCP}")
print('-'*20)

total_unidades_aventa2023CP=(unidades_a_vender_1ersemestreCP+unidades_a_vender_2dosemestreCP)
print(f'Total de unidades a vender CP:{total_unidades_aventa2023CP}')
total_inventarioFinal2023CP=(inventario_finalCP+inventario_final_2dosemestreCP)
print(f'Total inventario final CP:{total_inventarioFinal2023CP}')
total_deUnidades2023CP=(total_unidadesCP+total_unidades_2dosemestreCP)
print(f'Total de unidades CP:{total_deUnidades2023CP}')
total_inventarioInicial2023CP=(inventario_inicialCP+inverario_inicial_2dosemestreCP)
print(f'Total de inventario inicial CP:{total_inventarioInicial2023CP}')
total_unidades_aProducir2023CP=(Unidades_a_producir_1ersemestreCP+Unidades_a_producir_2dosemestreCP)
print(f'Total de unidades a producir CP:{total_unidades_aProducir2023CP}')

#**********************************************
# 4. Presupuesto de Requerimiento de Materiales
#**********************************************
print('-'*20)
print('\t\t- - - 4. Presupuesto de Requerimiento de Materiales - - -')
# PRODUCTO CF
print('\tPRODUCTO CF')
print('-'*20)
print(f'Unidades a Producir -  Primer Semestre: {Unidades_a_producir_1ersemestre}')
print(f'Unidades a Producir -  Segundo Semestre: {Unidades_a_producir_2dosemestre}')
print(f'Unidades a Producir -  Total 2022: {total_unidades_aProducir2023}')
print('-'*20)

#
# Primer Semestre
#

print('\t1er Semestre')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A1}')
total_material_A_requerido_1sem = Unidades_a_producir_1ersemestre * matPrima_A1
print(f'Total de Material Requerido: {total_material_A_requerido_1sem}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B1}')
total_material_B_requerido_1sem = Unidades_a_producir_1ersemestre * matPrima_B1
print(f'Total de Material Requerido: {total_material_B_requerido_1sem}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C1}')
total_material_C_requerido_1sem = Unidades_a_producir_1ersemestre * matPrima_C1
print(f'Total de Material Requerido: {total_material_C_requerido_1sem}')
print('-'*20)

#
# Segundo Semestre
#
print('\t2do Semestre')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A1}')
total_material_A_requerido_2sem = Unidades_a_producir_2dosemestre * matPrima_A1
print(f'Total de Material Requerido: {total_material_A_requerido_2sem}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B1}')
total_material_B_requerido_2sem = Unidades_a_producir_2dosemestre * matPrima_B1
print(f'Total de Material Requerido: {total_material_B_requerido_2sem}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C1}')
total_material_C_requerido_2sem = Unidades_a_producir_2dosemestre * matPrima_C1
print(f'Total de Material Requerido: {total_material_C_requerido_2sem}')
print('-'*20)

#
# Total 2022
#
print('\tTotal 2022')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A1}')
total_material_A_requerido_total_2022 = total_unidades_aProducir2023 * matPrima_A1
print(f'Total de Material Requerido: {total_material_A_requerido_total_2022}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B1}')
total_material_B_requerido_total_2022 = total_unidades_aProducir2023 * matPrima_B1
print(f'Total de Material Requerido: {total_material_B_requerido_total_2022}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C1}')
total_material_C_requerido_total_2022 = total_unidades_aProducir2023 * matPrima_C1
print(f'Total de Material Requerido: {total_material_C_requerido_total_2022}')
print('-'*20)

####################################################################################
# PRODUCTO CD
print('\tPRODUCTO CD')
print('-'*20)
print(f'Unidades a Producir -  Primer Semestre: {Unidades_a_producir_1ersemestreCD}')
print(f'Unidades a Producir -  Segundo Semestre: {Unidades_a_producir_2dosemestreCD}')
print(f'Unidades a Producir -  Total 2022: {total_unidades_aProducir2023CD}')
print('-'*20)

#
# Primer Semestre
#

print('\t1er Semestre')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A2}')
total_material_A_requerido_1sem_CD = Unidades_a_producir_1ersemestreCD * matPrima_A2
print(f'Total de Material Requerido: {total_material_A_requerido_1sem_CD}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B2}')
total_material_B_requerido_1sem_CD = Unidades_a_producir_1ersemestreCD * matPrima_B2
print(f'Total de Material Requerido: {total_material_B_requerido_1sem_CD}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C2}')
total_material_C_requerido_1sem_CD = Unidades_a_producir_1ersemestreCD * matPrima_C2
print(f'Total de Material Requerido: {total_material_C_requerido_1sem_CD}')
print('-'*20)

#
# Segundo Semestre
#
print('\t2do Semestre')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A2}')
total_material_A_requerido_2sem_CD = Unidades_a_producir_2dosemestreCD * matPrima_A2
print(f'Total de Material Requerido: {total_material_A_requerido_2sem_CD}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B2}')
total_material_B_requerido_2sem_CD = Unidades_a_producir_2dosemestreCD * matPrima_B2
print(f'Total de Material Requerido: {total_material_B_requerido_2sem_CD}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C2}')
total_material_C_requerido_2sem_CD = Unidades_a_producir_2dosemestreCD * matPrima_C2
print(f'Total de Material Requerido: {total_material_C_requerido_2sem_CD}')
print('-'*20)

#
# Total 2022
#
print('\tTotal 2022')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A2}')
total_material_A_requerido_total_2022_CD = total_unidades_aProducir2023CD * matPrima_A2
print(f'Total de Material Requerido: {total_material_A_requerido_total_2022_CD}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B2}')
total_material_B_requerido_total_2022_CD = total_unidades_aProducir2023CD * matPrima_B2
print(f'Total de Material Requerido: {total_material_B_requerido_total_2022_CD}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C2}')
total_material_C_requerido_total_2022_CD = total_unidades_aProducir2023CD * matPrima_C2
print(f'Total de Material Requerido: {total_material_C_requerido_total_2022_CD}')
print('-'*20)

######################################################################################
# PRODUCTO CP
print('\tPRODUCTO C')
print('-'*20)
print(f'Unidades a Producir -  Primer Semestre: {Unidades_a_producir_1ersemestreCP}')
print(f'Unidades a Producir -  Segundo Semestre: {Unidades_a_producir_2dosemestreCP}')
print(f'Unidades a Producir -  Total 2022: {total_unidades_aProducir2023CP}')
print('-'*20)

#
# Primer Semestre
#

print('\t1er Semestre')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A3}')
total_material_A_requerido_1sem_CP = Unidades_a_producir_1ersemestreCP * matPrima_A3
print(f'Total de Material Requerido: {total_material_A_requerido_1sem_CP}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B3}')
total_material_B_requerido_1sem_CP = Unidades_a_producir_1ersemestreCP * matPrima_B3
print(f'Total de Material Requerido: {total_material_B_requerido_1sem_CP}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C3}')
total_material_C_requerido_1sem_CP = Unidades_a_producir_1ersemestreCP * matPrima_C3
print(f'Total de Material Requerido: {total_material_C_requerido_1sem_CP}')
print('-'*20)

#
# Segundo Semestre
#
print('\t2do Semestre')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A3}')
total_material_A_requerido_2sem_CP = Unidades_a_producir_2dosemestreCP * matPrima_A3
print(f'Total de Material Requerido: {total_material_A_requerido_2sem_CP}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B3}')
total_material_B_requerido_2sem_CP = Unidades_a_producir_2dosemestreCP * matPrima_B3
print(f'Total de Material Requerido: {total_material_B_requerido_2sem_CP}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C3}')
total_material_C_requerido_2sem_CP = Unidades_a_producir_2dosemestreCP * matPrima_C3
print(f'Total de Material Requerido: {total_material_C_requerido_2sem_CP}')
print('-'*20)

#
# Total 2022
#
print('\tTotal 2022')
# Material A
print('-'*20)
print('\tMaterial A')
print(f'Requerimiento de Material: {matPrima_A3}')
total_material_A_requerido_total_2022_CP = total_unidades_aProducir2023CP * matPrima_A3
print(f'Total de Material Requerido: {total_material_A_requerido_total_2022_CP}')

# Material B
print('-'*20)
print('\tMaterial B')
print(f'Requerimiento de Material: {matPrima_B3}')
total_material_B_requerido_total_2022_CP = total_unidades_aProducir2023CP * matPrima_B3
print(f'Total de Material Requerido: {total_material_B_requerido_total_2022_CP}')

# Material C
print('-'*20)
print('\tMaterial C')
print(f'Requerimiento de Material: {matPrima_C3}')
total_material_C_requerido_total_2022_CP = total_unidades_aProducir2023CP * matPrima_C3
print(f'Total de Material Requerido: {total_material_C_requerido_total_2022_CP}')
print('-'*20)

######################################################################################################
# Total de Requerimientos
print('\tTOTAL DE REQUERIMIENTOS')
#
# 1er Semestre
#
print('-'*20)
print('\t1er Semestre')
total_requerimientos_mat_A_1sem = total_material_A_requerido_1sem + total_material_A_requerido_1sem_CD + total_material_A_requerido_1sem_CP
print(f'Material A: ${total_requerimientos_mat_A_1sem}')
total_requerimientos_mat_B_1sem = total_material_B_requerido_1sem + total_material_B_requerido_1sem_CD + total_material_B_requerido_1sem_CP
print(f'Material B: ${total_requerimientos_mat_B_1sem}')
total_requerimientos_mat_C_1sem = total_material_C_requerido_1sem + total_material_C_requerido_1sem_CD + total_material_C_requerido_1sem_CP
print(f'Material C: ${total_requerimientos_mat_C_1sem}')
#
# 2do Semestre
#
print('-'*20)
print('\t2do Semestre')
total_requerimientos_mat_A_2sem = total_material_A_requerido_2sem + total_material_A_requerido_2sem_CD + total_material_A_requerido_2sem_CP
print(f'Material A: ${total_requerimientos_mat_A_2sem}')
total_requerimientos_mat_B_2sem = total_material_B_requerido_2sem + total_material_B_requerido_2sem_CD + total_material_B_requerido_2sem_CP
print(f'Material B: ${total_requerimientos_mat_B_2sem}')
total_requerimientos_mat_C_2sem = total_material_C_requerido_2sem + total_material_C_requerido_2sem_CD + total_material_C_requerido_2sem_CP
print(f'Material C: ${total_requerimientos_mat_C_2sem}')
#
# Total 2022
#
print('-'*20)
print('\tTotal 2022')
total_requerimientos_mat_A_Total_2022 = total_material_A_requerido_total_2022 + total_material_A_requerido_total_2022_CD + total_material_A_requerido_total_2022_CP
print(f'Material A: ${total_requerimientos_mat_A_Total_2022}')
total_requerimientos_mat_B_Total_2022 = total_material_B_requerido_total_2022 + total_material_B_requerido_total_2022_CD + total_material_B_requerido_total_2022_CP
print(f'Material B: ${total_requerimientos_mat_B_Total_2022}')
total_requerimientos_mat_C_Total_2022 = total_material_C_requerido_total_2022 + total_material_C_requerido_total_2022_CD + total_material_C_requerido_total_2022_CP
print(f'Material C: ${total_requerimientos_mat_C_Total_2022}')
print('-'*20)

#**********************************************
# 5. Presupuesto de Compra de Materiales
#**********************************************
print('\t\t5. Presupuesto de Compra de Materiales')
print('-'*20)

#
# 1er Semestre
#
print('\t1er Semestre')
# Material A
print('Material A')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_A_1sem}')
print(f'( + ) Inventario Final: $ {matA_1s}')
total_de_materiales_A_1sem = total_requerimientos_mat_A_1sem + matA_1s
print(f'Total de Materiales: $ {total_de_materiales_A_1sem}')
inventario_inicial_materiales_A_1sem = matA_1s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_A_1sem}')
material_a_comprar_A_1sem = total_de_materiales_A_1sem - inventario_inicial_materiales_A_1sem
print(f'Material a Comprar: $ {material_a_comprar_A_1sem}')
print(f'Precio de Compra: $ {matA_Costo_1s}')
total_de_material_A_costo_1sem = material_a_comprar_A_1sem * matA_Costo_1s
print(f'Total de Material A en $: {total_de_material_A_costo_1sem}')
print('-'*20)

# Material B
print('Material B')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_B_1sem}')
print(f'( + ) Inventario Final: $ {matB_1s}')
total_de_materiales_B_1sem = total_requerimientos_mat_B_1sem + matB_1s
print(f'Total de Materiales: $ {total_de_materiales_B_1sem}')
inventario_inicial_materiales_B_1sem = matB_1s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_B_1sem}')
material_a_comprar_B_1sem = total_de_materiales_B_1sem - inventario_inicial_materiales_B_1sem
print(f'Material a Comprar: $ {material_a_comprar_B_1sem}')
print(f'Precio de Compra: $ {matB_Costo_1s}')
total_de_material_B_costo_1sem = material_a_comprar_B_1sem * matB_Costo_1s
print(f'Total de Material B en $: {total_de_material_B_costo_1sem}')
print('-'*20)

# Material C
print('Material C')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_C_1sem}')
print(f'( + ) Inventario Final: $ {matC_1s}')
total_de_materiales_C_1sem = total_requerimientos_mat_C_1sem + matC_1s
print(f'Total de Materiales: $ {total_de_materiales_C_1sem}')
inventario_inicial_materiales_C_1sem = matC_1s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_C_1sem}')
material_a_comprar_C_1sem = total_de_materiales_C_1sem - inventario_inicial_materiales_C_1sem
print(f'Material a Comprar: $ {material_a_comprar_C_1sem}')
print(f'Precio de Compra: $ {matC_Costo_1s}')
total_de_material_C_costo_1sem = material_a_comprar_C_1sem * matC_Costo_1s
print(f'Total de Material B en $: {total_de_material_C_costo_1sem}')
print('-'*20)

compras_totales_1sem = total_de_material_A_costo_1sem + total_de_material_B_costo_1sem + total_de_material_B_costo_1sem
print(f'Compras totales: $ {compras_totales_1sem}')
print('-'*20)

#
# 2do Semestre
#
print('\t2do Semestre')
# Material A
print('Material A')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_A_2sem}')
print(f'( + ) Inventario Final: $ {matA_2s}')
total_de_materiales_A_2sem = total_requerimientos_mat_A_2sem + matA_2s
print(f'Total de Materiales: $ {total_de_materiales_A_2sem}')
inventario_inicial_materiales_A_2sem = matA_2s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_A_2sem}')
material_a_comprar_A_2sem = total_de_materiales_A_2sem - inventario_inicial_materiales_A_2sem
print(f'Material a Comprar: $ {material_a_comprar_A_2sem}')
print(f'Precio de Compra: $ {matA_Costo_2s}')
total_de_material_A_costo_2sem = material_a_comprar_A_2sem * matA_Costo_2s
print(f'Total de Material A en $: {total_de_material_A_costo_2sem}')
print('-'*20)

# Material B
print('Material B')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_B_2sem}')
print(f'( + ) Inventario Final: $ {matB_2s}')
total_de_materiales_B_2sem = total_requerimientos_mat_B_2sem + matB_2s
print(f'Total de Materiales: $ {total_de_materiales_B_2sem}')
inventario_inicial_materiales_B_2sem = matB_2s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_B_2sem}')
material_a_comprar_B_2sem = total_de_materiales_B_2sem - inventario_inicial_materiales_B_2sem
print(f'Material a Comprar: $ {material_a_comprar_B_2sem}')
print(f'Precio de Compra: $ {matB_Costo_2s}')
total_de_material_B_costo_2sem = material_a_comprar_B_2sem * matB_Costo_2s
print(f'Total de Material B en $: {total_de_material_B_costo_2sem}')
print('-'*20)

# Material C
print('Material C')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_C_2sem}')
print(f'( + ) Inventario Final: $ {matC_2s}')
total_de_materiales_C_2sem = total_requerimientos_mat_C_2sem + matC_2s
print(f'Total de Materiales: $ {total_de_materiales_C_2sem}')
inventario_inicial_materiales_C_2sem = matC_2s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_C_2sem}')
material_a_comprar_C_2sem = total_de_materiales_C_2sem - inventario_inicial_materiales_C_2sem
print(f'Material a Comprar: $ {material_a_comprar_C_2sem}')
print(f'Precio de Compra: $ {matC_Costo_2s}')
total_de_material_C_costo_2sem = material_a_comprar_C_2sem * matC_Costo_2s
print(f'Total de Material B en $: {total_de_material_C_costo_2sem}')
print('-'*20)

compras_totales_2sem = total_de_material_A_costo_2sem + total_de_material_B_costo_2sem + total_de_material_B_costo_2sem
print(f'Compras totales: $ {compras_totales_2sem}')
print('-'*20)
#
# Total 2022
#
print('\tTotal 2022')
# Material A
print('Material A')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_A_Total_2022}')
print(f'( + ) Inventario Final: $ {matA_2s}')
total_de_materiales_A_total_2022 = total_requerimientos_mat_A_Total_2022 + matA_2s
print(f'Total de Materiales: $ {total_de_materiales_A_total_2022}')
inventario_inicial_materiales_A_total_2022 = matA_2s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_A_total_2022}')
material_a_comprar_A_total_2022 = total_de_materiales_A_total_2022 - inventario_inicial_materiales_A_total_2022
print(f'Material a Comprar: $ {material_a_comprar_A_total_2022}')
print(f'Precio de Compra: $ {matA_Costo_2s}')
total_de_material_A_costo_total_2022 = material_a_comprar_A_total_2022 * matA_Costo_2s
print(f'Total de Material A en $: {total_de_material_A_costo_total_2022}')
print('-'*20)

# Material B
print('Material B')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_B_Total_2022}')
print(f'( + ) Inventario Final: $ {matB_2s}')
total_de_materiales_B_total_2022 = total_requerimientos_mat_B_Total_2022 + matB_2s
print(f'Total de Materiales: $ {total_de_materiales_B_total_2022}')
inventario_inicial_materiales_B_total_2022 = matB_2s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_B_total_2022}')
material_a_comprar_B_total_2022 = total_de_materiales_B_total_2022 - inventario_inicial_materiales_B_total_2022
print(f'Material a Comprar: $ {material_a_comprar_B_total_2022}')
print(f'Precio de Compra: $ {matB_Costo_2s}')
total_de_material_B_costo_total_2022 = material_a_comprar_B_total_2022 * matB_Costo_2s
print(f'Total de Material B en $: {total_de_material_B_costo_total_2022}')
print('-'*20)

# Material C
print('Material C')
print('-'*20)

print(f'Requerimiento de Materiales: $ {total_requerimientos_mat_C_Total_2022}')
print(f'( + ) Inventario Final: $ {matC_2s}')
total_de_materiales_C_total_2022 = total_requerimientos_mat_C_Total_2022 + matC_2s
print(f'Total de Materiales: $ {total_de_materiales_C_total_2022}')
inventario_inicial_materiales_C_total_2022 = matC_2s
print(f'( - ) Inventario Inicial: $ {inventario_inicial_materiales_A_total_2022}')
material_a_comprar_C_total_2022 = total_de_materiales_C_total_2022 - inventario_inicial_materiales_C_total_2022
print(f'Material a Comprar: $ {material_a_comprar_C_total_2022}')
print(f'Precio de Compra: $ {matC_Costo_2s}')
total_de_material_C_costo_total_2022 = material_a_comprar_C_total_2022 * matC_Costo_2s
print(f'Total de Material B en $: {total_de_material_C_costo_total_2022}')
print('-'*20)

compras_totales_2022 = total_de_material_A_costo_total_2022 + total_de_material_B_costo_total_2022 + total_de_material_B_costo_total_2022
print(f'Compras totales: $ {compras_totales_2022}')
print('-'*20)

#**************************************************************
# 6. Determinación del saldo de Proveedores y Flujo de Salidas
#**************************************************************

print('\t\t- - - 6. Determinación del saldo de Proveedores y Flujo de Salidas - - -')
print('-'*20)

print('\tTotal')
print(f'Saldo de Proveedores 31-Dic-2022 {proveedores}')
print(f'Compras 2023 {compras_totales_2022}')
total_de_proveedores_2023 = proveedores + compras_totales_2022
print(f'Total de Proveedores 2023 {total_de_proveedores_2023}')
print('-'*20)

print('\n\tImporte')
print('\tSalidas de Efectivo: ')
proveedores_del_2022 = proveedores
print(f'Por Proveedores del 2022 $ {proveedores_del_2022}')
proveedores_del_2023 = compras_totales_2022 * 0.5
print(f'Por Proveedores del 2023 $ {proveedores_del_2023}')
print('-'*20)

print('\n\tTotal')
total_de_salidas_2023 = proveedores_del_2022 + proveedores_del_2023
print(f'Total de Salidas 2023: {total_de_salidas_2023}')
print('-'*20)

saldo_de_proveedores_del_2023 = total_de_proveedores_2023 + total_de_salidas_2023
print(f'Saldo de Proveedores del 2023 $ {saldo_de_proveedores_del_2023}')
print('-'*20)

#**************************************************************
# 7. Presupuesto de Mano de Obra Directa
#**************************************************************
print(' \t\t\t - - - 7. Presupuesto de mano de obra - - -')
print('-' * 20)
print('\tPrimer Semestre')
print('Producto CF')
print(f'Unidades a producir semestre1: {Unidades_a_producir_1ersemestre}')
print(f'Horas requeridas por unidad semestre: {hrs_ManoObra_1}')
total_de_horas_requeridas_sem = (Unidades_a_producir_1ersemestre * hrs_ManoObra_1)
cuota_por_hora = 15
print(f'Cuota por hora semestre 1: {cuota_por_hora}') 
cf_importe_M_O_D_s1 = ( total_de_horas_requeridas_sem * cuota_por_hora)
print(f'Importe de M.O.D: {cf_importe_M_O_D_s1}')
print('-'*20)

print('\tSegundo semestre')
print(f'Unidades a producir semestre2: {Unidades_a_producir_2dosemestre}')
print(f'Horas requeridas por unidad semestre2: {hrs_ManoObra_1}')
total_de_horas_requeridas_semestre2 = (Unidades_a_producir_2dosemestre * hrs_ManoObra_1)
cuota_por_hora_s2 = 18
print(f'Cuota por hora semestre 2: {cuota_por_hora_s2}')
cf_importe_M_O_D_s2 = (total_de_horas_requeridas_semestre2 * cuota_por_hora_s2) 
print(f'Importe de M.O.D: {cf_importe_M_O_D_s2}')
cf_total_2022 = (cf_importe_M_O_D_s1 + cf_importe_M_O_D_s2) #
print('-'*20)

print('\tPrimer Semestre')
print('Producto CD')
print(f'Unidades a producir semestre1: {Unidades_a_producir_1ersemestreCD}')
print(f'Horas requeridas por unidad semestre1: {hrs_ManoObra_2}')
cd_total_horas_requeridas_s1 = (Unidades_a_producir_1ersemestreCD * hrs_ManoObra_2)
cd_importe_M_O_D_s1 = (cd_total_horas_requeridas_s1 * cuota_por_hora )
print(f'Importe de M.O.D: {cd_importe_M_O_D_s1}')
print('-'*20)

print('\tSegundo semestre')
print(f'Unidades a producir semestre2: {Unidades_a_producir_2dosemestreCD}')
print(f'Horas requeridas por unidad semestre2: {hrs_ManoObra_2}')
cd_total_horas_requeridas_s2 = (Unidades_a_producir_2dosemestreCD * hrs_ManoObra_2)
cd_importe_M_O_D_s2 = (cd_total_horas_requeridas_s2 * cuota_por_hora_s2)
print(f'Importe de M.O.D: {cd_importe_M_O_D_s2}')
cd_total_2022 = (cd_importe_M_O_D_s1 + cd_importe_M_O_D_s2) #
print('-'*20)

print('\tPrimer Semestre')
print('Producto CP')
print(f'Unidades a producir semestre1: {Unidades_a_producir_1ersemestreCP}')
print(f'Horas requeridas por unidad semestre1: {hrs_ManoObra_3}')
cp_total_horas_requeridas_s1 = (Unidades_a_producir_1ersemestreCP * hrs_ManoObra_3)
cp_importe_M_O_D_s1 = (cp_total_horas_requeridas_s1 * cuota_por_hora)
print(f'Importe de M.O.D: {cp_importe_M_O_D_s1}')
print('-'*20)

print('\tSegundo semestre')
print(f'Unidades a producir semestre2: {Unidades_a_producir_2dosemestreCP}')
print(f'Horas requeridas por unidad semestre2: {hrs_ManoObra_3}')
cp_total_horas_requeridas_s2 = (Unidades_a_producir_2dosemestreCP * hrs_ManoObra_3)
cp_importe_M_O_D_s2 = (cp_total_horas_requeridas_s2 * cuota_por_hora_s2)
print(f'Importe de M.O.D: {cp_importe_M_O_D_s2}')
print('-'*20)

cp_total_2022 = (cp_importe_M_O_D_s1 + cp_importe_M_O_D_s2)
total_de_horas_requeridas_seme = ( total_de_horas_requeridas_sem + cd_total_horas_requeridas_s1 + cp_total_horas_requeridas_s1)
total_de_horas_requeridas_semestre2 = (total_de_horas_requeridas_semestre2 + cd_total_horas_requeridas_s2 + cp_total_horas_requeridas_s2)
total_horas_requeridas = (cf_total_2022 + cd_total_2022 + cp_total_2022)
total_M_O_D_semestre1 =(cf_importe_M_O_D_s1 + cd_importe_M_O_D_s1 + cp_importe_M_O_D_s1)
total__M_O_D_semestre2 =(cf_importe_M_O_D_s2 + cd_importe_M_O_D_s2 + cp_importe_M_O_D_s2)
total_M_O_D_por_semestre = (cf_total_2022 + cd_total_2022 + cp_total_2022)


########################
#8. Presupuesto de Gastos Indirectos de fabricacion
########################

print(' \t\t\t - - - 8. Presupuestos de Gastos Indirectos de Fabricacion - - -')
print('-'*20)
print('\tPrimer Semestre')
depreciacionA_GIF = depreciacionA_Fabricacion/2
print(f'Depreciacion: {depreciacionA_GIF}')
print(f'Seguro: {seguros_A}')
print(f'Mantenimiento: { mant_1s}')
print(f'Energeticos: {energeticos_1s}')
print(f'Varios: {varios_1s}')
total_GIF_Semestre1 =(depreciacionA_GIF + seguros_A + mant_1s + energeticos_1s + varios_1s)
print(f'Total G.I.F por semestre: {total_GIF_Semestre1}')
print('-'*20)

print('\tSegundo Semestre')
print(f'Depreciacion: {depreciacionA_GIF}')
print(f'Seguro: {seguros_A}')
print(f'Mantenimiento: {mant_2s}')
print(f'Energeticos: {energeticos_2s}')
print(f'Varios: {varios_2s}')
total_GIF_Semestre2 =(depreciacionA_GIF + seguros_A + mant_2s + energeticos_2s + varios_2s)
print(f'Total G.I.F por semestre: {total_GIF_Semestre2}')
print('-'*20)

print('\tTotal 2023')
depreciacionA_Fabricacion_total2023 = (depreciacionA_GIF + depreciacionA_GIF)
print(f'Depreciacion: { depreciacionA_Fabricacion_total2023}')
seguros_A_t2023 = (seguros_A + seguros_A)
print(f'Seguro: {seguros_A_t2023}')
mant_t2023 = (mant_1s + mant_2s)
print(f'Mantenimiento: { mant_t2023}')
energeticos_t2023 = (energeticos_1s + energeticos_2s)
print(f'Energeticos: {energeticos_t2023}')
varios_A = (varios_1s + varios_2s)
print(f'Varios: {varios_A}')
total_GIF_total2023 = (depreciacionA_Fabricacion_total2023 + seguros_A_t2023 + mant_t2023 + energeticos_t2023 + varios_A)
print(f'Total G.I.F por semestre: {total_GIF_total2023}')
print('-'*20)

print('Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion')
print(f'Total M.O.D Anual: { total_GIF_total2023 }')
print(f'(/) Total horas M.O.D. Anual: {total_horas_requeridas}')
costo_por_hora_GIF = (total_GIF_total2023 / total_horas_requeridas)
print(f'(=) Costo por Hora de G.I.F: {costo_por_hora_GIF}')

# ***
#           DESARROLLO
#           9.  PRESUPUESTO DE GASTO DE OPERACION
#           Allan
# ***

print('-'*20)
print('\t\t\t- - - 9. Presupuesto de Gasto de Operacion- - -')

print('\t1er semestre')
depreciacion_1ersemestre = depreciacion_A/2
print(f'Depreciacion primer semestre{depreciacion_1ersemestre}')
sueldos_y_salarios_1ersemestre = sueldosS_A/2
print(f'Sueldos y salarios primer semestre {sueldosS_A}')
comisiones_1ersemestre = comisiones*0.01
print(f'Comisiones primer semestre {comisiones}')
print(f'Varios primer semestre {varios_1s}')
intereses_prestamo_1ersemestre =  intereses_prestamo_A/2
print(f'Intereses del prestamo del primer semestre {intereses_prestamo_A}')
Total_de_Gastos_de_Operacion_1er_semestre =  depreciacion_1ersemestre+sueldos_y_salarios_1ersemestre+comisiones_1ersemestre+varios_1s
print(f'Total de Gastos de Operacion 1er semestre {Total_de_Gastos_de_Operacion_1er_semestre}')
print('-'*20)

print(f'\t2do semestre')
depreciacion_2dosemestre = depreciacion_A/2
print(f'Depreciacion segundo semestre{depreciacion_2dosemestre}')
sueldos_y_salarios_2dosemestre = sueldosS_A/2
print(f'Sueldos y salarios segundo semestre {sueldosS_A}')
comisiones_2dosemestre = comisiones*0.01
print(f'Comisiones segundo semestre {comisiones}')
print(f'Varios segundo semestre {varios_2s}')
intereses_prestamo_2dosemestre =  intereses_prestamo_A/2
print(f'Intereses del prestamo del segundo semestre {intereses_prestamo_A}')
Total_de_Gastos_de_Operacion_2do_semestre =  depreciacion_2dosemestre+sueldos_y_salarios_2dosemestre+comisiones_2dosemestre+varios_2s
print(f'Total de Gastos de Operacion 2do semestre {Total_de_Gastos_de_Operacion_2do_semestre}')
print('-'*20)

# AQUÍ FALTA UNA PARTE SIMILAR AL CÓDIGO ANTERIOR PARA CORRECCIÓN
print(f'\tTotal 2023')
# AQUÍ COMIENZA LO QUE FALTA DE CODIFICAR
Total_de_Gastos_de_Operacion_2023 = Total_de_Gastos_de_Operacion_1er_semestre + Total_de_Gastos_de_Operacion_2do_semestre
print(f'Total de Gastos de Operacion 2023 {Total_de_Gastos_de_Operacion_2023}')
print('-'*20)

# ***
#        DESARROLLO
#     10. DETERMINACION DEL COSTO UNITARIO DE PRODUCTOS TERMINADOS
#        Allan
# ***

print('\t\t\t- - - 10. Determinacion del Costo Unitario de Productos Terminados - - -')
print('-'*20)
#       Prodcuto CF

Producto_CF = prodCF_2s  
print(f'\tCosto') 
costo_mat_A = matA_Costo_2s

print(f'Material A : $ {costo_mat_A}')

costo_mat_B = matB_Costo_2s
print(f'Material B : $ {costo_mat_B}')

costo_mat_C = matC_Costo_1s
print(f'Material C : $ {costo_mat_C}')

Costo_Mano_de_Obra = cuota_por_hora
print(f'Mano de Obra : $ {cuota_por_hora}')

Hora_de_Mano_de_Obra = hrs_ManoObra_2
 
total_GIF_total2023 = (depreciacionA_Fabricacion_total2023 + seguros_A_t2023 + mant_t2023 + energeticos_t2023 + varios_A)
costo_por_hora_GIF = total_GIF_total2023
print(f'Gastos Indirectos de Fabricacion: {costo_por_hora_GIF}')
print(f'Total_MOD_Anual: { total_GIF_total2023 }')
print('-'*20)

print('\tCantidad')
costo_mat_A = matA_Costo_2s

print(f'Material A : $ {costo_mat_A}')

costo_mat_B = matB_Costo_2s
print(f'Material B : $ {costo_mat_B}')

costo_mat_C = matC_Costo_2s
print(f'Material C : $ {costo_mat_C}')

Costo_Mano_de_Obra = cuota_por_hora
print(f'Mano de Obra : $ {cuota_por_hora}')

Hora_de_Mano_de_Obra = hrs_ManoObra_2
 
total_GIF_total2023 = (depreciacionA_Fabricacion_total2023 + seguros_A_t2023 + mant_t2023 + energeticos_t2023 + varios_A)
print(f'Gastos Indirectos de Fabricacion: {costo_por_hora_GIF}')
print(f'Total_MOD_Anual: { total_GIF_total2023 }')
print('-'*20)

print(f'\tCosto Unitario ')
# AQUÍ ESTO DEBE DE IMPRIMIRSE 
costo_unitarioA = (costo_mat_A * costo_mat_A)
costo_unitarioB = (costo_mat_B * costo_mat_B)
costo_unitarioC = (costo_mat_C * costo_mat_C)
costo_unitarioOb = (hrs_ManoObra_2 * hrs_ManoObra_2)
costo_unitarioGI = (hrs_ManoObra_2 * costo_por_hora_GIF )
Costo_unitarioCF = (costo_unitarioA + costo_unitarioB + costo_unitarioC + costo_unitarioOb + costo_unitarioGI)
print('-'*20)

print(f'\tCosto Unitario ') 

#       Producto CD

Producto_CD = prodCD_2s
print(f'Costo') 
costo_mat_A = matA_Costo_2s

print(f'Material A : $ {costo_mat_A}')

costo_mat_B = matB_Costo_2s
print(f'Material B : $ {costo_mat_B}')

costo_mat_C = matC_Costo_1s
print(f'Material C : $ {costo_mat_C}')

Costo_Mano_de_Obra = cuota_por_hora
print(f'Mano de Obra : $ {cuota_por_hora}')

Hora_de_Mano_de_Obra = hrs_ManoObra_2
 
print(f'Gastos Indirectos de Fabricacion')
total_GIF_total2023 = (depreciacionA_Fabricacion_total2023 + seguros_A_t2023 + mant_t2023 + energeticos_t2023 + varios_A)
print(f'Total_MOD_Anual: { total_GIF_total2023 }')
print('-'*20)

print('\tCantidad')
costo_mat_A = matA_Costo_2s

print(f'Material A : $ {costo_mat_A}')

costo_mat_B = matB_Costo_2s
print(f'Material B : $ {costo_mat_B}')

costo_mat_C = matC_Costo_2s
print(f'Material C : $ {costo_mat_C}')

Costo_Mano_de_Obra = cuota_por_hora
print(f'Mano de Obra : $ {cuota_por_hora}')

Hora_de_Mano_de_Obra = hrs_ManoObra_2
 
print(f'Gastos Indirectos de Fabricacion')
total_GIF_total2023 = (depreciacionA_Fabricacion_total2023 + seguros_A_t2023 + mant_t2023 + energeticos_t2023 + varios_A)
print(f'Total_MOD_Anual: { total_GIF_total2023 }')
print('-'*20)

print(f'\tCosto Unitario ')
# AQUÍ ESTO SE DEBE DE IMPRIMIR 
costo_unitarioA = (costo_mat_A * costo_mat_A)
costo_unitarioB = (costo_mat_B * costo_mat_B)
costo_unitarioC = (costo_mat_C * costo_mat_C)
costo_unitarioOb = (hrs_ManoObra_2 * hrs_ManoObra_2)
costo_unitarioGI = (hrs_ManoObra_2 * costo_por_hora_GIF )
Costo_unitarioCD = (costo_unitarioA + costo_unitarioB + costo_unitarioC + costo_unitarioOb + costo_unitarioGI)
print('-'*20)

print(f'\tCosto Unitario ') 

#Producto CP

Producto_CP = prodCP_2s  
print(f'Costo') 
costo_mat_A = matA_Costo_2s

print(f'Material A : $ {costo_mat_A}')

costo_mat_B = matB_Costo_2s
print(f'Material B : $ {costo_mat_B}')

costo_mat_C = matC_Costo_1s
print(f'Material C : $ {costo_mat_C}')

Costo_Mano_de_Obra = cuota_por_hora
print(f'Mano de Obra : $ {cuota_por_hora}')

Hora_de_Mano_de_Obra = hrs_ManoObra_2
 
print(f'Gastos Indirectos de Fabricacion')
total_GIF_total2023 = (depreciacionA_Fabricacion_total2023 + seguros_A_t2023 + mant_t2023 + energeticos_t2023 + varios_A)
print(f'Total_MOD_Anual: { total_GIF_total2023 }')

print('Cantidad')
costo_mat_A = matA_Costo_2s

print(f'Material A : $ {costo_mat_A}')

costo_mat_B = matB_Costo_2s
print(f'Material B : $ {costo_mat_B}')

costo_mat_C = matC_Costo_2s
print(f'Material C : $ {costo_mat_C}')

Costo_Mano_de_Obra = cuota_por_hora
print(f'Mano de Obra : $ {cuota_por_hora}')

Hora_de_Mano_de_Obra = hrs_ManoObra_2
 
print(f'Gastos Indirectos de Fabricacion')
total_GIF_total2023 = (depreciacionA_Fabricacion_total2023 + seguros_A_t2023 + mant_t2023 + energeticos_t2023 + varios_A)
print(f'Total_MOD_Anual: { total_GIF_total2023 }')
print('-'*20)

print(f'\tCosto Unitario ')
# AQUÍ ESTO SE DEBE IMPRIMIR 
costo_unitarioA = (costo_mat_A * costo_mat_A)
costo_unitarioB = (costo_mat_B * costo_mat_B)
costo_unitarioC = (costo_mat_C * costo_mat_C)
costo_unitarioOb = (hrs_ManoObra_2 * hrs_ManoObra_2)
costo_unitarioGI = (hrs_ManoObra_2 * costo_por_hora_GIF )
Costo_unitarioCP = (costo_unitarioA + costo_unitarioB + costo_unitarioC + costo_unitarioOb + costo_unitarioGI)
print('-'*20)

# ***
#           DESARROLLO
#           VALUACION DE INVENTARIOS FINALES
#           Allan
# ***

#       Inventario Final de Materiales

print('-'*20)
print('\t- - - 11. Valuacion de Inventarios Finales - - -')
print('-'*20)

print(f'\tDescripcion')
Material_A = matA_2s
print(f'Material A {matA_2s}')
Material_B = matB_2s
print(f'Material B{matB_2s}')
Material_C = matC_2s
print(f'Material C{matC_2s}')
print('-'*20)

Costo_UnitarioA = costo_mat_A
print(f'Material A{costo_mat_A}')

Costo_UnitarioB = costo_mat_B
print(f'Material B{costo_mat_B}')

Costo_UnitarioC = costo_mat_C
print(f'Material C{costo_mat_C}')
print('-'*20)

Costo_TotalA = matA_2s * costo_mat_A
Costo_TotalB = matB_2s * costo_mat_B
Costo_TotalC = matC_2s * costo_mat_C

print(f'Costo_Total A: {Costo_TotalA}')
print(f'Costo Total B: {Costo_TotalB}')
print(f'Costo Total C: {Costo_TotalC}')
print('-'*20)

Inv_FinMat = (Costo_TotalA + Costo_TotalB + Costo_TotalC)
print(f'\nInventario Final de Materiales: {Inv_FinMat} \n')
print('-'*20)

# Inventario Final de Producto Terminado

print('\tDescripcion')
# AQUÍ SE DEBE IMPRIMIR
Producto_D = (inventario_final_2dosemestre)
Producto_Di = (inventario_final_2dosemestreCD)
Producto_Z = (inventario_final_2dosemestreCP)
print('-'*20)

print('\tCosto Unitario')
# AQUÍ SE DEBE IMPRIMIR
Costo_unitarioCF = (costo_unitarioA + costo_unitarioB + costo_unitarioC + costo_unitarioOb + costo_unitarioGI)
Costo_unitarioCD = (costo_unitarioA + costo_unitarioB + costo_unitarioC + costo_unitarioOb + costo_unitarioGI)
Costo_unitarioCP = (costo_unitarioA + costo_unitarioB + costo_unitarioC + costo_unitarioOb + costo_unitarioGI)
print('-'*20)

print('\tCosto Total')
# AQUÍ FALTA INFO Y SE DEBE IMPRIMIR
Inv_fin_PT = (Producto_D + Producto_Di + Producto_Z)
print(f'Total de Material B en $: {total_de_material_C_costo_total_2022}')
print('-'*20)

#******************      
#     DESARROLLO
#Presupuesto Maestro
# Aldair
#*******
#******11************
print('\t\tII. Presupuesto Financiero')
print('\t\t\t- - - Estado de Costo de Produccion y Ventas- - -')
print('-'*20)

print(f'Saldo inicial de Materiales: {inv_mats}')
print(f'(+) Compras de Materiales: {compras_totales_2022}')
Mat_Dispo=(inv_mats+compras_totales_2022)
print(f'(=) Material Disponible: {Mat_Dispo}')
print(f'(-) Inventario Final de Materiales: {Inv_FinMat}')
Mat_Utili=(Mat_Dispo-Inv_FinMat)
print(f'(=) Materiales Utilizados: {Mat_Utili}')
print(f'(+) Mano de Obra Directa: {total_M_O_D_por_semestre}')
print(f'(+) Gastos de Fabricacion Indirectos: {total_GIF_total2023}')
costo_prod=(Mat_Utili+total_M_O_D_por_semestre+total_GIF_total2023)
print(f'(=) Costo de Produccion: {costo_prod}')
print(f'(+) Inventario inicial de productos terminados: {inv_ProdFin}')
T_prod_dispo=(costo_prod+inv_ProdFin)
print(f'(=) Total de produccion disponible: {T_prod_dispo}')
print(f'(-) Inventario Final de productos terminados: {Inv_fin_PT}')
costo_ventas=(T_prod_dispo-Inv_fin_PT)
print(f'(=) Costo de Ventas: {costo_ventas}')
print('-'*20)

#******12***********
print('\t\tI. Presupuesto Financiero')
print('\t\t\t- - - Estado de Resultados- - -')
print('-'*20)

print(f'Ventas: {Total_de_ventas_por_1ersemestre}')
print(f'(-) Costo de ventas: {costo_ventas}')
Utili_bruta = (Total_de_ventas_por_1ersemestre - costo_ventas)
print(f'(=) Utilidad Bruta: {Utili_bruta}')
print(f'(-) Gastos de Operacion: {Total_de_Gastos_de_Operacion_2023}')
Util_operacion=(Utili_bruta-Total_de_Gastos_de_Operacion_2023)
print(f'(=) Utilidad de Operacion: {Util_operacion}')
ISR_3=(Util_operacion*0.3)
print(f'(-) ISR: {ISR_3}')
PTU_1=(Util_operacion*0.1)
print(f'(-) PTU: {PTU_1}')
Util_neta=(Util_operacion-ISR_3-PTU_1)
print(f'(=) Utilidad Neta: {Util_neta}')
print('-'*20)

#******13***********
print('\t\tI. Presupuesto Financiero')
print('\t\t\t- - - Estado de Flujo de Efectivo- - -')
print('-'*20)

print(f'Saldo inicial de Efectivo: {efectivo}')
print('\tEntradas')
print(f'Entradas Cobranza 2023: {Por_cobranza2023}')
print(f'Entradas Cobranza 2022: {Por_cobranza2022}')
total_cobranza=(Por_cobranza2023+Por_cobranza2022)
print(f'Total de Entradas: {total_cobranza}')
Efectivo_Dispo=(efectivo+total_cobranza)
print(f'Efectivo Disponible: {Efectivo_Dispo}')
print('-'*20)

print('\tSalidas')
print(f'Proveedores 2023: {total_de_proveedores_2023}')
print(f'Proveedores 2022: {proveedores_del_2022}')
print(f'Pago Mano de Obra Directa: {total_M_O_D_por_semestre}')
pagos_gastos_indirectos_fabricacion=(total_GIF_total2023-depreciacionA_Fabricacion_total2023)
print(f'Pago Gastos Indirectos de Fabricación : {pagos_gastos_indirectos_fabricacion}')
pagos_gasto_operacion=(Total_de_Gastos_de_Operacion_2023-(depreciacion_1ersemestre+depreciacion_1ersemestre))
print(f'Pago de Gastos de Operación: {pagos_gasto_operacion}')
activo_maquinaria = int(input('Dame la Compra de activo fijo de maquinaria: '))
print(f'Pago ISR 2022 : {isr}')
print('-'*20)

Total_salidas=(isr+activo_maquinaria+pagos_gasto_operacion+pagos_gastos_indirectos_fabricacion+total_M_O_D_por_semestre+proveedores_del_2022+total_de_proveedores_2023)
print(f'Total de salidas: {Total_salidas}')
flujo_efectivoactual=Efectivo_Dispo-Total_salidas
print(f'Fuljo de efectivo anual: {flujo_efectivoactual}')
print('-'*20)

#********14********
print('\t\tI. Presupuesto Financiero')
print('\t\t\t- - - Balance General- - -')
print('-'*20)

print('\tACTIVO CIRCULANTE')
print(f'Efectivo: {efectivo}')
print(f'Clientes: {clientes}')
print(f'Deudores Diversos: {deudores}')
print(f'Funcionarios y Empleados: {funcionarios}')
print(f'Inventario Materiales: {inv_mats}')
print(f'Inventario Producto Terminado: {inv_ProdFin}')
tActCircu = (flujo_efectivoactual+Saldo_de_clientesfinal+deudores+funcionarios+Inv_FinMat+Inv_fin_PT)
print(f'Total Activo Circulantes {tActCircu}')
print('-'*20)

print('\tACTIVO NO CIRCULANTE')
print(f'Tereno: {terry}')
print(f'Planta y Equipo:{planta}')
print(f'Depreciacion Acumulada: {despAcum}')
tActNo= float(despAcum+depreciacionA_Fabricacion_total2023+depreciacion_1ersemestre)
print(f'Total Activo NO Circulantes: {tActNo}')
act_total=(tActCircu+tActNo)
print(f'\n\tActivo Total:{act_total}')
print('-'*20)

print('\tPASIVO CORTO PLAZO')
print(f'Proveedores: {proveedores}')
print(f'Documentos por pagar: {docx}')
print(f'ISR por pagar: {isr}')
print(f'PTU por pagar: {PTU_1}')
pasivo_cortoplazo=(proveedores+docx+isr+PTU_1)
print(f'Total de Pasivo a Corto Plazo: {pasivo_cortoplazo}')
print('-'*20)

print('\tPASVIO LAGO PLAZO')
print(f'Prestamos Bancarios: {prestamos}')
print(f' Total de Pasivo Largo Plazo : {prestamos}')
pas_tot=(pasivo_cortoplazo+prestamos)
print(f'\n\tPasivo Total: {pas_tot}')
print('-'*20)

print('\tCAPITAL CONTABLE')
print(f'Capital aportado: {capital_contr}')
print(f'Capital Ganado: {capital_ganado}')
print(f'Utilidad del Ejercicio: {PTU_1}')
tCapCont= float(capital_contr+capital_ganado+PTU_1)
print(f'Total de Capital Contable: {tCapCont}')
sum_pasCapital=(pas_tot+tCapCont)

print(f'\n\tSuma de PASIVO Y CAPITAL: {sum_pasCapital}')
print('-'*20)
