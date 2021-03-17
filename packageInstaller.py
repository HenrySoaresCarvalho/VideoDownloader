import subprocess
import sys

def package_installer(package : list) -> None:
    for i in package:
        subprocess.check_call([sys.executable, "-m", "pip", "install", i])