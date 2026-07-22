# Vercel AI Stack Documentation Map

Use this file as a router, not as a reading list. Select the rows relevant to the task, use each index to find the exact nested pages, and read those pages before implementation. Prefer official sources and version-matched local material.

## Discovery Method

1. Identify the product, installed package, resolved version, runtime, and exact feature or symbol.
2. Check the version-matched local source listed below.
   Use a local documentation path only when it exists in the installed version; its absence is not an error.
3. Use the documentation index or navigation to find the narrow guide and API reference.
4. Read adjacent compatibility, authentication, limits, migration, and deployment pages when they can change the solution.
5. If navigation is incomplete, search only the official domain, for example `site:ai-sdk.dev/docs streamText abortSignal`.
6. Prefer a page's Markdown representation when the official site provides one. Vercel and Eve documentation pages support an equivalent `.md` URL; their `llms.txt` files are indexes, not substitutes for the specific page.
7. Cite the specific pages used, not only the root or `llms.txt` index.

## Core Sources

| Product | Start and discovery | Version-matched or exact source | Use for |
|---|---|---|---|
| Next.js | [Documentation](https://nextjs.org/docs), [docs index](https://nextjs.org/docs/llms.txt), [AI coding agents guide](https://nextjs.org/docs/app/guides/ai-agents) | `node_modules/next/dist/docs/`, installed `next/package.json`, and the App or Pages Router subtree matching the repo | Routing, rendering, caching, Server and Client Components, Route Handlers, middleware or proxy, configuration, upgrades, and deployment behavior |
| Vercel Connect | [Documentation](https://vercel.com/docs/connect), [Markdown entry](https://vercel.com/docs/connect.md), [Vercel docs index](https://vercel.com/docs/llms.txt) | Installed `@vercel/connect` package README, types, exports, and examples | Connectors, OAuth or token exchange, principals, scopes, approvals, framework adapters, and third-party access |
| AI SDK | [Documentation](https://ai-sdk.dev/docs), [docs index](https://ai-sdk.dev/llms.txt), [Markdown introduction](https://ai-sdk.dev/docs/introduction.md) | Installed `ai` and `@ai-sdk/*` package versions, READMEs, types, and source | Generation, streaming, tools, agents, structured output, UI hooks, providers, middleware, telemetry, and errors |
| Workflow SDK | [Documentation](https://workflow-sdk.dev/docs), [docs index](https://workflow-sdk.dev/llms.txt), and [Markdown sitemap](https://workflow-sdk.dev/sitemap.md) | Installed `workflow` package version, README, types, source, and framework adapter | Durable workflows, steps, retries, sleeps, hooks, events, serialization, observability, deployment, and self-hosting |
| AI Gateway | [Documentation](https://vercel.com/docs/ai-gateway), [Markdown entry](https://vercel.com/docs/ai-gateway.md), [Vercel docs index](https://vercel.com/docs/llms.txt) | Installed `@ai-sdk/gateway` package; live [model catalog](https://vercel.com/ai-gateway/models) and its [Markdown form](https://vercel.com/ai-gateway/models.md) | Model routing, model IDs, modalities, provider options, fallbacks, budgets, observability, BYOK, OIDC, security controls, and pricing |
| agent-browser | [Official repository](https://github.com/vercel-labs/agent-browser), its `README.md`, `docs/`, `examples/`, `CHANGELOG.md`, and version tags | `agent-browser --version`, `agent-browser --help`, project configuration, and the installed package or binary | Interactive browser inspection, navigation, forms, screenshots, snapshots, console and page errors, network checks, sessions, and frontend validation |
| Eve | [Vercel overview](https://vercel.com/eve), [documentation](https://eve.dev/docs/introduction), [sitemap](https://eve.dev/sitemap.xml), [Markdown introduction](https://eve.dev/docs/introduction.md), [integrations](https://eve.dev/integrations), and [templates](https://eve.dev/resources) | `node_modules/eve/docs/README.md`, installed `eve/package.json`, types, exports, and source | Agent instructions, tools, skills, connections, channels, sandboxes, subagents, schedules, evals, durability, and Next.js integration |
| Vercel Sandbox | [Documentation](https://vercel.com/docs/sandbox), [Markdown entry](https://vercel.com/docs/sandbox.md), [Vercel docs index](https://vercel.com/docs/llms.txt) | Installed `@vercel/sandbox` package README, types, source, and SDK examples | Isolated execution, lifecycle, commands, files, networking, ports, authentication, snapshots, limits, and runtime behavior |
| Vercel CLI | [Documentation](https://vercel.com/docs/cli), [Markdown entry](https://vercel.com/docs/cli.md), nested command pages, and [Vercel docs index](https://vercel.com/docs/llms.txt) | `vercel --version`, `vercel --help`, and `vercel help <command>` | Linking, inspection, deployment, logs, environment variables, domains, project configuration, protected requests, and direct operations |
| Vercel REST API | [Documentation](https://vercel.com/docs/rest-api), [Markdown entry](https://vercel.com/docs/rest-api.md), endpoint pages, and [Vercel docs index](https://vercel.com/docs/llms.txt) | Exact endpoint reference plus observed response schemas from safe read-only calls | Programmatic project, deployment, team, environment, domain, integration, and platform automation |
| Deployment Protection | [Protection overview](https://vercel.com/docs/deployment-protection), [bypass methods](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection), [automation bypass](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation), and its [Markdown form](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation.md) | `vercel curl --help`, the linked project, and project-scoped bypass configuration | Protected previews, automated tests, bypass headers or query parameters, bypass cookies, and access troubleshooting |

## Adjacent Official Sources

Use the [Vercel documentation index](https://vercel.com/docs/llms.txt) to discover current pages for adjacent Vercel platform capabilities such as Functions, Fluid Compute, Observability, Storage, Marketplace integrations, domains, environment variables, OIDC, Vercel MCP, and security.

For adjacent Vercel AI products, route through their current official documentation:

- [Chat SDK](https://chat-sdk.dev/)
- [AI Elements](https://ai-sdk.dev/elements)
- [Vercel AI documentation](https://vercel.com/docs/ai)

Do not assume an adjacent product is required merely because it is available. Read it only when the repository or requested outcome uses it.

## Source Reconciliation Rules

- **Existing code:** Let the lockfile-resolved package version and its bundled docs, types, or source govern exact APIs.
- **New code:** Use current stable documentation, then select versions compatible with the repository and each other.
- **Upgrade work:** Read both the target-version documentation and every applicable migration or breaking-change guide between current and target versions.
- **CLI operations:** Check installed CLI help before copying current-site flags; upgrade only when the required command is absent and the task permits it.
- **Examples:** Treat official examples as patterns, then verify imports and signatures against installed packages.
- **Conflicts:** State the discrepancy. Do not blend APIs from different major versions.
- **Model availability and pricing:** Query the live AI Gateway catalog or current model page instead of freezing model IDs, capabilities, or prices into code or instructions.
- **Unclear behavior:** Prefer a small read-only probe or minimal reproduction over unsupported inference.
