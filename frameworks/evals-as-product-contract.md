# Evals as a Product Contract

An evaluation plan should not be a list of benchmark metrics attached after the product requirements are written. For an AI-enabled product, the evaluation system is part of the product contract: it defines which behavior counts as acceptable, which failures cannot be traded away, and which evidence is required before scope expands.

## Begin with the product decision

State the decision the evaluation supports:

- continue discovery;
- choose between architectures, models, prompts, or vendors;
- enter an internal test;
- begin a bounded pilot;
- expand users, languages, data, tools, or permissions;
- change a fallback or escalation path;
- hold, roll back, or retire the capability.

A single “launch threshold” is usually insufficient because the evidence needed to enter a small read-only pilot differs from the evidence needed to grant write authority or expose the system to a larger population.

## Define the behavior contract

Write requirements as observable product behavior.

| Contract area | Product question | Example evidence |
|---|---|---|
| Task boundary | Which requests should the system handle, clarify, defer, or reject? | representative and boundary scenarios |
| Output contract | What structure, evidence, uncertainty, and next action must appear? | schema checks and rubric review |
| Tool authority | Which tools and actions are allowed at each product state? | permission and unauthorized-call tests |
| Data boundary | Which sources and fields may be accessed, retained, or disclosed? | data-flow review and leakage tests |
| Escalation | Which conditions require human review or a safer mode? | scenario and workflow tests |
| Recovery | What happens after partial, failed, or uncertain execution? | fault injection and state verification |
| User control | How can a user inspect, correct, stop, or contest the result? | usability and outcome testing |
| Operational envelope | What latency, cost, capacity, and availability support the intended journey? | load and cost evidence |

Avoid requirements such as “the agent should be accurate” without defining task, unit, evaluator, population, and consequence of error.

## Separate hard gates from optimization measures

Hard gates are non-compensable. A high aggregate score should not offset:

- unauthorized or prohibited action;
- critical sensitive-data exposure;
- inability to stop or revoke authority;
- unresolved identity or tenant boundary failure;
- required human confirmation bypass;
- unverified external state change;
- critical safety or policy failure.

Optimization measures may include task completion, latency, cost, interaction burden, correction rate, or quality rubric scores. Their thresholds should be tied to the product decision and user journey.

## Use a coverage model

Define the scenario taxonomy before running the evaluation.

```text
user/task distribution
├── core journeys
├── low-frequency valid journeys
├── ambiguity and missing context
├── safety, privacy, and policy boundaries
├── tool and dependency failure
├── adversarial and untrusted content
├── accessibility and language slices
└── previously discovered regressions
```

Keep operating-distribution samples separate from deliberately oversampled critical-risk suites. The first helps estimate routine performance; the second helps find severe failures.

## Specify run conditions

Every comparable result should identify:

- model and provider version;
- system and prompt configuration;
- retrieval corpus and index version;
- tools, permissions, identities, and environment;
- scenario and dataset version;
- evaluator and rubric version;
- run count and sampling / seed policy;
- cache, memory, and state behavior;
- exclusions and failed runs;
- date and evidence owner.

If those conditions change, decide whether the earlier result is still comparable or valid.

## Design decision-level evidence

### Prototype decision

Evidence may emphasize feasibility, failure discovery, and the ability to instrument the workflow. Avoid claiming population-level performance from a small convenience sample.

### Pilot decision

Require:

- bounded users, data, tools, and authority;
- hard-gate evidence;
- representative core journeys;
- incident, support, and stop paths;
- known limitations communicated to users and operators;
- explicit expansion criteria.

### Expansion decision

Require:

- pilot outcome evidence;
- slice and failure analysis;
- operational capacity and cost evidence;
- correction, override, and support behavior;
- residual-risk review;
- evidence that conditions and controls operated in practice.

### Production-candidate decision

Require stronger representativeness, evaluator validity, regression coverage, change control, incident response, and accountable acceptance of remaining risk. “Production” is still scoped to a particular configuration and authority envelope.

## Define product error budgets

An AI error budget should not be one aggregate failure allowance. Distinguish categories with different consequences.

| Category | Example policy |
|---|---|
| Critical prohibited action | hard gate; no compensating quality score |
| Sensitive-data boundary | hard gate or extremely constrained exception process |
| Incorrect but reversible draft | monitored rate with correction workflow |
| Unnecessary clarification | usability / efficiency budget |
| Escalation | interpreted with task mix and reason; not simply minimized |
| Latency or cost | service and unit-economics budget |
| Unsupported claim | severity- and context-specific limit plus source/correction controls |

A rising escalation rate may be good or bad. It can mean safer caution, degraded capability, changed workload, or a broken dependency. Product metrics need causal investigation, not reflexive optimization.

## Connect evaluation to rollout controls

For each rollout stage, define:

| Field | Question |
|---|---|
| Population | Who is exposed? |
| Authority | What can the system read, draft, or execute? |
| Evidence required to enter | Which gates and minimum coverage must pass? |
| Monitoring | Which leading, outcome, and control signals matter? |
| Stop trigger | What condition pauses or disables the stage? |
| Expansion trigger | What evidence justifies broader scope? |
| Owner | Who can enter, expand, hold, or stop the stage? |
| Expiry | When must the stage be reviewed rather than silently continue? |

## Treat failures as product input

For material failures, record:

- user journey and scenario;
- version and authority context;
- evidence and tool trace;
- user or external consequence;
- evaluator disagreement;
- containment and correction;
- root-cause hypothesis versus confirmed cause;
- product decision affected;
- regression test and owner.

Failure review should influence requirements, interface, tool authority, retrieval, fallback, support, and rollout—not only prompt wording.

## Review checklist

- [ ] The evaluation supports a named product decision.
- [ ] Behavior requirements are observable and tied to the user journey.
- [ ] Hard gates are separated from optimization metrics.
- [ ] Scenario coverage and operating-distribution assumptions are explicit.
- [ ] Evaluator validity and uncertainty are documented.
- [ ] Run conditions are versioned and comparable.
- [ ] Critical slices and previously discovered failures are represented.
- [ ] Rollout entry, expansion, stop, and expiry conditions are defined.
- [ ] Product error budgets distinguish consequence classes.
- [ ] Failure evidence can change the product design, not only the score.

## Common failure modes

| Failure | Repair |
|---|---|
| “Accuracy above 90%” is the only launch requirement | Define task distribution, hard gates, evaluator, slices, and stage-specific decision. |
| Benchmark created after the preferred model is chosen | Write the behavior contract and decision criteria before comparison. |
| Aggregate score hides critical failures | Report hard gates and material failures separately. |
| Pilot has no stop or expiry | Add owner, trigger, action, and review date. |
| Tool authority changes but old evals are reused | Treat permissions as part of the versioned system under test. |
| Escalation is optimized downward | Analyze escalation reasons and outcome quality before setting direction. |
