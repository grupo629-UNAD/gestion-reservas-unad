import datetime

def log_error(message):
    """
    Esta función registra los errores en un archivo de texto.
    """

    # Obtener fecha y hora actual
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Abrir archivo en modo "a" (append)
        with open("utils/system_logs.txt", "a") as file:
            file.write(f"[{timestamp}] ERROR DETECTED: {message}\n")

    except Exception as e:
        print(f"CRITICAL: Could not write to log file. Details: {e}")