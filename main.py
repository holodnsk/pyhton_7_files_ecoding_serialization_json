#Ultra Lite
#1 Вручную создайте текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
#2 Создайте шаблон документа doc
#3 Внесите данные из файла в шаблон

from docxCreator import generate_report

# brand model fuel price
generate_report('Toyota', 'Corolla', 7, 1500000)

#Lite
#2 Создайте csv-файл с данными о машине.
#3 Создайте json-файл с данными о машине.


#Pro
#2 Замерьте время генерации отчета (время выполнения пункта 3).
#3 В каждый файл из задания Light добавьте параметр: время, затраченное на генерацию отчета.