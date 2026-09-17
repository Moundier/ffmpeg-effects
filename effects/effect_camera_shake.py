from effects.base import ffmpeg_effect

class effect_camera_shake(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"crop=iw-120:ih-120:"
            f"60+25*sin(35*t):"
            f"60+25*cos(31*t),"
            f"scale=iw+120:ih+120"
            f"{output_label}"
        )