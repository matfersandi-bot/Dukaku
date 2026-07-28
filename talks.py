from main import preguntar
from hablar import respuesta
from voz import sonido, detener


def main():

    print("=" * 50)
    print(" DU CACU")
    print("=" * 50)
    print("Habla cuando escuches el mensaje.")
    print("Comandos:")
    print(" • salir")
    print(" • adiós")
    print(" • para")
    print()

    while True:

        try:

            texto = respuesta()

            if texto is None or texto.strip() == "":
                continue

            texto = texto.strip().lower()

            print(f"\n Tú: {texto}")

            # Finalizar programa
            if texto in ["salir", "adiós", "hasta luego"]:
                detener()
                sonido("Hasta luego. Fue un gusto conversar contigo.")
                break

            # Detener la voz
            if texto in ["para", "detente", "silencio", "cállate"]:
                detener()
                print(" Voz detenida.")
                continue

            print(" Pensando...")

            respuesta_ia = preguntar(texto)

            print(f"\n Du Cacu:\n{respuesta_ia}\n")

            sonido(respuesta_ia)

        except KeyboardInterrupt:
            detener()
            print("\nPrograma terminado.")
            break

        except Exception as e:
            print(f"\n⚠ Error: {e}")


if __name__ == "__main__":
    main()