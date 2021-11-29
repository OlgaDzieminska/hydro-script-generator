from table_generator.TableGenerator import addHeadersToTable


def prepareHeadersForObliczenieObjetosciISumObjetosci():
    rok_header = ('Rok', 0, 0, 3, 2)
    miesiac_header = ('Miesiąc', 0, 2, 3, 2)
    liczba_dni_w_miesiacu_header = ('Liczba dni w miesiącu n', 0, 4, 3, 3)
    SQ_header = ('SQ [m\u00B3/s]', 0, 7, 3, 4)
    V_header = ('V [mln m\u00B3]', 0, 11, 3, 4)
    SumV_header = ('\u03a3 V [mln m\u00B3]', 0, 15, 3, 4)

    headers_definitions = [rok_header, miesiac_header, liczba_dni_w_miesiacu_header, SQ_header, V_header, SumV_header]

    return headers_definitions


def appendObliczenieObjetosciISumObjetosciTableToDocument(document):
    number_of_columns = 19
    number_of_rows_for_headers_cells = 3
    headers_for_obliczenie_objetosci_i_sum_objetosci_table = prepareHeadersForObliczenieObjetosciISumObjetosci()
    ObliczenieObjetosciISumObjetosciTable = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    ObliczenieObjetosciISumObjetosciTable.style = 'Table Grid'

    addHeadersToTable(ObliczenieObjetosciISumObjetosciTable, headers_for_obliczenie_objetosci_i_sum_objetosci_table)