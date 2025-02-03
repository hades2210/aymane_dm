import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

CLIENTS_CSV = "Clients.csv"
DEVIS_CSV = "Devis.csv"

def load_data():
    try:
        data_dir = Path(__file__).parent
        clients_path = data_dir / CLIENTS_CSV
        devis_path = data_dir / DEVIS_CSV

        clients_df = pd.read_csv(clients_path, encoding='latin1', sep=';')
        devis_df = pd.read_csv(devis_path, encoding='latin1', sep=';')

        print("Available columns in clients_df:", clients_df.columns.tolist()) # Debugging
        print("Available columns in devis_df:", devis_df.columns.tolist()) # Debugging
        return clients_df, devis_df

    except FileNotFoundError as e:
        messagebox.showerror("Error", f"Could not find CSV file - {e}\nLooking in: {data_dir}")
        return None, None
    except UnicodeDecodeError as e:
        messagebox.showerror("Error", f"Encoding issue with CSV file - {e}")
        return None, None
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")
        return None, None

def reporting_devis_par_intervalle(parent_frame):
    _, devis_df = load_data()
    if devis_df is None:
        return

    try:
        # Assuming 'MONTANT_TOTAL' is the column name for total amount in Devis.csv
        if 'MONTANT_TOTAL' not in devis_df.columns:
            messagebox.showerror("Error", "Column 'MONTANT_TOTAL' not found in Devis.csv")
            return

        bins = [0, 1000, 5000, 10000, float('inf')]
        labels = ["0-1000€", "1000-5000€", "5000-10000€", ">10000€"]

        devis_df['Intervalle_Montant'] = pd.cut(devis_df['MONTANT_TOTAL'], bins=bins, labels=labels, right=True, include_lowest=True)
        interval_counts = devis_df['Intervalle_Montant'].value_counts().sort_index()

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(interval_counts.index.astype(str), interval_counts.values, color='skyblue')
        ax.set_title("Nombre de Devis par Intervalle de Montant Total")
        ax.set_xlabel("Intervalles de Montant")
        ax.set_ylabel("Nombre de Devis")

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='bottom', fontweight='bold')

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Error generating Devis report: {e}")

def reporting_clients_par_departement(parent_frame):
    clients_df, _ = load_data()
    if clients_df is None:
        return

    try:
        if 'CODE_POSTAL' not in clients_df.columns:
            messagebox.showerror("Error", "Column 'CODE_POSTAL' not found in Clients.csv")
            return

        clients_df['CODE_POSTAL'] = clients_df['CODE_POSTAL'].astype(str)
        clients_df['Departement'] = clients_df['CODE_POSTAL'].str[:2]
        departement_count = clients_df['Departement'].value_counts().to_dict()

        keys_sorted = sorted(departement_count.keys())
        values_sorted = [departement_count[k] for k in keys_sorted]

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(keys_sorted, values_sorted, color='green')
        ax.set_title("Nombre de Clients par Département")
        ax.set_xlabel("Départements")
        ax.set_ylabel("Nombre de Clients")

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, str(int(yval)), ha='center', va='bottom', fontweight='bold')

        plt.xticks(rotation=45)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Error generating Clients report: {e}")

class ReportingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application de Reporting")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        self.devis_tab = ttk.Frame(self.notebook)
        self.clients_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.devis_tab, text="Reporting Devis")
        self.notebook.add(self.clients_tab, text="Reporting Clients")

        self.create_devis_tab_ui()
        self.create_clients_tab_ui()

    def create_devis_tab_ui(self):
        devis_button = ttk.Button(self.devis_tab, text="Afficher Rapport Devis", command=self.show_devis_report)
        devis_button.pack(pady=10)
        self.devis_report_frame = tk.Frame(self.devis_tab) # Frame to hold the plot, allows to clear previous plots
        self.devis_report_frame.pack(pady=10, expand=True, fill="both")

    def create_clients_tab_ui(self):
        clients_button = ttk.Button(self.clients_tab, text="Afficher Rapport Clients", command=self.show_clients_report)
        clients_button.pack(pady=10)
        self.clients_report_frame = tk.Frame(self.clients_tab) # Frame to hold the plot, allows to clear previous plots
        self.clients_report_frame.pack(pady=10, expand=True, fill="both")

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def show_devis_report(self):
        self.clear_frame(self.devis_report_frame)
        reporting_devis_par_intervalle(self.devis_report_frame)

    def show_clients_report(self):
        self.clear_frame(self.clients_report_frame)
        reporting_clients_par_departement(self.clients_report_frame)


if __name__ == "__main__":
    app = ReportingApp()
    app.mainloop()