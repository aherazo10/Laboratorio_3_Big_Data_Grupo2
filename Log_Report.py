logs = [
    "INFO Usuario conectado",
    "ERROR Base de datos",
    "INFO Archivo cargado",
    "WARNING Memoria alta",
    "INFO Sesion iniciada",
    "ERROR Fallo de red"
]

log_counts = {}

for line in logs:
    words = line.split()
    log_type = words[0]

    if log_type in log_counts:
        log_counts[log_type] += 1
    else:
        log_counts[log_type] = 1

print("Log Summary")
for log_type, count in log_counts.items():
    print(f"{log_type}: {count}")