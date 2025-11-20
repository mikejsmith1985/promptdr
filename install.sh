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

echo "PromptDr installed!"
echo ""
echo "Usage:"
echo "  Short prompts → pdr hello world"
echo "  Long / rage / multi-line prompts → use a here-document:"
echo "    pdr << 'EOF'"
echo "    your entire wall of text here"
echo "    EOF"
echo ""
echo "  Alternative (also safe):"
echo "    pdr 'your entire prompt in single quotes'"
echo ""
echo "The here-document (<< 'EOF') is the most reliable method in VS Code + WSL."
echo "It never fails — no matter how many quotes, parentheses, or newlines you have."