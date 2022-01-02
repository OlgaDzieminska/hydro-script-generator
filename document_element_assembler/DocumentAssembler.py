import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm
from docx.shared import Pt

from Constants import TEMP_FOLDER_DIRECTORY, CHART_IMAGES_DIRECTORY


def createDocumentWithFirstPage(city_name, river_name):
    document = Document()
    __appendFirstPageToDocument(document, city_name, river_name)
    return document


def __appendFirstPageToDocument(document, city_name, river_name):
    run = document.add_paragraph().add_run()
    font = run.font

    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph1 = document.add_paragraph('Katedra Hydrotechniki\nWydział Inżynierii Lądowej i Środowiska\nPolitechniki Gdańskiej')

    font.name = 'Arial'
    font.size = Pt(12)
    paragraph1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    document.add_picture('./resources/pg_logo.png', width=Cm(14))
    title = document.add_heading('OPERAT HYDROLOGICZNY', 0)
    title.add_run().bold = True
    title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    riverAndCityParagraphContent = 'RZEKA:%s \nPRZEKRÓJ:%s' % (river_name, city_name)
    r1 = document.add_paragraph(riverAndCityParagraphContent)
    r1.add_run().bold = True
    r1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER


def addChartToDocument(document, index_of_element, chart_title, chart_filename):
    addHeadingToDocumentElement(document, index_of_element, chart_title)
    path_to_chart_file = os.path.join(TEMP_FOLDER_DIRECTORY, CHART_IMAGES_DIRECTORY, chart_filename)
    document.add_picture(path_to_chart_file, width=Cm(19))


def addHeadingToDocumentElement(document, index_of_element, element_name):
    page_heading_content = '%s. %s' % (str(index_of_element), element_name)
    page_heading = document.add_heading(page_heading_content, 2)
    page_heading.add_run().bold = True
    page_heading.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
