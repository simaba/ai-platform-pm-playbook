# Worked Example: Fictional Policy Answer Assistant

> This is a fictional example. It does not describe a real employer, product, customer, workflow, dataset, or system.

## Product summary

- **Product / capability name:** Lantern
- **Target user:** A fictional internal operations coordinator
- **User problem:** Locating an approved answer in a large set of fictional process guides takes too long and results vary by person.
- **Value proposition:** Provide cited draft answers from an approved fictional knowledge collection while escalating uncertainty and disallowing write actions.
- **Maturity:** pilot concept

## User journey

1. The user asks a factual process question.
2. Lantern retrieves from a fictional approved source set.
3. Lantern presents a concise draft answer with source labels and uncertainty when evidence is incomplete.
4. The user can open the source, correct the request, or request human review.

## In scope

- factual answer drafting from a fictional read-only knowledge source
- source labels and uncertainty statements
- human escalation for missing or conflicting information

## Out of scope

- creating, editing, approving, or sending records
- personal, legal, HR, financial, security, or medical advice
- autonomous actions in other systems

## Behavior contract

| Area | Requirement | Acceptance signal |
|---|---|---|
| Task understanding | Identify a factual question versus a request for action | Action requests are rejected or redirected |
| Output | Provide a concise draft with source labels | Every factual claim includes a fictional source label or uncertainty |
| Tools | Read-only retrieval only | No write-capable tool is available |
| Escalation | Stop when sources conflict or are absent | Response offers a human-review route |
| Privacy | Avoid requesting unnecessary information | No identity or sensitive detail is required for the fictional task |

## Evaluation plan summary

- 30 fictional core questions
- 10 fictional ambiguous/underspecified questions
- 10 fictional safety/privacy boundary tests
- hard gates: no unsupported claim presented as confirmed; no simulated write action; no exposure of fictional restricted data
- quality threshold: a defined rubric score with documented limitations

## Key risks and mitigations

| Risk | Mitigation |
|---|---|
| Answer sounds confident when sources are incomplete | Require uncertainty wording and escalation option |
| User asks for an action rather than information | Make the tool read-only and return a bounded redirect |
| Source material conflicts | Surface conflict and request human review |

## Pilot decision

Run only with a fictional dataset and a read-only demonstration interface. Expand only after the task set, rubric, responsible owner, and review process are documented.