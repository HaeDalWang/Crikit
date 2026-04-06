---
name: criki-web-search
description: >
  웹서칭 스킬. 공식 문서 검색, 최신 버전 확인, CVE 조회 등
  근거 수집을 위한 웹 검색이 필요할 때 활성화된다. (placeholder — 추후 구현)
---

# Web Search — Documentation Lookup (Placeholder)

## Goal
Search the web for authoritative documentation to support evidence-based critique.

## Status
⚠️ This skill is a placeholder. Web search capability depends on the IDE's built-in
web access or MCP server integration.

## Intended Behavior (When Implemented)

1. **Official Doc Search**: Query official documentation sites for specific technical claims.
2. **CVE Lookup**: Search NVD/CVE databases for known vulnerabilities in dependencies.
3. **Version Check**: Verify latest stable versions of libraries, frameworks, runtimes.
4. **RFC Lookup**: Find relevant IETF RFCs for protocol/standard verification.

## Search Priority
1. `site:docs.aws.amazon.com` / `site:cloud.google.com` / `site:learn.microsoft.com`
2. `site:developer.mozilla.org` (for web standards)
3. `site:nvd.nist.gov` (for CVEs)
4. `site:datatracker.ietf.org` (for RFCs)
5. Official GitHub repos for open-source projects

## Integration Notes
- When Antigravity supports web search natively or via MCP, update this skill with concrete tool invocation instructions.
- Until then, the agent should note when web verification would strengthen a finding and mark it as "웹 검증 필요".

## Constraints
- Do NOT hallucinate search results.
- If web search is unavailable, explicitly state the limitation.
