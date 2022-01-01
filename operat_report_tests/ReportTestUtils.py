from random import randint

TEST_CITY_NAME = 'Nowy Sącz'
TEST_RIVER_NAME = 'Dunajec'
MULTIANNUAL_YEARS_RANGE = range(1986, 1989 + 1)
TEN_YEARS_RANGE = range(1982, 1991 + 1)


def saveTestDocumentFileAndPrintFileName(document):
    doc_name_iter = randint(0, 100)
    document_output_filepath = 'temp/' + str(doc_name_iter) + '.docx'
    document.save(document_output_filepath)
    print('Saved document to:' + document_output_filepath)
