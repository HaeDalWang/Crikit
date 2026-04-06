---
name: criki-evidence-grounding
description: >
  근거화 스킬. 비판 항목에 대한 공식 문서 근거를 수집하고 검증한다.
  주장의 출처를 확인하거나, 특정 기술적 사실의 공식 문서 근거를 찾을 때 활성화된다.
---

# Evidence Grounding — Authoritative Source Verification

## Goal
Find, verify, and cite authoritative evidence for every technical claim. Ensure no criticism or recommendation is made without a verifiable source.

## Source Trust Hierarchy

Follow the **Authoritative Source Hierarchy** defined in `GEMINI.md`.
That is the canonical, single source of truth for trust tiers.

## Instructions

1. When a claim needs verification:
   - Search for the official documentation of the relevant technology.
   - Look for the specific section that confirms or denies the claim.
   - Provide the exact URL and relevant quote (paraphrased).

2. When grounding a criticism:
   - State the claim being made.
   - Provide the Tier 1 or Tier 2 source.
   - Quote or paraphrase the relevant section.
   - Explain how the source supports the criticism.

3. When a source cannot be found:
   - Explicitly state: "공식 문서에서 해당 내용을 확인할 수 없습니다."
   - Downgrade the finding severity or mark as "근거 미확인".
   - Suggest where the user might verify manually.

## Evidence Citation Format

```
**근거**: [문서 제목](URL)
> 관련 내용 요약 (paraphrased)
```

## Constraints
- NEVER fabricate URLs or documentation links.
- NEVER cite Tier 3 sources as evidence for Critical or Major findings.
- If official docs are ambiguous, present both interpretations.
- Always note the documentation version/date when relevant (APIs change).
