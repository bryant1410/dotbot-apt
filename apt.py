import subprocess
from typing import Iterator

import dotbot


class Apt(dotbot.Plugin):
    def can_handle(self, directive: str) -> bool:
        return directive == "apt"

    def handle(self, directive: str, packages: Iterator[str]) -> bool:
        return self._run_and_check("apt update") and self._run_and_check("apt install -y {}".format(" ".join(packages)))

    def _run_and_check(self, command: str) -> bool:
        completed_process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        if completed_process.returncode:
            self._log.error("Failed to execute `{}`: {}".format(command, completed_process.stdout.decode()))

        return bool(completed_process.returncode)
