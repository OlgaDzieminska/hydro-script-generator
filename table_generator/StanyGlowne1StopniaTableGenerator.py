from HydrologyReportCreator import ORDERED_STANY
from table_generator import TableGenerator


def __prepareHeaders():
    lp_header = ('LP', 0, 0, 3, 2)
    wielolecie_header = ('Rok', 0, 2, 3, 3)
    stan_roczny_header = ('Stan roczny', 0, 5, 2, 6)
    NW_header_header = ('NW', 2, 5, 1, 2)
    SW_header_text = ('SW', 2, 7, 1, 2)
    WW_header_text = ('WW', 2, 9, 1, 2)

    states_headers = []
    column_index_for_month_header_cell = 1
    for month_number in ORDERED_STANY:
        states_headers.append((str(month_number), 2, column_index_for_month_header_cell, 1, 1))
        column_index_for_month_header_cell += 1

    headers_definitions = [lp_header, wielolecie_header, stan_roczny_header]
    headers_definitions.extend([NW_header_header, SW_header_text, WW_header_text])
    return headers_definitions


def __addTableContent(table, table_content):
    index = 0
    for current_year, table_data_row in table_content.iterrows():
        index += 1
        row_cells = table.add_row().cells
        cell_index_after_lp_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, 0, str(index), 2)
        cell_index_after_year_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_lp_cell, str(current_year), 3)
        cell_index_after_nw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_year_cell, table_data_row['NW'], 2)
        cell_index_after_sw_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_nw_cell, table_data_row['SW'], 2)
        cell_index_after_ww_cell = TableGenerator.addStyledContentToCellAndMerge(row_cells, cell_index_after_sw_cell, table_data_row['WW'], 2)

        if current_year == 'sum':
            __formatLastRow(row_cells)


def __formatLastRow(row_cells):
    run_with_text = row_cells[0].paragraphs[0].runs[0]
    run_with_text.clear()

    run_with_text = row_cells[2].paragraphs[0].runs[0]
    run_with_text.clear()
    run_with_sigma = row_cells[2].paragraphs[0].add_run(TableGenerator.SIGMA_SIGN)
    run_with_sigma.bold = True


def appendStanyGlowneTableToDocument(document, table_content):
    number_of_columns = 11
    headers_for_stany_glowne_table = __prepareHeaders()
    headers_for_stany_glowne_table.sort(key=lambda header: header[1], reverse=True)

    number_of_rows_for_headers_cells = headers_for_stany_glowne_table[0][1] + 1
    StanyGlowneTable = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    StanyGlowneTable.style = 'Table Grid'

    TableGenerator.addHeadersToTable(StanyGlowneTable, headers_for_stany_glowne_table)
    __addTableContent(StanyGlowneTable, table_content)
