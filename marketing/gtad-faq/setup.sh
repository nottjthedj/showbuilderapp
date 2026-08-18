#!/usr/bin/env bash
# Fetch the four display faces the infographics are typeset in and install them
# so headless Chromium can see them. Run once per machine before ./build.py.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$HERE/fonts"

base="https://raw.githubusercontent.com/google/fonts/main/ofl"
declare -A FONTS=(
  ["Oswald.ttf"]="$base/oswald/Oswald%5Bwght%5D.ttf"
  ["Inter.ttf"]="$base/inter/Inter%5Bopsz,wght%5D.ttf"
  ["BarlowCondensed-Bold.ttf"]="$base/barlowcondensed/BarlowCondensed-Bold.ttf"
  ["JetBrainsMono.ttf"]="$base/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"
)

for name in "${!FONTS[@]}"; do
  printf '%-28s ' "$name"
  curl -sSfL --max-time 60 -o "$HERE/fonts/$name" "${FONTS[$name]}"
  printf '%s bytes\n' "$(stat -c%s "$HERE/fonts/$name")"
done

mkdir -p ~/.fonts && cp "$HERE"/fonts/*.ttf ~/.fonts/ && fc-cache -f >/dev/null 2>&1 || true
echo "fonts installed — all four are SIL Open Font License 1.1"

# playwright-core drives an existing Chromium; it does NOT download a browser.
if [ ! -d "$HERE/node_modules/playwright-core" ]; then
  ( cd "$HERE" && npm init -y >/dev/null 2>&1 && npm i playwright-core --no-audit --no-fund )
fi
echo "ready — now run: python3 build.py && node shoot.js"
