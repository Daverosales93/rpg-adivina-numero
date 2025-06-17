import random
import time
import os

# Si deseas música, descomenta esto y coloca un mp3 en la misma carpeta
import pygame
pygame.mixer.init()
pygame.mixer.music.load("musica_epica.mp3")
pygame.mixer.music.play(-1)

# --- Datos del jugador ---
jugador = {
    "nombre": "",
    "vidas": 3,
    "pociones": 1,
    "nivel": "fácil",
    "victorias": 0
}

# --- Enemigos disponibles ---
enemigos = [
    {"nombre": "Slime Verde", "nivel": "fácil"},
    {"nombre": "Espectro de Humo", "nivel": "difícil"},
    {"nombre": "Señor de los Números", "nivel": "difícil"},
    {"nombre": "Gusano del Caos", "nivel": "fácil"},
]

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa(tiempo=1.5):
    time.sleep(tiempo)

def intro():
    limpiar()
    print("\U0001F3AE Bienvenido al RPG: *Adivina y Sobrevive*")
    jugador["nombre"] = input("\U0001F9D9‍♂️ ¿Cuál es tu nombre, héroe? ").strip().capitalize()
    print(f"\n¡Hola, {jugador['nombre']}! Comienza tu aventura numérica.")
    pausa()
    elegir_dificultad()

def elegir_dificultad():
    print("\nElige la dificultad:")
    print("1. 🟢 Fácil (números del 1 al 10)")
    print("2. 🔴 Difícil (números del 1 al 50)")
    eleccion = input(">>> ")

    if eleccion == "2":
        jugador["nivel"] = "difícil"
        print("Modo difícil activado. 😈 Buena suerte...")
    else:
        jugador["nivel"] = "fácil"
        print("Modo fácil seleccionado. ¡A entrenar!")

    pausa()
    iniciar_combate()

def iniciar_combate():
    enemigo = random.choice(enemigos)
    rango = 10 if jugador["nivel"] == "fácil" else 50
    numero_secreto = random.randint(1, rango)
    intentos = 0
    vidas = jugador["vidas"]

    limpiar()
    print(f"\n😈 Un enemigo aparece: {enemigo['nombre'].upper()} (modo {jugador['nivel']})")
    print(f"🔢 Adivina el número secreto entre 1 y {rango} para vencerlo.")

    while vidas > 0:
        intento = input("🎯 Tu número: ")

        if intento.lower() == "pocion":
            if jugador["pociones"] > 0:
                jugador["pociones"] -= 1
                vidas += 1
                print("🧪 Usaste una pocion y recuperaste 1 vida. ❤️")
                continue
            else:
                print("❌ No te quedan pociones.")
                continue

        if not intento.isdigit():
            print("❌ Eso no es un número.")
            continue

        intento = int(intento)
        intentos += 1

        if intento < numero_secreto:
            vidas -= 1
            print("📉 Demasiado bajo. El enemigo ríe. 😈")
        elif intento > numero_secreto:
            vidas -= 1
            print("📈 Demasiado alto. El enemigo te ataca.")
        else:
            print(f"\n🏆 ¡Adivinaste! Derrotaste a {enemigo['nombre']} en {intentos} intentos.")
            jugador["victorias"] += 1
            jugador["vidas"] = vidas
            pausa()
            break

        print(f"❤️ Vidas restantes: {vidas} | 🧪 Pociones: {jugador['pociones']}")
        pausa()

    if vidas == 0:
        print(f"\n💀 {jugador['nombre']}, el enemigo te derrotó...")
        guardar_partida()
    else:
        siguiente = input("\n🔬 ¿Quieres seguir luchando? (s/n): ").lower()
        if siguiente == "s":
            iniciar_combate()
        else:
            guardar_partida()

def guardar_partida():
    archivo = f"{jugador['nombre'].lower()}_partida.txt"
    with open(archivo, "w") as f:
        f.write(f"Nombre: {jugador['nombre']}\n")
        f.write(f"Victorias: {jugador['victorias']}\n")
        f.write(f"Nivel: {jugador['nivel']}\n")
        f.write(f"Pociones restantes: {jugador['pociones']}\n")
        f.write(f"Vidas restantes: {jugador['vidas']}\n")
    print(f"\n📂 Partida guardada en {archivo}. ¡Hasta la próxima, héroe!")

# --- Ejecutar juego ---
intro()
