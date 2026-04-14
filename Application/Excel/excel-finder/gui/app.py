import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import traceback
import os

from .file_list import FileListWidget
from .search_panel import SearchPanelWidget
from core import get_excel_files, search_in_workbook, export_results

class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Excel Text Finder")
        self.geometry("800x600")
        self.minsize(600, 400)
        
        # Configure grid weights
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        # Setup Panel
        self.search_panel = SearchPanelWidget(
            self, 
            on_load_folder=self.action_load_folder,
            on_search=self.action_search
        )
        self.search_panel.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        # File List Panel
        self.file_list = FileListWidget(self)
        self.file_list.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        
        self.current_folder = None
        
    def action_load_folder(self):
        folder_selected = filedialog.askdirectory(title="Select Folder with Excel Files")
        if folder_selected:
            self.current_folder = folder_selected
            self.search_panel.set_folder(folder_selected)
            self.search_panel.set_status("Scanning folder...")
            self.update_idletasks()
            
            # Use background thread for scanning to prevent UI freeze on huge directories
            threading.Thread(target=self._scan_folder_task, args=(folder_selected,), daemon=True).start()
            
    def _scan_folder_task(self, folder):
        try:
            files = get_excel_files(folder)
            
            # Safe GUI update
            self.after(0, self._on_scan_complete, files)
        except Exception as e:
            self.after(0, self._on_error, "Error scanning folder", str(e))
            
    def _on_scan_complete(self, files):
        self.file_list.load_files(files, base_folder=self.current_folder)
        if files:
            self.search_panel.set_status(f"Loaded {len(files)} Excel files.")
            self.search_panel.enable_search(True)
        else:
            self.search_panel.set_status("No .xlsx files found in selected folder.")
            self.search_panel.enable_search(False)
            
    def _on_error(self, title, message):
        messagebox.showerror(title, message)
        self.search_panel.set_status("Error occurred.")
        
    def action_search(self):
        options = self.search_panel.get_options()
        selected_files = self.file_list.get_selected_files()
        
        if not selected_files:
            messagebox.showinfo("Info", "No files selected for searching.")
            return
            
        # Disable UI components
        self.search_panel.enable_search(False)
        
        # Start search in background
        threading.Thread(
            target=self._search_task, 
            args=(selected_files, options, self.current_folder), 
            daemon=True
        ).start()
        
    def _search_task(self, files, options, export_folder):
        all_results = []
        try:
            for i, f in enumerate(files):
                # Update status
                self.after(0, lambda file=f, idx=i, total=len(files): self.search_panel.set_status(f"Searching {idx+1}/{total}: {os.path.basename(file)}"))
                
                res = search_in_workbook(
                    f, 
                    options['keyword'], 
                    options['match_exact'],
                    options.get('search_cols', ''),
                    options.get('search_rows', ''),
                    options.get('search_sheets', '')
                )
                all_results.extend(res)
                
            if all_results:
                self.after(0, lambda: self.search_panel.set_status(f"Search complete. Exporting {len(all_results)} results..."))
                
                # Export results
                output_path = export_results(all_results, export_folder)
                self.after(0, self._on_search_success, output_path, len(all_results))
            else:
                self.after(0, self._on_search_no_results)
                
        except Exception as e:
            traceback.print_exc()
            self.after(0, self._on_error, "Search Error", f"An error occurred during search/export:\n{e}")
            
    def _on_search_success(self, output_path, total_results):
        self.search_panel.set_status(f"Exported! Found {total_results} instances.")
        self.search_panel.enable_search(True)
        messagebox.showinfo("Export Successful", f"Found {total_results} results.\nExported to:\n{output_path}")

    def _on_search_no_results(self):
        self.search_panel.set_status("No results found.")
        self.search_panel.enable_search(True)
        messagebox.showinfo("No Results", "No matches were found for the given keyword in the selected files.")
