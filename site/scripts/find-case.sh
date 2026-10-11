#!/usr/bin/env bash
# Prints the absolute path of the case folder the site should show.
# Order: HUB_CASE_DIR (a path) > HUB_CASE (a folder name at the workspace root)
#        > the single project folder made with tools/new-case.py > my-case.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

if [ -n "${HUB_CASE_DIR:-}" ]; then
  echo "$HUB_CASE_DIR"; exit 0
fi
if [ -n "${HUB_CASE:-}" ]; then
  if [ ! -d "$ROOT/$HUB_CASE" ]; then
    echo "find-case: folder '$HUB_CASE' not found at $ROOT" >&2; exit 1
  fi
  echo "$ROOT/$HUB_CASE"; exit 0
fi

projects=()
for exporter in "$ROOT"/*/tools/export-hub.py; do
  [ -e "$exporter" ] || continue
  dir="$(dirname "$(dirname "$exporter")")"
  case "$(basename "$dir")" in my-case|demo-case) continue ;; esac
  projects+=("$dir")
done

if [ "${#projects[@]}" -eq 1 ]; then
  echo "${projects[0]}"
elif [ "${#projects[@]}" -gt 1 ]; then
  echo "find-case: found ${#projects[@]} project folders; using $(basename "${projects[0]}"). Set HUB_CASE to choose another." >&2
  echo "${projects[0]}"
else
  echo "$ROOT/my-case"
fi
