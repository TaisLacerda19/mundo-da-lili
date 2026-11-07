# Mundo da Lili

Scripts em Python que geram, com IA, os personagens e a narração de um desenho infantil sobre cores.

São quatro personagens: Lili (coelhinha), Bento (ursinho), Nina (gatinha) e Pipoca (pintinho). O roteiro em português tem cinco falas, em que a Lili ensina as cores e convida a criança a procurar um objeto vermelho em casa.

## O que cada script faz

| Script | API | Entrada | Saída |
| --- | --- | --- | --- |
| `gerar_personagens.py` | [Ideogram](https://ideogram.ai) | Um prompt de imagem por personagem, com o mesmo estilo visual | Imagens em `output_imagens/` |
| `gerar_narracao.py` | [ElevenLabs](https://elevenlabs.io) | Roteiro e uma voz para cada personagem | Áudios `.mp3` numerados em `output_audio/` |

## Como rodar

Requer Python 3.10 ou mais novo e uma chave de API de cada serviço. As chamadas às APIs podem consumir créditos da sua conta.

```bash
pip install -r requirements.txt
```

No PowerShell:

```powershell
$env:IDEOGRAM_API_KEY = "sua-chave"
$env:ELEVENLABS_API_KEY = "sua-chave"
python gerar_personagens.py
python gerar_narracao.py
```

As chaves ficam só em variáveis de ambiente, nunca no código. Se a chave não estiver definida, o script para com uma mensagem clara.

## Decisões do projeto

- **Prompts com o mesmo estilo:** todos repetem o estilo (ilustração 2D, contornos fortes, cores chapadas), para os personagens parecerem do mesmo desenho.
- **Roteiro como dados:** as falas ficam em uma lista, então dá para trocar o texto sem mexer na lógica.
- **Ordem nos arquivos:** os áudios saem numerados (`01_LILI.mp3`, `02_BENTO.mp3`), prontos para a edição.

## Estado atual

Este repositório guarda o código. As imagens e os áudios gerados não estão versionados, e a montagem do vídeo ainda não faz parte do projeto.
