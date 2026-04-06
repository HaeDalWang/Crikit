# Code Review Checklist — Quick Reference

## Security
- [ ] No hardcoded secrets (API keys, passwords, tokens)
- [ ] Input validation on all user-facing endpoints
- [ ] SQL queries use parameterized statements
- [ ] No eval() or dynamic code execution with user input
- [ ] Dependencies checked against known CVEs
- [ ] CORS configured correctly (not wildcard in production)
- [ ] Authentication/authorization on all protected routes

## Logic
- [ ] Edge cases handled (null, empty, boundary values)
- [ ] Error paths return meaningful messages
- [ ] No unreachable code or dead branches
- [ ] Async operations properly awaited
- [ ] Race conditions considered in concurrent code
- [ ] Loop termination guaranteed

## Performance
- [ ] No unnecessary O(n²) or worse algorithms
- [ ] Database queries optimized (no N+1)
- [ ] Large collections paginated
- [ ] Resources properly closed/released (connections, files, streams)
- [ ] No blocking calls in async context

## Maintainability
- [ ] Functions do one thing (single responsibility)
- [ ] Names convey intent clearly
- [ ] No magic numbers — use named constants
- [ ] Error handling is consistent across the codebase
- [ ] No copy-paste duplication
