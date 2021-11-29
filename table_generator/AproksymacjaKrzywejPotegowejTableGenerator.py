from table_generator.TableGenerator import addHeadersToTable


def prepareHeadersForAproksymacjaKrzywejPotegowej():
    lp_header = ('LP', 0, 0, 3, 2)
    dzien_miesiac_rok_header = ('Dzień/Miesiąc/Rok', 0, 2, 3, 2)
    H_header = ('H[m]', 0, 4, 3, 3)
    Q_header = ('Q [m\u00B3/s]', 0, 7, 3, 3)
    X_header = ('X=lnH', 0, 10, 3, 4)
    Y_header = ('Y=lnQ', 0, 14, 3, 4)
    X_2_header = ('X\u00B2', 0, 18, 3, 4)
    XY_header = ('X\u00D7Y', 0, 22, 3, 4)

    headers_definitions = [lp_header, dzien_miesiac_rok_header, H_header, Q_header, X_header, Y_header, X_2_header, XY_header]

    return headers_definitions


def appendAproksymacjaKrzywejPotegowejTableToDocument(document):
    number_of_columns = 26
    number_of_rows_for_headers_cells = 3
    headers_for_aproksymacja_table = prepareHeadersForAproksymacjaKrzywejPotegowej()
    AproksymacjaTable = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    AproksymacjaTable.style = 'Table Grid'

    addHeadersToTable(AproksymacjaTable, headers_for_aproksymacja_table)
