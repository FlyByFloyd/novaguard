from pathlib import Path

# File extensions that are commonly risky on Windows
RISKY_EXTENSIONS = {
    ".exe",
    ".msi",
    ".bat",
    ".cmd",
    ".ps1",
    ".vbs",
    ".js",
    ".jar",
    ".scr",
    ".dll",
}

# Directories we intentionally ignore
SKIP_DIRS = {
    ".venv",
    "__pycache__",
    ".git",
}


def scan_for_risky_files(path: str, max_examples: int = 10) -> dict:
    """
    Recursively scan a folder for risky file types.

    Returns a dictionary with:
      - scanned_files (int)
      - risky_count (int)
      - risky_examples (list of paths)
      - errors (list of error messages)
    """

    base_path = Path(path)

    result = {
        "scanned_files": 0,
        "risky_count": 0,
        "risky_examples": [],
        "errors": [],
    }

    # Basic validation
    if not base_path.exists():
        result["errors"].append(f"Path does not exist: {base_path}")
        return result

    if not base_path.is_dir():
        result["errors"].append(f"Path is not a directory: {base_path}")
        return result

    try:
        for item in base_path.rglob("*"):
            # Skip directories
            if item.is_dir():
                continue

            # Skip ignored directories (like .venv)
            if any(skip in item.parts for skip in SKIP_DIRS):
                continue

            result["scanned_files"] += 1

            extension = item.suffix.lower()

            if extension in RISKY_EXTENSIONS:
                result["risky_count"] += 1

                if len(result["risky_examples"]) < max_examples:
                    result["risky_examples"].append(str(item))

    except PermissionError:
        result["errors"].append(
            "Permission denied while scanning. Try a different folder."
        )
    except Exception as e:
        result["errors"].append(f"Unexpected error: {e}")

    return result
