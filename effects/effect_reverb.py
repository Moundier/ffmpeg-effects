from effects.base import ffmpeg_effect

class effect_reverb(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"aecho=0.8:0.9:1000:0.3"
            f"{output_label}"
        )