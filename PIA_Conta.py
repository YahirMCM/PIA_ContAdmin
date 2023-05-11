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
tActNo = (terry + planta - despAcum)
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
print('Producto CL')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {cl_ventas_1s}')
print(f'Precio de Ventas semestre1: {cl_1s}')
importe_de_venta_1ersemestre_cf = (cl_1s * cl_ventas_1s)
print(importe_de_venta_1ersemestre_cf)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {cl_ventas_2s}')
print(f'Precio de Ventas semestre2: {cl_2s}')
importe_de_venta_2dosemestre_cf = (cl_2s * cl_ventas_2s)
print(importe_de_venta_2dosemestre_cf)
#Carne diaria
print('Producto CE')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {ce_ventas_1s}')
print(f'Precio de Ventas semestre1: {ce_1s}')
importe_de_venta_1ersemestre_cd = (ce_1s * ce_ventas_1s)
print(importe_de_venta_1ersemestre_cd)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {ce_ventas_2s}')
print(f'Precio de Ventas semestre2: {ce_2s}')
importe_de_venta_2dosemestre_cd = (ce_2s * ce_ventas_2s)
print(importe_de_venta_2dosemestre_cd)
#carne pollo
print('Producto CR')
print('Primer Semestre')
print(f'Unidades a vender semestre1: {cr_ventas_1s}')
print(f'Precio de Ventas semestre1: {cr_1s}')
importe_de_venta_1ersemestre_cp = (cr_1s * cr_ventas_1s)
print(importe_de_venta_1ersemestre_cp)
print('Segundo Semestre')
print(f'Unidades a vender semestre2: {cr_ventas_2s}')
print(f'Precio de Ventas semestre2: {cr_2s}')
importe_de_venta_2dosemestre_cp = (cr_2s * cr_ventas_2s)
print(importe_de_venta_2dosemestre_cp)
Total_de_ventas_por_1ersemestre =(importe_de_venta_1ersemestre_cf+importe_de_venta_1ersemestre_cd+importe_de_venta_1ersemestre_cp)
Total_de_ventas_por_2dosemestre =(importe_de_venta_2dosemestre_cf+importe_de_venta_2dosemestre_cd+importe_de_venta_2dosemestre_cp)
Total_de_ventas_por_semestres = (Total_de_ventas_por_1ersemestre+Total_de_ventas_por_2dosemestre)
print(f'total de venta{Total_de_ventas_por_semestres}')


#***************
#2.Determinacion del saldo de clientes y flujo de entradas
#****************
print('\t\t- - - 2.Determinacion del saldo de clientes y flujo de entradas- - -')
print('-'*20)
Saldo_de_clientes_31_Dic_2022 = clientes
ventas_2022 = Total_de_ventas_por_semestres 
Total_de_clientes2022 = (Saldo_de_clientes_31_Dic_2022+ventas_2022) # ERROR EN ESTA LÍNEA -> CREO QUE LO CORREGÍ
print(f"Total de clientes 2022:{Total_de_clientes2022}")
print("Entradas de efectivo:")
Por_cobranza2022 = Saldo_de_clientes_31_Dic_2022
Por_cobranza2023 = (ventas_2022)*(0.8)
Cobranza_final = (Por_cobranza2022+Por_cobranza2023)
print(f"cobranza final:{Cobranza_final}")
Saldo_de_clientesfinal=(Total_de_clientes2022+Cobranza_final)


#****************************
#3. Presupuesto de Producción
#*****************************
#Producto CF
print('\t\t- - -3. Presupuesto de Producción - - -')
print('-'*20)
print('Producto CF')
print("primer semestre")
unidades_a_vender_1ersemestre = cl_ventas_1s
print(f'unidades a vender{unidades_a_vender_1ersemestre}')
inventario_inicial=prodCF_1s 
inventario_final= inventario_inicial
print(f'inventario final{inventario_final}')
total_unidades=(unidades_a_vender_1ersemestre+inventario_final)
print(f'total de unidades{total_unidades}')
Unidades_a_producir_1ersemestre = (total_unidades-inventario_inicial)

print("segundo semestre")
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

#Producto CD
print('Producto CD')
print("primer semestre")
unidades_a_vender_1ersemestreCD = ce_ventas_1s
print(f'unidades a vender CD {unidades_a_vender_1ersemestreCD}')
inventario_inicialCD=prodCD_1s
inventario_finalCD= inventario_inicialCD
print(f'inventario final CD {inventario_finalCD}')
total_unidadesCD=(unidades_a_vender_1ersemestreCD+inventario_finalCD)
print(f'total de unidades CD {total_unidadesCD}')
Unidades_a_producir_1ersemestreCD = (total_unidadesCD-inventario_inicialCD)
print("segundo semestre")
unidades_a_vender_2dosemestreCD = ce_ventas_2s
print(f'unidades a vender CD{unidades_a_vender_2dosemestreCD}')
inventario_inicial_2dosemestreCD = prodCD_2s
inventario_final_2dosemestreCD= inventario_inicial_2dosemestreCD
print(f'inventario final CD {inventario_final_2dosemestreCD}')
total_unidades_2dosemestreCD=(unidades_a_vender_2dosemestreCD+inventario_final_2dosemestreCD)
print(f'total de unidades CD{total_unidades_2dosemestreCD}')
inverario_inicial_2dosemestreCD=prodCD_2s
Unidades_a_producir_2dosemestreCD = (total_unidades_2dosemestreCD-inverario_inicial_2dosemestreCD)
print(f"Unidades a producir en el segundo semestre CD{Unidades_a_producir_2dosemestreCD}")

total_unidades_aventa2023CD=(unidades_a_vender_1ersemestreCD+unidades_a_vender_2dosemestreCD)
print(f'total de unidades a vender CD:{total_unidades_aventa2023CD}')
total_inventarioFinal2023CD=(inventario_finalCD+inventario_final_2dosemestreCD)
print(f'total inventario final CD:{total_inventarioFinal2023CD}')
total_deUnidades2023CD=(total_unidadesCD+total_unidades_2dosemestreCD)
print(f'total de unidades CD:{total_deUnidades2023CD}')
total_inventarioInicial2023CD=(inventario_inicialCD+inverario_inicial_2dosemestreCD)
print(f'total de inventario inicial CD:{total_inventarioInicial2023CD}')
total_unidades_aProducir2023CD=(Unidades_a_producir_1ersemestreCD+Unidades_a_producir_2dosemestreCD)
print(f'total de unidades a producir CD:{total_unidades_aProducir2023CD}')

#Producto CP
print('Producto CP')
print("primer semestre")
unidades_a_vender_1ersemestreCP = cr_ventas_1s
print(f'unidades a vender CP{unidades_a_vender_1ersemestreCP}')
inventario_inicialCP=prodCD_1s 
inventario_finalCP= inventario_inicialCP
print(f'inventario final CP:{inventario_finalCP}')
total_unidadesCP=(unidades_a_vender_1ersemestreCP+inventario_finalCP)
print(f'total de unidades CP:{total_unidadesCP}')
Unidades_a_producir_1ersemestreCP = (total_unidadesCP-inventario_inicialCP)

print("segundo semestre")
unidades_a_vender_2dosemestreCP = ce_ventas_2s
print(f'unidades a vender CP:{unidades_a_vender_2dosemestreCP}')
inventario_inicial_2dosemestreCP= ce_ventas_2s
inventario_final_2dosemestreCP= inventario_inicial_2dosemestreCP
print(f'inventario final CP:{inventario_final_2dosemestreCP}')
total_unidades_2dosemestreCP=(unidades_a_vender_2dosemestreCP+inventario_final_2dosemestreCP)
print(f'total de unidades CP:{total_unidades_2dosemestreCP}')
inverario_inicial_2dosemestreCP=prodCP_2s
Unidades_a_producir_2dosemestreCP = (total_unidades_2dosemestreCP-inverario_inicial_2dosemestreCP)
print(f"Unidades a producir en el segundo semestre CP:{Unidades_a_producir_2dosemestreCP}")

total_unidades_aventa2023CP=(unidades_a_vender_1ersemestreCP+unidades_a_vender_2dosemestreCP)
print(f'total de unidades a vender CP:{total_unidades_aventa2023CP}')
total_inventarioFinal2023CP=(inventario_finalCP+inventario_final_2dosemestreCP)
print(f'total inventario final CP:{total_inventarioFinal2023CP}')
total_deUnidades2023CP=(total_unidadesCP+total_unidades_2dosemestreCP)
print(f'total de unidades CP:{total_deUnidades2023CP}')
total_inventarioInicial2023CP=(inventario_inicialCP+inverario_inicial_2dosemestreCP)
print(f'total de inventario inicial CP:{total_inventarioInicial2023CP}')
total_unidades_aProducir2023CP=(Unidades_a_producir_1ersemestreCP+Unidades_a_producir_2dosemestreCP)
print(f'total de unidades a producir CP:{total_unidades_aProducir2023CP}')

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
print(f'Precio de Compra: $ {matA_Costo_3s}')
total_de_material_A_costo_total_2022 = material_a_comprar_A_total_2022 * matA_Costo_3s
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
print(f'Precio de Compra: $ {matB_Costo_3s}')
total_de_material_B_costo_total_2022 = material_a_comprar_B_total_2022 * matB_Costo_3s
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
print(f'Precio de Compra: $ {matC_Costo_3s}')
total_de_material_C_costo_total_2022 = material_a_comprar_C_total_2022 * matC_Costo_3s
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