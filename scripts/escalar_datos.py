import json
import shutil
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
FACTOR = 10
MAX_ENTERO_SEGURO = 2**53 - 1


def preparar_sitio():
    origen = RAIZ / "datos.json"
    datos = json.loads(origen.read_text(encoding="utf-8"))

    for indice, registro in enumerate(datos["registros"], start=1):
        for campo in ("recibidas", "resueltas"):
            valor = registro[campo]
            if type(valor) is not int or not 0 <= valor <= MAX_ENTERO_SEGURO // FACTOR:
                raise ValueError(f"Registro {indice}, {campo}: conteo fuera del rango válido")
            registro[campo] = valor * FACTOR

    destino = RAIZ / "_site"
    destino.mkdir(exist_ok=True)
    shutil.copyfile(RAIZ / "index.html", destino / "index.html")
    (destino / "datos.json").write_text(
        json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    preparar_sitio()
