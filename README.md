# AI Platform PM Playbook

A practitioner playbook for product decisions that conventional PRDs often leave implicit in AI platforms and agent products: behavior contracts, evaluation evidence, tool authority, rollout conditions, build-versus-buy trade-offs, and the operating model after launch.

This repository is not a collection of generic PM templates with “AI” added to the headings. Each artifact is intended to make one difficult product judgment more inspectable.

## The decisions this playbook is for

AI platform product work repeatedly crosses several boundaries:

- product behavior is probabilistic and version-dependent;
- quality depends on data, retrieval, prompts, tools, permissions, and evaluators—not only the model;
- a feature can move from draft assistance to consequential action by changing one tool permission;
- evaluation design determines what the team can responsibly claim;
- rollout stages need authority, evidence, stop, and expansion conditions;
- vendors can change models, pricing, policy, regions, or platform behavior;
- operational ownership extends through incidents, regressions, support, and retirement.

The PM’s job is not to eliminate uncertainty. It is to structure decisions so uncertainty, authority, evidence, and consequences are visible to the people accountable for them.

## Start here

| Artifact | Decision supported |
|---|---|
| [`templates/agent-product-prd.md`](templates/agent-product-prd.md) | What observable behavior, authority, user control, and operating limits define the product? |
| [`frameworks/evals-as-product-contract.md`](frameworks/evals-as-product-contract.md) | What evidence is required to prototype, pilot, expand, hold, or roll back? |
| [`templates/evaluation-plan.md`](templates/evaluation-plan.md) | How will scenarios, metrics, hard gates, run conditions, and reporting be recorded? |
| [`frameworks/build-vs-buy.md`](frameworks/build-vs-buy.md) | Which options survive hard constraints, and which trade-offs determine the decision? |
| [`worked-examples/fictional-agent-product-prd.md`](worked-examples/fictional-agent-product-prd.md) | How the product contract applies to a bounded read-only assistant concept |

## Product contract, not feature prose

For an agent or AI-enabled capability, define:

### User and decision boundary

- target user and job;
- decisions the system supports versus decisions it may make;
- requests it should handle, clarify, defer, or reject;
- consequences when the result is wrong, late, incomplete, or acted upon;
- users or groups who are affected but not direct operators.

### Behavior contract

- required output structure and evidence;
- uncertainty and contradiction behavior;
- tool and data authority by workflow state;
- escalation, correction, stop, and appeal paths;
- fallback and partial-execution behavior;
- prohibited uses and external effects.

### Operating contract

- service, latency, cost, and capacity envelope;
- model, prompt, retrieval, tool, and permission versioning;
- observability and incident ownership;
- data retention and memory behavior;
- change, rollback, and retirement triggers.

A good PRD should make it possible to design an evaluation and a rollout control without inventing the missing product semantics later.

## Evals are a product contract

The repository treats evaluation as part of product definition.

A defensible plan separates:

- hard gates from optimization metrics;
- operating-distribution estimates from critical-risk coverage;
- executable checks from human or model-judge measurements;
- prototype evidence from pilot and expansion evidence;
- aggregate results from material failure review;
- current system versions from changed authority, tools, or data.

See [`frameworks/evals-as-product-contract.md`](frameworks/evals-as-product-contract.md).

## Stage decisions

| Stage | Product question | Evidence emphasis |
|---|---|---|
| Discovery | Is the problem and user journey worth solving? | user need, consequence model, feasibility uncertainty |
| Prototype | Can a bounded design demonstrate the behavior contract and expose failure modes? | instrumentation, hard-gate feasibility, exploratory failures |
| Internal test | Can trained operators use and correct the system safely under limited authority? | workflow, correction, support, control operation |
| Pilot | Does the capability create value under stated population, data, tool, and exposure limits? | representative outcomes, slices, incidents, stop path |
| Expansion | Do pilot outcomes and controls justify broader users, languages, data, or authority? | operational evidence, residual risks, capacity, regression |
| Production candidate | Is the scoped configuration supportable, governable, and recoverable? | validity, reliability, incident, change, and owner evidence |

Every stage should have entry evidence, scope, owner, stop trigger, expansion trigger, and expiry. A pilot should not become unreviewed production through inertia.

## Build, buy, partner, or defer

The [`build-vs-buy`](frameworks/build-vs-buy.md) framework uses hard constraints before weighted comparison.

Review at least:

- user and product differentiation;
- time to evidence, not only time to demo;
- total cost including evaluation, integration, operations, migration, and exit;
- data, identity, tool, and regional boundaries;
- model and platform change risk;
- observability and incident access;
- portability and abstraction cost;
- vendor continuity and contract leverage;
- internal capability and operating ownership;
- reversibility and decision horizon.

A vendor proof of concept may establish capability while saying little about production support, evaluator validity, exit cost, or future platform changes.

## Metrics and error budgets

Avoid a single “accuracy” target or combined quality score.

Distinguish:

| Type | Examples |
|---|---|
| User outcome | task completion, correction burden, time saved, successful resolution |
| Quality | factual support, structure, relevance, language, source coverage |
| Hard gate | unauthorized action, sensitive-data exposure, confirmation bypass |
| Operational | latency, timeout, cost, recovery, dependency failure |
| Human-system | escalation, override, correction, reviewer disagreement, automation bias |
| Product guardrail | support load, accessibility, excluded-user harm, complaint or appeal |

Interpret metrics in context. A higher escalation rate can mean safer caution or degraded usefulness; a lower rate can mean better capability or unsafe overconfidence.

## Change control

An AI product decision should state which changes require renewed evidence:

- model or provider;
- prompt, policy, routing, or orchestration;
- retrieval corpus, ranking, or data distribution;
- tools, permissions, identities, and external actions;
- memory and persistence;
- user population, language, or geography;
- evaluator, rubric, threshold, or dataset;
- interface and human-approval flow;
- vendor terms, price, region, or support model;
- incidents or newly discovered failure classes.

Version the system under test as a product configuration, not merely a model name.

## Worked example

The fictional **Lantern** example is a read-only answer-drafting assistant using an invented knowledge collection. It demonstrates:

- explicit read-only authority;
- source and uncertainty requirements;
- clarification and human-review boundaries;
- hard gates for unsupported claims, write actions, and restricted data;
- a bounded pilot decision rather than a universal launch claim.

The example is intentionally simple. It exists to show the structure, not to imply that a short PRD and 50 test cases are sufficient for a real deployment.

## Quality standard for new material

A contribution should add one of:

- a product decision rule;
- a trade-off or failure mode;
- a worked example with stated assumptions and evidence quality;
- a versioned contract or schema;
- a review method that changes what the team would decide;
- a boundary between artifacts commonly confused in AI product work.

Avoid adding broad topic lists, maturity roadmaps, or generic templates unless they contain distinct judgment and a reviewer contract.

## Maturity and scope

This is an early but usable practitioner playbook. It includes a PRD template, evaluation-plan template, build-versus-buy framework, an eval-as-product-contract framework, and a fictional worked example.

It is not product, procurement, architecture, legal, security, privacy, compliance, safety, or investment advice. Adapt the artifacts to the actual users, authority, evidence, organization, and jurisdiction.

## Related repositories

| Repository | Distinct role |
|---|---|
| [`agent-eval`](https://github.com/simaba/agent-eval) | evaluation validity and structured reporting |
| [`everything-program-management`](https://github.com/simaba/everything-program-management) | general program artifacts and validation |
| [`decision-journal-agent`](https://github.com/simaba/decision-journal-agent) | decision capture and later review |
| [`governance-playbook`](https://github.com/simaba/governance-playbook) | enterprise governance operating model |
| [`release-governance`](https://github.com/simaba/release-governance) | release evidence and decision semantics |

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
