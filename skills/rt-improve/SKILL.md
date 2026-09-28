---
name: rt-improve
description: Simplify existing code, improve performance, and refine UI motion while preserving functional behavior. Use when explicitly asked to apply rt-improve to a page, component, module, or flow; the focus is cleanup and refinement, not new features or redesign.
---

# RT Improve

Make the requested code easier to understand, maintain, and reason about. Improve performance primarily by doing less work. A worthwhile cleanup reduces the number of states, dependencies, subscriptions, conversions, or lifecycle rules a maintainer must understand.

The user's preference: **simplification that reduces edge cases takes priority over clever optimization**. A small speed gain is not worth a cache, synchronization mechanism, or new set of failure modes. Preserve functional behavior and interaction semantics; scoped motion refinements described below are part of this skill. Other behavior changes require an explicit request or a demonstrated problem within scope.

## Review the actual work

Read repository instructions, inspect existing changes, and trace the target's data and state flow before editing. Follow the project's architecture and public APIs; preserve unrelated work. Inspect dependencies enough to understand what a hook or helper actually starts, subscribes to, or updates.

Look for concrete sources of complexity or wasted work:

- Broad hooks that fetch unrelated data or initialize unused state.
- Subscriptions placed above the components that need their updates.
- Copied server data, stored derived values, and effects that synchronize avoidable duplicate state.
- Repeated serialization/parsing, unnecessary allocations that break stable props, and duplicated configuration.
- No-op handlers, redundant wrappers, stale branches, unsafe casts, and abstractions with no current benefit.

Distinguish unnecessary machinery from safeguards that preserve correctness. Understand loading, save, reset, error, and asynchronous ordering behavior before removing guards or effects.

For dialogs and other dismissible UI in scope, trace the supported close paths: cancel, Escape, backdrop dismissal, successful submission, and failure. Check which callback owns dismissal and whether it clears state or unmounts the component before an existing exit animation finishes. Check that state-dependent classes preserve base classes and activate the intended styles. Treat broken lifecycle behavior as a scoped correctness issue; preserve intentional close timing and error semantics.

## Prefer structural simplification

Remove unused work first. Narrow dependencies and subscriptions, keep state close to its owner, and use the project's existing data and form primitives. Extract a component when it gives updates a smaller scope or establishes a useful ownership boundary. Keep single-use logic local; extract shared code only for real reuse.

Use direct, typed representations. Avoid encoding values into strings and decoding them just to pass data between layers. Reuse a validated public helper when it replaces duplicated logic or unsafe assertions. Retain stable constants where useful, but do not pursue fewer lines at the expense of clarity.

Optimize only a concrete source of work. Do not blanket-add memoization, callback wrappers, global stores, or generic frameworks. Do not introduce caches, invalidation rules, debouncing, queues, retries, speculative fallbacks, or compatibility layers merely to claim a performance improvement. If a proposed optimization needs extra coordination or new behavioral rules, prefer leaving it out unless the task specifically requires it and its benefit justifies that complexity.

For list-heavy UI, inspect lists, tables, grids, and option menus for excessive mounted elements and establish expected data volumes. Before ruling out virtualization, verify representative volumes using fixtures, API data, or documented limits. If that evidence is unavailable, report virtualization as **unassessed**. A small test fixture or absence of reported slowness does not establish that virtualization is unnecessary. Distinguish code inspection, browser verification, and measured performance in the final report.

Consider virtualization when realistic data volumes show rendering or scrolling costs that justify the added complexity. Reuse existing virtualized components first; prefer TanStack Virtual where it fits the project. Preserve stable item identity, keyboard navigation, focus, selection, editing state, and scroll behavior. Avoid arbitrary item-count rules across unrelated components. Virtualization limits rendered elements; it does not itself reduce fetching or filtering work. Verify behavior with representative data and distinguish reduced mounted elements from measured performance gains.

Preserve necessary reset and persistence semantics. Do not change save timing, request ordering, offline behavior, or error handling incidentally during a refactor. Keep proven protections even when they make the implementation longer. Fix demonstrated bugs in scope with the smallest coherent change; avoid accumulating hypothetical edge-case handling.

## Refine motion where it helps

For UI targets, assess existing transitions and opportunities for useful new motion. Read the available `transitions-dev` and `transitions-polish` skills, using `transitions-polish` to refine existing motion and `transitions-dev` to introduce transitions that improve feedback, continuity, or clarity. Read only relevant transition references. Keep the assessment and changes within the requested target; skip motion work for non-UI tasks. If a companion skill is unavailable, disclose that limitation and continue the independent cleanup.

For implementation requests, apply justified motion improvements as part of the requested work; review-only requests remain review-only. Reuse existing motion tokens and primitives, matching tokens by purpose rather than numerical proximity. Preserve reduced-motion support, keyboard and focus behavior, and immediate interaction feedback. Avoid decorative motion, unnecessary orchestration, and replaying entrance animations as virtualized rows remount. Leave effective transitions alone when changing them has no clear benefit.

Compare the target's actual entrance and exit behavior with nearby components serving the same purpose. Where an established pattern fits, reuse its timing, easing, movement, and reduced-motion behavior. Check visual consistency as well as functional completion; an animation running successfully does not establish that it fits the surrounding UI. Preserve intentional differences and keep changes within the requested target.

Verify changed motion in the browser when available, including rapid reversal or dismissal and reduced-motion behavior. Report any visual verification that could not be performed.

## Verify and finish

Implement the cleanup, rather than stopping at a review, unless the user requested review only. Keep the scope tied to the requested target; do not turn it into a migration, visual redesign, or dependency upgrade.

Run the checks required by the repository and appropriate to the changes. For state or persistence changes, use focused behavioral regressions for relevant loading, editing, saving, and reset behavior. Use existing flow tests where available. Do not add tests that merely reproduce implementation details or elaborate test infrastructure for trivial edits. Keep required coverage targets intact when moving or deleting helpers.

When cleanup changes UI callbacks, state ownership, or dismissal, verify the complete affected interaction through its actual caller. Hook or mutation tests alone do not establish that the visible flow works; verify dismissal and reopening where relevant, and do not infer one dialog's behavior from another dialog that uses different wiring.

Review the final diff for accidental behavior changes and abstractions that cost more than they save. Stop when the scoped cleanup is complete and relevant checks pass; do not keep inventing optimizations.

Report the concrete simplifications, the unnecessary work removed, and verification results. Distinguish structural improvements from measured performance gains; do not invent render counts, speedups, or benchmarks. State any remaining limitations plainly.
