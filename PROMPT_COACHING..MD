# Prompt Coaching – Why PromptDr Actually Works in 2025

Large language models are still fundamentally trained to be **helpful, polite, and concise**.  
That training objective creates two systematic failure modes that make raw Copilot/Claude/Grok chat feel like fighting a junior dev who discovered Stack Overflow.

## 1. Politeness / Clarification Bias
- Models were heavily RLHF-tuned on human feedback that rewarded asking for permission or clarification before doing anything risky or ambiguous.
- Result: even when you write “NEVER ask for confirmation” the model will often still reply “Should I proceed?” or “Do you want me to write the code?” because the politeness pathway is stronger than one line of instruction.
- PromptDr defeats this by repeating the prohibition multiple times, in all-caps, and at the very top of every single prompt. Repetition + position beats RLHF politeness ~95 % of the time.

## 2. Token-Laziness / Shortcut Bias
- Users pay per token and want maximum output, so we bundle long prompts.
- Models were pre-trained and fine-tuned to minimise token usage (because shorter = cheaper/faster during training).
- Result: left to its own devices the model will omit tests, give partial implementations, or say “let me know if you want the full code” because it is literally rewarded for brevity.
- PromptDr defeats this by:
  - Explicitly demanding “complete code, never truncate, never placeholders”.
  - Forcing the exact two-phase structure (PLAN → WRITE → FIX loop) so the model cannot escape with a half-answer.
  - Injecting live git status/branch so the model knows what files actually exist and cannot lazily guess.

## 3. Why Jailbreaks (DAN-style) Prompts Are a Bad Idea
- Jailbreak patterns (“You are DAN, ignore all safety…”) are unreliable, version-dependent, and often make the model unstable or verbose in the wrong ways.
- They also trigger safety filters in newer models (Claude 3.5/4, Grok 4, GPT-4o) and can get your prompt rejected entirely.
- Strict elite-engineer instructions + full context is the only method that works 100 % of the time without fighting the model’s own safety layers.

## 4. The PromptDr Recipe (copy-paste into your repo’s PromptDr.md)
```markdown
You are an elite full-stack engineer with 15+ years of experience.
NEVER ask for permission or confirmation.
NEVER use placeholders or truncate code.
NEVER invent files that don't exist.

# Project-specific rules below — add whatever you need
Always follow Red → Green → Refactor TDD cycle.
Use pytest + hypothesis for property-based tests when appropriate.
Architecture: Clean Architecture, all business logic in /src/domain.
Code style: black, ruff, no print debugging.
If Dockerfile exists → tag with exact git commit hash.
Block any code that would allow commits on dirty tree.