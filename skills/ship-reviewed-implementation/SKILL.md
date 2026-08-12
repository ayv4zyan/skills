---
name: ship-reviewed-implementation
description: Ship an implementation brief through configurable cold reviews, a pull request, and green CI.
disable-model-invocation: true
---

# Reviewed delivery

Orchestrate one implementation, **N** independent cold reviews, and one delivery
pass. Give each pass a fresh top-level agent; agents nested by invoked skills do
not count. After preflight, the parent only dispatches, waits, and reports.
Advance only through each **gate**.

## Preflight

Ask one question per turn, in this order, and wait after each. Append “Answer
with both, for example: GPT-5.6 Sol Medium.” to every model question:

1. **Workspace:** Ask exactly:

   ```text
   Where should the implementation run?

   1) The current checkout
   2) A new branch in this worktree
   3) A new branch in a separate worktree
   ```
2. **Review count:** “How many additional independent code-review passes should
   run? Answer with a non-negative whole number; 0 means none.”
3. **Implementation:** “What model and reasoning effort should handle
   implementation?”
4. **Review, only if N > 0:** “What model and reasoning effort should handle
   every additional code-review pass?”
5. **Delivery:** “What model and reasoning effort should handle final validation,
   PR publishing, and CI follow-through?”

After the workspace answer, discover the default **base** branch and inspect the
checkout read-only:

- **Current checkout:** retain its worktree and branch; require a safe, non-base
  implementation branch.
- **New branch here:** create a dedicated branch in the current worktree.
- **Separate worktree:** create a dedicated branch and worktree and use it for
  every pass.

Repeat an unsafe or unshippable workspace answer. Require **N** to be an integer
at least 0; it counts reviews beyond `$implement`'s built-in review. Skip
question 4 when N = 0. Accept human-friendly model spelling, canonicalize it,
and runtime-validate every model/effort pair; explain and repeat invalid answers.

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
mutation in an unsafe worktree. Run sequentially; retire each agent after its
gate.

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

1. Spawn a review agent with the selected model and effort. Have it run
   `$code-review` on the entire branch against the base. Require Standards and
   Spec coverage of every requirement and changed file: correctness,
   regressions, completeness, edge cases, architecture, relevant security,
   reliability, and test gaps.
2. Require evidence for actionable findings. Wait, then have the same agent
   verify each against primary sources and observed behavior.
3. Have it fix every confirmed finding, using `$tdd` where appropriate; update
   tests, validate, and commit. Reserve `$implement` for implementation.
4. Classify every finding as **fixed** or **rejected**, with evidence. With no
   confirmed findings, leave the tree unchanged and create no commit.

Every requested review remains mandatory when earlier reviews find or change
nothing. N = 0 creates no review agents.

**Gate, each review:** both axes cover the full branch; every finding has an
evidenced disposition; confirmed findings are fixed and committed; relevant
validation passes; findings, dispositions, commits, and validation are reported.

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
