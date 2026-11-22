# claude-skills

Personal user-level Claude Code skills. The repo root is the skills folder, so on any machine:

```bash
git clone https://github.com/anithomas/claude-skills ~/.claude/skills
```

(Windows: clone into `C:\Users\<you>\.claude\skills`.) Restart Claude Code and every skill here loads in every project.

## Rule
All user-level (general-purpose) skills live here, never in a project repo. Project repos keep only skills that are specific to that project (e.g. `logicmanse-site` keeps `apply-design-patch`).

## Skills
Keep this list in sync: every skill added, moved or removed here gets its README line updated in the same commit.

General
- `interview-me` — interviews you one question at a time about a fuzzy task, then writes one clear brief (from the Claude 15 tips kit).
- `detox` — audits your Claude setup (interface, memory, skills, connectors, scheduled tasks) and shows one checklist page; changes only what you tick (from the Claude 15 tips kit).
- `find-skills` — discover and install skills via the `npx skills` CLI (from vercel-labs/skills).

Video: sound design
- `video-sound-design-editor` — three-pass sound design (whooshes, textures, risers/hits) with level targets.

Video: HyperFrames (build and render videos as HTML compositions)
- `hyperframes` — mandatory entry point for any request to make, edit, animate or render a video or motion graphic.
- `hyperframes-core` — the composition contract: structure, `data-*` timing attributes, tracks, sub-compositions, variables.
- `hyperframes-cli` — the CLI development loop: init, add, lint, check, snapshot, preview, render, publish.
- `hyperframes-animation` — animation rules, scene blueprints, transitions and the runtime adapters (GSAP etc.).
- `hyperframes-keyframes` — punch-ins, zooms, Ken Burns, camera moves and other seek-safe keyframes.
- `hyperframes-audio` — mixing audio already in a composition: fades, gain, ducking, voiceover carve.
- `hyperframes-creative` — creative direction: design specs, palettes, typography, narration, beat planning.
- `hyperframes-registry` — search, install and wire registry blocks and components.
- `hyperframes-studio` — working with a person on a project in Studio.
- `general-video` — custom compositions when no specialized workflow fits: longer pieces, reels, montages, title cards.
- `motion-graphics` — short design-led motion graphics: kinetic type, stat count-ups, data-viz, logo stings, lower-thirds.
- `media-use` — resolve BGM, SFX, images, icons, logos, voice, color grades or LUTs into local files with a ledger.
- `motion-graphics-styles` — eight ready-made prompts (Paper Cut-Out, Particles, Liquid Glass, Kinetic Type, Isometric, Flat Vector, Risograph, 8-Bit) that build a playable, MP4-exportable HTML animation from a topic.

Video: LogicManse Publications
- `logicmanse-promo-video` — build and publish a LogicManse Publications title's promo video end to end: cue sheets, HyperFrames render, ElevenLabs voiceover, timestamped files, thumbnail, Drive link, Metricool post to all networks with AI-content flags.

Video: iterative build loop
- `cook` — the Cook Loop (from github.com/Leonxlnx/cook, MIT): long autonomous build-render-critique runs that match reference images or videos against a numeric bar. Asks all questions once at intake, then works unattended and holds the final render until you approve the stills.

Video: 2D animated long-form
- `reachmora-2d-longform` — make 3, 5, 10 or 15 minute faceless 2D animated YouTube videos (ink-on-paper cartoon style): pitches 10 ideas, writes the script, then turns your voiceover into a finished 1080p MP4 with code-drawn characters, music and SFX. By ReachMora (keep the credit in `CREDITS.md`). Needs ffmpeg and `scripts/setup.sh` (pip packages plus a ~460 MB speech model from GitHub).
- `voicestudio` — drive a running VoiceStudio backend (github.com/debpalash/VoiceStudio v0.5.8, AGPL-3.0, `LICENSE` included): local text-to-speech with saved or designed voices, transcription, dubbing and narration via its REST API or MCP server at `localhost:3900`. Needs the VoiceStudio app/backend running; the skill never downloads models or switches to a hosted provider without your say-so. (The project's `voicestudio-maintainer` skill is for contributing to its code and was not added.)

Video: code-drawn animation (HTML + MP4 from the same code)
- `animation` — story or explainer animated video: asks length, topic and style (default 30 s Storybook look), builds a self-contained HTML that plays with sound plus a deterministic frame-by-frame MP4, with a synthesized audio track and review rules. Optional voiceover (your recording or ElevenLabs) mixed in with the music ducked under it.
- `cinematic` — short Ghibli-style / classic Japanese feature-animation sequence: tapered ink lines, cel shading, painted watercolor/gouache backgrounds; same HTML + MP4 + synth audio pipeline, with art-direction and final polish checks.
