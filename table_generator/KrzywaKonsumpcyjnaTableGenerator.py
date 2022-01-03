from table_generator import TableGenerator
from table_generator.TableGenerator import SIGMA_SIGN


def __prepareHeadersForZestawienieSrednichMiesiecznychNatezenPrzeplywu():
    lp_header = ('LP', 0, 0, 3, 1)
    date_header = ('DZIEŃ-MIESIĄC-ROK', 0, 1, 3, 3)
    h_water_header = ('H[m]', 0, 4, 3, 2)
    Q_header = ('Q [m\u00B3/s]', 0, 6, 3, 2)
    X_header = ('X', 0, 8, 3, 3)
    Y_header = ('Y', 0, 11, 3, 3)
    X_power_header = ('X\u00B2', 0, 14, 3, 3)
    X_Y_header = ('X\u00D7Y', 0, 17, 3, 3)

    return [lp_header, date_header, h_water_header, Q_header, X_header, Y_header, X_power_header, X_Y_header]


def __addTableContent(table, table_content):
    for current_index, tr in table_content.iterrows():
        row_cells = table.add_row().cells
        cell_index_after_lp_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, 0, current_index, 1)
        cell_index_after_date_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_lp_cell, tr['date'], 3)
        cell_index_after_h_water_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_date_cell, tr['h_water'], 2)
        cell_index_after_Q_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_h_water_cell, tr['Q'], 2)
        cell_index_after_X_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_Q_cell, tr['X'], 3)
        cell_index_after_Y_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_X_cell, tr['Y'], 3)
        cell_index_after_X_power_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_Y_cell, tr['X_power'], 3)
        cell_index_after_X_Y_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_X_power_cell, tr['X_Y'], 3)

        if current_index == 'sum':
            __formatLastRow(row_cells)


def __formatLastRow(row_cells):
    run_with_zero = row_cells[0].paragraphs[0].runs[0]
    run_with_zero.clear()

    run_with_zero = row_cells[1].paragraphs[0].runs[0]
    run_with_zero.clear()

    run_with_zero = row_cells[4].paragraphs[0].runs[0]
    run_with_zero.clear()

    run_with_sigma = row_cells[6].paragraphs[0].runs[0]
    run_with_sigma.clear()
    run_with_sigma = row_cells[6].paragraphs[0].add_run(SIGMA_SIGN)
    run_with_sigma.bold = True


def appendTable(document, table_content):
    number_of_columns = 20
    number_of_rows_for_headers_cells = 3

    headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table = __prepareHeadersForZestawienieSrednichMiesiecznychNatezenPrzeplywu()
    zestawienieSrednichMiesiecznychNatezenPrzeplywu = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    zestawienieSrednichMiesiecznychNatezenPrzeplywu.style = 'Table Grid'

    TableGenerator.addHeadersToTable(zestawienieSrednichMiesiecznychNatezenPrzeplywu, headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table)
    __addTableContent(zestawienieSrednichMiesiecznychNatezenPrzeplywu, table_content)
