---
name: ship-reviewed-implementation
description: Ship an implementation brief through configurable cold reviews, a pull request, and green CI.
disable-model-invocation: true
---

# Reviewed delivery

Run one implementation pass, **N** independent cold-review passes, and one
delivery pass on a single checkout. Use a fresh top-level agent per pass; agents
nested by invoked skills do not count. After preflight, the parent only
dispatches, waits, and reports. Complete each pass's **gate** before advancing.

## Preflight

Ask one question per turn, in this order, and wait after each:

1. **Workspace:** “Where should the implementation run: the current checkout, a
   new branch in this worktree, or a new branch in a separate worktree?”
2. **Review count:** “How many additional independent code-review passes should
   run? Answer with a non-negative whole number; 0 means none.”
3. **Implementation:** “What model and reasoning effort should handle
   implementation? Answer with both, for example: GPT-5.6 Sol Medium.”
4. **Review, only if N > 0:** “What model and reasoning effort should handle
   every additional code-review pass? Answer with both, for example: GPT-5.6 Sol
   Medium.”
5. **Delivery:** “What model and reasoning effort should handle final validation,
   PR publishing, and CI follow-through? Answer with both, for example: GPT-5.6
   Sol Medium.”

After the workspace answer, discover the default **base** branch and inspect the
checkout read-only. Interpret the choices as follows:

- **Current checkout:** retain its worktree and branch; accept only a safe,
  non-base implementation branch.
- **New branch here:** create a dedicated branch in the current worktree.
- **Separate worktree:** create a dedicated branch and worktree and use it for
  every pass.

Reject and repeat a workspace answer that is unsafe or cannot produce a PR.
Accept **N** only as an integer at least 0; it counts reviews beyond
`$implement`'s built-in review. Skip question 4 when N = 0. For every model
answer, accept human-friendly spelling, record the canonical model and effort,
and validate that combination against the runtime; explain and repeat invalid
answers.

Let **T = N + 2**. Substitute numbers in every pass announcement, status, and
report heading using:

- `Pass 1/T — Implementation`
- `Pass k+1/T — Review k/N` for k = 1…N
- `Pass T/T — Delivery`

Thus review 7 of 10 is `Pass 8/12 — Review 7/10`; when N = 0, use
`Pass 1/2 — Implementation` and `Pass 2/2 — Delivery`.

**Gate:** every applicable answer is valid. After delivery is selected, resolve
the brief without another confirmation.

## Run contract

The user's text and every referenced spec, document, issue, or work item form the
**brief**. Gather all referenced sources and preserve the user's wording and
links in every dispatch. Apply repository instructions and report conflicts.
Ask only when missing information would materially change implementation.

For every pass: the complete brief is scope and acceptance authority; the base
is read-only comparison and PR target; all work stays in the chosen checkout on
one non-base branch; unrelated user work is preserved; and an unsafe worktree
blocks mutation. Run passes sequentially and retire each agent when its gate
closes.

## Implementation

Announce `Pass 1/T — Implementation`, then spawn a fresh agent with the selected
model and effort. Give it the complete brief, sources, repository instructions,
and workspace decision. Require it to:

1. Realize the workspace decision and record the checkout's absolute path and
   branch; run all later commands there.
2. Use `$implement` for the entire brief, including suitable tests, validation,
   its built-in review, and commit. Its review does not reduce N.
3. Report a requirement-to-change map, commits, and validation evidence.

**Gate:** the checkout is on a non-base working branch; every acceptance
criterion is implemented or explicitly blocked; relevant validation passes;
intended changes are committed; every claim has evidence.

## Cold reviews

A **cold review** receives no earlier findings or summaries. It reconstructs
context from the complete brief and sources, repository instructions, current
code, and full base-to-working-branch diff.

For k = 1…N, announce `Pass k+1/T — Review k/N`, then sequentially:

1. Spawn a fresh agent with the review model, effort, and checkout. Have it use
   `$code-review` on the entire branch against the base. Require Standards and
   Spec coverage of every requirement and changed file: correctness,
   regressions, completeness, edge cases, architecture, relevant security and
   reliability, and test gaps.
2. Require evidence for each actionable finding. Wait, then follow up with that
   agent to verify every finding against primary sources and observed behavior.
3. Have it fix every confirmed finding, using `$tdd` where appropriate; update
   tests, validate, and commit. `$implement` is reserved for implementation.
4. Classify every finding as **fixed** or **rejected**, with evidence. With no
   confirmed findings, leave the tree unchanged and create no commit.

Every requested review remains mandatory even when earlier reviews found or
changed nothing. When N = 0, create no review agents.

**Gate, each review:** both axes cover the full branch; every finding has an
evidence-backed disposition; confirmed findings are fixed and committed;
relevant validation passes; the report contains findings, dispositions,
commits, and validation.

## Delivery

Announce `Pass T/T — Delivery`, then spawn a fresh agent with the delivery model,
effort, and checkout. Require it to:

1. Verify the brief, branch, commits, worktree, and full diff; exclude unrelated,
   temporary, generated, debug, secret, and credential files.
2. Run final validation and fix and commit branch-caused failures.
3. Push the branch, setting its upstream if needed.
4. Create one PR into the base. Link an originating item when present; summarize
   the brief, implementation, reviews, and validation; record its number and URL.
5. Monitor every required check. Diagnose each failure from logs. For a
   branch-caused failure, fix, validate, commit, push, and monitor the replacement
   run until green. For an external or unrelated failure, establish the blocker
   with evidence.

**Gate:** all intended work is committed and on the remote branch; the PR targets
the base and contains the latest commits; required checks are green or a verified
external blocker remains; no branch-caused required failure is unresolved.

## Final report

Begin with:

| Decision | Selection |
| --- | --- |
| Workspace strategy | `<strategy>` — worktree `<directory name>` at `<absolute path>`; branch `<branch>` |
| Review passes | `<N>` |
| Implementation | `<model>` — `<reasoning effort>` |
| Review | `<model>` — `<reasoning effort>`, or `Not used — 0 additional passes` |
| Delivery | `<model>` — `<reasoning effort>` |

Use the current worktree's name and path when applicable. Then give the brief or
originating item and base; each runtime-labeled pass's work, findings,
dispositions, commits, and validation; publication and CI outcomes; whether the
brief is complete; whether actionable findings remain; and whether all intended
work is committed, pushed, and green.

End with the PR number and title; its clickable URL must be the final item.
