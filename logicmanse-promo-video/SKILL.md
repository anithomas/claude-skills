---
name: logicmanse-promo-video
description: Use when building a LogicManse Publications promo/marketing video (any title, long-form or Shorts) from a blueprint or concept.
---
# LogicManse Promo Video Production

Use this whenever asked to build a promotional video (YouTube, Shorts, Reels, TikTok) for a LogicManse Publications title — coloring books, activity books, workbooks, log books, etc.

## 1. Find the title's asset folder first
LogicManse titles live under `C:\Users\aniph\OneDrive\claude\Low Content Multi books\<Title>\` (check memory/project notes for the exact path — paths have moved before). Look for a pre-organized assets folder (e.g. `Google_Vids_Assets/`) with scene-numbered subfolders matching an existing script/strategy doc — these are pre-vetted, people-free, rights-clear assets. Always build the cue sheet FROM these real files. If the folder isn't connected yet, call `device_request_folder_access` on the title's root folder (not just a subfolder) before doing anything else. If no asset folder exists at all, say so before inventing filenames — never fabricate asset paths.

## 2. Get a beat structure to adapt
Either take an existing blueprint/script (e.g. from vidIQ) as the structural starting point (hook/intro/problem/exploration/climax/conclusion/CTA beats with timings), or build the same beat shape from scratch. Flag immediately if the source blueprint's tone doesn't fit the title — e.g. a generic "24 HOURS / shock challenge" blueprint reused for a children's book needs rewriting to a warm, family-friendly tone, not the original's extreme-challenge framing. Don't silently keep a mismatched tone.

## 3. Build cue sheets — long-form AND Shorts, every time
Produce both: a long-form cut (full beat structure, ~4 min typical) and a ~45–60s Shorts/Reels cut (Hook + condensed montage + Climax + CTA only), as separate timed JSON files. Each beat references real asset filenames relative to the asset folder, plus on-screen text, VO line, and a sound cue (whoosh/texture/riser/music passes — match the project's existing sound-design convention if one is documented, e.g. the `video-sound-design-editor` skill's three-pass levels). Mark any beat that needs footage not yet in the asset pack with a `needs_filming` note instead of inventing it.

## 4. Build thumbnails from existing art — free by default
Pick a clean, text-free piece of existing cover/character art from the asset folder (not a cover image that already has baked-in title text). Use Python/PIL locally: crop to 1280x720 (long-form) and 1080x1920 (Shorts/cover frame), overlay bold high-contrast caption text (a bold Google-fonts family like Poppins-Bold; white fill + black stroke; an optional solid color bar for a secondary line). This costs nothing. Only call vidIQ's `vidiq_generate_thumbnail` (22 credits/call) if the user explicitly asks for AI-generated thumbnail options — check `vidiq_balance` first and report the cost before spending it.

## 5. Make the CTA earn its place
Before defaulting to generic "like and subscribe," check the title's project folder for a strategy/roadmap doc (e.g. a `*_Series_Strategy.md` file). If there's a real open go/no-go decision about a future title, turn the CTA into a simple A/B comment poll on that real decision ("more of X" vs "a new Y") — it drives engagement AND gives the user genuine market signal instead of noise. Only fall back to a generic CTA when no such real decision exists to tie into.

## 6. Save everything to the title's Output folder, not just chat
After sending each deliverable to the user via SendUserFile, also commit it into the title's own `Output/` subfolder on their OneDrive (via the device bridge's file-commit tool). Deliverables that only exist as chat attachments aren't done.

## 7. Pushing a concept into vidIQ
vidIQ's shared "blueprint" pages (vidiq.com/blueprint/...) are read-only snapshots — no edit UI on the page, and no MCP/API tool to modify one in place. To get a finished concept into the user's vidIQ account, use the vidIQ script-generation tool with the full title/concept/research reflecting everything built above. Check the vidIQ credit balance first and mention the cost (roughly 1 credit per minute of script) since this spends real account credits — the user's own request to "push this to vidIQ" counts as approval for that spend, but still report the balance and cost.

## 8. Keep repos and local-only projects separate
If the active project has its own git repo (e.g. `ftf-video-engine` for the FTF recipe-book videos), commit and push cue sheets/scripts there per that project's own CLAUDE.md conventions. Titles without a repo (e.g. the Leia coloring book) are OneDrive-local-only — don't mix the two: never push a different title's output into an unrelated project's repo, and don't assume every LogicManse title has or needs a repo.
