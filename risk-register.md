# Risk Register

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|-----------|--------|-----------|-------|
| R1 | Build-time data resets on each CI run (no persistence) | High | Medium | Phase 3: persist to a data branch or use the GitHub API | Project owner |
| R2 | Timing noise from shared CI runners hides real regressions | Medium | Medium | Track averages and trends, not single runs | Project owner |
| R3 | Flaky tests inflate the failure rate | Medium | High | Investigate repeated failures; quarantine flaky tests | Project owner |
| R4 | Scope creep into a full dashboard product | Medium | Low | Keep to markdown reports until Phase 4 | Project owner |
| R5 | Actions free-tier minutes exhausted | Low | Low | Keep workflow short; use caching | Project owner |
