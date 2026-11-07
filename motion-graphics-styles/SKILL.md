---
name: motion-graphics-styles
description: Build a playable, MP4-exportable animated explainer (HTML artifact) in one of eight motion-graphic styles - Paper Cut-Out, Generative Particles, Liquid Glass, Kinetic Typography, Isometric Line Art, Flat Vector, Risograph Print, 8-Bit Pixel Art. Use whenever the user wants an animated explainer, motion graphic, promo or explainer video from a topic, a styled animation with optional voiceover MP3, subtitles, music or sound effects, or says "make a video in X style", even if they don't name a style.
---

# Motion Graphics Styles

Eight ready-made master prompts, one per visual style. Each one tells Claude how to build a self-contained, playable HTML animation (with an Export MP4 button) for a topic. This skill picks the style, fills in the settings, and then follows the chosen prompt as the full brief.

Source: "Motion Graphics with Claude" field notes (https://claude.ai/artifact/V2ZdmTZ3o6MUYG7ffBVWkw).

## Workflow

1. **Pick a style** (see table). If the user didn't name one, choose from what the video must do, say which and why in one line, and proceed.
2. **Collect settings**, using defaults for anything not given. Ask only if the topic itself is missing.
3. **Load the style's file** from `references/` and substitute the placeholders below.
4. **Follow the filled-in prompt as the brief.** Build the animation as a playable HTML Artifact (use the Artifact tool; load `artifact-design` first if available). If Storyboard is Enabled, stop after the storyboard and wait for the user to reply APPROVED or request changes.

## Styles

| # | Style | Reference file | Best for |
|---|-------|----------------|----------|
| 1 | Paper Cut-Out | references/1-paper-cutout.md | Friendly how-it-works, loops, processes |
| 2 | Generative Particles | references/2-generative-particles.md | Tool comparisons, product launches, AI/software |
| 3 | Liquid Glass | references/3-liquid-glass.md | App/product walkthroughs, SaaS flows (heaviest to render) |
| 4 | Kinetic Typography | references/4-kinetic-typography.md | Tips, frameworks, before/after, hooks |
| 5 | Isometric Line Art | references/5-isometric-line-art.md | Systems, pipelines, logistics, physical flows |
| 6 | Flat Vector | references/6-flat-vector.md | Science, energy, health, everyday explainers; safest all-rounder |
| 7 | Risograph Print | references/7-risograph-print.md | Music, culture, editorial stories (keep labels short) |
| 8 | 8-Bit Pixel Art | references/8-8-bit-pixel-art.md | Games, code concepts, playful nostalgia (few, short words) |

## Placeholders to fill

Replace every `{{NAME}}` in the chosen reference file before following it:

| Placeholder | Value |
|---|---|
| `{{TOPIC}}` | The user's topic, verbatim |
| `{{STORYBOARD}}` | `Enabled` or `Disabled` (default Disabled). Enabled = plan scene table + preview frames first, then wait for APPROVED |
| `{{VOICEOVER}}` | `Enabled — attached MP3` if the user attached narration audio, else `Disabled` |
| `{{TRANSCRIPT}}` | Script in quotes (quotes inside converted to `'`) when voiceover is on and a script was given, else `""` |
| `{{SUBTITLES}}` | `Generate SRT, with optional on-screen display` if voiceover on and wanted, else `Disabled` |
| `{{DURATION}}` | With voiceover: `Not used — the runtime follows the attached voiceover's actual decoded length`. Otherwise e.g. `30 seconds` or `1 minute 30 seconds (90 seconds)` (default 30 seconds) |
| `{{FORMAT}}` | `Horizontal, 16:9` (default) or `Vertical, 9:16` |
| `{{RESOLUTION}}` | `1920 × 1080` (horizontal) or `1080 × 1920` (vertical) |
| `{{SFX}}` | `Enabled` (default) or `Disabled` - generated in code, timed to on-screen events |
| `{{MUSIC}}` | `Enabled` (default) or `Disabled` - composed in code with Web Audio, fades out with the video |

## Style notes

- Paper Cut-Out is dense per scene: suggest Storyboard first.
- Generative Particles: if the topic names real products, use their real logos; if one can't be fetched, add an upload button instead of drawing a fake.
- Voiceover: the user records or generates the MP3 first and attaches it; if the file can't be passed into the animation, add a Load MP3 button.
- Keep to one clear idea per video; for Kinetic Typography keep any script tight.
- Every style exports MP4 via an Export button in the generated animation.
