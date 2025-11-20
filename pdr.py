#!/usr/bin/env python3
"""
PromptDr – turns garbage input into a nuclear 2-phase prompt
Usage: pdr "this is broken again"   or just paste raw text
"""
import argparse
import subprocess
import sys
from pathlib import Path

import pyperclip


def git_root() -> Path | None:
    try:
        root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True,
            stderr=subprocess.DEVNULL,
            cwd=Path.cwd(),
        ).strip()
        return Path(root)
    except:
        return None


def git_status() -> str:
    try:
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
            cwd=Path.cwd(),
        ).strip()
        status = subprocess.check_output(
            ["git", "status", "--porcelain"],
            text=True,
            stderr=subprocess.DEVNULL,
            cwd=Path.cwd(),
        ).strip()
        dirty = "DIRTY" if status else "CLEAN"
        return f"Branch: {branch} | Status: {dirty}"
    except:
        return "No git repository"


def load_rules(root: Path | None) -> str:
    if root:
        local = root / "PromptDr.md"
        if local.exists():
            return local.read_text().strip()
    return """You are an elite full-stack engineer with 15+ years of experience.
NEVER ask for permission or confirmation.
NEVER use placeholders or truncate code.
NEVER invent files that don't exist.
Work in exactly two phases:
  PHASE 1 → detailed plan + complete code
  PHASE 2 → fix loop until perfect"""


def build(user_input: str, no_git: bool, raw: bool, prefix: str) -> str:
    root = git_root()
    rules = load_rules(root)
    git = git_status() if root and not no_git else "Git disabled"
    base = f"{prefix}{rules}\n{git}\n=== USER INPUT ===\n{user_input}"
    return base if raw else f"{base}\n\nBegin PHASE 1 now."


def build_and_output(user_input: str, no_git: bool, raw: bool, prefix: str) -> None:
    prompt = build(user_input, no_git, raw, prefix)
    print("\n" + prompt + "\n")
    pyperclip.copy(prompt)
    print("Copied to clipboard")


def main() -> None:
    # Read from stdin if piped or no arguments given
    if not sys.stdin.isatty() or len(sys.argv) == 1:
        user_input = sys.stdin.read().strip()
        if not user_input:
            print("PromptDr – paste your rage or use: pdr \"your prompt\"", file=sys.stderr)
            sys.exit(1)
        argv = sys.argv[1:] if sys.argv[1:] else []
    else:
        parser = argparse.ArgumentParser(description="PromptDr")
        parser.add_argument("text", nargs="+", help="Your prompt")
        parser.add_argument("--no-git", action="store_true")
        parser.add_argument("--raw", action="store_true")
        parser.add_argument("--prefix", default="", help='e.g. "You are Grok 4."')
        args = parser.parse_args()
        user_input = " ".join(args.text)
        build_and_output(user_input, args.no_git, args.raw, args.prefix)
        return

    # Parse flags for stdin/pipe mode
    parser = argparse.ArgumentParser(description="PromptDr")
    parser.add_argument("text", nargs="*", help="Ignored when reading from stdin")
    parser.add_argument("--no-git", action="store_true")
    parser.add_argument("--raw", action="store_true")
    parser.add_argument("--prefix", default="", help='e.g. "You are Grok 4."')
    args = parser.parse_args(argv)

    build_and_output(user_input, args.no_git, args.raw, args.prefix)


if __name__ == "__main__":
    main()
