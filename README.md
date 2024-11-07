# Transcrição de Video
Este projeto em Python permite transcrever automaticamente o áudio de vídeos a partir de uma URL fornecida pelo usuário. O sistema baixa o vídeo, extrai o áudio e utiliza uma ferramenta de reconhecimento de fala para gerar a transcrição do conteúdo.

#Funcionalidades
- **O usuário fornece uma URL de vídeo do YouTube.**
- **O áudio do vídeo é extraído diretamente da URL sem necessidade de download local.**
- **O áudio extraído é transcrito em texto utilizando o modelo Whisper otimizado para português.**
- **A transcrição do vídeo é exibida no console.**

# Pré-requisitos
Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:
- **Python 3.x (recomendado 3.7 ou superior)**
- **pip para instalar pacotes**
  
As bibliotecas necessárias são:

- **yt-dlp: Para baixar o áudio do vídeo do YouTube.**
- **transformers: Para usar o pipeline de transcrição automática.**
- **torch: Para a execução do modelo de transcrição.**
- **Para instalar as dependências, basta executar o comando abaixo:**
  Para instalar as dependências, basta executar o comando abaixo:
 


