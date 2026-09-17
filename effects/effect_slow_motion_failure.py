from effects.base import ffmpeg_effect

class effect_slow_motion_failure(ffmpeg_effect):
    def __init__(self, factor: float = 3.0):
        self.factor = factor

    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"setpts={self.factor}*PTS"
            f"{output_label}"
        )