from effects.base import ffmpeg_effect

class effect_vine_boom(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"bass=g=12:f=60,"
            f"volume=1.5"
            f"{output_label}"
        )