Plantilla para el ramo de Programacion Basica (Python)
IPP, 2020



Trabajo Individual M2.

Fecha: 27/09/2020
Integrante :   Michael Saez.
'''

# La función crossDates es responsable de calcular la diferencia entre dos fechas.
def crossDates(dia_act, mes_act, ano_act, dia_nac, mes_nac, ano_nac): 

    # Crear 3 variables, cada una inicializada en 0 para ser utilizadas posteriormente.
    dia_total = 0
    mes_total = 0
    ano_total = 0

    ''' Si el día actual es mayor al día de nacimiento, calcular sobre dia_total la diferencia entre ambos días.
        Si, en cambio, el día actual es inferior al día de nacimiento, calcular la cantidad de días 
        que tiene el mes en curso (30, 31 o 28) y de acuerdo a ello calcular la diferencia de días ''' 
    if dia_act > dia_nac: 
        dia_total = dia_act - dia_nac  
    elif mes_act == 1 or mes_act == 3 or mes_act == 5 or mes_act == 7 or mes_act == 10 or mes_act == 12:
        dia_total = 31 + (dia_act - dia_nac)
        mes_act = mes_act - 1
    elif mes_act == 4 or mes_act == 6 or mes_act == 9 or mes_act == 11:
        dia_total = 30 + (dia_act - dia_nac)
        mes_act = mes_act - 1
    else:
        dia_total = 28 + (dia_act - dia_nac)
        mes_act = mes_act - 1

    # Así mismo calcular la diferencia entre el mes actual y el mes de nacimiento sobre mes_total.
    if mes_act > mes_nac:
        mes_total = mes_act - mes_nac    
    else:
        mes_total = 12 + (mes_act - mes_nac)
        ano_act = ano_act - 1

    # Finalmente calcular, también, la diferencia entre el año actual y el año de nacimiento sobre el año_total.
    ano_total = ano_act - ano_nac

    # Retornar el dia, mes y año resultantes.
    return dia_total, mes_total, ano_total

# La función decomposeNum es responsable de la des-composición de un número.
def decomposeNum(num): 

    # Obtener el último dígito del número
    fdeNum = num % 10 

    # Restar este dígito al número 
    num = int(num / 10) 

    # Retornar el dígito y el nuevo número 
    return fdeNum, num 

# La función decomposeDate es responsable de la des-composición de una fecha
def decomposeDate(num): 

    # Obtener el año
    iYears = int (num % 10000) 

    # Descomponer el año
    num = int (num / 10000) 

    # Obtener el mes
    iMonths = int (num % 100) 

    # Descomponer el mes
    num = int (num / 100) 

    # Obtener el dia
    iDays = int (num % 100) 

    # Retornar los años, meses y días, por separado.
    return iYears, iMonths, iDays 

def fibonacci(num):
    fib = 0 #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
    
    ''' Disminuir el número de serie de fibonacci en uno, 
        porque la primera iteración no se cuenta.'''
    num = num - 1 
    
    ''' Mientras la variable fib corresponde al valor de fibonacci(1), la variable 
        auxiliar iAux corresponderá a fibonacci(2) y serán los valores iniciales de esta sucesión'''
    iAux = 1 
    
    ''' La variable auxiliar iAux2 servirá como variable de almacenamiento 
        temporal que dará apoyo al proceso de interación de fibonacci'''
    iAux2 = 0 
    
    # Calcular fibonacci(i) desde i hasta num
    for i in range (num):
        iAux2 = fib
        fib = fib + iAux
        iAux = iAux2 

    # Retornar Fib  
    return fib

def mcm(a,b):
    mcm = 0 # esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion

    ''' iDividendo corresponde al dividendo de la operación que 
    calcula el mcm y se inicializa en 2'''
    iDividendo = 2 
    
    ''' iResto se inicializa en 1 para trabajar 
    con el ciclo while'''
    fResto = 1.0 
    
    ''' Mientras el resto sea superior a 0 entonces calcular el mcm, 
        sino, incrementar el dividendo y volver a ejecutar el ciclo'''
    while fResto > 0.0: 
        
        fResto = 0.0
        fResto += iDividendo % a
        fResto += iDividendo % b

        if fResto == 0.0:
            mcm = iDividendo
        else:
            iDividendo = iDividendo + 1          

    # Retornar mcm        
    return mcm

def mcd(a, b):
    mcd = 0 #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion

    # fResto se inicializa en 0
    fResto = 0.0 

    # Mientras el resto de b sea mayor a 0, calcular mcd
    while b > 0: 
        fResto = b
        b = a % b
        a = fResto

    mcd = a
     
    # Retornar mcd
    return mcd

def reverse_num(num):
    reverse = '0' #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion
 
    # Crear variable sNum que representa al parámetro recibido casteado a string
    sNum = str(num) 

    # Crear una lista vacía que se llenará con el número recibido en la función
    numbers = [] 

    # Crear un contador que representa el largo de dígitos entregados a la función
    count = len(sNum) 

    # Mientras contador llegue a 0, descomponer número, agregar el dígito a la lista y disminuir contador en 1
    while count > 0: 

        # Descomponer el número
        iDigit, num = decomposeNum(num) 

        # Agregar el dígito a la lista
        numbers.append(iDigit) 

        # Disminuir el contador en 1
        count = count - 1 

    reverse = numbers 
 
    # Retornar reverse
    return reverse 

def reverse_text(text):
    reverse = "" #esta es la variable que tendra que contener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion

    # Castear text sobre sTexto para validar que se trabajará con una cadena
    sTexto = str(text)

    # Recorrer texto entregado a la función, a la inversa
    for i in reversed(sTexto):

        # Registrar valor del texto en reverse
        reverse += i

    # Retornar reverse
    return reverse 

def palindromo(text):
    # Aqui escribir el desarrollo de las funcion

    # Castear text sobre sText para validar que se trabajará con una cadena
    sText = str (text)

    # Si texto es equivalente al texto invertido, retornar True.
    if (sText == reverse_text(text)): 
        return True
    else:
        return False

def num_mayores(num): 
    n_mayores = 0 #esta es la variable que se tendra que tener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion

    # Crear contador para el cálculo de los números pares.
    iContador = 0 

    # Mientras iContador sea menor a 10, calcular número mayor de la serie.
    while iContador < 10: 
        if num % 2 == 0:        
            iContador = iContador + 1         
            num = num + 1           
        else:
            num = num + 1   

    # Almacenar en la variable n_mayores el último numero de al serie de los 10 mayores.
    n_mayores = num - 1 

    # Retornar el último número mayor de la serie
    return n_mayores 

def factorial(num):
    fact = 1 #esta es la variable que se tendra que tener el resultado al final de la funcion
    # Aqui escribir el desarrollo de las funcion

    # Crear contacor para el cálculo del factorial
    iContador = 1 

    # Iterar tantas veces como sea el valor ingresado a la función
    while iContador < num: 

        # Se calcular el factorial
        fact = fact * (iContador + 1) 

        # Incrementar el contador en 1
        iContador = iContador + 1 

    # Retornar el factorial resultante
    return fact 

def primo(num):
    # Aqui escribir el desarrollo de las funcion

    # Crear un contador para el cálculo del número primo
    iContador = 2 

    # Mientras el contador no llegue al valor del número ingresado a la función, calcular número primo.
    while iContador < num: 
        if(num % iContador != 0):  
            return True
            break

        # Si no es primo, sumar 1 a contador y retornar false    
        else:
            iContador = iContador + 1 
            return False


def equi_parentesis(text):
    # Aqui escribir el desarrollo de las funcion

    # Crear contador para calcular paréntesis de apertura
    iContadorApertura = 0 

    # Crear contador para calcular paréntesis de cierre
    iContadorCierre = 0 

    # Crear lista vacía que apoyará el proceso de cálculo
    lTexto = [] 

    # Llenar la lista lTexto con los valores entregados a la función
    for i in text: 
        lTexto.append(i)

    # Mientras existan paréntesis de apertura, sumar 1 a contador
    while ("(" in lTexto) == True: 
        iContadorApertura = iContadorApertura + 1 

        # Eliminar el paréntesis
        lTexto.remove("(") 

    # Mientras existan paréntesis de cierre, sumar 1 a contador
    while (")" in lTexto) == True: 
        iContadorCierre = iContadorCierre + 1 

        # Eliminar el paréntesis
        lTexto.remove(")") 

    # Si el contador de Apertura es homólogo al contador de Cierre, retornar True... Sino, false.
    if (iContadorApertura == iContadorCierre): 
        return True
    else:
        return False

def get_fecha(fecha):
    #si el formato es DDMMAAAA
    dia = 0 #estas son las variable que tendran que contener los resultados al final de la funcion
    mes = 0
    ano = 0
    # Aqui escribir el desarrollo de las funcion

    # Obtener el año
    ano = int (fecha % 10000) 

    # Descomponer el año
    fecha = int (fecha / 10000) 

    # Obtener el mes
    mes = int (fecha % 100) 

    # Descomponer el mes
    fecha = int (fecha / 100) 
    
    # Obtener el dia
    dia = int (fecha % 100) 

    # Retornar día, mes y año, respectivamente.
    return dia,mes,ano

def min_vivido(fech_act,fec_nac):
    min_dias = 0#estas son las variable que tendran que contener los resultados al final de la funcion
    horas_dias = 0
    total_dia = 0
    # Aqui escribir el desarrollo de las funcion

    # Crear variables de apoyo
    ano_act = 0
    mes_act = 0
    dia_act = 0
    ano_nac = 0
    mes_nac = 0
    dia_act = 0
    ano_total = 0
    mes_total = 0
    dia_total = 0

    # Calcular fechas 
    ano_act, mes_act, dia_act = decomposeDate(fech_act)
    ano_nac, mes_nac, dia_nac = decomposeDate(fec_nac)

    # Calcular resta de fechas
    dia_total, mes_total, ano_total = crossDates(dia_act, mes_act, ano_act, dia_nac, mes_nac, ano_nac)

    # Calcular total_dia, horas_dias, min_dias
    total_dia = int ((dia_total) + (mes_total * 365/12) + (ano_total * 365))
    horas_dias = int (total_dia * 24)
    min_dias = int (horas_dias * 60)

    # Retornar valores
    return min_dias, horas_dias, total_dia, 

if __name__ == '__main__':
    #El programa esta programado para que al momento de ejecutarse, imprima todos los resultados de todas las funciones
    # cada funcion vendra con un caso de prueba, en el cual estara comentado su resultados

    #IMPORTANTE: NO SE CONFIEN CON SOLO TENER EL CASO DE PRUEBA. SIN EMBARGO USTEDES IGUAL PUEDEN
    #CAMBIAR LOS PARAMETROS PARA REALIZAR SUS PROPIAS PRUEBAS
    print("La serie fibonacci esta retornando: ", end="")
    print(fibonacci(10)) #si se ingresa 10 el resultado debe ser: 34
    print("El MCM esta retornando: ", end="")
    print(mcm(20,14)) #si se ingresa 20,14 el resultado debe ser: 140
    print("El MCD esta retornando: ", end="")
    print(mcd(20,14)) #si se ingresa 20,14 el resultado debe ser: 2
    print("El numero ingresado al revez es: ", end="")
    print(reverse_num(123456789)) #si se ingresa 123456789 el resultado debe ser: 987654321
    print("La palabra ingresada al revez es: ", end="")
    print(reverse_text("abcdef")) #si se ingresa "abcdef" el resultado debe ser: fedcba
    print("El resultado si un numero es palindromo es: ", end="")
    print(palindromo(1234321)) #si se ingresa 1234321 el resultado debe ser: True
    print("El ultimo numero de la seria de los 10 mayores es: ", end="")
    print(num_mayores(15)) #si se ingresa 15 el resultado debe ser: 34
    iContador = 0
    num = 15
    lista = []
    while iContador < 10: # Se almacenan los siguientes 10 números pares al objeto pasado por parámetro en la lista cadena[]
        if num % 2 == 0:        
            lista.append(num)
            iContador = iContador + 1         
            num = num + 1           
        else:
            num = num + 1   
    print("La serie de los 10 mayores es: " + str(lista))
    print("El resultado de factorial es: ", end="")
    print(factorial(10)) #si se ingresa 10 el resultado debe ser: 3628800
    print("El resultado del numero si es primo es: ", end="")
    print(primo(7)) #si se ingresa 7 el resultado debe ser: True
    print("El resultado de estar equilibrado de parentesis es: ", end="")
    print(equi_parentesis("(sasa(asdsa)))")) #si se ingresa "(sasa(asdsa)))" el resultado debe ser: False
    print("La tupla de la fecha separada es: ", end="")
    print(get_fecha(25072017)) #si se ingresa 25072017 el resultado debe ser: (25, 7, 2017)
    print("La tupla de los minutos de mi vida es: ", end="")
    print(min_vivido(25072017,11101982)) #si se ingresa 25072017,11101982 el resultado debe ser: (17802720, 296712, 12363)
