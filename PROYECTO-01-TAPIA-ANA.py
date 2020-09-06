from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales 
from lifestore_file import lifestore_products


##LOGIN DE USUARIO
usuarios=[["Javier","AmoProgramar"],["EMTECH","emtech"],["Ana Tapia","amo el queso"],["Seb","messi"],["Max","1510"],["Santiago", "0404"]]

#Hacemos una lista unicamente con los nombres de usuarios porque vamos a ver si el nombre que introduzca el usario pertenece al registro
lista_usuarios=[]
for usuario in usuarios:
  lista_usuarios.append(usuario[0])

msg=input("¿Desea iniciar sesión? (Si/No)")

while msg=="si":
  usuario_entrada=input("Ingrese su usuario")
  if usuario_entrada in lista_usuarios:
    posicion=lista_usuarios.index(usuario_entrada)
    usuario_contraseña=input("Ingrese su contraseña")
    if usuario_contraseña==usuarios[posicion][1]:
      print("Bienvenido")
      print()
      
      ##1 PRODUCTOS MÁS VENDIDOS Y PRODUCTOS REZAGADOS
      print("01 PRODUCTOS MÁS VENDIDOS Y REZAGADOS")
      #Productos con más ventas
      lista_ventas=[]
      i=0
      contador=1
      lifestore_sales.append([0,0])

      for producto in lifestore_sales:
        if lifestore_sales[i-1][1]==lifestore_sales[i][1]:
          contador+=1
        else:
          lista_ventas.append([lifestore_sales[i-1][1],contador])
          contador=1
        i+=1
      lista_ventas.remove([0,1])
      lifestore_sales.remove([0,0])
      #print(lista_ventas) #Lista_ventas:lista de sublistas donde cada una muestra el id del producto y cuántas veces ha sido vendido

      lista_ventas_ordenada = []
      while lista_ventas:
        maximo = lista_ventas[0][1]
        producto_max = lista_ventas[0]
        for producto in lista_ventas:
          if maximo < producto[1]:
            maximo = producto[1]
            producto_max = producto
        lista_ventas_ordenada.append(producto_max)
        lista_ventas.remove(producto_max)
      #print(lista_ventas_ordenada)

      mejores_50 = []
      for producto in lista_ventas_ordenada:
        ID = producto[0]
        mejores_50.append([lifestore_products[ID - 1][1]])
      i=0
      print("Productos con mayores ventas:")
      for producto in mejores_50:
        print([i + 1, producto])
        i += 1




      #Productos con más búsquedas:
      lista_busquedas=[] #Lista_busquedas:lista de sublistas donde cada una muestra el id del producto y cuántas veces ha sido buscado
      i=0
      contador=1
      lifestore_searches.append([0,0]) #Añadimos un elemento a la lista que no afecte para que todos los elementos de la lista tengan con cual comparrase, si no pusieramos este valor, el primer elemento se compararía con el segundo, el segundo con el tercero,...  el penúltimo con el último y al llegar al ultimo elemento nuestra ciclo for fallaría
      for producto in lifestore_searches:
        if lifestore_searches[i-1][1]==lifestore_searches[i][1]:
          contador+=1
        else:
          lista_busquedas.append([lifestore_searches[i-1][1],contador])
          contador=1
        i+=1
      lista_busquedas.remove([0,1])
      lifestore_searches.remove([0,0]) #Es importante eliminar lo que añadimos inicialmente para no modificar la lista original lifestor_searches
      #print(lista_busquedas) 

      #Vamos a ordenar lista_busquedas de mayor de menor respecto al número de búsquedas de cada producto
      #El primer elemento de la lista será el producto con el mayor número de ventas, después se compara con el segundo producto, si el segundo producto tiene un mayor número de ventas, ahora ese producto reemplazará al primero.
      lista_busquedas_ordenada = []
      while lista_busquedas:
        maximo = lista_busquedas[0][1]
        producto_max = lista_busquedas[0]
        for producto in lista_busquedas:
          if maximo < producto[1]:
            maximo = producto[1]
            producto_max = producto
        lista_busquedas_ordenada.append(producto_max)
        lista_busquedas.remove(producto_max)
      #print(lista_busquedas_ordenada)

      mejores_100 = []
      #print("Productos con más búsquedas:")
      for producto in lista_busquedas_ordenada:
        ID = producto[0]
        mejores_100.append([lifestore_products[ID - 1][1]])
      i=0
      print()
      print()
      print()
      print("Productos con mayores búsquedas:")
      for producto in mejores_100:
        print([i + 1, producto])
        i += 1




      #Productos con menores ventas y menores busquedas por categoria:

      #Lo que hacemos es volter la lista de las ventas de mayor a manor, para que ahora nos quede de menor a mayor.
      x=len(lista_ventas_ordenada)
      lista_ventas_ordenada2=[]
      i=0
      for producto in lista_ventas_ordenada:
        lista_ventas_ordenada2.append(lista_ventas_ordenada[x-i-1])
        i+=1
      #print(lista_ventas_ordenada2)

      #Hacemos lo mismo para las búsquedas:
      x=len(lista_busquedas_ordenada)
      lista_busquedas_ordenada2=[]
      i=0
      for producto in lista_busquedas_ordenada:
        lista_busquedas_ordenada2.append(lista_busquedas_ordenada[x-i-1])
        i+=1
      #print(lista_busquedas_ordenada2)

      #Vamos a añadir la categoría a las listas:
      categorias_ventas=[]
      for producto in lista_ventas_ordenada2:
        ID=producto[0]
        categorias_ventas.append([producto,lifestore_products[ID-1][3]])
      #print(categorias_ventas)

      #Hacemos lo mismo para las búsquedas
      categorias_busquedas=[]
      for producto in lista_busquedas_ordenada2:
        ID=producto[0]
        categorias_busquedas.append([producto,lifestore_products[ID-1][3]])
      #print(categorias_busquedas)


      #Para cada categoría vamos a hacer dos listas, una para las ventas y otra para las búsquedas, es más trabajo pero así se puede imprimir una única lista en caso de que sólo se quiera ver una
      categorias=['procesadores','tarjetas de video','tarjetas madre','discos duros','memorias usb','pantallas','bocinas','audifonos']
      print()
      print()
      print()
      print("Productos con menores ventas:")
      print("Categoría: Procesadores")
      #Vamos a hacer in ciclo for que itere en cada uno de los productos de categorias_ventas para ver si el producto corresponde o no a cada una de las categorías
      procesadores_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='procesadores':
          ID=producto[0][0]
          contador+=1
          procesadores_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]]) 
      i=1
      for producto in procesadores_ventas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Tarjetas de video")
      tarjetasdevideo_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='tarjetas de video':
          ID=producto[0][0]
          contador+=1
          tarjetasdevideo_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in tarjetasdevideo_ventas:
        print([i,producto])
        i+=1
      
      print()
      print("Categoría: Tarjetas madre")
      tarjetasmadre_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='tarjetas madre':
          ID=producto[0][0]
          contador+=1
          tarjetasmadre_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in tarjetasmadre_ventas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Discos Duros")
      discosduros_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='discos duros':
          ID=producto[0][0]
          contador+=1
          discosduros_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in discosduros_ventas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Memorias USB")
      memoriasusb_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='memorias usb':
          ID=producto[0][0]
          contador+=1
          memoriasusb_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in memoriasusb_ventas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Pantallas")
      pantallas_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='pantallas':
          ID=producto[0][0]
          contador+=1
          pantallas_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in pantallas_ventas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Bocinas")
      bocinas_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='bocinas':
          ID=producto[0][0]
          contador+=1
          bocinas_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in bocinas_ventas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Audifonos")
      audifonos_ventas=[]
      contador=0
      for producto in categorias_ventas:
        if producto[1]=='audifonos':
          ID=producto[0][0]
          contador+=1
          audifonos_ventas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in audifonos_ventas:
        print([i,producto])
        i+=1

      print()
      print()
      print()
      print("Productos con menores búsquedas:")
      print("Categoría: Procesadores")
      procesadores_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='procesadores':
          ID=producto[0][0]
          contador+=1
          procesadores_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in procesadores_busquedas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Tarjetas de video")
      tarjetasdevideo_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='tarjetas de video':
          ID=producto[0][0]
          contador+=1
          tarjetasdevideo_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in tarjetasdevideo_busquedas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Tarjetas madre")
      tarjetasmadre_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='tarjetas madre':
          ID=producto[0][0]
          contador+=1
          tarjetasmadre_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in tarjetasmadre_busquedas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Discos Duros")
      discosduros_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='discos duros':
          ID=producto[0][0]
          contador+=1
          discosduros_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in discosduros_busquedas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Memorias USB")
      memoriasusb_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='memorias usb':
          ID=producto[0][0]
          contador+=1
          memoriasusb_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in memoriasusb_busquedas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Pantallas")
      pantallas_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='pantallas':
          ID=producto[0][0]
          contador+=1
          pantallas_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in pantallas_busquedas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Bocinas")
      bocinas_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='bocinas':
          ID=producto[0][0]
          contador+=1
          bocinas_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in bocinas_busquedas:
        print([i,producto])
        i+=1

      print()
      print("Categoría: Audifonos")
      audifonos_busquedas=[]
      contador=0
      for producto in categorias_busquedas:
        if producto[1]=='audifonos':
          ID=producto[0][0]
          contador+=1
          audifonos_busquedas.append([lifestore_products[ID-1][1] ,producto[0][1]])
      i=1
      for producto in audifonos_busquedas:
        print([i,producto])
        i+=1








      ##2 PRODUCTOS POR RESEÑA EN EL SERVICIO
      lista_scores=[]
      i=0
      contador=1
      lifestore_sales.append([0,0,0])
      suma=0

      for producto in lifestore_sales:
        if lifestore_sales[i-1][1]==lifestore_sales[i][1]:
          contador+=1
          suma+=lifestore_sales[i][2]
        else:
          lista_scores.append([lifestore_sales[i-1][1],suma/contador])
          contador=1
          suma=lifestore_sales[i][2]
        i+=1
      lista_scores.remove([0,0.0])
      lifestore_sales.remove([0,0,0])
      #print(lista_scores)

      #Los ordenamos de mayor a menor respecto al score promedio, es el mismo procedimiento que en las ventas y búsquedas
      lista_scores_ordenados1 = []
      while lista_scores:
        maximo = lista_scores[0][1]
        producto_max = lista_scores[0]
        for producto in lista_scores:
          if maximo < producto[1]:
            maximo = producto[1]
            producto_max = producto
        lista_scores_ordenados1.append(producto_max)
        lista_scores.remove(producto_max)
      #print(lista_scores_ordenados1)

      #Los ordenamos de menor a mayor respecto al score simplemente volteando la lista lista_scores_ordenados1
      x=len(lista_scores_ordenados1)
      lista_scores_ordenados2=[]
      i=0
      for producto in lista_scores_ordenados1:
        lista_scores_ordenados2.append(lista_scores_ordenados1[x-i-1])
        i+=1
      #print(lista_scores_ordenados2)

      #Hacemos una lista de los mejores y peores 20 productos
      mejores_20 = []
      for j in range(20):
        ID = lista_scores_ordenados1[j][0]
        mejores_20.append([lifestore_products[ID - 1][1]])
      i=0
      print()
      print()
      print()
      print()
      print()
      print("02 PRODUCTOS POR RESEÑA EN EL SERVICIO")
      print("Productos con mejores reseñas:")
      for producto in mejores_20:
        print([i + 1, producto])
        i += 1

      peores_20=[]
      for j in range(20):
        ID = lista_scores_ordenados2[j][0]
        peores_20.append([lifestore_products[ID-1][1]])
      i=0
      print()
      print()
      print()
      print("Productos con peores reseñas:")
      for producto in peores_20:
        print([i + 1, producto])
        i += 1








      ##3 TOTAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES, TOTAL ANUAL Y MESES CON MÁS VENTA AL AÑO
      print()
      print()
      print()
      print()
      print()
      print("03 TOTAL DE INGRESOS Y VENTAS")
      #Vamos a crear una lista que nos muestre para cada fecha, el id del producto que se vendió y cuánto cuesta el producto
      lista_ingresos=[]
      i=0
      for producto in lifestore_sales:
        ID=producto[1]
        lista_ingresos.append([ID,producto[3],lifestore_products[ID-1][2]])
        i+=1
      #print(lista_ingresos)
      

      #Vamos a hacer una lista totales_mensuales que indique el mes, número de ventas en el mes e ingresos totales del mes
      totales_mensuales=[]
      contador=0
      meses=['01','02','03','04','05','06','07','08','09','10','11']
      meses2=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre']
      i=0
      suma=0
      total_ganancia=0
      for mes in meses:
        for producto in lista_ingresos:
          x=producto[1][3:5]
          if x==mes:
            contador+=1
            suma+=producto[2]
        totales_mensuales.append([meses2[i], contador,suma])
        total_ganancia+=suma
        contador=0
        suma=0
        i+=1
      #print(totales_mensuales) #Esta lista muestra [mes, número de ventas en el mes, ganancias del mes]
      print("Número de ventas anual:")
      print(len(lifestore_sales))
      print("Ingreso Anual:")
      print(total_ganancia)
      print()
      print("Número de ventas promedio por mes")
      print((len(lifestore_sales))//11)
      print("Ingreso promedio mensual")
      print(total_ganancia/11)

      totales_mensuales_ordenados = []
      while totales_mensuales:
        maximo = totales_mensuales[0][1]
        producto_max = totales_mensuales[0]
        for producto in totales_mensuales:
          if maximo < producto[1]:
            maximo = producto[1]
            producto_max = producto
        totales_mensuales_ordenados.append(producto_max)
        totales_mensuales.remove(producto_max)
      print()
      print("Meses con más ventas al año:")
      for producto in totales_mensuales_ordenados:
        print(producto)
    







      ##CONCLUSIONES
      print()
      print()
      print()
      print()
      print()
      #Podemos preguntarnos si los productos que no buscan los clientes, tampoco son comprados, así que hacemos una lista con los 25 productos menos buscados y los 25 menos vendidos, depsués vemos qué productos se encuentran en ambas listas.audifonos_busquedas
      peores_25buscados=[]
      i=0
      for producto in range(25):
        peores_25buscados.append(lista_busquedas_ordenada2[i][0])
        i+=1
      
      peores_25vendidos=[]
      i=0
      for producto in range(25):
        peores_25vendidos.append(lista_ventas_ordenada2[i][0])
        i+=1
      
      #print(peores_20buscados)
      #print(peores_20vendidos)
      novendidos_nobuscados=[]
      for producto in peores_25vendidos:
        if producto in peores_25buscados:
          novendidos_nobuscados.append(producto)
      
      print("Productos que no son vendidos y tampoco son buscados")
      i=1
      for producto in novendidos_nobuscados:
        print([i,lifestore_products[producto-1][1]])
        i+=1


      #Ahora queremos saber qué productos si son buscados pero no comprados por los clientes
      mejores_25buscados=[]
      i=0
      for producto in range(25):
        mejores_25buscados.append(lista_busquedas_ordenada[i][0])
        i+=1
      print(mejores_25buscados)

      novendidos_sibuscados=[]
      for producto in peores_25vendidos:
        if producto in mejores_25buscados:
          novendidos_sibuscados.append(producto)
      print()
      print()
      print()
      print("Productos que si son buscados pero que no son vendidos")
      i=1
      for producto in novendidos_sibuscados:
        print([i,lifestore_products[producto-1][1]])
        i+=1

      
      break 


    else:
      print("Contraseña incorrecta")
      msg=input("¿Desea intentarlo de nuevo?")
  else:
    print("Usuario no válido")
    msg=input("¿Desea intentarlo de nuevo?")
    
