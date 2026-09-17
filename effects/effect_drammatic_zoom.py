from effects.base import ffmpeg_effect

class effect_dramatic_zoom(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"scale=iw*1.2:ih*1.2,"
            f"crop=iw/1.2:ih/1.2,"
            f"setpts=PTS"
            f"{output_label}"
        )