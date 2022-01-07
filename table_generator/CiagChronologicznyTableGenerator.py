from table_generator import TableGenerator


def __prepareHeaders():
    lp_header = ('LP', 0, 0, 3, 2)
    wielolecie_header = ('Rok', 0, 2, 3, 3)
    przeplyw_max_header = ('Przepływ maksymalny Qmax,i [m\u00B3/s]', 0, 5, 3, 3)

    headers_definitions = [lp_header, wielolecie_header, przeplyw_max_header]
    return headers_definitions


def __addTableContent(table, table_content):
    index = 0
    for current_year, max_Q in table_content.iteritems():
        index += 1
        row_cells = table.add_row().cells
        cell_index_after_lp_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, 0, str(index), 2)
        cell_index_after_year_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_lp_cell, current_year, 3)
        cell_index_after_max_przeplyw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_year_cell, max_Q, 3)


def appendTable(document, table_content):
    number_of_columns = 8
    number_of_rows_for_headers_cells = 3
    headers_for_przeplywy_glowne_table = __prepareHeaders()
    PrzeplywyGlowneTable = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    PrzeplywyGlowneTable.style = 'Table Grid'

    TableGenerator.addHeadersToTable(PrzeplywyGlowneTable, headers_for_przeplywy_glowne_table)
    __addTableContent(PrzeplywyGlowneTable, table_content)
