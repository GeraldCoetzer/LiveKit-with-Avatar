# Setup Guide

This project uses Python with a virtual environment.\
The following steps describe installation and execution on Linux/macOS
and Windows.

------------------------------------------------------------------------

## Requirements

-   Python 3.9 or newer
-   pip installed
-   Git (optional, if you clone the repository)

------------------------------------------------------------------------

## Installation and Execution

### Linux / macOS

``` bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start
python agent_worker.py download-files

# Final start
python agent_worker.py dev
```

### Windows

``` powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start
python agent_worker.py download-files

# Final start
python agent_worker.py dev
```

Go to the browser and open:\
https://agents-playground.livekit.io/\
Select the folder containing the files; for example:\
C:\GC\Argus\training\AI\course\LiveKit-mit-Avatar
