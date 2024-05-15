from tabulate import tabulate

def printTabla(table=[],style="fancy_grid"):
    data_test = [
    ["Nombre", "Edad", "Género"],
    ["Juan", 25, "Masculino"],
    ["María", 30, "Femenino"],
    ["Carlos", 35, "Masculino"],
    ["Ana", 28, "Femenino"]
    ]
    # Imprimir tabla
    print(tabulate(table, headers="firstrow", tablefmt=style))