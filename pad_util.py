import pandas as pd
import numpy as np
import datetime 

class Report:
    
    def __init__(self, caminho, tag):
        self.caminho = caminho
        self.tag = tag
        
    def read_inventario_xls(self):
      #result_placa_df = pd.read_excel(caminho, sheet_name=0, skiprows=2, usecols=[0, 3, 4, 6, 7, 8,9,10,11,12, 13, 14, 15, 16, 17, 18])
      result_placa_df = pd.read_excel(self.caminho, sheet_name=0)
      result_placa_df = pd.DataFrame(result_placa_df)
      
      qt_col = len(result_placa_df.columns)
      qt_linha = len(result_placa_df)
      
      if qt_col == 19:
          result_placa_df = result_placa_df.drop([0, 1, qt_linha-2, qt_linha-1], axis=0)
          # print(qt_linha, qt_col)
      if qt_col == 21:
          result_placa_df = result_placa_df.drop([0, 2, qt_linha-3, qt_linha-1], axis=0)
          # print(qt_linha, qt_col)
      result_placa_df = result_placa_df.dropna(axis=1, how="all")
      result_placa_df = result_placa_df.dropna(axis=0, how="all")
      
      # #grava o nome atual das colunas
      listColsPlacas = result_placa_df.columns.values.tolist()
      #Altera o nome das colunas com base no indice atual
      columnsNamePlacas = {listColsPlacas[0]:'Placa', 
                           listColsPlacas[1] : 'Modelo',
                           listColsPlacas[2] : 'Numero_de_serie', 
                           listColsPlacas[3] : "cod_de_produto", 
                           listColsPlacas[4] : 'Serial', 
                           listColsPlacas[5] : 'NE',
                           listColsPlacas[6] : 'Slot',
                           listColsPlacas[7] : 'PosicaoRack', 
                           listColsPlacas[8] : 'Sub_Rack',  
                           listColsPlacas[9] : 'Versao_Firmware', 
                           listColsPlacas[10] : 'Versao_Hardware', 
                           listColsPlacas[11] : 'Descricao', 
                           listColsPlacas[12] : 'Chassi_Id', 
                           listColsPlacas[13] : 'Inibido', 
                           listColsPlacas[14] : 'Em_teste', 
                           listColsPlacas[15] : 'Plataforma',}
      result_placa_df.rename(columns=columnsNamePlacas, inplace = True)
    
      result_placa_df['EAN'] = result_placa_df['Numero_de_serie'].str.slice(4, 20)
      result_placa_df['Região'] = self.tag
      result_placa_df.sort_values(by=['NE', 'Chassi_Id', 'Modelo'])
      return result_placa_df
  
    
    def comparador_ne_chassi_id_modelo(self, modelo_1, modelo_2):
        df = self.read_inventario_xls()
        temp_df = df.query(f'Modelo == "{modelo_1}"').groupby(['NE', 'Chassi_Id'])["Chassi_Id"].count().rename(f'{modelo_1}_total').to_frame()
        temp_df2 = df.query(f'Modelo == "{modelo_2}"').groupby(['NE', 'Chassi_Id'])["Chassi_Id"].count().rename(f'{modelo_2}_total').to_frame()
        df_new = pd.merge(df, temp_df, on=['NE', 'Chassi_Id'], how='left')
        df_new2 = pd.merge(df_new, temp_df2, on=['NE', 'Chassi_Id'], how='left')
        df_new2["Comparador"] = '-'
        df_new2.loc[(df_new2[f'{modelo_1}_total'] >= 1) & (df_new2[f"{modelo_2}_total"] > 0), "Comparador"] = "Possui Conjunto"
              
        # print(df_new2)
        # # print(type(df))
        return df_new2

    def list_ne(self):
        df = self.read_inventario_xls()
        ne_unique = df['NE'].sort_values().unique()
        return ne_unique
    
    
    def find_ne(self, ne):
        df = self.read_inventario_xls()
        df_filter = df[df.NE.isin(ne)]
        return df_filter
    
    
    def filter_modelo(self, df):
        return df['Modelo'].sort_values().unique()
    
    
    def find_modelo(self, df, modelo):
        return df[df.Modelo.isin(modelo)]
    

class Calculo_Potencia:
    
    def __init__(self):
        pass
    
    def cal_pot(self):
        pass
        