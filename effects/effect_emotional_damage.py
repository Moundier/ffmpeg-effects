from effects.base import ffmpeg_effect

class effect_emotional_damage(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"eq=contrast=1.8:brightness=-0.15,"
            f"vignette=PI/4,"
            f"colorbalance=rs=.3:bs=.3"
            f"{output_label}"
        )