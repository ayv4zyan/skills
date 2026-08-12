---
name: ship-reviewed-implementation
description: Ship an implementation brief through configurable cold reviews, a pull request, and green CI.
disable-model-invocation: true
---

# Reviewed delivery

Run an implementation phase, the chosen number of review phases, and a delivery
phase on one brief and checkout. Use a fresh top-level agent for every pass;
nested agents created by skills do not count. After preflight, the parent only
dispatches, waits, and reports. Advance only through a pass's **gate**.

## Preflight

Ask these questions in order, one per turn, and wait for each answer:

- **Workspace:** “Where should the implementation run: the current checkout, a
  new branch in this worktree, or a new branch in a separate worktree?”
- **Review count:** “How many additional independent code-review passes should
  run? Answer with a non-negative whole number; 0 means none.”
- **Implementation:** “What model and reasoning effort should handle
  implementation? Answer with both, for example: GPT-5.6 Sol Medium.”
- **Review, only when the count exceeds 0:** “What model and reasoning effort
  should handle every additional code-review pass? Answer with both, for
  example: GPT-5.6 Sol Medium.”
- **Delivery:** “What model and reasoning effort should handle final validation,
  PR publishing, and CI follow-through? Answer with both, for example: GPT-5.6
  Sol Medium.”

Interpret the workspace decision as:

- **Current checkout:** keep its worktree and branch. Accept only a safe,
  non-base implementation branch.
- **New branch here:** create a dedicated branch in the current worktree.
- **Separate worktree:** create a dedicated branch and worktree; run every pass
  there.

After the workspace answer, discover the default **base** branch and use
read-only inspection to validate the strategy. If it is unsafe or cannot produce
a PR, explain and repeat that question. Accept the review count only as an
integer at least 0; it counts cold reviews beyond `$implement`'s built-in review.
When the count is 0, skip the review-model question. For each requested model,
accept human-friendly spelling, record the canonical model and effort, and
validate the combination against the current runtime. If an answer is invalid,
explain and repeat that question.

Set **N** to the review count and **T** to `N + 2`. Label every pass announcement,
status update, and report section:

- `Pass 1/T — Implementation`
- `Pass k+1/T — Review k/N`, for review `k` from 1 through `N`
- `Pass T/T — Delivery`

Substitute actual numbers in every label. For example, with `N = 10`, the
seventh review is `Pass 8/12 — Review 7/10`. With `N = 0`, use
`Pass 1/2 — Implementation` and `Pass 2/2 — Delivery`.

**Gate:** the workspace strategy, review count, implementation selection, and
delivery selection are valid; the review selection is also valid when `N > 0`.
After the delivery selection, resolve the brief without another confirmation.

## Brief and invariants

Treat the user's request—plain text or references to specs, documents, issues,
or other work items—as the **brief**. Gather every referenced source. Preserve
the user's wording and links in every pass dispatch. Apply repository
instructions and report conflicts. Ask only about missing information that
would materially change implementation.

Across all passes:

- Treat the brief and referenced sources as the scope and acceptance authority.
- Keep the base read-only as review comparison and PR target.
- Use one selected checkout and non-base working branch.
- Preserve unrelated user work; an unsafe worktree blocks mutation.
- Run one pass at a time and retire its agent when its gate closes.

## Implementation phase

Announce its runtime pass label, then spawn an agent with the implementation
selection. Have it:

1. Read the complete brief, sources, and repository instructions.
2. Realize the workspace strategy, recording checkout absolute path and branch.
3. Run all subsequent commands in that checkout.
4. Use `$implement` for the complete brief, including appropriate tests,
   validation, its built-in review, and commit. The built-in review does not
   reduce `N`.
5. Report a requirement-to-change map, commits, and validation evidence.

**Gate:** the recorded checkout is on a non-base working branch; every acceptance
criterion is implemented or explicitly blocked; relevant validation passes;
intended changes are committed; and every claim has evidence.

## Cold review protocol

A **cold review** reconstructs context from the complete brief, its sources,
repository instructions, current code, and full base-to-working-branch diff. It
receives no earlier review findings or summaries.

For each cold review:

1. Spawn a fresh agent with the review selection and checkout path. Have it use
   `$code-review` on the entire branch against the base. Require Standards and
   Spec coverage for every requirement and changed file, including correctness,
   regressions, completeness, edge cases, architecture, relevant security and
   reliability, and test gaps.
2. Require evidence for every actionable finding. Wait for the review, then
   follow up with the same agent to verify each finding against primary sources
   and observed behavior.
3. Have it fix every confirmed finding directly, using `$tdd` where appropriate;
   update tests, validate, and commit. Reserve `$implement` for the implementation
   phase.
4. Classify each finding as **fixed** or **rejected**, with evidence. If none are
   confirmed, leave the tree unchanged and create no commit.

**Gate:** both review axes cover the full branch; every finding has an
evidence-backed disposition; every confirmed finding is fixed and committed;
relevant validation passes; and the report includes findings, dispositions,
commits, and validation.

## Review phase

For `k` from 1 through `N`, announce its runtime pass label and run the cold
review protocol against the preceding pass's branch. Run all `N` reviews
sequentially; every one remains mandatory when earlier reviews found or changed
nothing. When `N = 0`, skip this phase and create no review agents.

## Delivery phase

Announce its runtime pass label, then spawn an agent with the delivery selection
and checkout path. Have it:

1. Verify the implemented brief, branch, commits, worktree, and full diff.
   Exclude unrelated, temporary, generated, debug, secret, and credential files.
2. Run final validation; fix and commit branch-caused failures.
3. Push the working branch, setting its upstream when needed.
4. Create one PR into the base. Link an originating work item when present;
   summarize the brief, implementation, reviews, and validation; record its
   number and URL.
5. Monitor every required check. For each failure, inspect logs and establish
   root cause. Fix a branch-caused failure on the same branch, validate, commit,
   push, and monitor the replacement run; repeat until green. For an external or
   unrelated failure, gather enough evidence to establish the blocker.

**Gate:** all intended work is committed and present on the remote branch; the
PR targets the base and contains the latest commits; required checks are green
or a verified external blocker remains; and no branch-caused required failure
is unresolved.

## Final report

Begin with this populated table:

| Decision | Selection |
| --- | --- |
| Workspace strategy | `<strategy>` — worktree `<directory name>` at `<absolute path>`; branch `<branch>` |
| Review passes | `<N>` |
| Implementation | `<model>` — `<reasoning effort>` |
| Review | `<model>` — `<reasoning effort>`, or `Not used — 0 additional passes` |
| Delivery | `<model>` — `<reasoning effort>` |

Use the current worktree's directory name and path when applicable. Then report
the brief or originating item and base. Report every pass under its runtime label
with its work, findings, dispositions, commits, and validation. Then report
publication and CI outcomes; whether the brief is complete; whether actionable
findings remain; and whether all intended work is committed, pushed, and green.

End with PR number and title; make its clickable URL the final item.

