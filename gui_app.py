import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CodeFortressGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Code Fortress: Visual Vulnerability & Secret Auditor')
        self.root.geometry('1000x700')
        self.root.configure(bg='#2C2F33')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2C2F33')
        self.style.configure('TButton', background='#7289DA', foreground='white')
        self.style.configure('TLabel', background='#2C2F33', foreground='white')

        self.create_widgets()

    def create_widgets(self):
        # Top Frame
        top_frame = ttk.Frame(self.root, padding='10')
        top_frame.pack(fill=tk.X)

        self.scan_button = ttk.Button(top_frame, text='Scan Codebase', command=self.start_scan)
        self.scan_button.pack(side=tk.LEFT, padx=5)

        self.status_label = ttk.Label(top_frame, text='Ready', font=('Arial', 10))
        self.status_label.pack(side=tk.LEFT, padx=10)

        # Middle Frame
        middle_frame = ttk.Frame(self.root)
        middle_frame.pack(fill=tk.BOTH, expand=True)

        self.code_viewer = tk.Text(middle_frame, bg='#23272A', fg='white', insertbackground='white')
        self.code_viewer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.findings_table = ttk.Treeview(middle_frame, columns=('Type', 'Severity', 'Location'), show='headings')
        self.findings_table.heading('Type', text='Type')
        self.findings_table.heading('Severity', text='Severity')
        self.findings_table.heading('Location', text='Location')
        self.findings_table.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Bottom Frame
        bottom_frame = ttk.Frame(self.root, padding='10')
        bottom_frame.pack(fill=tk.X)

        self.figure = plt.Figure(figsize=(5, 3), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, bottom_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def start_scan(self):
        self.status_label.config(text='Scanning...')
        self.scan_button.config(state=tk.DISABLED)
        threading.Thread(target=self.perform_scan).start()

    def perform_scan(self):
        directory = filedialog.askdirectory()
        if not directory:
            self.status_label.config(text='Ready')
            self.scan_button.config(state=tk.NORMAL)
            return

        # Simulate scan process
        findings = [
            {'type': 'Hardcoded Secret', 'severity': 'High', 'location': 'main.py:23'},
            {'type': 'Misconfiguration', 'severity': 'Medium', 'location': 'config.json:10'},
            {'type': 'Vulnerability', 'severity': 'Critical', 'location': 'utils.py:45'}
        ]

        # Update GUI
        self.root.after(0, self.update_ui, findings)

    def update_ui(self, findings):
        self.code_viewer.delete(1.0, tk.END)
        self.code_viewer.insert(tk.END, 'Simulated code content...')

        self.findings_table.delete(*self.findings_table.get_children())
        for finding in findings:
            self.findings_table.insert('', tk.END, values=(finding['type'], finding['severity'], finding['location']))

        # Update chart
        self.plot.clear()
        severity_counts = {'Critical': 0, 'High': 0, 'Medium': 0, 'Low': 0}
        for finding in findings:
            severity_counts[finding['severity']] += 1
        self.plot.bar(severity_counts.keys(), severity_counts.values(), color=['#FF0000', '#FF8000', '#FFFF00', '#00FF00'])
        self.canvas.draw()

        self.status_label.config(text='Scan Complete')
        self.scan_button.config(state=tk.NORMAL)

if __name__ == '__main__':
    root = tk.Tk()
    app = CodeFortressGUI(root)
    root.mainloop()