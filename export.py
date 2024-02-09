import config
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


def export_results(df, average_turning_points_count):
    wb = Workbook()
    ws = wb.active

    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    for cell in ws[1]:
        cell.style = 'Pandas'
    
    ws.append([])
    ws.append(['Average turning points count', average_turning_points_count])
    ws.append(['Starting date', config.starting_date])
    ws.append(['Ending date', config.ending_date])
    
    wb.save('results.xlsx')
    print('Results exported to results.xlsx')