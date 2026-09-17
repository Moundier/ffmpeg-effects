from effects.base import ffmpeg_effect

class effect_earthquake(ffmpeg_effect):
    def __init__(self, intensity: float = 40):
        self.intensity = intensity

    def filter(self, input_label: str, output_label: str) -> str:
        i = self.intensity
        return (
            f"{input_label}"
            f"crop=iw-120:ih-120:"
            f"60+{i}*sin(35*t):"
            f"60+{i}*cos(31*t),"
            f"scale=iw+120:ih+120"
            f"{output_label}"
        )