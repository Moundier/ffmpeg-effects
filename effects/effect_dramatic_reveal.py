from effects.base import ffmpeg_effect

class effect_dramatic_reveal(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"fade=t=in:st=0:d=2"
            f"{output_label}"
        )