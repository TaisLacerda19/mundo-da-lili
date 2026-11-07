"""
Mundo da Lili - Gerador de Narração (ElevenLabs)
"""

import os
import requests

API_KEY = os.environ.get("ELEVENLABS_API_KEY")

if not API_KEY:
    raise SystemExit(
        "Erro: variável de ambiente ELEVENLABS_API_KEY não encontrada.\n"
        "Defina-a antes de rodar o script."
    )

VOICES = {
    "LILI": "XJ2fW4ybq7HouelYYGcL",
    "BENTO": "bA58y3FqVI6b6gTNh0oT",
    "NINA": "MkTSSXNgnBULS6ek4pon",
    "PIPOCA": "XjGYkUkzth8BPs29fmcV",
}

OUTPUT_DIR = "output_audio"

ROTEIRO = [
    {"personagem": "LILI", "fala": "Oi, amiguinhos! Eu sou a Lili! Hoje eu vou brincar de encontrar cores com o Bento! Vamos?"},
    {"personagem": "BENTO", "fala": "Lili, olha essa bola! Ela é... azul!"},
    {"personagem": "LILI", "fala": "Hmm, será mesmo? Vamos olhar de perto! Essa bola é vermelha, Bento!"},
    {"personagem": "BENTO", "fala": "Ohh, é verdade! Ela é bem vermelha!"},
    {"personagem": "LILI", "fala": "Amiguinho, você consegue encontrar algo vermelho aí na sua casa? Olha em volta!"},
]


def gerar_audio(texto, voice_id, caminho_saida):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
    payload = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }
    response = requests.post(url, headers=headers, json=payload, timeout=120)
    if response.status_code != 200:
        raise RuntimeError(f"Erro na API ElevenLabs ({response.status_code}): {response.text}")
    with open(caminho_saida, "wb") as f:
        f.write(response.content)
    print(f"Gerado: {caminho_saida}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i, linha in enumerate(ROTEIRO, start=1):
        personagem = linha["personagem"]
        fala = linha["fala"]
        voice_id = VOICES.get(personagem)
        if not voice_id or voice_id.startswith("COLE_AQUI"):
            print(f"Pulei a fala {i} ({personagem}): defina o voice_id desse personagem em VOICES.")
            continue
        nome_arquivo = f"{i:02d}_{personagem}.mp3"
        caminho = os.path.join(OUTPUT_DIR, nome_arquivo)
        gerar_audio(fala, voice_id, caminho)
    print("\nConcluído! Os áudios estão na pasta:", OUTPUT_DIR)


if __name__ == "__main__":
    main()