# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:40:45 2020

@author: mellouki
"""


import pandas as pd

data = pd.read_excel(r"C:\Users\mello\Bureau\Covid-situation-par-région.xlsx") 
df = pd.DataFrame(data, columns = ['Date','Tanger-Tétouan-Al Hoceïma','Oriental','Fès-Meknès','Rabat-Salé-Kénitra',
                                   'Béni Mellal-Khénifra',
                                   'Casablanca-Settat',
                                  'Marrakech-Safi','Drâa-Tafilalet','Souss-Massa','Guelmim-Oued Noun',
                                   'Laâyoune-Sakia El Hamra',
                                   'Dakhla-Oued Ed Dahab',
                                   'cas confirmés','cas exclus suite à un résultats négative','nombre de mort',
                                   'nombre guéri','nombre total de mort',
                                   'nombre total de guéri'])

print(df)