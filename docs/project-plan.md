# Project Plan

## Goal
Make CI build performance and test reliability visible, so slowdowns and failures are caught and prioritised early.

## Scope
**In scope:** automated tests on every push, build-time recording, a generated delivery report, project documentation.
**Out of scope:** deployment pipelines, multi-repo aggregation, dashboards beyond markdown reports.

## Milestones
| # | Milestone | Target | Done when |
|---|-----------|--------|-----------|
| 1 | Repo and test suite | Week 1 | Tests pass locally |
| 2 | CI workflow | Week 1 | Tests run on every push |
| 3 | Build-time recording | Week 2 | CSV updated each run |
| 4 | Delivery report | Week 2 | Report appears in run summary |
| 5 | Documentation | Week 3 | Plan, roadmap and risk register complete |

## Resources and budget
One owner, GitHub free tier (Actions minutes included). Budget: none.

## Stakeholders
Engineering teams (consumers of the report), project owner (delivery and prioritisation).

## Quality standards
All code covered by tests; CI must be green before merge; docs updated with each change.
