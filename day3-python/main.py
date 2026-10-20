import os
from datetime import date
from rich import print

client_name = os.environ.get("CLIENT_NAME", "a client")

shoot_date = date.fromisoformat(os.environ.get("SHOOT_DATE", "2026-12-12"))

days_left = (shoot_date - date.today()).days
print(f"[bold green]{days_left}[/bold green] days until the shoot with {client_name}.")