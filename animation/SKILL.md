---
name: animation
description: Make an animated video, either a story or an explainer, delivered as a self-contained HTML file that plays with sound plus an MP4 rendered from the same code. Use whenever someone says "create an animation", "make an animated video", "animate X", "make an animated explainer", or asks to redo or extend one of these videos. Before building, asks for the length, topic, style, and whether to plan together first (with a design sheet of the characters or key elements) or get straight to work, skipping anything already given; defaults are 30 seconds, the Storybook look and straight to work. Can also add a voiceover (an uploaded recording or ElevenLabs) that the music ducks under. Always use this skill instead of building animations ad hoc, because it holds the intake questions, the deterministic render kit, the parallel MP4 renderer, the audio synth and the review rules.
---

# Animation

Makes an animated video, a story or an explainer, as one self-contained HTML file that plays in a browser with sound, plus an MP4 rendered frame by frame from the same code.

Everything lives in this skill folder. `scripts/new_animation.sh` starts a project from `template/`, which holds a working 12-second example in the default Storybook look. Below, `SK` is this skill folder and `P` is the video's project folder.

## 1. Ask before building

Don't assume what the video is. Check the request for these four things:

- **Length**: how long the video should be.
- **Topic**: what it's about. A topic can be a story (characters, a plot) or an explainer (how something works, a concept, a process). If the topic makes it clear which one it is, don't ask. If it could go either way, ask which one is wanted as part of the topic question.
- **Style**: the look. The request may name a style or a style guide, or give an example (a video, image, motion graphic or earlier video).
- **Plan together or just get to work**: plan the video together first, or go straight to making it?

Ask only for the ones that weren't given, in one short message, and say the default for each: 30 seconds for length, the Storybook look for style (see [references/default-style.md](references/default-style.md)), and getting straight to work if there's no choice. There's no default topic. If the answer doesn't pick one ("whatever", "default", "you pick"), use the default. Don't start building until you have a topic. If all four were given, skip the questions and start.

Don't make up other requirements. Use only what was asked for plus the defaults. When you deliver, write one line naming any choice you made on their behalf, so it's easy to change.

**Fixed defaults (don't ask):** 16:9 at 1920x1080, 24 fps, music and sound effects on, no voiceover. Add a voiceover only when the request asks for narration, a voice or a recording (step 5).

**Style examples: look and motion only.** When the request gives an example of the style (a video, an image, a motion graphic, a style guide), take only two things from it: how it looks (palette, lighting, materials, line, texture, type) and how it moves (camera, timing, easing, transitions). Never copy its content, structure, shot order, characters, props or specific elements. Details are in [references/content-and-style.md](references/content-and-style.md).

## 2. Plan the video

- **Story:** a character who wants something, what gets in the way, and how it turns out, told in shots of characters in places.
- **Explainer:** one idea per beat, in the order a viewer needs them. Show the thing itself working (the parts, the flow, before and after) and move the camera to reveal each step. Short labels of a few words are fine when they name what's on screen; no paragraphs. Use real-world facts only, and check any you aren't sure of.
- Write a short beat list (one line per beat, with rough times).

**If planning together was chosen**, get sign-off before making the video:

1. Post the beat list.
2. Start the project (section 3), build just the key designs, and render a design sheet with `node render.mjs --design` (it turns around each item: front, three-quarter and side, with a name and a one-line note). For a story, include the main characters and any key objects. For an explainer, include the key elements: the main object or machine, its important parts, and any symbols or labels that will recur.
3. Send the sheet and the beat list together, and wait for an answer. Change what's asked for and send a new sheet until it's approved. Only then build the scenes and render the video.

**If getting straight to work was chosen** (or nothing was chosen), post the beat list for reference and keep building without waiting.

## 3. Start the project

- `P` is the folder the request names. Otherwise use a new subfolder named `<slug>-animation/` in the current working folder.
- Run `bash "$SK/scripts/new_animation.sh" "$P"`. It copies the template, installs the rendering library and esbuild, reuses an installed Playwright (installs one only if none works), and makes sure Python has numpy and scipy (in `~/.cache/animation-skill/venv` if the system Python lacks them). If it reports node or ffmpeg missing, pass on the `brew install` line it prints.
- Layout: `src/beats.json` (title, length, cue times), `src/story.js` (sets, characters, shots; it holds explainers too), `src/kit.js` (the shared kit; extend it, don't fork it), `src/assets/title.woff2` (title font, Fraunces, OFL), `audio/audio.py` + `audio/audiolib.py` (sound), `audio/mixvoice.py` (voiceover mix), `build.mjs`, `render.mjs`, and `build/` for outputs. Replace the example entirely.

## 4. Build

Read [references/craft.md](references/craft.md) before writing scene code.

1. **Beats.** Write `src/beats.json`: `title`, `duration`, `fps`, and named `cues` for every moment that needs a sound or a cut. Picture and sound both read these times, so change timing here only.
2. **Sets, characters, objects.** Build each location once as a `THREE.Scene` with the kit's helpers, and add builders to `kit.js` for anything new the video needs (machines, organs, products, buildings, creatures). For explainers, model the subject clearly enough that each part reads at a glance. Make each character and key object a factory in the story's `cast`, and list them in the story's `design` array, so the film and the design sheet always use the same models (the template shows how).
3. **Animate on global time `t`** so things stay put across cuts. Use `keys`, `seg`, `ease`, `onPath` and the `pose()` functions. Nothing may depend on the previous frame, a clock or `Math.random`.
4. **Shots.** List shots in order with `set`, `dur`, a `cam(local, p)` function and an optional `in` transition (`dissolve`, `dip`, `iris`, `whip`, `wipe`). Durations must add up to `duration`.
5. **Words on screen** go in `overlay(g, t)` with `title()`: the title, and for explainers short labels.
6. **Quick checks:** `node build.mjs`, then `node render.mjs --stills 1,4.5,9` (one time per beat). Look at `build/stills/sheet.jpg` and fix problems before the full render.

## 5. Sound

Edit `audio/audio.py`: music that suits the mood, and sound effects on the cues from `beats.json` (steps for walks, a sound for each pickup, landing, click or transformation). `audiolib.py` has instruments, effects and ambience beds; add new sounds there when needed.

**No voiceover** (the default): run `./py audio/audio.py build/audio.wav` and go to step 6.

**With a voiceover** (when the request asks for narration, a voice, a narrator or a voiceover, or the user gives a recording): follow 5a to 5d. The voice is the master clock: the picture and the music follow it, and the voice is never cut or covered.

### 5a. Write the narration
- Write the spoken lines in the beat list, one line per beat. Plan about 2.5 words per second (12 s is roughly 28 words), short spoken sentences, numbers as words. For an explainer, the voice says what the picture is showing at that moment.
- Check the facts of anything presented as true, and never invent statistics.

### 5b. Get the voice
- **The user's own recording:** copy it to `P/build/voice.mp3` (or .wav/.m4a). Don't edit it. If there is also script text, use it to place the cues.
- **ElevenLabs (when the connector is available):** call `creative_generate_speech` with `model_id` `eleven_v4`, `generations_count` 1 and a leading tag such as `[cheerful]` or `[calm]`. First call it once with `estimate_only` and tell the user the credit cost (about 140 credits for 11 s). Use the voice the user names. If they name none, ask `creative_list_voices` for a clear, natural one that fits the topic, and say which you picked. Never invent a voice id and never regenerate to retry: each call is charged. Poll `creative_get_flow_run_status` until it completes, then download the `media[0].url` mp3 with `curl -L -o build/voice.mp3 "<url>"` (the link is signed and expires). Keep the ElevenLabs flow link to hand to the user.
- **Neither is available:** ask the user for a recording, or make the video without a voice and say so.
- Several parts (one per scene) are fine: save them as `voice1.mp3`, `voice2.mp3`, and so on.

### 5c. Fit the picture to the voice
- Read the length with `ffprobe -v error -show_entries format=duration -of csv=p=0 build/voice.mp3`. Set `duration` in `src/beats.json` to the voice length plus about 1.5 s (0.4 s of lead-in, the rest as a tail for the closing sound and title), and move the `cues` and shot lengths so each action lands on the words that describe it. Shot durations must still add up to `duration`.
- For several parts, decide each part's start time (usually the start of its shot) and pass it as `file@seconds` in 5d.
- You can't hear the result: judge sync from the printed clip times and the stills at each cue time, and tell the user to watch once for timing.

### 5d. Mix
1. `./py audio/audio.py build/music_sfx.wav` builds the music and effects on their own (do not write to `build/audio.wav` yet).
2. `./py audio/mixvoice.py build/music_sfx.wav build/audio.wav build/voice.mp3` mixes the voice over it, pulls the music and effects down under the speech (sidechain), and writes `build/audio.wav`. It prints each clip's start and end time. Options: `build/voice1.mp3@0.4 build/voice2.mp3@7.5` to place clips, `--delay` for the first start (default 0.4 s), `--gap` between unplaced clips (0.35 s), `--music 0.8` for the bed level.
3. If it warns that the voice runs past the film, raise `duration` as in 5c, then redo 5d.
4. Step 6's render takes `build/audio.wav` and normalizes it to -16 LUFS, so the voice stays on top. The HTML file has no voice: deliver the MP4 as the version with narration, and say so.

## 6. Render and review

1. `node build.mjs` writes `build/<slug>.html` with the rendering library, the font and the sound inside.
2. `node render.mjs` renders with parallel headless Chromium workers, adds the sound at -16 LUFS, and writes `build/<slug>.mp4` plus `build/review/contact-*.jpg` (one tile per second). In a cloud container it runs about 2 frames a second, so 30 seconds takes about 6 minutes; run it in the background. On a Mac it uses the GPU. Use `--scale 0.5` for a fast draft, `--scale 2` for 4K, `--from`/`--to` for a section.
3. Review every contact sheet against the checklist in [references/content-and-style.md](references/content-and-style.md). Fix, rebuild and re-render until it passes.

## 7. Deliver

- Deliver the HTML (click or space to play with sound, arrow keys to step) and the MP4 from `P/build/`, with the length and one line on any choice that wasn't specified. With a voiceover, only the MP4 has the voice; say so, and give the voice's credit cost and ElevenLabs flow link if one was used.
- When changes are asked for, move the previous cut to `P/v1/` (then `v2/`, ...) before re-rendering.
- Add new review lessons from feedback to `references/content-and-style.md`.
