import json
import os
from pathlib import Path


def _config_dir() -> Path:
    appdata = os.environ.get("APPDATA", os.path.expanduser("~"))
    dir_path = Path(appdata) / "chinese-polisher"
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def _config_path() -> Path:
    return _config_dir() / "config.json"


def get_api_key() -> str:
    path = _config_path()
    if not path.exists():
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("api_key", "")
    except (json.JSONDecodeError, OSError):
        return ""


def save_api_key(key: str) -> None:
    path = _config_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"api_key": key}, f, ensure_ascii=False, indent=2)
