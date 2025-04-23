[EN]*********************************
# httpx-setting-tool

## Description
The `httpx-setting-tool` allows users to enable or disable the httpx client and manage the configuration settings. The tool stores settings in a `config.json` file and can control whether httpx is active or not. It allows the user to start an httpx connection to a test URL (`https://example.com`) based on the configuration.

This tool is executed via the `start.py` script.

## Requirements
- Python 3.x
- httpx library (install via `pip install httpx`)

## Usage
1. Clone or download the repository.
2. Install the required libraries using `pip install -r requirements.txt` (if provided).
3. Run the tool by executing `python start.py` in your terminal.

### Options
1. Enable httpx: Activates the httpx client for making HTTP requests.
2. Disable httpx: Disables the httpx client.
3. Start httpx: Attempts to start an httpx connection to `https://example.com` based on the current setting.
4. Exit: Exits the program.

## Configuration
The configuration is stored in `config.json`. If the file does not exist, a default configuration will be used with httpx enabled.

## License
This project is licensed under the MIT License.


[DE]*********************************                                                                         
# httpx-setting-tool
## Beschreibung
Das `httpx-setting-tool` ermöglicht es den Benutzern, den httpx-Client zu aktivieren oder zu deaktivieren und die Konfigurationseinstellungen zu verwalten. Das Tool speichert die Einstellungen in einer `config.json`-Datei und kann steuern, ob httpx aktiv ist oder nicht. Es ermöglicht dem Benutzer, eine httpx-Verbindung zu einer Test-URL (`https://example.com`) basierend auf der Konfiguration zu starten.

Dieses Tool wird über das Skript `start.py` ausgeführt.

## Anforderungen
- Python 3.x
- httpx-Bibliothek (installieren über `pip install httpx`)

## Verwendung
1. Klonen oder laden Sie das Repository herunter.
2. Installieren Sie die erforderlichen Bibliotheken mit `pip install -r requirements.txt` (falls bereitgestellt).
3. Führen Sie das Tool aus, indem Sie `python start.py` im Terminal eingeben.

### Optionen
1. httpx aktivieren: Aktiviert den httpx-Client für HTTP-Anfragen.
2. httpx deaktivieren: Deaktiviert den httpx-Client.
3. httpx starten: Versucht, eine httpx-Verbindung zu `https://example.com` basierend auf der aktuellen Einstellung zu starten.
4. Beenden: Beendet das Programm.

## Konfiguration
Die Konfiguration wird in `config.json` gespeichert. Wenn die Datei nicht vorhanden ist, wird eine Standardkonfiguration verwendet, bei der httpx aktiviert ist.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.
