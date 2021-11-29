from main import ORDERED_STANY
from table_generator.TableGenerator import addHeadersToTable


def prepareHeadersForStanyGlowne():
    lp_header = ('LP', 0, 0, 3, 3)
    wielolecie_header = ('Rok', 0, 3, 3, 3)
    stan_roczny_header = ('Stan roczny', 0, 6, 2, 9)
    NW_header_header = ('NW', 2, 6, 1, 3)
    SW_header_text = ('SW', 2, 9, 1, 3)
    WW_header_text = ('WW', 2, 12, 1, 3)

    states_headers = []
    column_index_for_month_header_cell = 1
    for month_number in ORDERED_STANY:
        states_headers.append((str(month_number), 2, column_index_for_month_header_cell, 1, 1))
        column_index_for_month_header_cell += 1

    headers_definitions = [lp_header, wielolecie_header, stan_roczny_header]
    headers_definitions.extend([NW_header_header, SW_header_text,WW_header_text])
    return headers_definitions


def appendStanyGlowneTableToDocument(document):
    number_of_columns = 15
    headers_for_stany_glowne_table = prepareHeadersForStanyGlowne()
    headers_for_stany_glowne_table.sort(key=lambda header: header[1], reverse=True)

    number_of_rows_for_headers_cells = headers_for_stany_glowne_table[0][1] + 1
    StanyGlowneTable = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    StanyGlowneTable.style = 'Table Grid'

    addHeadersToTable(StanyGlowneTable, headers_for_stany_glowne_table)