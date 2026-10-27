# claude-skills

Personal user-level Claude Code skills. The repo root is the skills folder, so on any machine:

```bash
git clone https://github.com/anithomas/claude-skills ~/.claude/skills
```

(Windows: clone into `C:\Users\<you>\.claude\skills`.) Restart Claude Code and every skill here loads in every project.

## Rule
All user-level (general-purpose) skills live here, never in a project repo. Project repos keep only skills that are specific to that project (e.g. `logicmanse-site` keeps `apply-design-patch`).

## Skills
- `find-skills` — discover and install skills via the `npx skills` CLI (from vercel-labs/skills).
- `video-sound-design-editor` — three-pass sound design (whooshes, textures, risers/hits) with level targets.
