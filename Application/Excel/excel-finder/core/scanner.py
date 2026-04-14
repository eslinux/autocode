import os

def get_excel_files(directory):
    """
    Scans the given directory for Excel files (.xlsx).
    Returns a list of absolute file paths.
    """
    excel_files = []
    if not os.path.exists(directory) or not os.path.isdir(directory):
        return excel_files
        
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.xlsx') and not file.startswith('~$'):
                excel_files.append(os.path.join(root, file))
                
    return excel_files
