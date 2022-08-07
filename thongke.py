#%%
import re
import pandas as pd
import matplotlib
import seaborn  as sns
import matplotlib.pyplot as plt
from sympy import true

cartier = pd.read_csv('./thongke.csv')
#print(cartier)
def split_spiliter(dataframe, col_name, delimiter, sword,lance,axe,rapier,sai):
    dataframe['str_split'] = dataframe[col_name].str.split(delimiter)
    dataframe[sword] = dataframe.str_split.str.get(0).str.strip()
    dataframe[lance] = dataframe.str_split.str.get(1).str.strip()
    dataframe[axe] = dataframe.str_split.str.get(2).str.strip()
    dataframe[rapier] = dataframe.str_split.str.get(3).str.strip()
    dataframe[sai] = dataframe.str_split.str.get(4).str.strip()
    dataframe.fillna(0, inplace = True)
    del dataframe['str_split']

# sat thuong trung binh cua cac loai vu khi
# cartier_mean = cartier[['sword','lance','axe','rapier','sai']].mean().round(2).to_frame(name = 'Values')
# cartier_mean['Name'] = ['sword','lance','axe','rapier','sai']
# #cartier_mean['Name'] = ['total_damage','total_damage_taken','total_time','exp','healing','sword','lance','axe','rapier','sai','sword_use_time','lance_use_time','axe_use_time','rapier_use_time','sai_use_time']

# plt.figure(figsize=(15, 7))
# sns.barplot(x= "Name" , y = 'Values', data=cartier_mean )
# plt.title('Sát thương trung bình của các loại vũ khí')
# plt.xlabel('Weapons')
# plt.ylabel('Damages')
# plt.show()
#-----------------------------------------------------------------------------------------------------------
# sat thuong lon nhat cua cac loai vu khi
# cartier_mean = cartier[['sword','lance','axe','rapier','sai']].max().round(2).to_frame(name = 'Values')
# cartier_mean['Name'] = ['sword','lance','axe','rapier','sai']
# #cartier_mean['Name'] = ['total_damage','total_damage_taken','total_time','exp','healing','sword','lance','axe','rapier','sai','sword_use_time','lance_use_time','axe_use_time','rapier_use_time','sai_use_time']

# plt.figure(figsize=(15, 7))
# sns.barplot(x= "Name" , y = 'Values', data=cartier_mean )
# plt.title('Sát thương lớn nhất của các loại vũ khí qua các màn chơi')
# plt.xlabel('Weapons')
# plt.ylabel('Damages')
# plt.show()
#-----------------------------------------------------------------------------------------------------------
# tong so lan cac vu khi duoc su dung
# cartier_mean = cartier[['sword_use_time','lance_use_time','axe_use_time','rapier_use_time','sai_use_time']].sum().to_frame(name = 'Values')
# cartier_mean['Name'] = ['sword','lance','axe','rapier','sai']
# #cartier_mean['Name'] = ['total_damage','total_damage_taken','total_time','exp','healing','sword','lance','axe','rapier','sai','sword_use_time','lance_use_time','axe_use_time','rapier_use_time','sai_use_time']

# plt.figure(figsize=(15, 7))
# sns.barplot(x= "Name" , y = 'Values', data=cartier_mean )
# plt.title('Tổng số lần các vũ khí được sử dụng')
# plt.xlabel('Weapons')
# plt.ylabel('Times')
# plt.show()
#-----------------------------------------------------------------------------------------------------------
# Các chỉ số tổng hợp trung bình
cartier_mean = cartier[['total_damage','total_damage_taken','total_time','exp','healing']].mean().round(2).to_frame(name = 'Values')
cartier_mean['Name'] = ['total_damage','total_damage_taken','total_time','exp','healing']
#cartier_mean['Name'] = ['total_damage','total_damage_taken','total_time','exp','healing','sword','lance','axe','rapier','sai','sword_use_time','lance_use_time','axe_use_time','rapier_use_time','sai_use_time']

plt.figure(figsize=(15, 7))
sns.barplot(x= "Name" , y = 'Values', data=cartier_mean )
plt.title('Các chỉ số tổng hợp trung bình')
plt.xlabel('Stats')
plt.ylabel('Values')
plt.show()


