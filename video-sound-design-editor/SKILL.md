---
name: video-sound-design-editor
description: Sound design video edits using a rigorous three-pass workflow for whooshes, textures, and risers/hits. Use when the user asks to sound design or add audio effects to video projects, edits, or compositions.
---
# Video Sound Design Editor

Sound design video projects by mapping audio to motion, events, and anticipation across three distinct passes.

## Core Philosophy
1. **Sound emphasizes motion**: Every sound emphasizes something visual (a slide, pop, change, transition, or build). If nothing happens on screen, no sound plays.
2. **Three jobs, three families**:
   - **Whooshes**: Movement (slides, pans, zooms, scene transitions).
   - **Textures**: Non-sliding events (pops, clicks, reveals, gear turns, UI updates).
   - **Risers & Hits**: Anticipation and resolution into the next segment.
3. **Levels discipline**:
   - Whooshes: -10 to -12 dB (never loud).
   - Textures: -6 to -7 dB.
   - Risers: -5 dB.
   - Music: -19 dB.
   - Voice: Always the king (dialogue is never covered).

## The Three-Pass Workflow

### Pass 1: Whooshes (Movement)
- Scan top-to-bottom for every zoom, text slide, object/image slide, camera pan, and scene transition.
- Align the peak of the chosen whoosh to the **fastest frame** of the movement.
- Set level to -12 dB (up to -10 dB for heavy movements).

### Pass 2: Textures (Events without sliding)
- Scan top-to-bottom for pops, clicks, reveals, letter-by-letter writes, and UI events.
- Match specific textures to events:
  - Clean UI/text pops -> `Pop`
  - UI clicks / color shifts -> `Sci-fi click` or `UI click`
  - Letter-by-letter / typewriters -> `Gears` (`tiny gearwheel` / `complex mechanism gizmo`)
  - New element reveals -> `Sci-fi impact`
- Set levels to -6 to -7 dB.

### Pass 3: Risers & Hits (Anticipation)
- Place the first riser about 5 seconds after the hook, blended into a cut with a hit underneath.
- Place risers and hits at segment changes, A-roll to B-roll transitions, and major topic shifts.
- Set level to -5 dB.

## Rules & Guardrails
- Never place music under animations or graphics (music belongs under talking heads only).
- Never use a whoosh for a pop or a pop for a slide.
- Never push any sound effect louder than the dialogue voice.
