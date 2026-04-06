# Infrastructure Review Checklist — Quick Reference

## Security
- [ ] IAM follows least-privilege principle
- [ ] No public access to databases or internal services
- [ ] Encryption enabled at-rest and in-transit
- [ ] Secrets managed via secrets manager (not env vars or config files)
- [ ] Network segmentation in place (VPC, subnets, security groups)
- [ ] Audit logging enabled (CloudTrail, GCP Audit Logs, etc.)

## Reliability
- [ ] Multi-AZ / multi-region for critical services
- [ ] Health checks configured for all services
- [ ] Autoscaling policies defined
- [ ] Backup and disaster recovery plan exists
- [ ] Resource limits set (CPU, memory, storage)
- [ ] Circuit breakers for external dependencies

## Cost
- [ ] No over-provisioned resources
- [ ] Lifecycle policies for storage (S3, ECR, logs)
- [ ] Spot/preemptible instances where applicable
- [ ] Unused resources identified and removed
- [ ] Reserved capacity for predictable workloads

## Maintainability
- [ ] All values parameterized (no hardcoded IDs, ARNs, IPs)
- [ ] Remote state with locking (Terraform)
- [ ] Modular structure (reusable modules)
- [ ] Resources tagged/labeled consistently
- [ ] Provider and module versions pinned
