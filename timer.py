import time
from datetime import datetime

TEMP_FILE = ".current_session"
LOG_FILE = "sessions.txt"

def start_session(name):
    with open(TEMP_FILE, "w") as f:
        f.write(f"{name}|{time.time()}")
    print("⏳ Session started!")

def stop_session():
    try:
        with open(TEMP_FILE, "r") as f:
            name, start = f.read().split("|")

        duration = round((time.time() - float(start)) / 60, 2)

        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} | {name} | {duration} minutes\n")

        print(f"✅ Saved: {name} ({duration} minutes)")

    except FileNotFoundError:
        print("No active session.")

def view_sessions():
    try:
        with open(LOG_FILE, "r") as f:
            print("\n📜 Session History\n")
            print(f.read())
    except FileNotFoundError:
        print("No sessions yet.")
