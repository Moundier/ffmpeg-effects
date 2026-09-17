from effects.base import ffmpeg_effect

class effect_flash_bang(ffmpeg_effect):
    name = "flashbang"
    description = "Adds an absurd white flash."

    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            "eq=brightness=0.8:contrast=2"
            f"{output_label}"
        )