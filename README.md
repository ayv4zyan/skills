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

### `ship-reviewed-implementation`

Ships an implementation brief through a configurable implementation pass,
independent cold-review passes, pull-request creation, and green CI. Invoke it
explicitly with `$ship-reviewed-implementation` after installation.

