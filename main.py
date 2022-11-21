import csv

from datos import alumnos, titulo


def csv_to_dict(file_path: str) -> dict:
    with open(file_path, mode='r', newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
         # Guardamos todas las filas del csv en una lista de diccionarios. Cada diccionario corresponde a un alumno.
        csv_rows = [row for row in reader]
        # Por cada campo (DNI, nota ...), recorremos cada fila (datos de un alumno), y cogemos el valor del campo del alumno.
        # así creamos un diccionario cuya clave sea "notas" y su valor una lista de todas las notas. 
        datos_por_columnas = {fieldname: [row.get(fieldname) for row in csv_rows] for fieldname in reader.fieldnames}
        return datos_por_columnas
    
        
def calcular_resumen_notas(datos_por_columnas: dict) -> dict:
    columna_notas = "Nota_parcial"
    notas = datos_por_columnas[columna_notas]
    # Todo se lee como un string, hay que convertirlo a float para poder operar
    notas = list([float(nota) for nota in notas])
    resumen_notas = {
        "nota_media": sum(notas) / len(notas),
        "nota_maxima": max(notas),
        "nota_minima": min(notas)
    }
    return resumen_notas


def resumen_to_txt(resumen_notas: dict, file_path: str) -> None:
    with open(file=file_path, mode='w', encoding='utf-8') as file:
        file.write("Resumen notas del parcial\n")
        for key, value in resumen_notas.items():
            file.write(f"{key}: {value}\n")       


if __name__ == "__main__":
    csv_file = "calificacionesV2.csv"
    txt_file = "resumen.txt"
    
    with open (csv_file, "w", newline="", encoding="utf-8") as file:
        
        headers = titulo.split(",") 
        writer = csv.writer(file, delimiter=",")
        writer.writerow(headers)
        writer.writerows(alumnos)
        
    datos_por_columnas = csv_to_dict(csv_file)
    resumen_notas = calcular_resumen_notas(datos_por_columnas)
    resumen_to_txt(resumen_notas, txt_file)
    