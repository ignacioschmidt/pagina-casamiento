#!/usr/bin/env python3
"""
Genera imágenes watercolor botánicas para la página de casamiento
usando la API de Replicate + FLUX.
"""

import os
import sys
import time
import requests

try:
    import replicate
except ImportError:
    print("Instalando replicate...")
    os.system(f"{sys.executable} -m pip install replicate requests")
    import replicate

API_TOKEN = os.environ.get("REPLICATE_API_TOKEN", "")
client = replicate.Client(api_token=API_TOKEN)

IMAGENES = [
    {
        "archivo": "botanical-hero-top.png",
        "prompt": (
            "watercolor botanical illustration, corner bouquet of garden roses and eucalyptus branches, "
            "soft dusty pink and sage green, cream white background, elegant wedding stationery style, "
            "loose brushstrokes, fine art, no text"
        ),
        "aspect_ratio": "1:1",
    },
    {
        "archivo": "botanical-hero-bottom.png",
        "prompt": (
            "watercolor floral garland, horizontal arrangement of peonies wildflowers and leaves, "
            "soft blush pink cream and sage green, white background, wedding invitation style, "
            "wide composition, delicate brushstrokes, no text"
        ),
        "aspect_ratio": "16:9",
    },
    {
        "archivo": "botanical-info.png",
        "prompt": (
            "watercolor botanical branch with small roses and eucalyptus leaves, "
            "dusty rose and muted green, white background, loose watercolor style, "
            "wedding decoration illustration, no text"
        ),
        "aspect_ratio": "3:4",
    },
    {
        "archivo": "botanical-regalo.png",
        "prompt": (
            "watercolor flower arrangement, garden roses peonies and greenery, "
            "romantic soft pastel colors, cream background, elegant wedding illustration, "
            "centered composition, fine art watercolor, no text"
        ),
        "aspect_ratio": "1:1",
    },
    {
        "archivo": "botanical-footer.png",
        "prompt": (
            "watercolor floral border strip, wildflowers eucalyptus and delicate leaves, "
            "very wide horizontal composition, soft muted pastel colors, white background, "
            "wedding stationery style, seamless border, no text"
        ),
        "aspect_ratio": "21:9",
    },
]

def descargar(url, destino):
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    with open(destino, "wb") as f:
        f.write(resp.content)

def main():
    os.makedirs("img", exist_ok=True)

    for i, img in enumerate(IMAGENES, 1):
        destino = os.path.join("img", img["archivo"])
        if os.path.exists(destino):
            print(f"[{i}/{len(IMAGENES)}] Ya existe {img['archivo']}, saltando.")
            continue
        print(f"[{i}/{len(IMAGENES)}] Generando {img['archivo']}...")

        for intento in range(5):
            try:
                output = client.run(
                    "black-forest-labs/flux-schnell",
                    input={
                        "prompt": img["prompt"],
                        "num_outputs": 1,
                        "aspect_ratio": img["aspect_ratio"],
                        "output_format": "png",
                        "output_quality": 95,
                        "go_fast": True,
                    },
                )

                url = output[0] if isinstance(output, list) else str(output)
                descargar(url, destino)
                print(f"    Guardado en {destino}")
                break

            except Exception as e:
                if "429" in str(e) and intento < 4:
                    espera = 15 * (intento + 1)
                    print(f"    Rate limit — esperando {espera}s...")
                    time.sleep(espera)
                else:
                    print(f"    ERROR: {e}")
                    break

        if i < len(IMAGENES):
            print(f"    (pausa 12s para no saturar la API...)")
            time.sleep(12)

    print("\nListo! Imágenes guardadas en img/")
    print("Ahora actualizá el index.html reemplazando los <img> botánicos con los nuevos archivos.")

if __name__ == "__main__":
    main()
