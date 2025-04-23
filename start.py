import os
import httpx
import json

# Der Pfad zur Konfigurationsdatei
config_file = 'config.json'

# Standardkonfiguration (falls die Datei nicht existiert)
default_config = {
    "httpx_enabled": True  # Standard ist aktiviert
}

# Funktion, um die Konfiguration zu laden
def load_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        return default_config

# Funktion, um die Konfiguration zu speichern
def save_config(config):
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

# Funktion, um httpx zu deaktivieren
def disable_httpx():
    config = load_config()
    config["httpx_enabled"] = False
    save_config(config)
    print("httpx wurde deaktiviert.")

# Funktion, um httpx zu aktivieren
def enable_httpx():
    config = load_config()
    config["httpx_enabled"] = True
    save_config(config)
    print("httpx wurde aktiviert.")

# Funktion, die httpx-Verbindung startet oder nicht
def start_httpx():
    config = load_config()
    if config["httpx_enabled"]:
        client = httpx.Client()
        response = client.get("https://example.com")
        print(response.status_code)
    else:
        print("httpx ist deaktiviert. Keine Verbindung möglich.")

# Menü für den Benutzer, um httpx zu aktivieren oder zu deaktivieren
def menu():
    while True:
        # XenexAi ASCII-Art Banner
        print("""
X   X EEEEE N   N EEEEE X   X     A    III
 X X  E     NN  N E      X X     A A    I
  X   EEEE  N N N EEEE    X     AAAAA   I
 X X  E     N  NN E      X X   A     A  I
X   X EEEEE N   N EEEEE X   X  A     A III
""")
        print("httpx-setting-tool v.01.0de \n\n--- Httpx Steuerung ---")
        print("1. httpx aktivieren")
        print("2. httpx deaktivieren")
        print("3. httpx starten")
        print("4. Beenden")
        
        choice = input("Bitte wählen Sie eine Option: ")
        
        if choice == '1':
            enable_httpx()
        elif choice == '2':
            disable_httpx()
        elif choice == '3':
            start_httpx()
        elif choice == '4':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == '__main__':
    menu()

