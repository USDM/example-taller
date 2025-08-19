"""
Objetivo: Extraer subtitulos de un video
Solo va a cambiar cuando la lógica de extracción de subtitulos cambie
"""
class SubtitleExtractor:
  
  """
  Objetivo: Extraer subtitulos de un video
  Solo va a cambiar cuando la lógica de extracción de subtitulos cambie
  """
  def extract_subtitles(self, video_url:str):
    video_id = self._get_youtube_video_id(video_url)
    subtitles = self.get_transcription_with_vtt(video_id, video_url)
    return subtitles


  def _get_youtube_video_id(self, video_url: str) -> str:
      import re
      match = re.search(r"v=([^&]+)", video_url)
      if match:
          return match.group(1)
      match = re.search(r"youtu\.be/([^?&/]+)", video_url)
      if match:
          return match.group(1)
      match=re.search(r"youtube\.com\/shorts\/([^?&/]+)", video_url)
      if match:
          return match.group(1)
      match=re.search(r"youtube\.com\/live\/([^?&/]+)", video_url)
      if match:
          return match.group(1)
      return None
  

  def get_transcription_with_vtt(self, video_id, video_url):
        import subprocess
        import os
        import webvtt

        lang = "en"

        output_dir = "subtitles"
        os.makedirs(output_dir, exist_ok=True)

        vtt_file = os.path.join(output_dir, f"{video_id}.{lang}.vtt")

        # Primero intenta obtener subtítulos oficiales
        command = [
            "yt-dlp",
            "--sub-lang", lang,
            "--write-sub",
            "--skip-download",
            "-o", f"{vtt_file}",
            video_url
        ]

        try:
            subprocess.run(command, check=True)
            final_vtt_file = f"{vtt_file}.{lang}.vtt"
            
            # Si no encuentra subtítulos oficiales, intenta con automáticos
            if not os.path.exists(final_vtt_file):
                command_auto = [
                    "yt-dlp",
                    "--sub-lang", lang,
                    "--write-auto-sub",
                    "--skip-download",
                    "-o", f"{vtt_file}",
                    video_url
                ]
                subprocess.run(command_auto, check=True)
        
        except subprocess.CalledProcessError:
            # Si falla con subtítulos oficiales, intenta con automáticos
            command_auto = [
                "yt-dlp",
                "--sub-lang", lang,
                "--write-auto-sub",
                "--skip-download",
                "-o", f"{vtt_file}",
                video_url
            ]
            subprocess.run(command_auto, check=True)

        video_id = video_url.split("v=")[-1]

        vtt_file = f"{vtt_file}.{lang}.vtt"
        
        if not os.path.exists(vtt_file):
            raise FileNotFoundError(f"No se encontró el archivo VTT: {vtt_file}")

        text = ""
        for caption in webvtt.read(vtt_file):
            text += f"{caption.start} - {caption.text}\n"

        print("@TEXT TEXT TEXT", text)

        os.remove(vtt_file)

        return text.strip()