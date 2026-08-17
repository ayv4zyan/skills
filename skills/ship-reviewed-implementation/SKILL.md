---
name: ship-reviewed-implementation
description: Ship an implementation brief through configurable cold reviews, a pull request, and green CI.
disable-model-invocation: true
---

# Reviewed delivery

Orchestrate one implementation, **N** independent cold reviews, and one delivery
pass. After preflight, the parent only dispatches, waits, and reports. Each
dispatch is a fresh top-level agent; agents nested by invoked skills do not
count. Advance only through each **gate**.

## Preflight

Send this block exactly, then wait for one reply:

```text
Answer all items in one reply, by number or in order.

1. Where should the implementation run?
   1) The current checkout
   2) A new branch in this worktree
   3) A new branch in a separate worktree

2. How many additional independent code-review passes should run? Answer with a non-negative whole number; 0 means none.

3. What model and reasoning effort should handle each pass? Answer with both, for example: GPT-5.6 Sol Medium.
   3.1 Implementation
   3.2 Every additional code-review pass (skip if question 2 is 0)
   3.3 Delivery (final validation, PR publishing, and CI follow-through)
```

Answers map as: (1) workspace, (2) review count **N**, (3.1) implementation
model and effort, (3.2) review model and effort when N > 0, (3.3) delivery
model and effort. Accept one reply by number or in listed order. A single
answer to 3 applies to every applicable 3.x.

After a workspace answer, discover the default **base** branch and inspect the
checkout read-only:

- **Current checkout:** retain its worktree and branch; require a safe, non-base
  implementation branch.
- **New branch here:** create a dedicated branch in the current worktree.
- **Separate worktree:** create a dedicated branch and worktree and use it for
  every pass.

When any answer is missing, unsafe, unshippable, or invalid, explain and re-send
only those items with their original numbers, then wait. When re-sending any of
3.1–3.3, include question 3. Require **N** to be an integer at least 0; it
counts reviews beyond `$implement`'s built-in review. Question 3.2 applies only
when N > 0; a four-answer in-order reply is then workspace, N, implementation,
delivery. Accept human-friendly model spelling, canonicalize it, and
runtime-validate every model/effort pair.

Let **T = N + 2**. Substitute numbers in every pass announcement, status, and
report heading using:

- `Pass 1/T — Implementation`
- `Pass k+1/T — Review k/N` for k = 1…N
- `Pass T/T — Delivery`

For example, review 7 of 10 is `Pass 8/12 — Review 7/10`; when N = 0, use
`Pass 1/2 — Implementation` then `Pass 2/2 — Delivery`.

**Gate:** every applicable answer is valid. After delivery is selected, resolve
the brief without another confirmation.

## Run contract

The **brief**—the user's text plus every referenced spec, document, issue, or
work item—is scope and acceptance authority. Resolve every source. Preserve the
user's wording and links in each dispatch, including the complete brief, sources,
repository instructions, base, and workspace decision. Report instruction
conflicts; ask only when missing information would materially change the result.

Keep every pass in the chosen checkout on one non-base branch; the base is
read-only comparison and PR target. Preserve unrelated user work and block
mutation in an unsafe worktree. Run sequentially; retire each agent when its
dispatch completes.

## Implementation

Announce `Pass 1/T — Implementation`, then spawn the implementation agent with
the selected model and effort. Require it to:

1. Realize the workspace decision and report the checkout's absolute path and
   branch; all later commands run there.
2. Use `$implement` for the entire brief, including suitable tests, validation,
   built-in review, and commit. That review does not reduce N.
3. Report a requirement-to-change map, commits, and validation evidence.

**Gate:** non-base working branch; every acceptance criterion implemented or
explicitly blocked; relevant validation passing; intended changes committed;
every claim evidenced.

## Cold reviews

A **cold review** receives no earlier findings or summaries. It reconstructs
context from its dispatch, current code, and the full base-to-branch diff.

For k = 1…N, announce `Pass k+1/T — Review k/N`, then:

1. Spawn a review agent with the selected review model and effort. Have it run
   `$code-review` on the entire branch against the base. Require Standards and
   Spec coverage of every requirement and changed file: correctness,
   regressions, completeness, edge cases, architecture, relevant security,
   reliability, and test gaps.
2. Require evidence for actionable findings. Wait, then have the same agent
   verify each against primary sources and observed behavior.
3. Have it classify every finding as **confirmed** or **rejected**, with
   evidence, and report that disposition. Wait for the report. The review
   agent leaves the tree unchanged.
4. When confirmed findings exist, spawn an implementation agent with the
   implementation model and effort. Send it the confirmed findings as the work.
   Require it to use `$implement` for those findings, including suitable tests,
   validation, built-in review, and commit.

Every requested review remains mandatory when earlier reviews find or change
nothing. N = 0 creates no review agents.

**Gate, each review:** both axes cover the full branch; every finding has an
evidenced disposition; confirmed findings are applied and committed by the
implementation agent; relevant validation passes; findings, dispositions,
commits, and validation are reported.

## Delivery

Announce `Pass T/T — Delivery`, then spawn the delivery agent with the selected
model and effort. Require it to:

1. Verify the brief, branch, commits, worktree, and full diff; exclude unrelated
   or unsafe artifacts: temporary, generated, debug, secret, and credential files.
2. Run final validation; fix and commit branch-caused failures.
3. Push the branch, setting its upstream if needed.
4. Create one PR into the base. Link any originating item; summarize the brief,
   implementation, reviews, and validation; record its number and URL.
5. Monitor every required check and diagnose failures from logs. Fix, validate,
   commit, and push branch-caused failures, then monitor replacement runs until
   green. Establish external or unrelated blockers with evidence.

**Gate:** intended work is committed and remote; the PR targets the base with the
latest commits; required checks are green or externally blocked with evidence;
no branch-caused required failure remains.

## Final report

Begin with:

| Decision | Selection |
| --- | --- |
| Workspace strategy | `<strategy>` — worktree `<directory name>` at `<absolute path>`; branch `<branch>` |
| Review passes | `<N>` |
| Implementation | `<model>` — `<reasoning effort>` |
| Review | `<model>` — `<reasoning effort>`, or `Not used — 0 additional passes` |
| Delivery | `<model>` — `<reasoning effort>` |

Use the current worktree's name and path when applicable. Then report the brief
or originating item and base; each runtime-labeled pass's work, findings,
dispositions, commits, and validation; publication and CI; brief completion;
remaining actionable findings; and whether intended work is committed, pushed,
and green.

End with the PR number and title; its clickable URL must be the final item.
