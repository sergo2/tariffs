# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math
import os
import time

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

path_to_excel_files = "C:\\Users\\YudakovSA\\Documents\\git\\tariffs\\ТД\\"
output_file_suffix = "nlk"

# Мэппинг колонок из Excel-файла на колонки в csv. Первая колонка имеет нулевой номер. Имя товара и расстояние будет заменено
cols_dict = {7:'commodity_name',3:'station1',5:'station2',8:'baseTariff',6:'distance'}
# Мэппинг кодов товара на название
commodity_dict = {'пшеница':402, 'ячмень':452, 'кукуруза':453, 'сахар':454, 'зерно бобов':455, 'подсолнечник':459}
# Целевой порядок колонок в csv-файле
target_cols = ['commodity','station1','station2','baseTariff','deadline']
# Тип строк в diff-файле
diff_type_dict = {'both':'ИЗМЕНЕНИЕ', 'right_only':'ДОБАВЛЕНИЕ', 'left_only':'УДАЛЕНИЕ'}