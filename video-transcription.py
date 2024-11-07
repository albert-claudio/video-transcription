from yt_dlp import YoutubeDL
from transformers import pipeline

def transcribe_youtube_video_pt(youtube_url):
    """
    Transcribes a YouTube video into Portuguese text without saving the audio locally.

    Args:
        youtube_url: The URL of the YouTube video.

    Returns:
        The transcribed text in Portuguese.
    """
    try:
        # Configurações para baixar o áudio como um stream temporário
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '-',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'quiet': True,
        }

        # Criar pipeline de ASR usando um modelo otimizado para velocidade
        asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-small")

        # Baixar e transcrever o áudio diretamente
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            audio_url = info['url']
            transcription = asr_pipeline(audio_url)

        return transcription['text']

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Exemplo de uso
youtube_url = input("Enter URL here: ")  # Insira o URL do vídeo

transcription = transcribe_youtube_video_pt(youtube_url)

if transcription:
    print("Transcrição (Português):")
    print(transcription)
