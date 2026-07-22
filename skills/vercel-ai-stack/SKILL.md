---
name: vercel-ai-stack
description: Build, review, debug, configure, deploy, or validate applications using the Vercel AI stack with current official documentation. Use whenever a task involves one or more of Next.js, AI SDK, AI Gateway, Workflow SDK, Vercel Connect, Eve, Vercel Sandbox, agent-browser, Vercel CLI or REST API, Vercel deployments, or protected preview access, even when only one of them appears.
license: MIT
metadata:
  author: sceiler
  version: "1.0.0"
---

# Vercel AI Stack

Use current, task-specific sources instead of relying on training knowledge. Treat documentation roots as indexes: discover and read the nested guides, API references, examples, and version notes required for the task before writing code or changing Vercel state.

## Documentation-First Workflow

1. Establish repository context.
   - Read the repository's canonical agent instructions.
   - Inspect manifests, lockfiles, imports, framework configuration, and `.vercel/project.json` when present.
   - Determine installed versions, the package manager, the Next.js router, the deployment target, and which Vercel AI products are actually involved.
   - Preserve the existing architecture unless the user requests a migration.

2. Route to current sources.
   - Read [references/documentation-map.md](references/documentation-map.md).
   - Select only the product sections relevant to the task.
   - Prefer sources in this order:
     1. Version-matched documentation bundled with the installed package.
     2. The relevant nested page in current official documentation.
     3. The official repository documentation, examples, changelog, or release notes for the installed version.
     4. Installed package types and source when documentation leaves an exact signature or behavior unclear.
   - Use official documentation indexes, site navigation, linked pages, and official-domain search to discover nested material. Do not stop at a product landing page.

3. Read enough to act correctly.
   - Read the task's concept or getting-started page plus the exact guide or API reference for the feature being used.
   - Check migration, compatibility, runtime, authentication, limits, and deployment pages when they can affect the implementation.
   - Follow relevant links from the selected page instead of guessing missing details.
   - Reconcile current live documentation with the installed version. Use version-matched behavior for the existing code; use current migration guidance when upgrading.
   - Record the direct pages that informed non-obvious decisions.

4. Implement within the requested scope.
   - Use the repository's package manager and established patterns.
   - Do not install `latest`, replace frameworks, or change providers solely because current docs describe a newer path.
   - Inspect the linked Vercel project and team before applying configuration or deployment changes.
   - Treat environment, domain, integration, billing, project, team, and REST API writes as state-changing operations. Perform them only when the user's task authorizes them.
   - Keep tokens, API keys, connection credentials, and protection-bypass secrets out of source, logs, command output, URLs, and final responses.

5. Verify the complete path.
   - Run the repository's relevant lint, typecheck, tests, and production build.
   - Exercise changed APIs with real requests when safe.
   - Use `agent-browser` for browser-visible navigation, interaction, console errors, screenshots, and UI validation.
   - When deployment is part of the task, verify the actual preview or production artifact rather than stopping at a local build.
   - Report the exact documentation used, verification performed, deployment URL, and any remaining limitation.

## Product Selection Defaults

Apply these as defaults, not as permission to rewrite an existing application.

- **Next.js**: Use it as the application framework when it is already present or the user chooses it. Prefer its installed, version-matched documentation before online examples.
- **Eve**: Use Eve as the default framework for new AI agents. In existing non-Eve agents, preserve the current framework unless migration is requested.
- **AI SDK**: Use it for model calls, streaming, structured output, tools, and agent primitives. Verify the API against the installed major version.
- **AI Gateway**: Prefer it as the model-routing layer for AI SDK applications deployed on Vercel unless direct provider access is an explicit requirement. Verify model IDs, modalities, provider options, fallbacks, and security controls live.
- **Workflow SDK**: Use it when work must survive restarts, pause, resume, retry, wait for events, or run durably over time. Keep workflow and step boundaries consistent with current SDK restrictions.
- **Vercel Connect**: Use it for user- or app-authorized access to supported third-party services. Verify connector, principal, token, scope, and framework-specific integration details.
- **Vercel Sandbox**: Use it for isolated or untrusted code execution, generated code, ephemeral development environments, or agent-controlled shell work. Verify runtime, lifecycle, networking, authentication, and limits.
- **Vercel CLI**: Prefer it for linked-project inspection, direct developer operations, deployments, logs, environment management, and protected-deployment HTTP checks.
- **Vercel REST API**: Prefer it for programmatic, repeatable, or service-to-service platform automation. Verify the endpoint, API version, scope, target team/project, pagination, and response schema before writing.
- **Adjacent products**: Follow current official documentation for related products such as Chat SDK, AI Elements, Vercel Functions, Observability, Storage, or Vercel MCP when the task leads to them. Do not load all adjacent documentation preemptively.

Do not conflate these boundaries. AI SDK provider support does not prove AI Gateway supports the same provider or modality. Vercel Connect authorization does not prove the resulting identity can access a third-party resource. A successful local build does not prove the deployed runtime or protected preview works.

## Frontend Validation with agent-browser

Use `agent-browser` as the default manual browser-inspection path for local, preview, and production frontends.

1. Inspect the installed command surface with `agent-browser --help` when syntax may have changed.
2. Open the real page and capture an interactive snapshot.
3. Exercise the user-visible flow, including loading, success, empty, and error states implicated by the change.
4. Inspect browser console errors, page errors, and relevant network requests.
5. Check the viewport sizes involved in the task and capture screenshots when visual evidence is useful.

Continue to run an existing Playwright, Cypress, or other formal end-to-end suite for regression coverage. Do not create an ad hoc browser script when `agent-browser` can perform the manual check directly.

## Protected Vercel Deployments

Distinguish Vercel control-plane authentication from deployment access. A valid CLI or REST token does not by itself bypass Vercel Authentication on a preview URL.

- Prefer `vercel curl` from the linked project for HTTP and API checks because it can handle deployment protection automatically.
- For `agent-browser` or another browser-style tool, send `x-vercel-protection-bypass` with the project-specific `VERCEL_AUTOMATION_BYPASS_SECRET` on the first request.
- Also send `x-vercel-set-bypass-cookie: true` when later navigation or assets must remain authorized.
- Scope custom headers to the deployment origin. Do not send a bypass secret to unrelated origins.
- Prefer headers over query parameters. Use the documented query parameter only when the caller cannot set headers, because URLs can leak through history, logs, analytics, and referrers.
- Confirm that an ambient bypass secret belongs to the linked project before using it. Do not print its value.
- Treat an authentication page or redirect as an access-layer result until the bypass path has been verified, not as evidence that the application is broken.

Read the current deployment-protection and CLI pages in the documentation map before relying on exact flags or header behavior.

## When Documentation Is Unavailable

Do not silently fall back to memory.

1. Use installed docs, package README files, types, source, CLI help, and lockfile-resolved versions.
2. State which live source could not be reached and which local evidence replaced it.
3. Separate verified behavior from inference.
4. Avoid irreversible or production-facing changes until the relevant behavior is verified.

## Completion Standard

Before declaring the task complete, confirm that:

- The relevant current or version-matched documentation was read beyond its root page.
- Product boundaries and versions were verified rather than assumed.
- Implementation and configuration match the selected documentation.
- Automated checks and the real runtime or browser flow were verified in proportion to the change.
- Secrets were not exposed.
- The final response links the direct documentation pages used and, when applicable, the URL where the deployed change can be tested.
