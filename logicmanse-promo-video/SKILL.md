---
name: logicmanse-promo-video
description: Use when building and publishing a LogicManse Publications promo/marketing video (any title, long-form or Shorts) end to end: cue sheet, HyperFrames render, ElevenLabs voiceover, thumbnail, Drive link, Metricool post to all networks.
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

## 9. End-to-end pipeline (proven on the Leia Coloring Book Short, Nov 2026)
Run these in order; each step is idempotent (skip if its output already exists).
1. **Assets + cue sheet** (sections 1-5). Keep the VO script short: a ~25-30s Short needs about 60-70 words.
2. **Build in HyperFrames** (`hyperframes` skill): project at `<Title>\Output\hf-shorts\`, 1080x1920, GSAP paused timeline registered as `window.__timelines["main"]`. Hook = real photo of the subject first, then the art. Music bed at volume 0.15 under the voiceover.
3. **Voiceover from ElevenLabs** (not local Kokoro; Ani rejected that voice as dull). Tools: `creative_list_voices` then `creative_generate_speech`, model `eleven_v4`. Default voice: **Liz, voice_id `1Hdh5sdoicm1xyz0gQhD`** (young, cheerful, social-media). Backup: Mira `rdEyNni8e60Jlx1RsV9N`. Write the script with punctuation and a leading `[cheerful]` tag. Costs about 350 credits per take, so generate one take per voice. Fetch the mp3 with `creative_get_generations` (signed URL, expires), convert to wav with ffmpeg, then run `npx hyperframes transcribe` for word times and **retime scenes to the words** (ElevenLabs reads faster than Kokoro; the Leia VO was 25s vs 31s).
4. **Render**: `npx hyperframes check` (density/sub-composition warnings are cosmetic), then `npx hyperframes render -o <name>.mp4`.
5. **Timestamp every deliverable** (section 10) and save to `<Title>\Output\`.
6. **Thumbnail** (section 4) with the real photo inset. Save a stamped copy.
7. **Compress for social**: `scripts/compress_social.sh` (target under 10 MB; Chrome upload limit is 10 MB and `SendUserFile` rejects ~30 MB).
8. **Drive upload via the local sync folder (no browser).** Google Drive for Desktop is installed: `H:\My Drive\` is aniphilip@gmail.com (G: is the hotmail account; do not use it). Copy the stamped social MP4 and thumbnail with plain `cp` into the **theme subfolder** of `H:\My Drive\Social Posts\`: `Leia Books\` (Leia titles), `Cook Books\` (FTF recipe book and other cooking titles), `Low Content Books\` (log books, planners, everything else). Create a new theme folder if a new theme appears, and add it to this list. The parent folder `Social Posts` (id `1f7cgGkQARm6R1QMMdyvZ_DEfbR3XNNWE`) is shared as **Anyone with the link, Viewer** (already done), so every subfolder and file inherits public access (the Drive connector's `share_file` only supports users/groups, so this one-time share is manual). Then find each file's id with the Drive connector `search_files` (title contains the stamped name; wait up to a minute for sync) and confirm `get_file_permissions` shows `type: anyone`. Media URL = `https://drive.google.com/file/d/<id>/view?usp=sharing`. Never automate the Drive web UI in Chrome (froze every time).
9. **Publish via Metricool** (section 11).
10. **Report**: send the public URLs of each network post, and the stamped file paths.

## 10. Timestamped files
Every deliverable (final video, social copy, thumbnail, voiceover, cue sheets) gets a local-time stamp: `<name>_YYYY-MM-DD_HHMM.<ext>`. Use `scripts/stamp.py FILE...` (copies; originals stay, so existing Drive/Metricool links keep working). Never overwrite an earlier stamped file; a re-render gets a new stamp.

## 11. Metricool posting rules (brand `Logicmanse Publications`, blogId 7582300, timezone America/New_York)
- Call `getBrandSettings` first for blogId and timezone. Networks: facebook, instagram, tiktok, youtube. Skip Pinterest unless an image and board are supplied.
- `media` = the public Drive link (Metricool imports it). `videoThumbnailUrl` = the thumbnail's Drive link (Instagram/Facebook/YouTube; TikTok only on Business accounts).
- `facebookData.type = REEL`, `instagramData.type = REEL`, `youtubeData` = `{type: "short", title (<100 chars), madeForKids (see below), privacy: "public", category, tags}`, `tiktokData.privacyOption = PUBLIC_TO_EVERYONE`.
- **Always set the AI-content flags to true** (Ani's standing rule; his VO and art are AI): `instagramData.isAiGenerated`, `youtubeData.isAiGeneratedContent`, `tiktokData.isAigc`. They can't be edited after publishing.
- "Post now": Metricool rejects past times, so schedule 5-8 minutes ahead of the current America/New_York time (note: DST ended Nov 1, offset is -05:00). Confirm with `getScheduledPosts` that each network reads `PUBLISHED` and report the `publicUrl`s.
- Post text: hook line, what's inside, buy link, the A/B poll, hashtags. Do not claim anything the book doesn't contain.
- Don't automate Instagram/TikTok cover edits afterward: not possible from the web or Metricool once published.
- **One `createScheduledPost` per network** (not one post with all providers) so each gets its own caption, link treatment and hashtag set. Save all four captions first as a stamped `<name>-social-copy_<stamp>.md` next to the video.
- `youtubeData`: set `category` (`HOWTO_STYLE` for recipes, `EDUCATION` for workbooks, `ENTERTAINMENT` for coloring/activity books) and 8-10 `tags` (topic, title, `logicmanse`, `shorts`). `madeForKids: true` only for children's titles (Leia); cook books and log books are `false`. Title ends with `#shorts`. On TikTok set `title` and `commercialContentOwnBrand: true` (we promote our own book).

## 12. CTA site link: verify before every post
The CTA must point to the title's own page on logicmanse.ca, never a guess.
1. Find the slug from the live books index: `curl -sL https://www.logicmanse.ca/books/ | grep -oE 'href="/books/[^"]+"'`.
2. Confirm the page returns 200 and its `<title>` names the book: `curl -s -o /dev/null -w '%{http_code}' <url>`. Pull the real facts (recipe/page counts, formats, Etsy/Amazon buttons) from the page text for the caption.
3. Known pages: Leia `https://www.logicmanse.ca/books/leia-coloring-book/`; Family Table Favorites Vol. 1 `https://www.logicmanse.ca/books/family-table-favorites-vol1/` (72 recipes, 15 sections, 158 pages, Etsy PDF + Amazon paperback). Other book pages: `heart-health-log-book`, `renovation-repair-record-book`, `rental-property-record-book`. If a title has no page yet, stop and tell Ani instead of linking the home page.
4. Link treatment: Facebook and YouTube get the full clickable `https://` URL. Instagram and TikTok captions don't make links clickable, so write `👉 Link in bio: logicmanse.ca/books/<slug>`. Put the same URL in the video's end card text when it fits.
5. For a recipe video, name the recipe's page numbers in the book (from `book_data.json`), e.g. "Full recipe on pages 18-19".

## 13. Hashtags
- **Count**: 5 per post on every network (Instagram now caps at 5; 3-5 performs best on TikTok, Facebook and YouTube). Put them on the last line of the caption.
- **Mix**: 1 dish or subject tag + 1 cuisine/region tag + 1 broad category tag + 1 product tag + 1 audience/format tag. Examples:
  - Cook books: `#MasalaDosa #KeralaFood #SouthIndianFood #Cookbook #FamilyRecipes` (TikTok swaps the last for `#recipe`; YouTube swaps it for `#Shorts`).
  - Leia/children's: `#ColoringBook #KidsActivities #DogLovers #ScreenFreeFun #KidsBooks`.
  - Log books/planners: `#HealthTracker #LogBook #Planner #Organization #SelfCare` (adjust to the book).
- CamelCase on Facebook/YouTube for readability; lowercase is fine on Instagram/TikTok.
- No banned or spammy tags (`#follow4follow`, `#like4like`), no tag unrelated to the video, no brand tags of other companies.
- End with an engagement prompt before the hashtags (an A/B choice tied to real next content, e.g. "Comment 🥥 for coconut chutney or 🍲 for chicken stew & appam", only naming recipes that are in the book).

## 14. Cook book (FTF) cinematic recipe videos (proven on Masala Dosa, Nov 2026)
- Source data: `Cook Book Digital Product\Family Table Favorites HQ\01_Volume_1\Layout\book_data.json` (ingredients, steps, pages); hero photo from `01_Volume_1\Source_Photos\reference_imagineart_pics\`. Project lives at `04_Marketing\Social_Media\<Recipe>_Test\hf-<recipe>\`.
- **No real people's faces.** Ani rejected stock clips showing faces. Use faceless AI clips: vidIQ `vidiq_generate_video`, model `seedance-2-fast`, 720p, 9:16, 4s (120 credits each). Prompt pattern: "Cinematic vertical food film, macro close-up of <step>, warm golden window light, shallow depth of field, slow push-in. No people, no faces, no hands, no text." One clip per recipe step (soak, temper, masala, pour, fold, plated beauty shot); about 5-6 clips is ~600-720 credits, so state the total before submitting. Stretch a 4s clip to a 7s line with `data-playback-rate` (~0.56).
- Narration: Indian-accented voice **Dhara `ZbxPfVOKktgkLqi5LCBx`** (eleven_v4, `[warm]` tag), ~75 words for ~30s. If the API generation reports `failed`, Ani can download the take from the ElevenLabs flow page (saved as `New tts node.mp3` in Downloads).
- Music: cooking-style bed from `vidiq_generate_music` (25 credits), e.g. "warm cheerful cooking-show music, acoustic guitar and ukulele, hand percussion, bansuri flute, 100 bpm, instrumental", volume 0.22 under the VO.
- Film look: warm soft-light gradient, vignette, animated SVG grain, 190px letterbox bars, slow push-in on every clip, word-timed captions. End card over the plated beauty shot: book name, recipe pages, then post with the section 12 link.
- HyperFrames gotcha: never nest a timed `<video>` inside a timed wrapper (check error `video_nested_in_timed_element`); give the `<video>` itself `class="clip scene"` with `width/height:100%; object-fit:cover`.
