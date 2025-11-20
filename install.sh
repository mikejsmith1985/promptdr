#!/usr/bin/env bash
set -e

REPO="mikejsmith1985/promptdr"
TAG="latest"

case "$(uname -s)" in
  Linux*)   BINARY="pdr-linux" ;;
  Darwin*)  BINARY="pdr-macos" ;;
  CYGWIN*|MINGW32*|MSYS*|MINGW*) BINARY="pdr-windows.exe" ;;
  *) echo "Unsupported OS: $(uname -s)"; exit 1 ;;
esac

URL="https://github.com/$REPO/releases/$TAG/download/$BINARY"

mkdir -p "$HOME/bin"
curl -L "$URL" -o "$HOME/bin/pdr"
chmod +x "$HOME/bin/pdr"

# Ensure ~/bin is in PATH
if ! echo "$PATH" | grep -q "$HOME/bin"; then
  echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
  echo "Added ~/bin to PATH (run 'source ~/.bashrc' or restart terminal)"
fi

echo "PromptDr installed! Use: pdr <your prompt> or just paste raw text"