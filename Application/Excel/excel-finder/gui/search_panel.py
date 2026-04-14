import tkinter as tk
from tkinter import ttk

class SearchPanelWidget(ttk.Frame):
    def __init__(self, parent, on_load_folder, on_search):
        super().__init__(parent)
        
        self.on_load_folder = on_load_folder
        self.on_search = on_search
        
        # Folder Selection
        folder_frame = ttk.Frame(self)
        folder_frame.pack(fill="x", pady=5)
        
        ttk.Label(folder_frame, text="Folder:").pack(side="left")
        self.folder_value = tk.StringVar()
        self.folder_entry = ttk.Entry(folder_frame, textvariable=self.folder_value, state="readonly")
        self.folder_entry.pack(side="left", fill="x", expand=True, padx=5)
        
        ttk.Button(folder_frame, text="Browse and Load Files", command=self.on_load_folder_clicked).pack(side="right")
        
        # Search Term Input
        search_frame = ttk.Frame(self)
        search_frame.pack(fill="x", pady=(15, 5))
        
        ttk.Label(search_frame, text="Search Keyword (e.g. kw1|kw2):").pack(side="left")
        self.keyword_value = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.keyword_value).pack(side="left", fill="x", expand=True, padx=5)
        
        # Search Options Frame
        options_frame = ttk.LabelFrame(self, text="Search Options")
        options_frame.pack(fill="x", pady=5, padx=5)
        
        # Option: Match entire cell contents
        self.match_exact_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(options_frame, text="Match entire cell content (Khớp toàn bộ)", variable=self.match_exact_var).pack(anchor="w", padx=5, pady=2)
        
        # Search Columns
        col_frame = ttk.Frame(options_frame)
        col_frame.pack(fill="x", padx=5, pady=2)
        ttk.Label(col_frame, text="Search Columns (e.g. A|B|C):", width=25).pack(side="left")
        self.search_cols_var = tk.StringVar()
        ttk.Entry(col_frame, textvariable=self.search_cols_var).pack(side="left", fill="x", expand=True)

        # Search Rows
        row_frame = ttk.Frame(options_frame)
        row_frame.pack(fill="x", padx=5, pady=2)
        ttk.Label(row_frame, text="Search Rows (e.g. 1|2|3):", width=25).pack(side="left")
        self.search_rows_var = tk.StringVar()
        ttk.Entry(row_frame, textvariable=self.search_rows_var).pack(side="left", fill="x", expand=True)

        # Search Sheets
        sheet_frame = ttk.Frame(options_frame)
        sheet_frame.pack(fill="x", padx=5, pady=2)
        ttk.Label(sheet_frame, text="Search Sheets (e.g. Sheet1|Sheet2):", width=25).pack(side="left")
        self.search_sheets_var = tk.StringVar()
        ttk.Entry(sheet_frame, textvariable=self.search_sheets_var).pack(side="left", fill="x", expand=True)
        
        # Action Buttons
        action_frame = ttk.Frame(self)
        action_frame.pack(fill="x", pady=(15, 5))
        
        self.search_btn = ttk.Button(action_frame, text="Search and Export", command=self.on_search_clicked, state="disabled")
        self.search_btn.pack(side="right")
        
        self.status_var = tk.StringVar(value="Ready to load folder.")
        ttk.Label(action_frame, textvariable=self.status_var, font=('Helvetica', 9, 'italic')).pack(side="left")

    def on_load_folder_clicked(self):
        self.on_load_folder()
        
    def on_search_clicked(self):
        if not self.keyword_value.get().strip():
            tk.messagebox.showwarning("Warning", "Please enter a search keyword.")
            return
        self.on_search()
        
    def set_folder(self, folder_path):
        self.folder_value.set(folder_path)
        
    def set_status(self, text):
        self.status_var.set(text)
        
    def enable_search(self, enable=True):
        if enable:
            self.search_btn.config(state="normal")
        else:
            self.search_btn.config(state="disabled")
            
    def get_options(self):
        return {
            "keyword": self.keyword_value.get(),
            "match_exact": self.match_exact_var.get(),
            "search_cols": self.search_cols_var.get(),
            "search_rows": self.search_rows_var.get(),
            "search_sheets": self.search_sheets_var.get()
        }
