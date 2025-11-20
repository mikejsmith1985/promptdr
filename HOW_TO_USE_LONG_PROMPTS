### How to use long / multi-line / rage prompts (the right way)

| Method                  | Command                                                                                     | Works in VS Code WSL terminal? | Notes
|-------------------------|---------------------------------------------------------------------------------------------|--------------------------------|-------------
| Short prompts           | `pdr hello world`                                                                           | Yes                            | Instant
| Long prompts (recommended) | `pdr << 'EOF'`<br>`your entire wall of text`<br>`EOF`                                       | Yes                            | **Never fails** — no quotes, no carrot, no length limit
| Single quotes fallback  | `pdr 'your entire wall of text'`                                                            | Usually                        | Works unless VS Code terminal mangles quotes
| Pipe from file          | `echo "your prompt" > /tmp/prompt.txt && pdr < /tmp/prompt.txt`                             | Yes                            | Great for saved prompts

**Use the here-document (`<< 'EOF'`) for anything longer than ~80 characters.**  
It is the only method that survives VS Code’s terminal bugs, unbalanced quotes, parentheses, and newlines — every single time.

Example:
```bash
pdr << 'EOF'
I'm not sure if you're focused on the right thing...
[your full Ollama 400-line rage here]
EOF