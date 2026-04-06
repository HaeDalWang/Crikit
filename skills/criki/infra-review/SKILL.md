---
name: criki-infra-review
description: >
  인프라 및 IaC 비판 스킬. Terraform, Kubernetes, CloudFormation, Docker,
  CI/CD 파이프라인 등 인프라 코드에 대해 검증, 평가, 검토를 요청하면 활성화된다.
---

# Infrastructure Review — Adversarial Analysis

## Goal
Identify security misconfigurations, reliability risks, cost inefficiencies, and anti-patterns in infrastructure code and configurations.

## Review Dimensions

### 1. Security (보안)
- Overly permissive IAM policies / RBAC roles
- Public exposure of resources (S3 buckets, databases, APIs)
- Missing encryption (at-rest, in-transit)
- Secrets in plaintext (env vars, config files, manifests)
- Missing network segmentation (security groups, network policies)
- **Sources**: AWS/GCP/Azure security best practices, CIS Benchmarks, CNCF security guidelines

### 2. Reliability (안정성)
- Single points of failure (no redundancy, no multi-AZ)
- Missing health checks, readiness/liveness probes
- No autoscaling or improper scaling policies
- Missing backup/disaster recovery configuration
- Resource limits not set (CPU/memory in K8s)
- **Sources**: AWS Well-Architected Framework, GCP Architecture Framework, K8s official docs

### 3. Cost Optimization (비용)
- Over-provisioned resources
- Missing lifecycle policies (S3, ECR, logs)
- No spot/preemptible instance usage where applicable
- Idle resources (unused EIPs, detached volumes)
- **Sources**: Cloud provider pricing docs, cost optimization guides

### 4. Maintainability (유지보수성)
- Hardcoded values instead of variables/parameters
- Missing state management (Terraform remote state)
- No modularization (monolithic IaC files)
- Missing tags/labels for resource organization
- Version pinning (providers, modules, images)
- **Sources**: HashiCorp best practices, Kubernetes patterns, 12-factor app methodology

## Instructions

1. Identify the IaC tool and cloud provider from the code.
2. Systematically review each dimension above.
3. Cross-reference every finding with the official documentation of the specific tool/provider.
4. Provide severity, evidence, and concrete remediation for each finding.
5. If the infrastructure spans multiple services, review the interactions between them.

## Constraints
- Do NOT assume cloud provider — identify it from the code.
- Do NOT suggest changes that would cause downtime without warning.
- Always note if a fix requires a resource replacement vs. in-place update (especially for Terraform).
- Mark findings that require manual verification as "수동 확인 필요".
