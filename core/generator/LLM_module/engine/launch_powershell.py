from pathlib import Path
import subprocess


async def run_powershell_module(ROOT_DIRECTORY: Path
):
    powershell_script_path: Path = ROOT_DIRECTORY / "core" / "generator" / "LLM_module" / "engine" / "scripts" / "script.ps1"
    result = subprocess.Popen(
        [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            f"[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; & '{str(powershell_script_path)}'",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",  # Добавьте эту строку
        errors="replace",  # И эту для обработки некорректных байтов
    )
    stdout, stderr = result.communicate()
    print("STDOUT:", stdout)
    print("STDERR:", stderr)
    print("Return code:", result.returncode)
    print("testing chrome CDP callable...")
