import queue
import tempfile
import threading
import os
import time
import numpy as np
import sounddevice as sd
import soundfile as sf
import webrtcvad
from faster_whisper import WhisperModel
from df.enhance import enhance, init_df
from voz import detener

# CONFIGURACIÓN

SAMPLE_RATE = 16000
CHANNELS = 1
DTYPE = "float32"

FRAME_MS = 30

FRAME_SIZE = int(SAMPLE_RATE * FRAME_MS / 1000)

VAD_MODE = 2

MAX_RECORD_SECONDS = 10

print("🔊 Cargando DeepFilterNet...")

model_df, df_state, _ = init_df()

print("✅ DeepFilterNet listo.")

print("🧠 Cargando Whisper...")

model_whisper = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("✅ Whisper listo.")

vad = webrtcvad.Vad()

vad.set_mode(VAD_MODE)

audio_queue = queue.Queue()

def callback(indata, frames, time_info, status):

    if status:
        print(status)

    audio_queue.put(indata.copy())
    stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype=DTYPE,
    callback=callback
)

# ==========================
# Escuchar hasta detectar voz
# ==========================

def escuchar_audio():

    print("\n🎤 Esperando voz...")

    stream.start()

    grabando = False

    frames = []

    silencio = 0

    max_silencio = 20

    while True:

        bloque = audio_queue.get()

        bloque16 = (bloque.flatten() * 32767).astype(np.int16)

        bytes_audio = bloque16.tobytes()

        if vad.is_speech(bytes_audio, SAMPLE_RATE):

            if not grabando:
                print("🗣️ Voz detectada...")

            grabando = True

            silencio = 0

            frames.append(bloque.flatten())

        elif grabando:

            frames.append(bloque.flatten())

            silencio += 1

            if silencio >= max_silencio:

                print("✅ Fin de la frase")

                break

        if grabando:

            segundos = len(frames) * FRAME_MS / 1000

            if segundos >= MAX_RECORD_SECONDS:

                print("⏹ Tiempo máximo alcanzado")

                break

    stream.stop()

    if len(frames) == 0:
        return None

    return np.concatenate(frames)

stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype=DTYPE,
    callback=callback
)


# Mejorar audio con DeepFilterNet


def limpiar_audio(audio):

    print("🧹 Eliminando ruido...")

    try:
        audio_limpio = enhance(
            model_df,
            df_state,
            audio
        )

        return np.asarray(audio_limpio, dtype=np.float32)

    except Exception as e:
        print(f"Error DeepFilterNet: {e}")
        return audio

    # ==========================
# Whisper
# ==========================

def transcribir(audio):

    print("🧠 Transcribiendo...")

    archivo = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    sf.write(
        archivo.name,
        audio,
        SAMPLE_RATE
    )

    try:

        segmentos, info = model_whisper.transcribe(
            archivo.name,
            language="es",
            beam_size=5,
            vad_filter=False
        )

        texto = ""

        for segmento in segmentos:
            texto += segmento.text + " "

        texto = texto.lower().strip()

        return texto

    finally:

        archivo.close()

        if os.path.exists(archivo.name):
            os.remove(archivo.name)

# ==========================
# Función pública
# ==========================
def respuesta():

    try:

        audio = escuchar_audio()

        if audio is None:
            return ""

        audio = limpiar_audio(audio)

        texto = transcribir(audio)

        print(f"lo que escuchó {texto}")

        if texto in [
            "para",
            "detente",
            "silencio",
            "alto"
        ]:
            detener()

        return texto

    except Exception as e:

        print(f"Error: {e}")

        return ""
    