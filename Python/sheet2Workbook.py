#Extract all sheet in source excel to separate excel file (a file for each sheet)

# Prepare
#   pip install xlwings

# Usage:
#   python .\sheet2Workbook.py .\myexcel.xlsx

import sys
import os
import xlwings as xw


def main():
    print("\n\n----- MAIN Start------")

    arguments  = sys.argv
    if (len(arguments) != 2) or (not os.path.exists(arguments[1])):
        print("Please input url list file")
        return
    
    infile = arguments[1]
    infile_no_ext = os.path.splitext(os.path.basename(infile))[0]

    wb_source = xw.Book(infile)

    for sheetname in wb_source.sheet_names:
        wb_des = xw.Book()
        ws_source = wb_source.sheets[sheetname]
        ws_source.copy(before=wb_des.sheets[0]) #copy sheet from ws_source to wb_des

        wb_des_filename = infile_no_ext + "_" + sheetname + ".xlsx"
        wb_des.save(wb_des_filename)
        wb_des.close()
        print(f"Extract sheet: {sheetname} to file: {wb_des_filename}")
        
        
    wb_source.close()
    print("----- MAIN End------")

if __name__ == '__main__':
    main()
    