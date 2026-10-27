---
name: full-send
description: Use only when the current user’s operative request contains the standalone sentence “full send” (case insensitive, optional final . ! or ?, whitespace or newline variations). Run the full reviewed implementation and delivery cycle. Do not activate for embedded phrases, quotations, code, reported examples, or discussion of the trigger itself.
---

# Full send

## Activation

Apply this skill only to the current request when the user uses `full send` as an operative standalone sentence. Match case insensitively, allowing whitespace or a newline between the words and an optional final `.`, `!`, or `?`. The sentence must stand on its own at a real sentence boundary, including on a separate line; a comma or semicolon does not make an embedded phrase a standalone sentence. Quoted text, code, reported examples, and discussion of the phrase do not invoke it. Naming the skill alone does not bypass this gate.

Matches: `Change button color. full send.` and `Change button color. Full send`.
Does not match: `Send the full report`, `full send mode`, `Change the button, full send`, or a request to explain “full send”.

## Workflow

Apply these rules to the requested implementation, whether it comes from an issue or a direct task. Honor the user's applicable overrides and constraints.

1. Implement and verify the requested changes. Do not force a workaround merely to produce a fix; ask when something needed is unavailable. Verify every web interface change using browser use, and add a UI element only when it has a clear purpose. If implementing an issue, assign it to the user.
2. After verification, create a separate-context subagent using `gpt-6.1-sol` with `high` reasoning effort to audit the implementation. Evaluate its findings against evidence; challenge incorrect findings with your reasoning. Fix every confirmed problem, including unrelated ones, and tell the user about additional fixes. Ask the same reviewer to verify all fixes; repeat until that reviewer confirms all findings are resolved.
3. Commit and push the branch, then create a pull request using the global skill named `PR`. If that skill cannot be found, stop and tell the user it is missing. If the PR skill classifies merge danger as `two-way`, merge the pull request yourself. For other classifications, follow the PR skill and applicable instructions.
