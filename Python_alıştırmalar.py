# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

types_list = [8, 3.2, 8j + 18, "Hello World", True, 23 < 22, [1, 2, 3, 4], {
    "Name"  : "Ali_Sir",
    "Age"   : 25,
    "Adress": "Aydın"
}, ("Machine Learning", "Data Science"),{"Python", "Machine Learning", "Data Science"}]

for type_ in types_list:
    print(type(type_))

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."

new_text = text.upper().replace(".", "").replace(",", "").split(" ")
print(new_text)

# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
# Adım 1: Verilen listenin eleman sayısına bakınız.
count = 0
for eleman in lst:
    count += 1
print(count)

# ya da

print(len(lst))

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A", "T", "A"] listesi oluşturunuz.

lst[:4]

# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)

# Adım 5: Yeni bir eleman ekleyiniz.

lst.append("Welt")

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")

# Görev 4:  Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict['Daisy'][1] = 13

# Adım 4: Key değer Ahmet value değeri [Turkey, 24] olan yeni bir değer ekleyiniz.

dict['Ahmet'] = ["Turkey", 24]

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict["Antonio"]

# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan
# ve bu listeleri return eden fonksiyon yazınız.
even, odd = list(), list()
def evenorodd(list_):
    for number in list_:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd
evenorodd([1,2,3,4,5,6,7])
####################################
my_list = [1,2,4,5,6,7,8,9]
even = [number for number in my_list if number % 2 == 0]
odd = [number for number in my_list if not number % 2 == 0]

print(even, ",", odd)
####################################

# Görev 6:  List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns

df = sns.load_dataset("car_crashes")
num_col = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# Görev 7:  List Comprehension yapısı kullanarak car_crashes verisinde isminde
# "no" barındırmayan değişkenlerin isimkerinin sonuna "FLAG" yazınız.


import seaborn as sns

df = sns.load_dataset("car_crashes")

new_col = [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns

# Görev 8: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

import seaborn as sns

og_list = ["abbrev", "no_previous"]

df = sns.load_dataset("car_crashes")

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols].head()


