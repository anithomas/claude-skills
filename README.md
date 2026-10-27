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
