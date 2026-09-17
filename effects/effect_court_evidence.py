from effects.base import ffmpeg_effect

class effect_court_evidence(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"drawbox=x=100:y=100:w=500:h=300:"
            f"color=red@0.8:t=8"
            f"{output_label}"
        )