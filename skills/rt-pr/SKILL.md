---
name: rt-pr
description: Commit, push, and open a pull request for existing task-related changes only; use when publication is requested without implementation or repair.
---

# RT-PR

Publish the changes already present in the checkout. This skill is strictly a delivery workflow: it must not alter the implementation.

## Non-negotiable scope

- Do not implement, modify, refactor, reformat, regenerate, fix, resolve conflicts, update dependencies, or run write-mode formatters/generators.
- Do not reset, clean, discard, stash, amend, rebase, or force-push. Preserve unrelated and pre-existing user work exactly as found.
- Treat the user’s request, referenced issue/spec, and repository diff as the scope authority. Do not invent missing requirements.
- If the diff is empty, incomplete, unrelated, ambiguous, or contains secret/credential material, stop before staging and report the evidence and concern.

## Workflow

1. Establish the checkout, current branch, remote, and default base branch. Inspect all relevant state read-only: `git status`, the full working-tree and index diffs, untracked paths, branch history, and the base-to-branch diff. Read repository instructions that govern the changed files.
2. Classify the existing changes by task relevance and completeness. A file is not task-related merely because it is changed or untracked. Inspect untracked files before considering them, and stop if the scope cannot be established safely.
3. Use a descriptive lowercase `agent/<meaningful-description>` branch. If already on a suitable `agent/` branch, keep it; otherwise create a new branch from the current checkout without changing file contents. Do not overwrite an existing branch or resolve a branch-name collision by force.
4. Stage only confirmed task-related files or hunks, using explicit paths or interactive staging for mixed files. Never stage unrelated, generated, temporary, debug, secret, or credential files. Review `git diff --cached`, `git diff --cached --check`, and the staged path list before each commit.
5. Create focused commits for the coherent groups that already exist, with clear imperative messages describing the actual changes. Do not split or rewrite content merely to manufacture focus. If changes are already committed on the task branch, do not create empty or replacement commits.
6. Run only relevant non-mutating verification available for the existing changes, such as diff checks and read-only tests/checks. Do not fix failures. Recheck `git status` afterward and record what ran, what passed, and any failure or omission.
7. Push the branch to its configured remote, setting its upstream when needed. Never force-push. If pushing is blocked, stop and report the exact error rather than changing history.
8. Open one pull request into the detected base branch using the available GitHub integration or `gh`. Use a specific title and a concise description with these sections:

   - **Problem** — the user-visible problem or task being delivered.
   - **Changes** — the committed changes, without claiming any work that was not present.
   - **Verification** — the checks run and their results, including anything not run.

## Completion report

Report the branch name, each commit hash and message, the PR URL, the base branch, verification evidence, and any concerns or limitations. If the workflow stopped, report the reason and the exact state left untouched.
