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

### `full-send`

Model-invokable for an operative standalone sentence such as `Change button
color. full send.` Runs the reviewed implementation and delivery cycle, merging
the PR only if the PR skill classifies its merge danger as two-way.

### `full-stop`

Model-invokable for an operative standalone sentence such as `Change button
color. full stop.` Runs the same cycle through a PR; only the merge is omitted.

### `rt-summarize`

Explains software issues and changes using **Entities**, **Problem**, **Before**,
and **After**. Defines interface controls concretely and keeps the problem
statement at the level of the affected user capability. User-invocable only; invoke with
`$rt-summarize` after installation.

```bash
npx skills add ayv4zyan/skills --skill rt-summarize --agent codex --global --yes
```

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
