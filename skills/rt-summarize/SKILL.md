---
name: rt-summarize
description: Summarize software issues and changes with defined entities, a high-level user-visible problem, and explicit before/after behavior. Use only when the user explicitly invokes rt-summarize.
---

# RT Summarize

Explain the issue or change from the user's perspective using established task evidence. Produce these four sections in order.

## Entities

Define the domain entities and interface controls needed to understand the summary. Give each a stable name and a concrete description. For a control, explain where the user encounters it and what it does: an "editor" should identify the actual editing popup or screen; a "filter" should identify the panel or control and the list it affects.

Include only terms needed by the following sections. Use these names consistently, defining any additional term before using it. Prefer explicit entity names over ambiguous references such as "it," "the screen," or "the data."

## Problem

Write one high-level sentence stating the unreliable or unavailable user capability. Name the affected control, its scope, and the entities or relationship it operates on. Keep the statement at the capability level; place concrete symptoms and examples in Before, and reserve causes and implementation details for a separately requested explanation.

Example:

> The cross-sell filter in a menu group does not reliably find dishes based on their cross-sell associations.

This level of abstraction must still identify the control: "cross-sells are broken" leaves the affected behavior unclear.

## Before

Describe observable behavior before the change, explicitly using the names defined in Entities. When an example helps, choose a concrete scenario and show what the user sees or can do. Explain counts and results separately when both matter.

## After

Describe observable behavior after the change using the same entity names, scenario, and comparison points as Before. Distinguish verified outcomes from expected behavior when the change is proposed or unverified.

## Final review

Check that every important term is defined, the Problem names the affected control at a high level, and Before and After provide a direct comparison. Keep the summary focused on user-visible behavior and proportionate to the issue.
