# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:24:19 2022

@author: Home
"""
# Librerias necesarias para algunas funciones

import pandas as pd
from pandas_datareader import data
import numpy_financial as npf
import tabulate as tab
from pandas import ExcelWriter

# clase interes simple
class interes_simple():
    def __init__(self):
        pass
    
    def valor_futuro_simple(self,capital_inicial, interes_monetario):
        self.capital=capital_inicial
        self.interes=interes_monetario

        valor_futuro=self.capital+self.interes
        return print(valor_futuro)

    def tiempo_simple(self,interes_monetario, capital_inicial,tasa ):
        self.int=interes_monetario
        self.cap=capital_inicial
        self.tasa=tasa

        tiempo_s=self.int/(self.cap*self.tasa)
        return print(tiempo_s)
    
    def tasa_simple(self,interes_monetario, capital_inicial, tiempo):
        self.inte=interes_monetario
        self.capi=capital_inicial
        self.tiempo=tiempo
        tasa_s=float(self.inte)/(float(self.capi)*float(self.tiempo))
        return print(tasa_s)

    def valor_presente_simple(self, interes_monetario, tasa,tiempo):
        self.inter=interes_monetario
        self.tas=tasa
        self.time=tiempo
        valor_presente_s=float(self.inter)/(float(self.time)*float(self.tas))
        return print(valor_presente_s)

# clase interes compuesto
class Interes_compuesto():  ## CLASE , ESTA ES LA CLASE
    def __init__(self): ## AQUI SE COLOCAN LOS PARAMETROS BASICOS DE LA CLASE
        pass

    def valor_futuro_compuesto(self, valor_presente, tasa, periodos): ## CREAMOS METODOS O INSTANCIAS
        self.valor_p=valor_presente
        self.tasa=tasa
        self.periodos=periodos
        
        valor_f_compuesto=self.valor_p*(1+self.tasa)^self.periodos
        return print(valor_f_compuesto)
    
    def valor_actual(self,valor_futuro,tasa,periodo): ## CREAMOS METODOS
        self.i=tasa
        self.p=periodo
        self.vf=valor_futuro
        
        valor_presente_compuesto=self.vf/(1+self.i)**self.p
        print("el valor actual de su operacion es: ")
        return print(valor_presente_compuesto)

    def amortizacion(self,monto,plazo,interes):
        self.monto=float(monto)
        self.p=plazo
        self.i=float(interes/100)
        global pago_mensual
        pago_mensual=self.monto*(self.i*(1+self.i)**self.p)/((1+self.i)**self.p-1)
        print("la cuota mensual del credito es: ")
        return print(round(pago_mensual))
    
    def crear_tabla_amortizacion(self,monto,plazo,interes,cuota_manejo=0,seguros=0):
        ## EN AGRADECIMIENTO A LOS INGENIEROS DE NUMPY_FINANCIAL, MIS RESPETOS
        ## Y TAMBIEN A LOS INGENIEROS DE TABULATE(CARPINTERIA PERFECTA DE IMPRESION)
        self.monto=monto
        self.plazo=plazo
        self.interes=interes/100
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
   
    def tasa_compuesta(self, nper, va, vf,):
        __texto__="Tasa_compuesta solo sirve para pago de intereses al final del periodo"
        self.nper=float(nper)
        self.va=float(va)
        self.vf=float(vf)

        tasa=(self.vf/self.va)**(1/self.nper)-1
        return print(tasa)

    def tiempo_negociacion(self,va,vf,tasa):
        __texto__="tiempo_negociacion solo sirve para pago de intereses al final del periodo"
        self.va=float(va)
        self.vf=float(vf)
        self.tasa=float(tasa/100)

        tiempo_n=np.log2((self.vf/self.va))/np.log2((1+self.tasa))
        return print(tiempo_n)

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

# MANEJO DE INTERESES

class interes():
    def __init__(self):
        pass
    global __tasas__
    __tasas__={'EM_EM':1,
'EM_ED':0.0333333333333333,
'EM_ES':6,
'EM_EC':4,
'EM_EB':2,
'EM_ET':3,
'EM_EA':12,
'EM_EQ':0.5,'ED_EM':30,
'ED_ED':1,
'ED_ES':180,
'ED_EC':120,
'ED_EB':60,
'ED_ET':90,
'ED_EA':360,
'ED_EQ':15,
'ES_EM':0.166666666666667,
'ES_ED':0.00555555555555556,
'ES_ES':1,
'ES_EC':0.666666666666667,
'ES_EB':0.333333333333333,
'ES_ET':0.5,
'ES_EA':2,
'ES_EQ':0.0833333333333333,
'EC_EM':0.25,
'EC_ED':0.00833333333333333,
'EC_ES':1.5,
'EC_EC':1,
'EC_EB':0.5,
'EC_ET':0.75,
'EC_EA':3,
'EC_EQ':0.125,'EB_EM':0.5,
'EB_ED':0.0166666666666667,
'EB_ES':3,
'EB_EC':2,
'EB_EB':1,
'EB_ET':1.5,
'EB_EA':6,
'EB_EQ':0.25,'ET_EM':0.333333333333333,
'ET_ED':0.0111111111111111,
'ET_ES':2,
'ET_EC':1.33333333333333,
'ET_EB':0.666666666666667,
'ET_ET':1,
'ET_EA':4,
'ET_EQ':0.166666666666667,'EA_EM':0.0833333333333333,
'EA_ED':0.00277777777777778,
'EA_ES':0.5,
'EA_EC':0.333333333333333,
'EA_EB':0.166666666666667,
'EA_ET':0.25,
'EA_EA':1,
'EA_EQ':0.0416666666666667,'EQ_EM':0.0833333333333333,
'EQ_ED':0.00277777777777778,
'EQ_ES':0.5,
'EQ_EC':0.333333333333333,
'EQ_EB':0.166666666666667,
'EQ_ET':0.25,
'EQ_EA':1,
'EQ_EQ':0.0416666666666667,
'EQ_EM':2,
'EQ_ED':0.0666666666666667,
'EQ_ES':12,
'EQ_EC':8,
'EQ_EB':4,
'EQ_ET':6,
'EQ_EA':24,
'EQ_EQ':1           
               }
    
    global __clave__
    __clave__=0

    global factor
    factor=0

    def convertir_tasas_equivalentes_efectivas(self,periodo_a_convertir,tasa,capitalizacion_actual):
        print("""la conversion solo funciona con tasas efectivas basicas a un año, si desea convertir una casa con capitalizacion
        diferente a la comun debe usar la formula TE=((1+Tasa_de_interes)**periodos )-1""")
        self.periodo_a_convertir=periodo_a_convertir.upper()
        self.tasa=float(tasa/100)
        self.capitalizacion_actual=capitalizacion_actual.upper()
        
        __clave__=self.periodo_a_convertir+"_"+self.capitalizacion_actual
        
        for i in __tasas__:
            factor=__tasas__[__clave__]
        
        valor=((1+self.tasa)**(factor)-1)

        return print("tasa efectiva equivalente de la capitalizacion actual:{} a {} es: {:.10f}".format(self.capitalizacion_actual,
        self.periodo_a_convertir,valor))

    global __nombres__
    __nombres__={'NM:NOMINAL ANUAL MENSUAL',
'NAD:NOMINAL ANUAL DIARIO',
'NAS:NOMINAL ANUAL SEMESTRAL',
'NAC:NOMINAL ANUAL CUATRIMESTRAL',
'NAB:NOMINAL ANUAL BIMESTRAL',
'NAT:NOMINAL ANUALTRIMESTRAL',
'NA:NOMINAL ANUAL',
'NAQ:NOMINAL ANUAL QUINCENAL',
'EM:EFECTIVO MENSUAL',
'ED:EFECTIVO DIARIO',
'ES:EFECTIVO SEMESTRAL',
'EC:EFECTIVO CUATRIMESTRAL',
'EB:EFECTIVO BIMESTRAL',
'ET:EFECTIVO TRIMESTRAL',
'EA:EFECTIVO ANUAL',
'EQ:EFECTIVO QUINCENAL'
}
    global Periodos_nom
    Periodos_nom={
    1:"NA",6:"NAB",4:"NAT",3:"NAC",2:"NAS",12:"NAM"
}
    def convertir_tasas_efectivas_a_nominales(self,capitalizacion_efectiva,tasa_efectiva,periodos):
        self.capitalizacion_efectiva=capitalizacion_efectiva
        self.tasa_efectiva=float(tasa_efectiva)
        self.periodos=int(periodos)
        
        tas_nom=self.tasa*self.periodos

        for name in Periodos_nom:
            if name==self.periodos:
                name_valor=Periodos_nom[name]

        return print("Tasa nominal {} equivalente a la tasa {} del {:.10f}".format(name_valor,self.capitalizacion_efectiva,tas_nom))

