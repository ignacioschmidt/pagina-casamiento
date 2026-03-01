#!/usr/bin/env python3
"""
Genera un ícono de regalo estilo line-art elegante para la sección Regalos.
Usa FLUX para generar + remove-bg para fondo transparente.
"""

import os
import sys
import requests

try:
    import replicate
except ImportError:
    os.system(f"{sys.executable} -m pip install replicate requests")
    import replicate

API_TOKEN = os.environ.get("REPLICATE_API_TOKEN", "")
client = replicate.Client(api_token=API_TOKEN)

PROMPT = (
    "minimalist elegant hand-drawn gift box icon, fine line art illustration, "
    "single delicate wrapped present with a ribbon bow on top, "
    "thin strokes in muted sage green color #7d9b82, "
    "simple and refined, wedding stationery style, "
    "centered on pure white background, no shadow, no text, no other objects, "
    "clean vector-like illustration, high contrast on white"
)

DESTINO = os.path.join("img", "icon-regalo.png")


def descargar(url, destino):
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    with open(destino, "wb") as f:
        f.write(resp.content)


def main():
    import time
    os.makedirs("img", exist_ok=True)

    tmp_file = os.path.join("img", "_tmp_regalo.png")

    # Paso 1: Generar el ícono con FLUX (skip si ya existe el temporal)
    if not os.path.exists(tmp_file):
        print("Generando ícono de regalo con FLUX...")
        output = client.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": PROMPT,
                "num_outputs": 1,
                "aspect_ratio": "1:1",
                "output_format": "png",
                "output_quality": 95,
                "go_fast": True,
            },
        )

        url_original = output[0] if isinstance(output, list) else str(output)
        descargar(url_original, tmp_file)
        print(f"  Imagen base guardada en {tmp_file}")
    else:
        print(f"  Imagen base ya existe en {tmp_file}, saltando generación.")

    # Esperar un poco para evitar rate limit entre las dos llamadas
    print("  Esperando 20s para evitar rate limit...")
    time.sleep(20)

    # Paso 2: Quitar fondo con bria/remove-background (con retry por rate limit)
    for intento in range(5):
        try:
            print(f"Quitando fondo (intento {intento + 1})...")
            with open(tmp_file, "rb") as f:
                output_bg = client.run(
                    "bria-ai/rmbg-2.0",
                    input={"image": f},
                )
            url_nobg = str(output_bg)
            descargar(url_nobg, DESTINO)
            print(f"  Ícono sin fondo guardado en {DESTINO}")
            break
        except Exception as e:
            if "429" in str(e) and intento < 4:
                espera = 20 * (intento + 1)
                print(f"  Rate limit — esperando {espera}s...")
                time.sleep(espera)
            else:
                raise

    # Limpiar temporal
    os.remove(tmp_file)
    print("\nListo!")


if __name__ == "__main__":
    main()
