from effects.base import ffmpeg_effect

class effect_security_camera(ffmpeg_effect):
    name = "security_camera"
    description = "Transforms the footage into an old surveillance camera recording."

    def filter(self, input_label: str, output_label: str) -> str:
        return (
            f"{input_label}"
            "format=gray,"
            "eq=contrast=1.35:brightness=-0.08,"
            "noise=alls=18:allf=t,"
            "vignette=PI/4,"
            "drawbox=x=0:y=0:w=iw:h=ih:color=black@0.15:t=18,"
            "drawgrid=w=iw:h=2:color=black@0.08:t=1,"
            "drawtext=text='CAM 04':x=30:y=30:"
            "fontsize=32:fontcolor=white:"
            "shadowcolor=black@0.8:shadowx=2:shadowy=2,"
            "drawtext=text='REC':x=30:y=75:"
            "fontsize=26:fontcolor=red:"
            "shadowcolor=black:shadowx=2:shadowy=2,"
            "drawtext=text='%{localtime\\:%Y-%m-%d %H\\\\\\:%M\\\\\\:%S}':"
            "x=w-tw-30:y=30:"
            "fontsize=26:fontcolor=white:"
            "shadowcolor=black@0.8:shadowx=2:shadowy=2,"
            "drawtext=text='MOTION DETECTED':"
            "x=w-tw-30:y=h-th-30:"
            "fontsize=22:fontcolor=white:"
            "shadowcolor=black@0.8:shadowx=2:shadowy=2"
            f"{output_label}"
        )