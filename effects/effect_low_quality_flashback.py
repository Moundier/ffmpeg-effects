from effects.base import ffmpeg_effect

class effect_low_quality_flashback(ffmpeg_effect):
    name = "flashback"
    description = "Creates an intentionally degraded flashback."

    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            "scale=iw/4:ih/4,"
            "scale=iw:ih:flags=neighbor,"
            "eq=contrast=1.3:saturation=0.5,"
            "noise=alls=30:allf=t"
            f"{output_label}"
        )