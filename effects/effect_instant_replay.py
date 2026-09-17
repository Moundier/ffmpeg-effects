from effects.base import ffmpeg_effect

class effect_instant_replay(ffmpeg_effect):
    name = "instant_replay"
    description = "Creates a dramatic replay of an event."

    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}split=2[original][replay];"
            "[replay]setpts=0.5*PTS,scale=iw*1.2:ih*1.2[replay_scaled];"
            f"[original][replay_scaled]concat=n=2:v=1:a=0{output_label}"
        )
