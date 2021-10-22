import pandas as pd
import pdb
def pdg_from_veliciny(nazev_souboru_veliciny, oh):
       """ Returns Pdg or a type of shutdown for a specific bussiness interval"""
       
       veliciny = pd.read_excel(io = nazev_souboru_veliciny, sheet_name = 'Pdg',  skiprows = [0,1], \
                                      usecols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
       veliciny.rename(columns={'Unnamed: 1':'unit_name'}, inplace=True)
       veliciny.rename(columns={'Obchodní hodina':'elna_name'}, inplace=True)
       breakpoint()
       for i in range (1, len(veliciny['elna_name'])):
              print(f" i = {i}")
              #breakpoint()
              name = str(veliciny['elna_name'][i-1])
              print(f" str(veliciny[elna_name][i]) = {str(veliciny['elna_name'][i])}" )
              #print(f' type = {type(str(veliciny[elna_name][i]))}')
              
              if pd.isna(veliciny['elna_name'][i]) == True:
                            print(f" isna ")
                            veliciny['elna_name'][i]  = name
              if str(veliciny['unit_name'][i]) == 'nan' or str(veliciny['unit_name'][i]) == 'NaN':
                     veliciny['unit_name'][i] = 'n'
       breakpoint()
       veliciny.set_index(['elna_name', 'unit_name'], inplace = True)
       b = [(              'CEZ', 'n'), (              'EDE', 'n'),(             'EME1', 'n'),(           'Celkem',   'n')] # indexy ktere nechci ze souboru Veliciny nacitat
       #veliciny.index = list(filter(lambda el: el not in b, veliciny.index))
       [veliciny.drop(labels = i,  inplace=True) for i in b]
       breakpoint()
       return veliciny.iloc[:,oh]
