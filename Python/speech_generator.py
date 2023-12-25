from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Hogy milyen erőre képes egy-két elejtett, konkrétumot csak részben tartalmazó mondat, azt nagyon jól megtanultuk idén. Míg tavaly a hitelességéért küzdött a Fed, az amerikai jegybank üzeneteit idén valósággal itta a piac. Sőt, talán kissé túl nagy kortyokkal itta: sejtelmes, kétértelmű utalások is olyan hullámokat vertek a piacokon, amelyeket még idehaza is komolyan megéreztünk."
)

response.stream_to_file('c://Alpar/out.mp3')