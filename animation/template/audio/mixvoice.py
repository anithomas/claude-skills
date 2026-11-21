# Mixes a voiceover over the music + sound-effect track and ducks the music under the voice.
# usage: ./py audio/mixvoice.py build/music_sfx.wav build/audio.wav voice1.mp3[@sec] [voice2.mp3[@sec] ...] [--delay 0.4] [--gap 0.35] [--music 0.8]
#   @sec     start time of that clip in seconds; without it a clip starts --gap after the previous one ends
#            (the first starts at --delay), so the picture's cues can be matched to the printed times.
#   --music  music + SFX gain while nobody speaks (default 0.8); the sidechain pulls it down further under the voice.
# Needs only ffmpeg/ffprobe. Output length = length of the music track; render.mjs picks up build/audio.wav.
import subprocess, sys

def dur(path):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                                capture_output=True, text=True, check=True).stdout.strip())

args = sys.argv[1:]
opt = {'--delay': 0.4, '--gap': 0.35, '--music': 0.8}
pos = []
i = 0
while i < len(args):
    if args[i] in opt: opt[args[i]] = float(args[i + 1]); i += 2
    else: pos.append(args[i]); i += 1
if len(pos) < 3: sys.exit(__doc__)
music, out, clips = pos[0], pos[1], pos[2:]

total = dur(music)
inputs, spans, t = [], [], opt['--delay']
for c in clips:
    path, _, at = c.partition('@')
    start = float(at) if at else t
    d = dur(path)
    spans.append((path, start, start + d))
    inputs.append(path)
    t = start + d + opt['--gap']

for p, s, e in spans:
    print(f'{p}: {s:.2f}s to {e:.2f}s ({e - s:.2f}s)')
end = max(e for _, _, e in spans)
if end > total - 0.3:
    print(f'WARNING: the voice ends at {end:.2f}s but the film is {total:.2f}s long: raise "duration" in src/beats.json '
          f'to about {end + 1.5:.1f}s (and the shot lengths), then re-run audio.py and this script.')

f = []
for k, (_, s, _e) in enumerate(spans):
    ms = int(s * 1000)
    f.append(f'[{k + 1}:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay={ms}|{ms}[c{k}]')
vs = ''.join(f'[c{k}]' for k in range(len(spans)))
f.append(f'{vs}amix=inputs={len(spans)}:normalize=0,apad=whole_dur={total},asplit=2[v][sc]')
f.append('[0:a]aformat=sample_rates=44100:channel_layouts=stereo[m]')
f.append('[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400:makeup=1[bg]')
f.append(f'[bg]volume={opt["--music"]}[bg2]')
f.append('[bg2][v]amix=inputs=2:duration=first:normalize=0[o]')
cmd = ['ffmpeg', '-v', 'error', '-y', '-i', music]
for p in inputs: cmd += ['-i', p]
cmd += ['-filter_complex', ';'.join(f), '-map', '[o]', '-ac', '2', '-ar', '48000', '-t', f'{total:.3f}', out]
subprocess.run(cmd, check=True)
print(f'wrote {out}: {total:.1f} s (voice + ducked music and effects)')
