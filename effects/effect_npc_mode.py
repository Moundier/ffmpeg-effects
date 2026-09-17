from effects.base import ffmpeg_effect

class effect_npc_mode(ffmpeg_effect):
    name = "npc_mode"
    description = "Creates awkward looping NPC-like movement."

    def __init__(self, fps: int = 8, speed: float = 0.8):
        self.fps = fps
        self.speed = speed

    def filter(self, input_label: str, output_label: str) -> str:
        return f"{input_label}fps={self.fps},setpts={self.speed}*PTS{output_label}"