# Document & Design Review Checklist — Quick Reference

## Technical Accuracy
- [ ] All service/API claims verified against official docs
- [ ] No deprecated technologies referenced as current
- [ ] Service limits and quotas correctly stated
- [ ] Technical terminology used correctly

## Logical Consistency
- [ ] No contradictions between sections
- [ ] Data flow is complete (no gaps between components)
- [ ] All assumptions are explicitly stated
- [ ] No circular dependencies in architecture

## Completeness
- [ ] Failure modes and error handling described
- [ ] Scalability analysis included (10x, 100x scenarios)
- [ ] Security considerations documented
- [ ] Rollback / migration strategy defined
- [ ] Non-functional requirements specified (latency, SLA, throughput)
- [ ] Cost estimation or resource planning included

## Feasibility
- [ ] Proposed solution within service limits
- [ ] Performance expectations realistic and benchmarked
- [ ] Technology choices align with constraints
- [ ] Dependencies and prerequisites identified
- [ ] Timeline matches scope
