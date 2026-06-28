# pip install gTTS

'''
Converts text into high-quality speech
Supports more than 30 languages
Automatically generates MP3 audio files
Simple and clean command-line interface
Built using Python and Google Text-to-Speech (gTTS)
'''
from gtts import gTTS
import datetime
import time
language_dist = {
    "afrikaans": "af",
    "arabic": "ar",
    "bengali": "bn",
    "chinese": "zh-CN",
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "english": "en",
    "finnish": "fi",
    "french": "fr",
    "german": "de",
    "greek": "el",
    "gujarati": "gu",
    "hindi": "hi",
    "hungarian": "hu",
    "indonesian": "id",
    "italian": "it",
    "japanese": "ja",
    "kannada": "kn",
    "korean": "ko",
    "malayalam": "ml",
    "marathi": "mr",
    "nepali": "ne",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "russian": "ru",
    "spanish": "es",
    "swahili": "sw",
    "tamil": "ta",
    "telugu": "te",
    "thai": "th",
    "turkish": "tr",
    "urdu": "ur",
    "vietnamese": "vi"
}
current_datetime = datetime.datetime.now()
d_t = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

def tts(text, language='en'):
    try:
        # Create the TTS object
        tts = gTTS(text=text, lang=language)
        
        # Save the speech to an audio file
        tts.save(f"Output {d_t}.mp3")
        print("File is Saved.")
        time.sleep(5)
        
    except Exception as e:
        print(f"Error: {e}")

lanG = input("Language : ")
txt = input("Text : ")
lang_filter = language_dist[lanG]
tts(txt, lang_filter)
