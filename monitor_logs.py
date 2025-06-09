import csv
import time
import os
from datetime import datetime

LOG_FILE = "/var/log/auth.log"
CSV_OUTPUT = "eventos_seguranca.csv"
EVENTOS_INTERESSANTES = ["Failed password", "authentication failure", "sudo", "su:"]

def analisar_logs():
    eventos = []
    with open(LOG_FILE, "r") as f:
        linhas = f.readlines()
        for linha in linhas:
            if any(evento in linha for evento in EVENTOS_INTERESSANTES):
                eventos.append([datetime.now(), linha.strip()])
    return eventos

def salvar_csv(eventos):
    existe = os.path.exists(CSV_OUTPUT)
    with open(CSV_OUTPUT, "a", newline="") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["DataHora", "Log"])
        writer.writerows(eventos)

if __name__ == "__main__":
    eventos = analisar_logs()
    if eventos:
        salvar_csv(eventos)
        print(f"{len(eventos)} eventos registrados.")
    else:
        print("Nenhum evento relevante encontrado.")
