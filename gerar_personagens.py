"""
Mundo da Lili - Gerador de Imagens dos Personagens (Ideogram)
"""

import os
import requests

API_KEY = os.environ.get("IDEOGRAM_API_KEY")

if not API_KEY:
    raise SystemExit(
        "Erro: variável de ambiente IDEOGRAM_API_KEY não encontrada.\n"
        "Defina-a antes de rodar o script."
    )

OUTPUT_DIR = "output_imagens"

PERSONAGENS = {
    "lili": (
        "flat 2D children's book illustration, cute baby rabbit girl character, "
        "big round head, simple round body, soft white fur, big brown eyes, "
        "pink bow on ear, pink t-shirt, yellow overalls, pink heart pocket, "
        "pink and white sneakers, cheerful pose, clean bold outlines, "
        "flat vibrant colors, no shading, character sheet style, "
        "transparent background, front facing, full body"
    ),
    "bento": (
        "flat 2D children's book illustration, cute baby bear boy character, "
        "big round head, simple round body, light brown fur, big round eyes, "
        "blue t-shirt, green shorts, colorful sneakers, goofy friendly pose, "
        "clean bold outlines, flat vibrant colors, no shading, "
        "character sheet style, transparent background, front facing, full body"
    ),
    "nina": (
        "flat 2D children's book illustration, cute baby kitten girl character, "
        "big round head, simple round body, light gray or cream fur, calm big eyes, "
        "whiskers, purple and white outfit, gentle thoughtful pose, "
        "clean bold outlines, flat vibrant colors, no shading, "
        "character sheet style, transparent background, front facing, full body"
    ),
    "pipoca": (
        "flat 2D children's book illustration, tiny baby chick character, "
        "extra big round head, small round body, fluffy yellow feathers, "
        "huge round eyes, tiny orange beak, tiny orange feet, excited pose, "
        "clean bold outlines, flat vibrant colors, no shading, "
        "character sheet style, transparent background, front facing, full body"
    ),
}


def gerar_imagem(prompt, caminho_saida):
    url = "https://api.ideogram.ai/generate"
    headers = {"Api-Key": API_KEY, "Content-Type": "application/json"}
    payload = {
        "image_request": {
            "prompt": prompt,
            "aspect_ratio": "ASPECT_1_1",
            "model": "V_2",
            "magic_prompt_option": "AUTO",
        }
    }
    response = requests.post(url, headers=headers, json=payload, timeout=120)
    if response.status_code != 200:
        raise RuntimeError(f"Erro na API Ideogram ({response.status_code}): {response.text}")
    data = response.json()
    image_url = data["data"][0]["url"]
    img_response = requests.get(image_url, timeout=120)
    img_response.raise_for_status()
    with open(caminho_saida, "wb") as f:
        f.write(img_response.content)
    print(f"Gerado: {caminho_saida}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for nome, prompt in PERSONAGENS.items():
        caminho = os.path.join(OUTPUT_DIR, f"{nome}.png")
        gerar_imagem(prompt, caminho)
    print("\nConcluído! As imagens estão na pasta:", OUTPUT_DIR)


if __name__ == "__main__":
    main()