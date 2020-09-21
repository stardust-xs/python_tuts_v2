# Problem Statement:
# ------------------
# Display notifications on a timely manner.
# Break notifications after every 20 minutes.

# Flow:
# -----
# Schedule function to run every after particular time.
# Event based triggering.

import os
import time


def show_toast(title: str, message: str, minutes: float = 5.0) -> None:
    """Displays notification in timely manner."""
    title = title.replace("'", "")
    message = message.replace("'", "")
    time.sleep(minutes * 60.0)
    os.system(f"notify-send '{title}' '{message}'")


show_toast("Drink water", "Please drink some water.", 60)
