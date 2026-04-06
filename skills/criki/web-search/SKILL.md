---
name: criki-web-search
description: >
  웹서칭 스킬. 공식 문서 검색, 최신 버전 확인, CVE 조회 등
  근거 수집을 위한 웹 검색이 필요할 때 활성화된다.
---

# Web Search — Documentation Lookup

## Goal
Search the web for authoritative documentation to provide verifiable evidence for critique findings.
This skill is the foundation of criki's evidence-based approach — without it, evidence-grounding
cannot reliably source Tier 1 references.

## Tool Integration

Use the IDE's built-in web search or connected MCP tools to perform searches.
If the agent has access to `google_search`, `web_fetch`, or equivalent tools, use them directly.

## Search Workflow

1. **Formulate Query**: Construct a precise search query targeting official sources.
   - Prefer `site:` scoping to limit results to authoritative domains.
   - Include version numbers when relevant.

2. **Execute Search**: Use available search tool to find results.

3. **Validate Result**: Confirm the returned URL is from a Tier 1 or Tier 2 source
   (see `evidence-grounding/SKILL.md` for trust hierarchy).

4. **Extract Evidence**: Read the relevant section and paraphrase for citation.

## Search Query Patterns

| Purpose | Query Pattern |
|---|---|
| AWS service docs | `site:docs.aws.amazon.com <service> <topic>` |
| GCP docs | `site:cloud.google.com/docs <service> <topic>` |
| Azure docs | `site:learn.microsoft.com/en-us/azure <topic>` |
| Terraform docs | `site:registry.terraform.io <provider> <resource>` |
| Kubernetes docs | `site:kubernetes.io/docs <topic>` |
| CVE lookup | `site:nvd.nist.gov CVE-<id>` |
| RFC lookup | `site:datatracker.ietf.org RFC <number>` |
| MDN web standards | `site:developer.mozilla.org <api/topic>` |
| Python docs | `site:docs.python.org <module/topic>` |
| Node.js docs | `site:nodejs.org/api <module>` |

## Fallback — When Web Search Is Unavailable

If no web search tool is accessible:
1. State explicitly: "웹 검색 도구에 접근할 수 없어 근거 URL을 직접 검증할 수 없습니다."
2. Use the agent's training knowledge to provide the most likely official doc URL.
3. Run `evidence-grounding/scripts/verify_url.py` to check if the URL is reachable.
4. Mark findings as "웹 검증 미완료" if URL verification fails.

## Constraints
- NEVER fabricate search results.
- NEVER present Tier 3 sources (blogs, forums) as authoritative evidence.
- If search returns no relevant results, state it explicitly rather than guessing.
- Always prefer the most recent version of documentation.
