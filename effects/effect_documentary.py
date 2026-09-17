from effects.base import ffmpeg_effect

class effect_documentary(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"format=gray,"
            f"eq=contrast=1.3,"
            f"noise=alls=12:allf=t"
            f"{output_label}"
        )