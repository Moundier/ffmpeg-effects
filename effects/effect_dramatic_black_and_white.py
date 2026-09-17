class effect_dramatic_black_and_white(ffmpeg_effect):
    name = "dramatic_bw"
    description = "Transforms the scene into an overly serious monochrome sequence."

    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"hue=s=0,"
            f"eq=contrast=1.5:brightness=-0.1,"
            f"vignette=PI/5"
            f"{output_label}"
        )
