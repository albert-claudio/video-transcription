# Transcrição de Vídeos do YouTube em Português

Este script permite transcrever vídeos do YouTube diretamente para texto em português, sem a necessidade de baixar o áudio localmente. Ele utiliza as bibliotecas `yt-dlp` para baixar o áudio e `transformers` da Hugging Face para realizar a transcrição utilizando o modelo `openai/whisper-small`.

## Dependências

Antes de executar o script, você precisa instalar as dependências necessárias. Utilize os seguintes comandos para instalar os pacotes:

```bash
pip install yt-dlp
pip install transformers
pip install torch
```
- **`yt-dlp`: Biblioteca para download de vídeos e áudios do YouTube.**
- **`transformers`: Biblioteca da Hugging Face para utilizar modelos de NLP, incluindo modelos de reconhecimento de fala.**
- **`torch`: Framework para execução de modelos de aprendizado profundo.**

# Descrição da Função
A função principal do código é a transcribe_youtube_video_pt(youtube_url). Ela realiza os seguintes passos:

- **Baixa o áudio do vídeo: Utiliza a biblioteca `yt-dlp` para extrair o áudio do vídeo a partir da URL fornecida.**
- **Converte o áudio para o formato `wav`: O áudio é extraído e convertido usando o `FFmpeg` para garantir a compatibilidade com o modelo de transcrição.**
- **Transcreve o áudio: O áudio convertido é passado para o modelo de reconhecimento de fala `openai/whisper-small`, disponível na Hugging Face, para gerar a transcrição.**
- **Retorna o texto transcrito: O texto transcrito é retornado em português, pronto para ser utilizado.**

# Como Funciona
Este script funciona da seguinte maneira:

- **Extração do áudio: O `yt-dlp` é configurado para baixar o áudio do vídeo diretamente, sem salvar o arquivo no disco, e o áudio é convertido para o formato `wav` usando `FFmpeg`.**
- **Reconhecimento de Fala (ASR): O pipeline de transcrição é criado utilizando o modelo `openai/whisper-small` da Hugging Face, que é especializado no reconhecimento de fala para diferentes idiomas, incluindo o português.**
- **Resultado: O texto transcrito é retornado e pode ser utilizado conforme necessário.**

# Licença
Este código está disponível para uso pessoal e acadêmico, sem garantias de funcionamento em todas as situações. Caso queira modificar ou distribuir o código, consulte a licença do repositório original de `yt-dlp` e da `Hugging Face` para mais detalhes.


