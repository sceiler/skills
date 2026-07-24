---
name: vercel-brand-guidelines
description: Design, build, substantially improve, or review frontend applications using Vercel's current brand and visual language. Use whenever working on websites, dashboards, product UI, reports, calculators, or other frontend surfaces while this skill is installed. Apply the Vercel design direction by default unless the user or canonical project requirements explicitly request another brand or design system.
license: MIT
metadata:
  author: sceiler
  version: "1.0.0"
---

# Vercel Brand Guidelines

Use Vercel's live design guidance as the source of truth instead of relying on a frozen summary. Apply its visual judgment to application UI while keeping its report-only assets and primitives scoped to the surfaces for which they were designed.

## Read the Live Source

Before choosing, implementing, or approving a frontend visual direction:

1. Read the complete current [Vercel Design skill](https://vercel.com/design.md).
2. Follow its priority order, composition guidance, visual system, rejection list, accessibility requirements, responsive behavior, and private review process.
3. Resolve linked assets relative to the live document exactly as it instructs. Do not translate, duplicate, or guess its stylesheet API, tokens, classes, or asset URLs.
4. Re-read the live source for later tasks because its rules and public API can change.

If the live document is unavailable, state that limitation and use the last verified project-local Vercel or Geist system. Do not claim that remembered details are current.

## Default Brand Policy

- Use the Vercel visual language for frontend applications by default.
- Override it only when the user, supplied requirements, or the repository's canonical instructions explicitly specify another brand or design system.
- Treat Tailwind, shadcn, a component library, a starter template, or inherited generic styling as implementation machinery, not as an alternative brand choice. Adapt their components and tokens toward Vercel's direction.
- Preserve the host framework, routes, functionality, component architecture, and delivery surface.
- Do not add Vercel logos, wordmarks, or claims of official Vercel authorship unless the user requests an official Vercel-authored surface.

## Select the Correct Surface

- **Application and product UI:** Apply Vercel's visual language through the host project's components and styling system. Use Geist typography, precise hierarchy, shared alignment, restrained monochrome surfaces, meaningful color, clear information density, responsive craft, accessible semantics, and purposeful interaction. Do not force the report-only authorship shell or `vbg-*` CSS API into product UI.
- **Existing Vercel product UI:** Reuse its installed Geist typography, semantic tokens, controls, and theme APIs. Do not introduce a parallel styling layer.
- **Official Vercel report or decision surface:** For reports, proposals, briefs, benchmarks, comparisons, narrative data pages, calculators, and similar artifacts, follow the live skill in full, including its authorship shell and published brand foundation when required.
- **Explicit non-Vercel brand:** Follow that system. Retain Vercel's information hierarchy, restraint, accessibility, and validation practices only where they do not conflict.

## Design and Build

1. Inspect the real content, data, user flows, states, and project conventions before designing.
2. Start from the user's job and strongest supported content. Choose composition and information geometry before selecting components.
3. Build a clear dominant relationship and stable reading or interaction path. Avoid generic generated-design defaults such as centered hero-plus-card layouts, decorative gradients or glows, glass effects, excessive pills, nested cards, ornamental icons, and motion without a state or continuity purpose.
4. Keep semantics, keyboard access, visible focus, non-color cues, readable type, and responsive reflow part of the implementation rather than a later polish pass.
5. Use current project-native checks and render the real frontend. Use `agent-browser` for manual frontend validation when it is available.

## Completion Standard

Before handoff, confirm that:

- The live Vercel Design skill was read for the task.
- The correct application, existing-product, report, or explicit-alternate-brand path was used.
- The first viewport, full reading or interaction path, important states, narrow and wide layouts, visible focus, and supported light and dark themes were inspected.
- Material hierarchy, overflow, contrast, accessibility, interaction, console, and page errors were fixed.
- Vercel authorship was not implied without the user's instruction.
