from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Type
import subprocess

from .effects import ffmpeg_effect
from ..effects.effect_camera_shake import effect_camera_shake
from ..effects.effect_drammatic_zoom import effect_drammatic_zoom
from ..effects.effect_freeze_frame import effect_freeze_frame
from ..effects.effect_vine_boom import effect_vine_boom
from ..effects.effect_slow_motion_failure import effect_slow_motion_failure
from ..effects.effect_emotional_damage import effect_emotional_damage

@dataclass
class section:
    start: float
    end: float
    effects: list[Type[ffmpeg_effect]]

MASTER = "master.mp4"
OUTPUT_DIR = Path("outputs")

TIMELINE = [
    section(1, 3, [effect_drammatic_zoom, effect_camera_shake]),
    section(4, 5, [effect_freeze_frame, effect_vine_boom]),
    section(7, 10, [effect_slow_motion_failure, effect_emotional_damage]),
]

def build_filter_graph(sections: list[section]) -> tuple[str, str]:
    inputs = []
    filters = []
    cursor = 0.0

    for i, section in enumerate(sections):
        if section.start > cursor:
            filters.append(
                f"[0:v]trim=start={cursor}:end={section.start},"
                f"setpts=PTS-STARTPTS[v{i}n]"
            )
            inputs.append(f"[v{i}n]")

        filters.append(
            f"[0:v]trim=start={section.start}:end={section.end},"
            f"setpts=PTS-STARTPTS[v{i}]"
        )

        current = f"[v{i}]"

        for j, effect_cls in enumerate(section.effects):
            output = f"[v{i}e{j}]"
            effect = effect_cls()
            filters.append(effect.filter(current, output))
            current = output

        inputs.append(current)
        cursor = section.end

    filters.append(
        f"[0:v]trim=start={cursor},"
        f"setpts=PTS-STARTPTS[vlast]"
    )
    inputs.append("[vlast]")

    filters.append(
        "".join(inputs) +
        f"concat=n={len(inputs)}:v=1:a=0[outv]"
    )

    return ";".join(filters), "[outv]"

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output = OUTPUT_DIR / f"edited_{timestamp}.mp4"

    graph, output_label = build_filter_graph(TIMELINE)

    command = [
        "ffmpeg",
        "-i", MASTER,
        "-filter_complex", graph,
        "-map", output_label,
        "-map", "0:a?",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        str(output),
    ]

    print(" ".join(command))
    subprocess.run(command, check=True)
    print(f"Output: {output}")

if __name__ == "__main__":
    main()