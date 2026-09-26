---
name: rt-improve
description: Improve an existing app by polishing transitions, removing unnecessary renders, simplifying code, and selectively applying TanStack Virtual. Invoke explicitly for an improvement pass that prioritizes readability, responsiveness, and fewer edge cases.
---

# RT Improve

Make the existing app smoother, faster, and easier to understand while reducing
the number of states and edge cases its code must handle. Preserve intended
behavior and the app's design language. Run only when explicitly invoked by the user.

## Choose improvements by their total cost

Inspect the requested area, its state and data flow, existing motion, and project
conventions. If the request covers the whole app, identify its main interactions
and expensive paths before choosing changes. Implement worthwhile improvements
within the user's scope; do not force every technique into every app.

For each candidate, identify the concrete problem, the simplest fix, and any new
state, lifecycle, or synchronization work it would create. Prefer changes that
remove work or make invalid states impossible. Reject optimizations whose benefit
depends on extra edge cases or ongoing coordination.

Do not introduce application caches, mirrored data, invalidation schemes, or
background synchronization solely for a speculative speedup. Preserve existing
data freshness guarantees. First remove duplicate computation, redundant requests,
and unnecessary updates at their source.

## Fix clipped shadows

Inspect shadows and focus rings for unintended clipping, especially at scroll
container edges and inside overflow or containment wrappers. Fix the responsible
layout or reserve enough space for the shadow while preserving scrolling and
intentional content clipping. Verify the first and last items at both scroll ends,
including hover, focus, and changed motion states at representative viewport sizes.

## Polish motion

- Read and use `transitions-polish` for existing transitions. Match timing, easing,
  distance, scale, and blur to the interaction's purpose.
- Read and use `transitions-dev` to introduce transitions when they improve
  feedback, continuity, or understanding. Load only the relevant recipes. Skip
  decorative motion that adds distraction, latency, or orchestration complexity.
- Resolve these skills from the installed skill catalog rather than hardcoding
  machine-specific paths. If either is unavailable, report the missing dependency
  and continue independent improvements; do not claim to have used it.
- Reuse existing motion tokens and component lifecycles. Keep reduced-motion
  support, keyboard interaction, and focus behavior intact. Verify rapid repeated
  interaction and interrupted open/close sequences for changed transitions.
- Prefer CSS and existing state hooks. Avoid adding timers or parallel animation
  state when the same result fits the component's current lifecycle. Choose a
  simpler recipe when integration would create extra coordination.

Follow the user's existing authorization for implementation; an improvement
request should result in changes, while a review-only request should remain a
review. Honor explicitly requested approval checkpoints.

## Remove unnecessary renders

Trace what triggers updates and which components actually need the changing
data. Use the project's profiler or targeted instrumentation when available to
identify costly repeated work. Render count alone is not a performance result;
distinguish development checks from behavior that affects users.

Prefer structural fixes:

- Keep transient state close to the components that use it.
- Remove redundant derived state and effects that copy or synchronize values
  already available during rendering.
- Narrow subscriptions and context consumers to the data they need, using the
  project's existing mechanisms.
- Remove redundant state writes and effect chains. Keep stable item identities
  and avoid accidental remounts.
- Move invariant work outside render and avoid repeating expensive transforms
  for unchanged inputs when the dependency relationship is simple and explicit.

Use memoization only for an identified cost and a boundary where it can actually
prevent work. Respect existing compiler and framework optimizations. Avoid blanket
`memo`, `useMemo`, and `useCallback`, custom equality checks that can hide updates,
suppressed dependency warnings, and refs used to conceal reactive data. Verify
that changes still propagate correctly; fewer renders must not mean stale UI.

## Virtualize only when it pays off

Consider TanStack Virtual for lists, tables, or grids where representative data
shows that mounting or updating many offscreen items is a meaningful cost.
Check existing virtualization first. Small collections and cheap rendering do
not justify a new dependency by themselves.

Before adding it, establish a representative baseline and inspect the installed
framework and package versions. Use current official TanStack Virtual documentation
for the appropriate adapter and APIs. Reuse the existing data source and loading
model; virtualization should not require a second data store or cache.

Account for the features the collection actually supports: stable item keys,
variable sizes, resizing, filtering and sorting, keyboard navigation, focus,
selection or editing, and scroll position. If unmounted content would break
required accessibility, browser find, printing, or another existing capability,
prefer a simpler improvement unless the behavior can be preserved without adding
fragile workarounds. Do not build speculative infrastructure for absent features.

Compare the same interaction and data before and after. Keep virtualization only
when its benefit is meaningful and its integration satisfies the simplicity goal.

## Clean and unslop the code

Remove dead code, redundant branches, duplicated sources of truth, needless
wrappers, and abstractions that obscure straightforward logic. Verify usage before
deleting exports or behavior. Use clear names, direct control flow, and the
project's established patterns.

Consolidate duplication when it expresses the same rule; avoid generalizing code
that merely looks similar. Remove comments that restate obvious code and retain
those explaining constraints or decisions. Preserve validation, error handling,
and intentional behavior. Avoid unrelated rewrites and dependency churn.

## Verify and report

Run the project's relevant checks and exercise the interactions affected by the
changes. Add focused regression coverage when changing state, identity,
subscriptions, or virtualization behavior creates a concrete regression risk;
do not add tests that merely mirror implementation or cosmetic edits.

For performance changes, compare representative behavior under the same
conditions. Report measured improvements only when measured; distinguish structural
reductions in work from unverified speed claims. If runtime or profiling access
is unavailable, state that limitation and avoid speculative complexity.

Finish with a concise account of what changed, why it is simpler or better, what
was verified, and any material limitation. Briefly explain skipped techniques
when relevant, such as virtualization offering no useful gain for the current list.

## Suggest skill improvements only for material gaps

When the user asks what this pass teaches us about improving `rt-improve`, use
evidence from the actual work. Recommend a change only when it addresses an
important, reusable gap that would materially improve future decisions or prevent
a significant failure. There is no quota for suggestions.

Check the current instructions and relevant transition skills first. If following
an existing rule would have covered the issue, treat it as an execution mistake,
not a reason to add another rule. Exclude minor preferences, speculative risks,
project-specific details, and extra examples of principles already covered.

For each qualifying suggestion, briefly explain what happened, why the existing
guidance was insufficient, and the smallest proposed edit and its expected benefit.
Prefer clarifying, replacing, or removing instructions over appending more rules.
Keep project-specific lessons in project documentation.

If nothing meets this bar, say: "No important changes to rt-improve suggested by
this pass." A request for suggestions does not authorize editing the skill;
present the proposals and apply them only when the user requests it.
