import speech_recognition as sr
from voz import detener

recognizer = sr.Recognizer()

recognizer.energy_threshold = 200
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1.2
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.8

print("🎤 Calibrando micrófono...")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)

print("✅ Micrófono listo")


def respuesta():

    with sr.Microphone() as source:

        try:

            print("\n🎤 Escuchando...")

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

            texto = recognizer.recognize_google(
                audio,
                language="es-CR"
            )

            texto = texto.lower().strip()

            if texto in [
                "para",
                "detente",
                "silencio",
                "alto",
                "cállate",
                "callate"
            ]:
                detener()

            return texto

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            print("No entendí.")
            return ""

        except sr.RequestError:
            print("Error con Google Speech.")
            return ""

        except Exception as e:
            print(e)
            return ""