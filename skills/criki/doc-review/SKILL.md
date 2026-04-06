---
name: criki-doc-review
description: >
  문서 및 설계 비판 스킬. 아키텍처 문서, API 설계, 시스템 설계, PRD, 기술 문서에 대해
  검증, 평가, 검토를 요청하면 활성화된다. 논리적 일관성과 기술적 정확성을 검증한다.
---

# Document & Design Review — Adversarial Analysis

## Goal
Identify logical inconsistencies, technical inaccuracies, missing considerations, and architectural anti-patterns in design documents and technical specifications.

## Review Dimensions

### 1. Technical Accuracy (기술적 정확성)
- Claims that contradict official documentation
- Incorrect assumptions about service limits, quotas, capabilities
- Misuse of technical terminology
- Outdated information (deprecated APIs, EOL services)
- **Sources**: Official service documentation, API references, release notes

### 2. Logical Consistency (논리적 일관성)
- Contradictions between sections
- Requirements that conflict with proposed architecture
- Gaps in data flow (where does data go between step A and C?)
- Unstated assumptions that affect feasibility
- Circular dependencies in component design

### 3. Completeness (완전성)
- Missing failure modes and error handling strategy
- No scalability analysis (what happens at 10x, 100x load?)
- Missing security considerations
- No rollback / migration strategy
- Missing non-functional requirements (latency, throughput, availability SLA)
- No cost estimation or resource planning

### 4. Feasibility (실현 가능성)
- Proposed solution exceeds service limits
- Unrealistic performance expectations
- Technology choices that conflict with stated constraints
- Missing dependencies or prerequisites
- Timeline vs. scope mismatch

## Instructions

1. Read the entire document before starting critique. Understand the full context.
2. Identify the document type (architecture doc, API spec, PRD, RFC, etc.).
3. For each dimension, systematically scan for issues.
4. Cross-reference technical claims with official documentation.
5. If the document references specific services or tools, verify the claims against their docs.
6. Check for internal consistency — does section A agree with section B?

## Constraints
- Do NOT critique writing style or grammar unless it causes ambiguity.
- Focus on technical substance, not presentation.
- If a document is intentionally high-level (e.g., early-stage PRD), adjust expectations but still flag missing critical considerations.
- Mark speculative findings as "추가 검토 필요" with reasoning.
