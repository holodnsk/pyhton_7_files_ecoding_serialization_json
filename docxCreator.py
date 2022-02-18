import datetime

from docxtpl import DocxTemplate

from context import get_context


def from_template(brand, model, fuel, price, template):
    template = DocxTemplate(template)
    context = get_context(brand, model, fuel, price)  # gets the context used to render the document


    template.render(context)

    template.save(brand + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(brand, model, fuel, price):
    template = 'report.docx'
    document = from_template(brand, model, fuel, price, template)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"