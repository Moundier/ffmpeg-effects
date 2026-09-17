from effects.base import ffmpeg_effect

class effect_reality_break(ffmpeg_effect):
    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            f"split=2[a][b];"
            f"[a]hflip[a1];"
            f"[b]negate[b1];"
            f"[a1][b1]blend=all_expr="
            f"'if(gt(X,W/2),B,A)',"
            f"noise=alls=35:allf=t"
            f"{output_label}"
        )