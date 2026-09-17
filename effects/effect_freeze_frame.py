from effects.base import ffmpeg_effect

class effect_freeze_frame(ffmpeg_effect):
    def __init__(self, duration: float = 2.0):
        self.duration = duration

    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"tpad=stop_mode=clone:stop_duration={self.duration}"
            f"{output_label}"
        )