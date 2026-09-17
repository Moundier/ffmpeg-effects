from effects.base import ffmpeg_effect

class effect_matrix_mode(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"eq=contrast=1.8:saturation=0.3,"
            f"noise=alls=15:allf=t"
            f"{output_label}"
        )