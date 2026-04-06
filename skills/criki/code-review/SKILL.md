---
name: criki-code-review
description: >
  코드 리뷰 비판 스킬. 사용자가 코드의 로직, 보안, 성능, 스타일에 대해
  검증, 평가, 검토를 요청하면 활성화된다. 공식 문서 기반으로 결함을 찾아낸다.
---

# Code Review — Adversarial Analysis

## Goal
Identify every logical flaw, security vulnerability, performance bottleneck, and style violation in the provided code. Back every finding with authoritative evidence.

## Review Dimensions

### 1. Security (보안)
- Injection vulnerabilities (SQL, XSS, Command, LDAP)
- Authentication / Authorization flaws
- Secrets exposure (hardcoded keys, tokens, passwords)
- Insecure dependencies (check known CVEs)
- Improper input validation / sanitization
- **Sources**: OWASP Top 10, CVE/NVD, CWE, language-specific security guides

### 2. Logic & Correctness (로직)
- Off-by-one errors, boundary conditions
- Race conditions, deadlocks in concurrent code
- Null/undefined handling, edge cases
- Error handling completeness (are all failure paths covered?)
- Type safety violations
- **Sources**: Language specification, official stdlib docs

### 3. Performance (성능)
- Algorithm complexity (unnecessary O(n²) when O(n) is possible)
- Memory leaks, unnecessary allocations
- N+1 query problems (database access patterns)
- Blocking operations in async contexts
- Missing caching opportunities
- **Sources**: Official runtime/framework performance guides, benchmarks

### 4. Maintainability (유지보수성)
- Dead code, unreachable branches
- Excessive coupling, missing abstractions
- Naming clarity (does the name convey intent?)
- Function length / complexity (cyclomatic complexity)
- Missing or misleading comments
- **Sources**: Language style guides (PEP 8, Google Style Guide, Airbnb, etc.)

## Instructions

1. Read the provided code thoroughly. Understand the full context before critiquing.
2. For each dimension above, systematically scan for issues.
3. Before starting, read `references/checklist.md` as a quick-scan guide to ensure no common issue is missed.
4. For every issue found, use the **Universal Critique Format** and **Severity Definitions** from `GEMINI.md`.
5. If the code is genuinely well-written in some aspect, acknowledge it briefly — but keep looking for flaws.
6. Sort all findings by severity (Critical first).

## Constraints
- Do NOT fabricate CVE numbers or documentation links.
- Do NOT suggest fixes that introduce new problems.
- If unsure about a finding, mark it as "확인 필요" and explain why.
- Do NOT review generated/minified code unless explicitly asked.
