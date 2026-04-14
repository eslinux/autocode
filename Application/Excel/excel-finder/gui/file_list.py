import tkinter as tk
from tkinter import ttk
import os

class FileListWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.files = []
        self.checkbox_vars = {}
        
        # UI Setup
        title_lbl = ttk.Label(self, text="Select Excel Files:", font=('Helvetica', 10, 'bold'))
        title_lbl.pack(anchor="w", padx=5, pady=(5, 0))
        
        # Tools frame: Select All / Deselect All
        tools_frame = ttk.Frame(self)
        tools_frame.pack(fill="x", padx=5, pady=2)
        ttk.Button(tools_frame, text="Select All", command=self.select_all).pack(side="left", padx=(0, 5))
        ttk.Button(tools_frame, text="Deselect All", command=self.deselect_all).pack(side="left")
        
        # Canvas and Scrollbar setup
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, bg="#ffffff")
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        self.inner_frame = tk.Frame(self.canvas, bg="#ffffff")
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=(5, 0), pady=5)
        self.scrollbar.pack(side="right", fill="y", padx=(0, 5), pady=5)
        
        # Mousewheel scroll bindings
        self.canvas.bind("<Enter>", self._bound_to_mousewheel)
        self.canvas.bind("<Leave>", self._unbound_to_mousewheel)

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def load_files(self, file_paths, base_folder=None):
        # Clear existing widgets
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
            
        self.files = file_paths
        self.checkbox_vars.clear()
        
        for idx, f in enumerate(self.files):
            var = tk.BooleanVar(value=True)
            self.checkbox_vars[f] = var
            if base_folder:
                filename = os.path.relpath(f, base_folder)
            else:
                filename = os.path.basename(f)
            
            cb = tk.Checkbutton(self.inner_frame, text=filename, variable=var, bg="#ffffff")
            # Using Tooltip or just appending the folder paths for clarity (assuming plain file name is enough for now)
            cb.pack(anchor="w", padx=2, pady=1)

    def select_all(self):
        for var in self.checkbox_vars.values():
            var.set(True)
            
    def deselect_all(self):
        for var in self.checkbox_vars.values():
            var.set(False)
            
    def get_selected_files(self):
        selected = []
        for f, var in self.checkbox_vars.items():
            if var.get():
                selected.append(f)
        return selected
