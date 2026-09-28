# Agent skills

Reusable agent skills maintained by [@ayv4zyan](https://github.com/ayv4zyan).

## Install

Install interactively:

```bash
npx skills add ayv4zyan/skills --skill ship-reviewed-implementation
```

Install globally for Codex without prompts:

```bash
npx skills add ayv4zyan/skills --skill ship-reviewed-implementation --agent codex --global --yes
```

## Available skills

### `rt-improve`

Simplifies existing code, reduces unnecessary work, and refines useful UI motion
while preserving behavior. Favors changes that reduce state and edge cases.
Uses the separately installed `transitions-polish` and `transitions-dev`
skills for UI motion.
```bash
npx skills add ayv4zyan/skills --skill rt-improve --agent codex --global --yes
```

User-invocable only. Invoke with `$rt-improve` after installation, optionally
naming a project area to improve.

### `ship-reviewed-implementation`

Ships an implementation brief through a configurable implementation pass,
independent cold-review passes, pull-request creation, and green CI. Invoke it
explicitly with `$ship-reviewed-implementation` after installation.
