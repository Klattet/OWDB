from dataclasses import dataclass
from .database import db
from pathlib import Path

@dataclass
class SidebarIcon:
    id: str
    name: str
    icon_path: str

def create_sidebar_icon(id: str, name: str, icon_path: Path):
    if "sidebar_icons" not in db.keys():
        db["sidebar_icons"] = {}
    if id in db["sidebar_icons"].keys():
        print(f"{id} already exists.")
    else:
        db["sidebar_icons"][id] = {"name": name, "icon_path": open(icon_path, "r")}

def remove_sidebar_icon(id: str):
    if "sidebar_icons" in db.keys() and id in db["sidebar_icons"]:
        del db["sidebar_icons"][id]

