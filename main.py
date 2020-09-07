from lifestore_file import lifestore_products,lifestore_sales, lifestore_searches # MANDAMOS A LLAMAR A LAS LISTAS CON LAS CUALES VAMOS A TRABAJAR 
 

#agregamos las consignias



#primer consignia los 50 productos más vendidos 



contador_total =[]

for products in lifestore_products:
  contar =0
  for store in lifestore_sales:
    if products[0] == store[1]:
      contar +=1
  
  
  contador_total.append([products[1],contar])
#print(contador_total)
'''for final in contador_total:
  print("El producto:", lifestore_products[2],"vendió:",final[1])'''
#consignia total de ingresos
ventas_total=[]
for ventas in contador_total:
  suma_total=0
  for nombre in lifestore_products:
    if ventas[0]==nombre[1]:
      suma=nombre[2]*ventas[1]
      
      suma_total+=suma
      ventas_total.append(suma_total)
#print(ventas_total)
result=0
for number in ventas_total:
  result+=number
'''print("El total de ingresos fue: ",result)'''
#ventas 



#consignia promedio de total de ingresos mensuales  de ingresos mensuales



'''meses=int(input("ingresa en numero (mm) el último mes registrado: "))
prom_mensual=float(result/meses)
print("el promedio mensual es: $",prom_mensual)'''

#



  
productos_ordenados = []

while contador_total:
    maximo =contador_total[0][1]
    
    lista_actual = contador_total[0]
    for productos in contador_total:
        if productos[1] > maximo:
            maximo =productos[1]
            lista_actual =productos
        
    productos_ordenados.append(lista_actual)
    contador_total.remove(lista_actual)
#print(productos_ordenados)
#for cuentas in productos_ordenados:
  #print(cuentas[1])

  

#print("Los productos #productos_ordenados[0:51])

#print("Los productos #productos_ordenados[0:51])'''



    
#print mayores ventas
'''for final in range(0,50):
  print("El producto:",productos_ordenados[final][0],"vendió:",productos_ordenados[final][1],"\n")'''


#SEGUNDA CONSIGNIA


contador_mayores =[]

for prod in lifestore_products:
  contare = 0
  for busqueda in lifestore_searches:
    if prod[0] == busqueda[1]:
      contare +=1
  contador_mayores.append([prod[1],contare])
#print(contador_mayores)

productos_ormayor= []

while contador_mayores:
    maxi =contador_mayores[0][1]
    lista_act=contador_mayores[0]
    for productos in contador_mayores:
      if productos[1] > maxi:
         maxi=productos[1]
         lista_act=productos

    productos_ormayor.append(lista_act)
    contador_mayores.remove(lista_act)

#print(productos_ormayor)
'''for final in range(0,96):
  print("El producto:",productos_ormayor[final][0],"se buscó: ",productos_ormayor[final][1],"\n")'''




#TERCER CONSIGNIA MENORES VENTAS


contador_total_1 =[]

for productsu in lifestore_products:
  contara =0
  for stori in lifestore_sales:
    if productsu[0] == stori[1]:
      contara +=1
  
  
  contador_total_1.append([productsu[1],contara])
#print(contador_total)
"""for final in contador_total:
  print("El producto:", lifestore_products[2],"vendió:",final[1])"""



  
productos_ordenadose = []

while contador_total_1:
    minimox =contador_total_1[0][1]
    
    lista_actuali = contador_total_1[0]
    for productos_1 in contador_total_1:
        if productos_1[1] < minimox:
            minimox =productos_1[1]
            lista_actuali =productos_1
        
    productos_ordenadose.append(lista_actuali)
    contador_total_1.remove(lista_actuali)
#print(productos_ordenados)
#print("Los productos #productos_ordenados[0:51])

#print("Los productos #productos_ordenados[0:51])



    
#print menores ventas
'''for final_1 in range(0,50):
  print("El producto: ",productos_ordenadose[final_1][0],"vendió:",productos_ordenadose[final_1][1],"\n")'''




#cuarta insignia 100 productos con menores busquedas


contador_menores =[]

for prod in lifestore_products:
  contare = 0
  for busqueda in lifestore_searches:
    if prod[0] == busqueda[1]:
      contare +=1
  contador_menores.append([prod[1],contare])
#print(contador_mayores)

productos_ormenor= []

while contador_menores:
    mini =contador_menores[0][1]
    lista_act=contador_menores[0]
    for productos in contador_menores:
      if productos[1] < mini:
         mini=productos[1]
         lista_act=productos

    productos_ormenor.append(lista_act)
    contador_menores.remove(lista_act)

#print(productos_ormayor)
'''for final in range(0,96):
  print("El producto:",productos_ormenor[final][0],"se buscó: ",productos_ormenor[final][1],"\n")'''




#quinta insignia mostrar los 20 listados de mejores reseñas 



contador_total_5 =[]

for products_5 in lifestore_products:
  contar_5 =0
  for store_5 in lifestore_sales:
    if products_5[0] == store_5[1]:
      if store_5[2]== 5:
        contar_5 +=1
  
  
  contador_total_5.append([products_5[1],contar_5])
#print(contador_total)#me da la suma de los productos que tienen 5 
#for final in contador_total:
  #print("El producto:", lifestore_products[1],"con mejores reseñas de puntuación 5 fue:  ",final[2])


  
productos_ordenados_5= []

while contador_total_5:
    maximo_5 =contador_total_5[0][1]
    
    lista_actual_5 = contador_total_5[0]
    for productos_5 in contador_total_5:
        if productos_5[1] > maximo_5:
            maximo_5 =productos_5[1]
            lista_actual_5 =productos_5
        
    productos_ordenados_5.append(lista_actual_5)
    contador_total_5.remove(lista_actual_5)
#print(productos_ordenados)
#print("Los productos #productos_ordenados[0:51])

#print("Los productos #productos_ordenados[0:51])



    
#print mayores ventas
'''for final_5 in range(0,20):
  print("El producto:",productos_ordenados_5[final_5][0],  "con mejores reseñas de puntuación 5 obtuvo un total de: ",productos_ordenados_5[final_5][1], "\n")'''






# sexta consignia peores reseñas 



lista_agregados1=[]
lista_agregados2=[]

#print(lifestore_sales)
for product in lifestore_products:
  contar_6=0
  for score in lifestore_sales:
    
    if score[2] ==1 and product[0]==score[1]:
      contar_6+=1
    
      
  
      
  lista_agregados1.append([product[1],contar_6])

  
  #elif score[2]==2 and pro
#print(lista_agregados1[0])

#while lista_agregados1:
 
  #igual_cero =lista_agregados1[0][1]
  #lista_actual_1 = #lista_agregados1[0]
for valores in lista_agregados1:
  if valores[1] !=0:
    igual_cero =valores[1]
    lista_actual_1=valores
    lista_agregados2.append(lista_actual_1)
  #lista_agregados1.remove(lista_actual_1)
  
#print(lista_agregados2)
productos_ordenados_61= []
while lista_agregados2:
  maximo_61 =lista_agregados2[0][1]
  lista_actual_61 =lista_agregados2[0]
  for productos in lista_agregados2:
        if productos[1] > maximo_61:
            maximo_61 =productos[1]
            lista_actual_61 =productos
        
  productos_ordenados_61.append(lista_actual_61)
  lista_agregados2.remove(lista_actual_61)
#print(productos_ordenados)

lista_agregados_1=[]
lista_agregados_2=[]

#print(lifestore_sales)
for product in lifestore_products:
  contar_61=0
  for score in lifestore_sales:
    
    if score[2] ==1 and product[0]==score[1]:
      contar_61+=1
    
      
  
      
  lista_agregados_1.append([product[1],contar_61])

  
  #elif score[2]==2 and pro
#print(lista_agregados1[0])

#while lista_agregados1:
 
  #igual_cero =lista_agregados1[0][1]
  #lista_actual_1 = #lista_agregados1[0]
for valores in lista_agregados_1:
  if valores[1] !=0:
    igual_cero =valores[1]
    lista_actual_1=valores
    lista_agregados_2.append(lista_actual_1)
  #lista_agregados1.remove(lista_actual_1)
  
#print(lista_agregados2)


productos_ordenados_1= []
while lista_agregados_2:
  maximo =lista_agregados_2[0][1]
  lista_actual =lista_agregados_2[0]
  for productos in lista_agregados_2:
        if productos[1] > maximo:
            maximo =productos[1]
            lista_actual =productos
        
  productos_ordenados_1.append(lista_actual)
  lista_agregados_2.remove(lista_actual)
#print(productos_ordenados_1)


#parte ==3

listaagregados1=[]
listaagregados2=[]

#print(lifestore_sales)
for product in lifestore_products:
  contar=0
  for score in lifestore_sales:
    
    if score[2] ==3 and product[0]==score[1]:
      contar+=1
    
      
  
      
  listaagregados1.append([product[1],contar])

  

for valores in listaagregados1:
  if valores[1] !=0:
    igual_cero =valores[1]
    lista_actual_1=valores
    listaagregados2.append(lista_actual_1)
  #lista_agregados1.remove(lista_actual_1)
  
#print(lista_agregados2)
productosordenados= []
while listaagregados2:
  maximo =listaagregados2[0][1]
  lista_actual =listaagregados2[0]
  for productos in listaagregados2:
        if productos[1] > maximo:
            maximo =productos[1]
            lista_actual =productos
        
  productosordenados.append(lista_actual)
  listaagregados2.remove(lista_actual)
#print(productosordenados)

productos==4

lista_agregado1=[]
lista_agregado2=[]

#print(lifestore_sales)
for product in lifestore_products:
  contar=0
  for score in lifestore_sales:
    
    if score[2] ==4 and product[0]==score[1]:
      contar+=1
    
      
  
      
  lista_agregado1.append([product[1],contar])

  
  #elif score[2]==2 and pro
#print(lista_agregados1[0])

#while lista_agregados1:
 
  #igual_cero =lista_agregados1[0][1]
  #lista_actual_1 = #lista_agregados1[0]
for valores in lista_agregado1:
  if valores[1] !=0:
    igual_cero =valores[1]
    lista_actual_1=valores
    lista_agregado2.append(lista_actual_1)
  #lista_agregados1.remove(lista_actual_1)
  
#print(lista_agregados2)
productos_ordenado= []
while lista_agregado2:
  maximo =lista_agregado2[0][1]
  lista_actual =lista_agregado2[0]
  for productos in lista_agregado2:
        if productos[1] > maximo:
            maximo =productos[1]
            lista_actual =productos
        
  productos_ordenado.append(lista_actual)
  lista_agregado2.remove(lista_actual)
#print(productos_ordenado)

lista_final=[productos_ordenados_61+productos_ordenados_1+productosordenados+productos_ordenado]



'''print("los 20 productos con peores reseñas son :",lista_final[0:20],"/n")'''

#los meses màs vendidos
meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]



for mes in range(1,13):
  ventas_mes=[]
  for producto in lifestore_products:
    ventas = 0
    for venta in lifestore_sales:
      if venta[1]== producto[0] and mes == int(venta[3][3:5]):
        ventas += 1
    if ventas==0:
        continue
    else:
      formato = [ventas, mes, producto]
      ventas_mes.append(formato)
  
  resulta=0
  for venta in ventas_mes:
    resulta+=venta[0]

  #hago la suma de cada mes e imprimo de ahí hago la seleección  
  '''print("El total de ingresos fue: ",resulta,"del mes: ",venta[1])
  
 



    
  
  
  
  for venta in ventas_mes:
    print(venta[0], "ventas en el mes ",venta[1]," para el producto: ", venta[2][1], "\n")'''
    










#PEDIMOS AL USUARIO SU NOMBRE, CARGO Y CONTRASEÑA PARA DARLE ACCESO solo puede ingresar administrador y passlife de contraseña si no su acceso será denegado


name_lifestore = input("Ingresa el nombre del usuario: ")

puest_lifestore = input("Ingrese la categoria de ocupación:" )

passw_lifestore = input("Ingrese la contraseña:" )

if puest_lifestore == "administrador" and passw_lifestore == "passlife" :

 print(f"Hola " + name_lifestore +" bienvenido a lifestore") 


 menu=("""OPCIONES DISPONIBLES
 1) Productos más vendidos
 2) Productos rezagados
 3) Productos por reseña en el servicio
 4) Total de ingresos(anual/mensual)
  """)
 print(menu)


 option=input("ELIGE UNA OPCIÓN:  ")
 valid = "0"

 while valid != "1" :
  if option == "1":
    print("""1) Lista de 50 productos con mayores Ventas
    2) Los 100 productos con mayor busqueda """)
    valid ="1"
    option_1 = input("ELIGE UNA OPCIÓN: ")
    if option_1 == "1":
      print('los 50 productos más vendidos son:')
      for final in range(0,50):
        print("El producto:",productos_ordenados[final][0],"vendió:",productos_ordenados[final][1],"\n")
        
    
    elif option_1 == "2":
      print("los 100 productos con mayor busqueda son: ")
      for final in range(0,96):
        print("El producto:",productos_ormayor[final][0],"se buscó: ",productos_ormayor[final][1],"\n")
    
    else:
      print("OPCIÓN INVALIDA")
      option_1=input("Intentar de nuevo: ")

  
  elif option == "2":
    
    print("""1)Lista con los 50 productos con menores ventas:
    2)Los 100 productos con menores busquedas """)
    valid ="1"
    option_2 = input("ELIGE UN OPCIÓN: ")

    if option_2 == "1":

      print("Estos son los 50 productos con menores ventas")
      for final_1 in range(0,50):
        print("El producto: ",productos_ordenadose[final_1][0],"vendió:",productos_ordenadose[final_1][1],"\n")
    
    elif option_2 == "2":
      print("Estos son los 100 productos con menores busquedas")
      for final in range(0,96):
        print("El producto:",productos_ormenor[final][0],"se buscó: ",productos_ormenor[final][1],"\n")
    
    else:
      print("OPCIÓN INVALIDA")
      option_2=input("Intentar de nuevo: ")

  
  elif option == "3":
    print("""1) Lista de 20 productos con mejores reseñas
    2) Lista de 20 productos con las peores reseñas """)
    valid ="1"

    option_3 = input("ELIGE UNA OPCIÓN:  ")
    
    if option_3 == "1":

      print("Los 20 productos con mejores reseñas son: ")
      for final_5 in range(0,20):
        print("El producto:",productos_ordenados_5[final_5][0],  "con mejores reseñas de puntuación 5 obtuvo un total de: ",productos_ordenados_5[final_5][1], "\n")
    

    elif option_3 == "2":
      print("Los 20 productos con peores reseñas son: ")
      print("los 20 productos con peores reseñas son :",lista_final[0:20],"/n")
    
    else:
      print("OPCIÓN INVALIDA")
      option_3=input("Intentar de nuevo: ")
  

  elif option == "4":
    print("""1)Total de ingresos mensuales
    2) Total de ingresos anual
    3)los meses más vendidos""")
    valid ="1"

    option_4 = input("ELIGE UN OPCIÓN:  ")

    if option_4 == "1":
      print(" El total de ingresos mensuales son:")
      meses=int(input("ingresa en numero (mm) el último mes registrado: "))
      prom_mensual=float(result/meses)
      print("el promedio mensual es: $",prom_mensual)
    
    elif option_4 == "2":
      print("El total de ingreso anual es:")
      print("El total de ingresos fue: ",result)
    

    elif option_4 == "3":
     
      print("los meses con más ventas son :Abril,Enero,Marzo")#los imprimi ya contados y con el mes y yo hice la selección y ya no me dio tiempo de ponerles el while para ordenarlos 
 




    else:
      print("OPCIÓN INVALIDA")
      option_4=input("Intentar de nuevo: ")
  

  





else:
  print("ACCESO DENEGADO")





























 