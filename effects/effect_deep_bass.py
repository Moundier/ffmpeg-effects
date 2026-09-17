from effects.base import ffmpeg_effect

class effect_deep_bass(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"bass=g=18:f=45,"
            f"lowpass=f=180"
            f"{output_label}"
        )