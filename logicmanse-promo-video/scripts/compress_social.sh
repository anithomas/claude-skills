#!/usr/bin/env bash
# Compress a render for Drive/Metricool upload (target <10 MB for a ~30s Short).
# Usage: compress_social.sh IN.mp4 OUT.mp4
set -euo pipefail
ffmpeg -y -loglevel error -i "$1" -c:v libx264 -crf 27 -maxrate 2000k -bufsize 4000k \
  -c:a aac -b:a 128k -movflags +faststart "$2"
