프로젝트 계획서: Project Adversary (증거 기반 비판자 에이전트)
버전: 2026.04.06-v1.0
대상 플랫폼: Antigravity (IDE)
주력 모델: Claude 4.6 Sonnet (추론/비판), Gemini 3.1 Pro High (복잡 논리 검증)

1. 프로젝트 개요 (Concept)
본 프로젝트의 목적은 사용자가 작성한 코드와 문서에 대해 **'무결성'**과 **'객관적 증거'**를 기준으로 날카롭게 반박하고 대안을 제시하는 독립적인 비판자(Adversarial Agent) 환경을 구축하는 것입니다. 단순한 조언자가 아닌, 논리적 결함을 찾아내어 수정을 강제하는 가디언 역할을 수행합니다.
결론적으로는 "시스템프롬프트" + "Skill들"의 조합 깃허브레포지토리를 만드는 것입니다

설계 철학 (Core Philosophy)
권위 기반 검증 (Authoritative Verification): 개인의 블로그나 커뮤니티 글이 아닌, 공식 문서(AWS, CNCF, HashiCorp, Google Cloud), RFC 표준, 공식 보안 권고(CVE)만을 최우선 신뢰 자료로 간주함.
