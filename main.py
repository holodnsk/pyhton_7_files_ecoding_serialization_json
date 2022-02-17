#Ultra Lite
#1 Вручную создайте текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
#2 Создайте шаблон документа doc
#3 Внесите данные из файла в шаблон

import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm



def get_context(company, result_sku_list):  # возвращает словарь аргументов
    return {
        'retailer': company,
        'sku_list': result_sku_list,
    }


def from_template(company, result_sku_list, template, signature):
    template = DocxTemplate(template)
    context = get_context(company, result_sku_list)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc  # adds the InlineImage object to the context
    template.render(context)

    template.save(company + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(company, result_sku_list):
    template = 'report.docx'
    signature = 'acc.png'
    document = from_template(company, result_sku_list, template, signature)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#Lite
#2 Создайте csv-файл с данными о машине.
#3 Создайте json-файл с данными о машине.

#Pro
#2 Замерьте время генерации отчета (время выполнения пункта 3).
#3 В каждый файл из задания Light добавьте параметр: время, затраченное на генерацию отчета.