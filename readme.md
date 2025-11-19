# Setup-Anleitung

Dieses Projekt verwendet Python mit einer virtuellen Umgebung.  
Die folgenden Schritte beschreiben die Installation und Ausführung unter Linux/macOS und Windows.

---

## Voraussetzungen
- Python 3.9 oder neuer
- pip installiert
- Git (optional, falls du das Repository klonst)

---

## Installation und Ausführung

### Linux / macOS
```bash
# Virtuelle Umgebung erstellen
python3 -m venv venv

# Virtuelle Umgebung aktivieren
source venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# Starten
python agent_worker.py download-files

# Final starten
python agent_worker.py dev



FÜR WINDOWS:

# Virtuelle Umgebung erstellen
python -m venv venv

# Virtuelle Umgebung aktivieren
.\venv\Scripts\Activate.ps1

# Abhängigkeiten installieren
pip install -r requirements.txt

# Starten
python agent_worker.py download-files

# Final starten
python agent_worker.py dev

# Go the browser to https://agents-playground.livekit.io/
# select the folder with the files; in this case 
# C:\GC\Argus\training\AI\course\LiveKit-mit-Avatar