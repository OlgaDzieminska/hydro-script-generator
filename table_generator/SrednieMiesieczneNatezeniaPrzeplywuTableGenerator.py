from main import ORDERED_HYDRO_MONTHS
from table_generator.TableGenerator import addHeadersToTable


def prepareHeadersForZestawienieSrednichMiesiecznychNatezenPrzeplywu():
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


def appendZestawienieSrednichMiesiecznychNatezenPrzeplywuTableToDocument(document):
    number_of_columns = 28
    headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table = prepareHeadersForZestawienieSrednichMiesiecznychNatezenPrzeplywu()
    headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table.sort(key=lambda header: header[1], reverse=True)

    number_of_rows_for_headers_cells = headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table[0][1] + 1
    ZestawienieSrednichMiesiecznychNatezenPrzeplywu = document.add_table(rows=number_of_rows_for_headers_cells, cols=number_of_columns)
    ZestawienieSrednichMiesiecznychNatezenPrzeplywu.style = 'Table Grid'

    addHeadersToTable(ZestawienieSrednichMiesiecznychNatezenPrzeplywu, headers_for_zestawienie_srednich_miesiecznych_natezen_przeplywu_table)