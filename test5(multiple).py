import pandas as pd
from gtts import gTTS
from pydub import AudioSegment
import sys
import os



sr_target = 16000
append_silence_Length_ms = 1000
# Set path and language
input_file = r"C:\Users\70P8182\Downloads\GGTTS_mp3\GGT_mp3\Inputaudio.csv"  # Path to the input CSV file
lang = "th"  # Default language
file_format = "mp3"

if file_format not in ["mp3", "wav"]:
    print("Invalid format. Choose 'mp3' or 'wav'.")
    sys.exit()

# Path for ffmpeg and ffprobe
AudioSegment.converter = r"C:\Users\70P8182\Downloads\GGTTS_mp3\GGT_mp3\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\70P8182\Downloads\GGTTS_mp3\GGT_mp3\ffprobe.exe"

# load CSV
df = pd.read_csv(input_file, header=None, names=["filename", "text"], encoding="utf-8")
df.dropna(inplace=True)  # remove empty lines

processed_names = set()
processed_texts = set()
count = 0

#Output directory
os.makedirs("output", exist_ok=True)

for _, row in df.iterrows():
    raw_name = str(row["filename"]).strip()
    text = str(row["text"]).strip()

    # Skip if text is empty
    if not text:
        continue
    
    # Skip if text already processed
    if text in processed_texts:
        print(f"⏭️ Skip duplicate text: '{text[:50]}...'")
        continue
    
    # Handle duplicate names by adding suffix
    original_name = raw_name
    suffix = 1
    while raw_name in processed_names:
        raw_name = f"{original_name}_{suffix}"
        suffix += 1
    
    processed_names.add(raw_name)
    processed_texts.add(text)

    safe_name = raw_name.replace(" ", "_").replace("/", "_").replace("\\", "_")
    mp3_path = os.path.join("output", f"{safe_name}.mp3")
    wav_path = os.path.join("output", f"{safe_name}.wav")

    # skip if file already exists
    if file_format == "mp3" and os.path.exists(mp3_path):
        print(f"⏭️ Skip existing {mp3_path}")
        continue
    if file_format == "wav" and os.path.exists(wav_path):
        print(f"⏭️ Skip existing {wav_path}")
        continue

    # create audio
    tts = gTTS(text=text, lang=lang)

    if file_format == "mp3":
        tts.save(mp3_path)
        print(f"✅ Saved: {mp3_path}")

    elif file_format == "wav":
        tts.save(mp3_path)
        print(f"✅ Temp MP3: {mp3_path}")

        sound = AudioSegment.from_mp3(mp3_path)
        if append_silence_Length_ms > 0:
            silence = AudioSegment.silent(duration=append_silence_Length_ms)
            sound = silence + sound + silence
        sound.export(wav_path, format="wav")
        os.remove(mp3_path)  # remove temporary MP3
        print(f"🎧 Exported WAV: {wav_path}")

    count += 1

print(f"\n🎉 Processed {count} new audio file(s).")

