#!/usr/bin/env bash
set -e

OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

case $OS in
  linux)  BINARY="pdr" ;;
  darwin) BINARY="pdr-mac" ;;
  mingw*|cygwin*|msys*) BINARY="pdr.exe"; OS="windows" ;;
  *) echo "Unsupported OS: $OS"; exit 1 ;;
esac

URL="https://github.com/mikejsmith1985/promptdr/releases/latest/download/$BINARY"
DEST="$$ HOME/bin/pdr $${BINARY#*.pdr}"  # keeps .exe on Windows

mkdir -p "$HOME/bin"
curl -L "$URL" -o "$DEST"
chmod +x "$DEST"

echo "PromptDr installed to $DEST"
echo "Run: pdr \"your prompt here\""