#!/usr/bin/env bash
set -euo pipefail

REPO="${CONTENT_FLYWHEEL_REPO:-76776198xiong-stack/hermes-content-flywheel-skill}"
BRANCH="${CONTENT_FLYWHEEL_BRANCH:-main}"
DEST="${HERMES_SKILLS_DIR:-$HOME/.hermes/skills}/social-media/content-flywheel"

log() {
  printf '%s\n' "$*"
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    log "Missing required command: $1"
    exit 1
  }
}

install_from_local() {
  local source_dir="$1"
  mkdir -p "$(dirname "$DEST")"
  rm -rf "$DEST"
  cp -R "$source_dir" "$DEST"
}

install_from_github() {
  need_cmd curl
  need_cmd unzip

  local tmp
  tmp="$(mktemp -d)"
  trap "rm -rf '$tmp'" EXIT

  local zip_url="https://github.com/${REPO}/archive/refs/heads/${BRANCH}.zip"
  log "Downloading ${zip_url}"
  curl -fsSL "$zip_url" -o "$tmp/repo.zip"
  unzip -q "$tmp/repo.zip" -d "$tmp"

  local extracted
  extracted="$(find "$tmp" -maxdepth 1 -type d -name '*hermes-content-flywheel-skill*' | head -n 1)"
  if [ -z "$extracted" ] || [ ! -d "$extracted/content-flywheel" ]; then
    log "Could not find content-flywheel in downloaded archive."
    exit 1
  fi

  install_from_local "$extracted/content-flywheel"
}

main() {
  if [ -d "content-flywheel" ] && [ -f "content-flywheel/SKILL.md" ]; then
    log "Installing from local checkout."
    install_from_local "content-flywheel"
  else
    log "Installing from GitHub."
    install_from_github
  fi

  chmod +x "$DEST/scripts/init_content_workspace.py" 2>/dev/null || true
  log "Installed content-flywheel to: $DEST"

  if command -v hermes >/dev/null 2>&1; then
    hermes skills list | grep content-flywheel || true
  else
    log "Hermes command not found in PATH. Start a new shell or verify Hermes installation."
  fi
}

main "$@"
