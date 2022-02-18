#Ultra Lite
#1 Вручную создайте текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
#2 Создайте шаблон документа doc
#3 Внесите данные из файла в шаблон

from docxCreator import generate_docx_report
import csv
import json
import time

# brand model fuel price
generate_docx_report('Toyota', 'Corolla', 7, 1500000)

#Lite
#1 Выполните задание уровня ultra light
#2 Создайте csv-файл с данными о машине.
#3 Создайте json-файл с данными о машине.
car_data = [['brand','model','fuel','price'],['Toyota', 'Corolla', 7, 1500000]]
with open('cars.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(car_data)

car_json = {'brand':'Toyota','model':'Corolla','fuel':7,'price':1500000}
with open('car.json','w') as f:
    json.dump(car_json,f)