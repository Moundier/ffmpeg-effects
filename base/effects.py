from abc import ABC, abstractmethod

class ffmpeg_effect(ABC):
    @abstractmethod
    def filter(self, input_label: str, output_label: str) -> str:
        pass