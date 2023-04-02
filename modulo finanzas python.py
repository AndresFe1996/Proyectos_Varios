# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:24:19 2022

@author: Home
"""
import pandas as pd
from pandas_datareader import data
import numpy_financial as npf
import tabulate as tab
import investpy as inv
from pandas import ExcelWriter
class Interes_compuesto():  ## CLASE , ESTA ES LA CLASE
    print("""BIENVENIDO AL MODULO DE FINANZAS FECHO POR MI, POR FAVOR PARA ESTA CLASE
          RECUERDA USAR TASAS E.A O E.V TEN EN CUENTA LA PERIODICIDAD PORFAVOR""")
    def __init__(self,capital,interes,plazo): ## AQUI SE COLOCAN LOS PARAMETROS BASICOS DE LA CLASE
        self.capital=capital
        self.interes=interes/100
        self.plazo=plazo
        
        self.i=0 ## interes VA este es un ejemplo de variable de clase, solo esta en la clase
        self.p=0 ## plazo VA
        self.vf_0=0 ## plazo VA
        self.vp_0=0
        self.monto=0
        
    def valor_futuro(self): ## CREAMOS METODOS O INSTANCIAS
        self.vf=self.capital*(1+self.interes)**self.plazo
        print("el valor futuro de su operacion es: ")
        return self.vf
    
    def valor_actual(self,vf_0,i,p): ## CREAMOS METODOS
        self.i=i
        self.p=p
        self.vf_0=vf_0
        
        self.va=self.vf/(1+self.i)**self.p
        print("el valor actual de su operacion es: ")
        return self.va

    def amortizacion(self,monto,plazo,interes):
        self.monto=float(monto)
        self.p=plazo
        self.i=float(interes/100)
        global pago_mensual
        pago_mensual=self.monto*(self.i*(1+self.i)**self.p)/((1+self.i)**self.p-1)
        print("la cuota mensual del credito es: ")
        return round(pago_mensual)
    
    def crear_tabla_amortizacion(self,monto,plazo,interes,cuota_manejo=0,seguros=0):
        ## EN AGRADECIMIENTO A LOS INGENIEROS DE NUMPY_FINANCIAL, MIS RESPETOS
        ## Y TAMBIEN A LOS INGENIEROS DE TABULATE(CARPINTERIA PERFECTA DE IMPRESION)
        self.monto=monto
        self.plazo=plazo
        self.interes=interes
        self.cuota_manejo=cuota_manejo
        self.seguros=seguros
        
        capital = self.monto  ## parametros de la funcion
        tasa = self.interes
        plazo = self.plazo
        
        cuota = round(npf.pmt(tasa, plazo, -capital, 0), 0) #redondea y usa el metodo pmt para calcular
        # la cuota del prestamo (del modulo numpy financial)
        datos = [] # crear una lista vacia
        saldo = capital # variable saldo = a capital
        interes_total=0
    
        for i in range(1, plazo+1): # bucle for que empieza en 1 y termina en el plazo+1
          pago_capital = npf.ppmt(tasa, i, plazo, -capital, 0) # cacula la cuota constante para i
          pago_int = cuota - pago_capital # calcula el pago de intereses 
          saldo -= pago_capital  # calcula el saldo disminuyendo la cuota por i veces
          costo_1=self.cuota_manejo
          costo_2=self.seguros
          cuota_total=cuota+costo_1+costo_2
          linea = [i, format(cuota, '0,.0f'),format(cuota_total,'0,.0f'),format(costo_1,'0,.0f'),format(costo_2,'0,.0f') ,
               format(pago_capital, '0,.0f'), format(pago_int, '0,.0f'), format(saldo, '0,.0f')]
          # la linea anterir crea una variable que almacena el periodo y establece un formato para cuota
          # pago capial, pago interes y saldo queda una lista asi [[i,cuota,capital,pago_int,saldo]]
          # esto para i iteracion del bucle
          interes_total+=pago_int
          datos.append(linea)  # finalmente se agrega todo en la variable datos
     
        #con el uso del modulo tabulate para imprimir, establecemos un formato mas comodo
        # tabulate constuye tablas
        print("capital a amortizar: ",capital,"periodos seleccionados: ",plazo,"interes E.F: ",tasa)
        print(tab.tabulate(datos, headers=['Periodo', 'Cuota',"Cuota tot","cuota_Uso","seguros" ,'Capital', 'Intereses', 'saldo'], tablefmt='psql'))

    def eliminar_IC(self):
        print("---eliminando datos---")
        self.capital=0
        self.interes=0
        self.plazo=0
        print("---datos eliminados satisfactorio---")
        
class Inversion():
    
    def __init__(self,inventario,FI,FF):
        self.inventario=inventario
        self.FI=FI
        self.FF=FF
        
    def descargar_yahoo_finance(self):
        INV=data.DataReader(self.inventario,data_source="yahoo",start=self.FI,end=self.FF)
        return print(INV)
    
    def descargar_investing(self,inventario,FI,FF):
        # pip install investpy ## 2022-10-23 el modulo presenta falla por problemas con investing
        # ver 
        self.inventario=inventario
        self.FI=FI
        self.FF=FF
        INV=inv.get_stock_historical_data(self.inventario, "colombia", self.FI, self.FF)
        return print(INV) 
    
        #misc{investpy,author = {Alvaro Bartolome del Canto},
            #title = {investpy - Financial Data Extraction from Investing.com with Python},
            #year = {2018-2021},
            #publisher = {GitHub},
            #journal = {GitHub Repository},
            #howpublished = {\url{https://github.com/alvarobartt/investpy}}\/
    

class  Simular_portafolio_RF(Interes_compuesto):
    def __init__(self,cantidad):
        self.cantidad=cantidad 
        global capitales
        global intereses
        global plazos
        capitales=[]
        intereses=[]
        plazos=[]
        
        # BUCLE FOR PARA INGRESAR DE ACUERDO A LA CANTIDAD 
        for i in range(self.cantidad):
            
            self.k=float(input("inserte capital:"))
            capitales.append(self.k)
                            
            self.i=float(input("inserte interes (porcentaje): "))/100
            intereses.append(self.i)
            
            self.p=float(input("inserte plazos: "))
            plazos.append(self.p)
    
    # MOSTRAR CUADRO DE LOS PARAMETROS INGRESADOS
    def Mostrar_cuadro(self):
        global data
        data={"capitales":capitales,"intereses":intereses,"plazos":plazos}
        global df
        df=pd.DataFrame(data)
        return print(df)
            
    def valor_futuro_pf(self):
        global vf
        vf=list((map(lambda x,y,z: x*(1+y)**z,capitales,intereses,plazos)))
        data={"capitales":capitales,"intereses":intereses,"plazos":plazos,"vf":vf}
        df=pd.DataFrame(data)
        return print(df) 

    def generar_excel_pf(self):
        escritor=pd.ExcelWriter("C:/Users/Home/´portafolios.xlsx", engine="xlsxwriter")
        df.to_excel(escritor,sheet_name="hoja1", index=False)
        escritor.save()
        print("data guardada")
    
    
inversion=Interes_compuesto(100000,2,1)
print(inversion.valor_futuro())
inversion.amortizacion(100000,60,5)
inversion.crear_tabla_amortizacion(48364, 24, 0.0292953486,23100,2781)


print(npf.__dict__)

inversion.valor_actual(1340.09556,0.05,6)
#inversion.prueba ## como podemos ver, la variable de clase es un metodo dentro del objeto instanciado

#inversion.eliminar_IC()



#print(inversion.__dict__) ## con dict podemos ver que atributos tiene la instancia(y la clase de donde se instancio)


acciones=Inversion("PFBCOLOM.CL","2022-12-29","2022-12-30")
#print(acciones.__dict__)

acciones.descargar_yahoo_finance()
acciones.descargar_investing("BIC_p1", "04/07/2022","05/07/2022") ## descarga de investing

# portafolio=Simular_portafolio_RF(2)

#portafolio.Mostrar_cuadro()

#portafolio.valor_futuro_pf()

#portafolio.generar_excel_pf()

actual=Interes_compuesto(100000, 15, 1)
actual.valor_futuro()
actual.valor_actual(200000, 15, 1)