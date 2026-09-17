from effects.base import ffmpeg_effect

class anime_speed(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"setpts=0.45*PTS,"
            f"eq=contrast=1.5:saturation=1.4"
            f"{output_label}"
        )