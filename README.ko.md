# Harness Kit

[English](./README.md)

Harness Kit은 구현 작업에 일관된 운영 방식을 얹고 싶은 저장소를 위한 재사용 가능한 Codex 워크플로 레이어입니다.

이 키트로 얻을 수 있는 것:

- 이슈 중심 실행 방식
- 역할별로 나뉜 `docs/` 구조
- 무엇을 만들었는지보다 어떻게 만들었는지를 남기는 기술 학습 노트
- 부트스트랩, 이슈 워크플로, 학습 노트, 서브 에이전트 운영을 위한 재사용 가능한 Codex 스킬

## 왜 쓰는가

대부분의 저장소에는 코드만 있고, 작업을 굴리는 일관된 방식은 없습니다.

Harness Kit은 어떤 프로젝트에도 가볍게 얹을 수 있는 운영 레이어를 제공해서:

- 새 작업을 즉흥적인 메모가 아니라 이슈 문서로 시작하고
- 결정, 학습 노트, 백로그를 예측 가능한 위치에 쌓고
- 여러 저장소에서 Codex 사용 방식을 반복 가능하게 만들고
- 작업 문맥을 잃지 않고 handoff 할 수 있게 해줍니다

## Quick Start

저장소를 클론합니다:

```powershell
git clone https://github.com/HyunKN/harness-kit.git
cd harness-kit
```

대상 저장소에 하네스를 설치합니다:

```powershell
python .\scripts\init_harness.py "C:\path\to\target-repo"
```

첫 번째 이슈를 생성합니다:

```powershell
python .\scripts\new_issue.py "C:\path\to\target-repo" renderall-partial-refresh "Reduce full rerenders"
```

그 다음 대상 저장소를 Codex에서 열고, 설치된 docs 구조와 skills를 기본 작업 방식으로 사용하면 됩니다.

이미 Codex 안에 있다면 그냥 Codex에게 맡기세요.

추천 프롬프트:

- `이 저장소에 harness-kit 설치해줘`
- `https://github.com/HyunKN/harness-kit 를 이 저장소에 설치하고 세팅까지 해줘`
- `이 저장소에 새 이슈 문서를 만들어줘. 제목은 Reduce full rerenders`

## 핵심 플로우

1. 표준 `docs/` 하네스를 저장소에 설치합니다.
2. 구현을 시작하기 전에 새 이슈를 엽니다.
3. 채팅 기록만 보지 않고, 해당 이슈를 기준으로 구현합니다.
4. 재사용하거나 다시 공부할 가치가 있는 내용은 기술 학습 노트로 남깁니다.
5. 서브 에이전트는 분석, 구현, 리뷰처럼 경계가 분명한 작업에서만 사용합니다.

## 무엇을 제공하는가

### 1. 재사용 가능한 docs 구조

부트스트랩 스크립트는 아래 역할을 가진 `docs/` 트리를 설치합니다:

- architecture
- product
- design
- reviews
- status
- issues
- records
- learning
- playbooks
- operations

### 2. Codex skills

포함된 스킬:

- `harness-bootstrap`
- `issue-driven-workflow`
- `technical-learning-note`
- `subagent-workflow`

이 스킬들은 특정 코드베이스에 묶이지 않고, 여러 프로젝트에서 같은 작업 방식을 재사용할 수 있게 설계되어 있습니다.

### 3. 작은 헬퍼 스크립트

- `scripts/init_harness.py`
  - 대상 저장소에 docs 하네스를 설치합니다
- `scripts/new_issue.py`
  - 새 이슈 문서를 만들고 백로그를 갱신합니다

## 저장소 구조

```text
.codex-plugin/           Codex plugin metadata
skills/                  Reusable Codex skills
scripts/                 Bootstrap and issue helpers
assets/templates/docs/   Docs templates copied into target repos
```

## 이런 경우에 잘 맞습니다

Harness Kit은 아래 같은 경우에 특히 잘 맞습니다:

- Codex를 자주 사용하고 있고
- 여러 저장소에서 같은 작업 방식을 쓰고 싶고
- 설명 가능성, handoff 품질, 오래 남는 노트를 중요하게 생각할 때

이 키트는 빌드 시스템도, 프레임워크도, 패키지 매니저도 아닙니다. 작업 운영 키트입니다.
