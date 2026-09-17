from effects.base import ffmpeg_effect

class effect_flashback(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"scale=iw/4:ih/4,"
            f"scale=iw:ih:flags=neighbor,"
            f"eq=contrast=1.3:saturation=0.5,"
            f"noise=alls=30:allf=t"
            f"{output_label}"
        )