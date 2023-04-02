# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:43:53 2022

@author: Home
"""

### convertirtidor de tasas python

class Interes:
    
    conceptos={"EM":"efectiva mensual","ED":"efectiva diaria","ES":"efectiva semestral",
               "EC":"efectiva cuatrimestral","EB":"efectiva bimestral","ET":"efectiva trimestral",
               "EA":"efectiva anual"}
    
    def __init__(self,periodo_actual,interes,periodicidad):
        self.periodicidad=periodicidad.upper()
        self.interes=float(interes)/100       
        self.periodo_actual=periodo_actual.upper()
    
    def calcular_tasas_efectivas_equivalentes(self):
        # EA A TODAS LAS PERIODICIDADES
        if self.periodo_actual=="EA" and self.periodicidad=="EM":
            valor=((1+self.interes)**(1/12)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EA" and self.periodicidad=="ED":
            valor=((1+self.interes)**(1/360)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EA" and self.periodicidad=="ES":
            valor=((1+self.interes)**(1/2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EA" and self.periodicidad=="EC":
            valor=((1+self.interes)**(1/3)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EA" and self.periodicidad=="EB":
            valor=((1+self.interes)**(1/6)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EA" and self.periodicidad=="ET":
            valor=((1+self.interes)**(1/4)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EA" and self.periodicidad=="EA":
            valor=((1+self.interes)**(1/4)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EA" and self.periodicidad=="EQ":
            valor=((1+self.interes)**(1/24)-1)
            return '{:.10f}'.format(valor)      
        
        # EM A TODAS LAS PERIODICIDADES 
        
        if self.periodo_actual=="EM" and self.periodicidad=="EM":
            valor=((1+self.interes)**(1/1)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EM" and self.periodicidad=="ED": # VALIDADO
            valor=((1+self.interes)**(1/30)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EM" and self.periodicidad=="ES": # VALIDADO
            valor=((1+self.interes)**(6)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EM" and self.periodicidad=="EC": # VALIDADO
            valor=((1+self.interes)**(4)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EM" and self.periodicidad=="EB": # VALIDADO
            valor=((1+self.interes)**(2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EM" and self.periodicidad=="ET": # VALIDADO
            valor=((1+self.interes)**(3)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EM" and self.periodicidad=="EA": # VALIDADO
            valor=((1+self.interes)**(12)-1)
            return '{:.10f}'.format(valor)    
        elif self.periodo_actual=="EM" and self.periodicidad=="EQ": # VALIDADO
            valor=((1+self.interes)**(1/2)-1)
            return '{:.10f}'.format(valor)        
        # ED A TODAS LAS PERIODICIDADES
        
        if self.periodo_actual=="ED" and self.periodicidad=="EM": # VALIDADO
            valor=((1+self.interes)**(30)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ED" and self.periodicidad=="ED": # VALIDADO
            valor=((1+self.interes)**(1/1)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ED" and self.periodicidad=="ES": # VALIDADO
            valor=((1+self.interes)**(180)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ED" and self.periodicidad=="EC": # VALIDADO
            valor=((1+self.interes)**(120)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ED" and self.periodicidad=="EB": # VALIDADO
            valor=((1+self.interes)**(60)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ED" and self.periodicidad=="ET": # VALIDADO
            valor=((1+self.interes)**(90)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ED" and self.periodicidad=="EA": # VALIDADO
            valor=((1+self.interes)**(360)-1)
            return '{:.10f}'.format(valor)       
        elif self.periodo_actual=="ED" and self.periodicidad=="EQ": # VALIDADO
            valor=((1+self.interes)**(15)-1)
            return '{:.10f}'.format(valor) 
        
        # ES A TODAS LAS PERIODICIDADES

        if self.periodo_actual=="ES" and self.periodicidad=="EM": # VALIDADO
            valor=((1+self.interes)**(1/6)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ES" and self.periodicidad=="ED": # VALIDADO
            valor=((1+self.interes)**(1/180)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ES" and self.periodicidad=="ES": # #VALIDADO
            valor=((1+self.interes)**(1/1)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ES" and self.periodicidad=="EC": # VALIDADO
            valor=((1+self.interes)**(1/1.5)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ES" and self.periodicidad=="EB": # VALIDADO
            valor=((1+self.interes)**(1/3)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ES" and self.periodicidad=="ET": # VALIDADO
            valor=((1+self.interes)**(1/2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ES" and self.periodicidad=="EA": # VALIDADO
            valor=((1+self.interes)**(2)-1)
            return '{:.10f}'.format(valor) 
        elif self.periodo_actual=="ES" and self.periodicidad=="EQ": # VALIDADO
            valor=((1+self.interes)**(1/12)-1)
            return '{:.10f}'.format(valor) 

        # EC A TODAS LAS PERIODICIDADES

        if self.periodo_actual=="EC" and self.periodicidad=="EM": # VALIDADO
            valor=((1+self.interes)**(1/4)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EC" and self.periodicidad=="ED": # VALIDADO
            valor=((1+self.interes)**(1/120)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EC" and self.periodicidad=="ES": # VALIDADO
            valor=((1+self.interes)**(6/4)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EC" and self.periodicidad=="EC": # VALIDADO
            valor=((1+self.interes)**(1/1)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EC" and self.periodicidad=="EB": # VALIDADO
            valor=((1+self.interes)**(1/2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EC" and self.periodicidad=="ET": # VALIDADO
            valor=((1+self.interes)**(1/(4/3))-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EC" and self.periodicidad=="EA": # 
            valor=((1+self.interes)**(3)-1)
            return '{:.10f}'.format(valor) 
        elif self.periodo_actual=="EC" and self.periodicidad=="EQ": # VALIDADO
            valor=((1+self.interes)**(1/8)-1)
            return '{:.10f}'.format(valor) 

        # EB A TODAS LAS PERIODICIDADES
        
        if self.periodo_actual=="EB" and self.periodicidad=="EM": # VALIDADO
            valor=((1+self.interes)**(1/2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EB" and self.periodicidad=="ED": # VALIDADO
            valor=((1+self.interes)**(1/60)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EB" and self.periodicidad=="ES": # VALIDADO
            valor=((1+self.interes)**(3)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EB" and self.periodicidad=="EC": # VALIDADO
            valor=((1+self.interes)**(2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EB" and self.periodicidad=="EB": # VALIDADO
            valor=((1+self.interes)**(1/1)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EB" and self.periodicidad=="ET": # VALIDADO
            valor=((1+self.interes)**(1/(2/3))-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EB" and self.periodicidad=="EA": # VALIDADO
            valor=((1+self.interes)**(6)-1)
            return '{:.10f}'.format(valor) 
        elif self.periodo_actual=="EB" and self.periodicidad=="EQ": # VALIDADO
            valor=((1+self.interes)**(1/4)-1)
            return '{:.10f}'.format(valor) 

        # ET A TODAS LAS PERIODICIDADES        

        if self.periodo_actual=="ET" and self.periodicidad=="EM": # VALIDADO
            valor=((1+self.interes)**(1/3)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ET" and self.periodicidad=="ED": # VALIDADO
            valor=((1+self.interes)**(1/90)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ET" and self.periodicidad=="ES": # VALIDADO
            valor=((1+self.interes)**(2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ET" and self.periodicidad=="EC": # VALIDADO
            valor=((1+self.interes)**(4/3)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ET" and self.periodicidad=="EB": # VALIDADO
            valor=((1+self.interes)**(1/(3/2))-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ET" and self.periodicidad=="ET": # VALIDADO
            valor=((1+self.interes)**(1/1)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="ET" and self.periodicidad=="EA": # VALIDADO
            valor=((1+self.interes)**(4)-1)
            return '{:.10f}'.format(valor) 
        elif self.periodo_actual=="ET" and self.periodicidad=="EQ": # VALIDADO
            valor=((1+self.interes)**(1/6)-1)
            return '{:.10f}'.format(valor)
        
        # EQ A TODAS LAS PERIODICIDADES

        if self.periodo_actual=="EQ" and self.periodicidad=="EM": # VALIDADO
            valor=((1+self.interes)**(2)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EQ" and self.periodicidad=="ED": # VALIDADO
            valor=((1+self.interes)**(1/15)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EQ" and self.periodicidad=="ES": # VALIDADO
            valor=((1+self.interes)**(12)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EQ" and self.periodicidad=="EC": # VALIDADO
            valor=((1+self.interes)**(8)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EQ" and self.periodicidad=="EB": # VALIDADO
            valor=((1+self.interes)**(4)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EQ" and self.periodicidad=="ET": # VALIDADO
            valor=((1+self.interes)**(6)-1)
            return '{:.10f}'.format(valor)
        elif self.periodo_actual=="EQ" and self.periodicidad=="EA": # VALIDADO
            valor=((1+self.interes)**(24)-1)
            return '{:.10f}'.format(valor) 
        elif self.periodo_actual=="EQ" and self.periodicidad=="EQ": # VALIDADO
            valor=((1+self.interes)**(1)-1)
            return '{:.10f}'.format(valor)

    def calcular_tasas_nominales_a_efectivas(self,tasa_nominal_actual,tasa_valor,capitalizacion):
        self.tasa_nominal=tasa_nominal_actual
        self.tasa_valor=tasa_valor/100
        self.capitalizacion=capitalizacion
    
        
        if self.tasa_nominal=="NA" and self.capitalizacion=="NM": # VALIDADO
            valor_nominal=((1+self.tasa_valor/12)**1)-1
            return "{:.10f}".format(valor_nominal)
        
        elif self.tasa_nominal=="NA" and self.capitalizacion=="ND": # NO CUADRA
            valor_nominal=((1+self.tasa_valor/360)**1)-1
            return "{:.10f}".format(valor_nominal)
        
        elif self.tasa_nominal=="NA" and self.capitalizacion=="NS": # NO CUADRA
            valor_nominal=((1+self.tasa_valor/2)**1)-1
            return "{:.10f}".format(valor_nominal)
        
        elif self.tasa_nominal=="NA" and self.capitalizacion=="NB": # NO CUADRA
            valor_nominal=((1+self.tasa_valor/6)**1)-1
            return "{:.10f}".format(valor_nominal)
        
        elif self.tasa_nominal=="NA" and self.capitalizacion=="NT": # NO CUADRA
            valor_nominal=((1+self.tasa_valor/4)**1)-1
            return "{:.10f}".format(valor_nominal)
        
        elif self.tasa_nominal=="NA" and self.capitalizacion=="NA":
            valor_nominal=((1+self.tasa_valor/1)**1)-1
            return "{:.10f}".format(valor_nominal)
        
        elif self.tasa_nominal=="NA" and self.capitalizacion=="NQ":
            valor_nominal=((1+self.tasa_valor/24)**1)-1
            return "{:.10f}".format(valor_nominal)
        
ejemplo=Interes("ea",33,"em")
ejemplo.calcular_tasas_efectivas_equivalentes()

# convertir formato de tasa en un formato mas legible
tasa_presentacion=print("tasa del",round(
    float(ejemplo.calcular_tasas_efectivas_equivalentes())*100,2),"%")


lista_tasas={"EA":1.5,"EA":6.5}



