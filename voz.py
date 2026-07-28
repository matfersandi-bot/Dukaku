import subprocess
import threading

# Proceso actual de la voz
_proceso = None

# Indica si está hablando
_hablando = False


def sonido(texto: str):
    """
    Reproduce un texto usando la voz de macOS.
    Si ya estaba hablando, la voz anterior se detiene.
    """

    global _proceso
    global _hablando

    detener()

    def hablar():
        global _proceso
        global _hablando
        try:
            _hablando = True
            _proceso = subprocess.Popen(["say", "-v", "Arnold", "-r", "175", texto])
            _proceso.wait()
        except Exception as e:
            print(f"Error de voz: {e}")
        finally:
            _hablando = False
            _proceso = None

    hilo = threading.Thread(target=hablar, daemon=True)
    hilo.start()


def detener():
    """
    Detiene inmediatamente la voz.
    """

    global _proceso
    global _hablando
    if _proceso is not None:
        try:
            _proceso.terminate()
            _proceso.wait(timeout=1)
        except Exception:
            pass

    _proceso = None
    _hablando = False


def hablando():
    """
    Devuelve True si la IA está hablando.
    """
    return _hablando