# Project Adversary — criki

**증거 기반 비판자 에이전트 스킬 패키지**

코드, 인프라, 문서에 대해 공식 문서와 표준을 근거로 날카롭게 비판하고 대안을 제시하는 Antigravity IDE용 Agent Skill입니다.

## 설치

### 전역 룰파일
```bash
cp GEMINI.md ~/.gemini/GEMINI.md
```

### 스킬 설치
```bash
cp -r skills/criki ~/.gemini/antigravity/skills/criki
```

## 사용법

Antigravity 채팅에서 다음과 같이 요청하세요:
- "이 코드 검증해줘"
- "인프라 설정 평가해줘"
- "설계 문서 검토해줘"

## 스킬 구조

```
criki/
├── SKILL.md                  # 메인 라우터 (페르소나, 서브스킬 라우팅)
├── code-review/              # 코드 비판
├── infra-review/             # 인프라/IaC 비판
├── doc-review/               # 문서/설계 비판
├── evidence-grounding/       # 근거화 (공식 문서 증거 수집)
└── web-search/               # 웹서칭 (placeholder)
```

## 심각도 레벨

| 레벨 | 설명 |
|------|------|
| Critical | 보안 취약점, 데이터 손실 위험, 프로덕션 장애 유발 |
| Major | 성능 저하, 아키텍처 안티패턴, 유지보수성 저하 |
| Minor | 코드 스타일, 네이밍 불일치, 경미한 비효율 |
| Info | 개선 제안, 베스트 프랙티스 권장 |

## 라이선스

MIT
