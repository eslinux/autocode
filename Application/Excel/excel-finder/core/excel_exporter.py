import os
import datetime
import xlsxwriter

def export_results(results, output_dir):
    """
    Exports the search results to a beautifully formatted Excel file using xlsxwriter.
    
    Returns the absolute path of the generated Excel file.
    """
    now = datetime.datetime.now()
    filename = now.strftime("ExcelSearchResult_%Y%m%d-%H%M.xlsx")
    output_path = os.path.join(output_dir, filename)
    
    workbook = xlsxwriter.Workbook(output_path)
    ws = workbook.add_worksheet("Search Results")
    
    # Formats
    header_format = workbook.add_format({
        'bold': True,
        'font_color': 'white',
        'bg_color': '#4F81BD',
        'border': 1
    })
    
    link_format = workbook.add_format({
        'font_color': 'blue',
        'underline': True
    })
    
    red_font_format = workbook.add_format({'font_color': 'red', 'bold': True})
    
    # Define headers
    headers = ["Search Keyword", "Source File Name", "Sheet Name", "Cell Location", "Hyperlink", "Match Context"]
    for col, h in enumerate(headers):
        ws.write(0, col, h, header_format)
        
    ws.set_column(0, 0, 20)
    ws.set_column(1, 1, 30)
    ws.set_column(2, 2, 20)
    ws.set_column(3, 3, 15)
    ws.set_column(4, 4, 15)
    ws.set_column(5, 5, 70)
    
    row_idx = 1
    for res in results:
        keyword = res['keyword']
        file_path = res['filepath']
        sheet_name = res['sheet_name']
        cell_coord = res['cell']
        text = res['text']
        file_name = os.path.basename(file_path)
        
        ws.write(row_idx, 0, keyword)
        ws.write(row_idx, 1, file_name)
        ws.write(row_idx, 2, sheet_name)
        ws.write(row_idx, 3, cell_coord)
        
        # Hyperlink to external file
        # Format: external:Drive:/dir/file.xlsx#Sheet1!A1
        link_url = f"external:{file_path}#'{sheet_name}'!{cell_coord}"
        ws.write_url(row_idx, 4, link_url, string="JUMP", cell_format=link_format)
        
        kw_formats = [
            workbook.add_format({'font_color': 'red', 'bold': True}),
            workbook.add_format({'font_color': 'blue', 'bold': True}),
            workbook.add_format({'font_color': 'green', 'bold': True}),
            workbook.add_format({'font_color': 'purple', 'bold': True}),
            workbook.add_format({'font_color': '#FF8C00', 'bold': True}), # Dark orange
            workbook.add_format({'font_color': '#FF00FF', 'bold': True})  # Magenta
        ]

        # Extract all occurrences of each matched keyword
        matched_kws = res.get('keywords', [keyword])
        kw_format_map = {}
        for i, kw in enumerate(matched_kws):
            kw_format_map[kw.lower()] = kw_formats[i % len(kw_formats)]
            
        lower_text = text.lower()
        matches = []
        for kw in matched_kws:
            kw_lower = kw.lower()
            start_idx = 0
            while True:
                idx = lower_text.find(kw_lower, start_idx)
                if idx == -1:
                    break
                matches.append((idx, idx + len(kw), kw_lower))
                start_idx = idx + len(kw)
                
        # Sort matches by start index
        matches.sort(key=lambda x: x[0])
        
        # Filter overlapping matches (keep the first one that starts at a given index and spans further, or just keep non-overlapping)
        filtered_matches = []
        last_end = 0
        for start, end, kw_lower in matches:
            if start >= last_end:
                filtered_matches.append((start, end, kw_lower))
                last_end = end
                
        rich_text_elements = []
        current_idx = 0
        for start, end, kw_lower in filtered_matches:
            if start > current_idx:
                rich_text_elements.append(text[current_idx:start])
                
            actual_kw = text[start:end]
            rich_text_elements.append(kw_format_map[kw_lower])
            rich_text_elements.append(actual_kw)
            
            current_idx = end
            
        if current_idx < len(text):
            rich_text_elements.append(text[current_idx:])
            
        # write_rich_string requires at least 2 elements and at least one format object.
        if len(rich_text_elements) >= 2 and any(hasattr(el, 'font_color') for el in rich_text_elements):
            try:
                ws.write_rich_string(row_idx, 5, *rich_text_elements)
            except Exception:
                ws.write(row_idx, 5, text)
        else:
            ws.write(row_idx, 5, text)
            
        row_idx += 1
        
    # Create Summary sheet
    ws_summary = workbook.add_worksheet("Summary")
    ws_summary.write(0, 0, "Search Keyword", header_format)
    ws_summary.write(0, 1, "Count", header_format)
    ws_summary.set_column(0, 0, 30)
    ws_summary.set_column(1, 1, 15)
    
    keyword_counts = {}
    for res in results:
        kw = res['keyword']
        keyword_counts[kw] = keyword_counts.get(kw, 0) + 1
        
    for i, (kw, count) in enumerate(keyword_counts.items(), start=1):
        ws_summary.write(i, 0, kw)
        ws_summary.write(i, 1, count)
        
    workbook.close()
    return output_path
