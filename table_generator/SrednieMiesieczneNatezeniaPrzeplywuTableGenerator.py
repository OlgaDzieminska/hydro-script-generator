from main import ORDERED_HYDRO_MONTHS
from table_generator import TableGenerator


def __prepareHeadersForZestawienieSrednichMiesiecznychNatezenPrzeplywu():
    lp_header = ('Lp', 0, 0, 3, 2)
    wielolecie_header = ('Rok', 0, 2, 3, 2)
    czestosc_wystapienia_stanow_header = ('SQ [m\u00B3/s]', 0, 4, 2, 24)

    months_headers = []
    column_index_for_month_header_cell = 4
    for month_number in ORDERED_HYDRO_MONTHS:
        months_headers.append((str(month_number), 2, column_index_for_month_header_cell, 1, 2))
        column_index_for_month_header_cell += 2

    headers_definitions = [lp_header, wielolecie_header,
                           czestosc_wystapienia_stanow_header]
    headers_definitions.extend(months_headers)
    return headers_definitions


def __addTableContent(table, table_content):
    index = 0
    for current_year, table_data_row in table_content.iterrows():  # dataframe
        index += 1
        row_cells = table.add_row().cells  # +wiersz, row cells są przypisywane komórki
        cell_index_after_lp_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, 0, str(index), 2)
        cell_index_after_year_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_lp_cell, str(current_year), 2)

        cell_column_index = cell_index_after_year_cell
        for current_month in ORDERED_HYDRO_MONTHS:
            TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_column_index, table_data_row[str(current_month)], 2)
            cell_column_index += 2

        if current_year == 'mean':
            __formatLastRow(row_cells)


def __formatLastRow(row_cells):
    run_with_text = row_cells[0].paragraphs[0].runs[0]
    run_with_text.clear()

    run_with_text = row_cells[2].paragraphs[0].runs[0]
    run_with_text.clear()
    run_with_mean = row_cells[2].paragraphs[0].add_run('średnie')
    run_with_mean.bold = True


def appendZestawienieSrednichMiesiecznychNatezenPrzeplywuTableToDocument(document, table_content):
    number_of_columns = 28
    headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table = __prepareHeadersForZestawienieSrednichMiesiecznychNatezenPrzeplywu()
    headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table.sort(key=lambda header: header[1], reverse=True)

    number_of_rows_for_headers_cells = headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table[0][1] + 1
    zestawienieSrednichMiesiecznychNatezenPrzeplywu = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    zestawienieSrednichMiesiecznychNatezenPrzeplywu.style = 'Table Grid'

    TableGenerator.addHeadersToTable(zestawienieSrednichMiesiecznychNatezenPrzeplywu, headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table)
    __addTableContent(zestawienieSrednichMiesiecznychNatezenPrzeplywu, table_content)
