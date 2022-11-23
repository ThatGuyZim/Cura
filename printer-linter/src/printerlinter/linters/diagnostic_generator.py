from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterator

from ..diagnostic import Diagnostic


class DiagnosticGenerator(ABC):
    def __init__(self, file: Path, settings: dict) -> None:
        """ Yields Diagnostics for file, these are suggested text replacements based on formatting rules in settings.

        @param file: A file to generate diagnostics for
        @param settings: A list of settings containing rules for creating diagnostics
        """
        self._settings = settings
        self._file = file

    @abstractmethod
    def check(self) -> Iterator[Diagnostic]:
        pass