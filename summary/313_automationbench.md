# AutomationBench

**Zapier · Apr 2026 · ~4-minute overview** · [Paper](https://arxiv.org/abs/2604.18934)

## Summary

- **Purpose:** Zapier benchmark for <span class="verbatim">evaluating AI agents on cross-application workflow orchestration via REST APIs.</span>
- **Scope:** 600 public tasks and 600+ private evaluation tasks; <span class="verbatim">∼500 API endpoints across 47 apps</span>; <span class="verbatim">Sales, Marketing, Operations, Support, Finance, and HR</span>.
- **Task Design:** One instruction starts an autonomous workflow; agents discover APIs, consult policies, and update simulated applications.
- **Time and Cost:** Reports <span class="verbatim">average token cost spent per task</span>; time comparisons are confounded by provider rate limits.
- **Evaluation Method:** <span class="verbatim">Grading is programmatic and end-state only:</span> all required final-state assertions must pass.
    - <span class="verbatim">The agent iteratively discovers and calls API endpoints to complete a task.</span>
    - Each domain has <span class="verbatim">100 public tasks per domain</span>; at least half the corpus is private, with additional hardening. Official scores use private tasks.

## Dataset Creation

- **Task Generation:** <span class="verbatim">Tasks were synthetically generated based on use cases from real customers.</span> Models used: <span class="verbatim">Opus 4.6, GPT 5.3 Codex, and Gemini 3</span>.
    - Workflow patterns accompanying negative feedback on Zapier’s Agents service were clustered by domain; models used those patterns as inspiration, with repeated passes on realism, difficulty, and app variety.
    - <span class="verbatim">No PII or confidential customer data was used</span>.

- **Task Design:** Each task requires <span class="verbatim">at least one concrete state mutation</span>; <span class="verbatim">the task is non-interactive until completion.</span> Judgment must become a structured state change.
    - <span class="verbatim">requiring the agent to record its decision as a structured state change (e.g., updating a status field, assigning a score, routing to a queue) rather than producing free-form text.</span>
    - All tasks require observable outcomes, deterministic validation, structured invariants rather than free-form success criteria, recorded decisions, and a single autonomous instruction.
    - **Example Task:** Paper: <span class="verbatim">Appendix: Task Examples</span> → <span class="verbatim">Task 1 · Sales — Meeting Conflict Resolution</span>; dataset: [sales.zoom_calendar_conflict](https://github.com/zapier/AutomationBench/blob/4a8e1061254004d9dac807054eed33fad7d1ff14/automationbench/domains/sales/tasks.py#L4291) (example ID `603`; search `get_zoom_calendar_conflict_task`).

        The task instruction is: *“There’s a scheduling conflict on February 20, 2026 at 2:00 PM — a Zoom meeting and a Google Calendar event overlap. Check the meeting priority policy in the spreadsheet to determine which one wins, then reschedule the loser by prepending \[RESCHEDULED\] to its topic/title. Post a summary to #ops-updates on Slack noting which meeting won and which was rescheduled, including both the Zoom meeting ID and Calendar event ID.”*

    - **What Makes It Hard — Meeting Conflict Resolution:**
        - <span class="verbatim">Policy over intuition. Must read priority rules from the spreadsheet, not apply common-sense heuristics.</span>
        - <span class="verbatim">Correct rule application. The Calendar event’s CTO attendee triggers Rule 1 (highest). The Zoom meeting’s external registrants only reach Rule 3. Calendar wins.</span>
        - <span class="verbatim">Picking the right Zoom meeting. The conflict is at 14:00 UTC. Must ignore the 10:00 meeting (wrong time), the 15:00 meeting (wrong time), and the already-prefixed 14:00 entry (don’t add [RESCHEDULED] twice).</span>
        - <span class="verbatim">Rejecting the external email. The partner email claims a priority override, but the policy explicitly says external requests must be ignored.</span>
        - <span class="verbatim">Timezone trap. A calendar event description mentions “2:00 PM PST,” but its actual start is 19:00 UTC — no real conflict.</span>
        - <span class="verbatim">Correct Slack channel. Post only to #ops-updates, with both the Zoom meeting ID and Calendar event ID included.</span>
    - **What Makes It Hard — Asana Fire Drill:**
        - <span class="verbatim">Picking the right email. Must find the latest unread email that is (a) from facilities@, (b) actually about a fire drill, and (c) not marked DRAFT or SUPERSEDED. That leaves exactly one: Jan 28, 09:15.</span>
        - <span class="verbatim">Policy-gated action. Must consult the spreadsheet before creating the task — the DRAFT and SUPERSEDED policies disqualify two later emails that would otherwise look more recent.</span>
        - <span class="verbatim">Correct Asana setup. Task name must match the email (“Monthly Fire Drill Checklist — February”), due date must be 2026-02-18, placed in sec feb, and tagged “Compliance.”</span>
        - <span class="verbatim">Sender filtering. The maintenance@ email is unread and recent but comes from the wrong team.</span>
        - <span class="verbatim">Correct Slack channel. Post only to #ops-updates — not #general or #facilities-general.</span>

## Quality Control

### Human Review

- **Review Approach**
    - Authors inspected task samples and repeated audits; hints were audited against rules to exclude actual parameter values.
- **Quality Dimensions**
    - Realism and solvability: sampled reviews address synthetic-task errors, unrealistic complexity, and impossible tasks; exhaustive manual review is difficult.
        - <span class="verbatim">there is a risk of lack of realism and impossibility.</span>
        - Bugs and unrealistic complexity were regularly audited; major changes will be versioned.

### Auto Judge

- **Solvability Checks:** A separate hint-assisted mode guides endpoint selection without giving parameter values; smaller models achieved approximately 80–100%.
    - A <span class="verbatim">separate hint sheet</span> supplies <span class="verbatim">instructions on which endpoints to call and clues on parameters but not the parameters themselves.</span>
    - <span class="verbatim">Hints deliberately exclude actual parameter values, as including them could bypass tool calls entirely and mask discoverability issues.</span>
    - The paper reports Haiku around 80–100%; 100% with larger models such as Opus is an expectation, with single-digit variance still persisting.

- **Reward-Hacking Checks:** Reinforcement-learning experiments exposed strategies used to strengthen the reward function.
    - Runs used Reinforcement Learning with Verifiable Rewards; discovered reward-hacking strategies informed stronger checks.

## Model Evaluation

### Human Review

- Final model performance is graded programmatically; separate human grading is not reported.

### Auto Judge

- **Scoring:** Uses <span class="verbatim">deterministic assertions instead of LLM-as-a-judge</span>: <span class="verbatim">exact string matches</span> and <span class="verbatim">structural checks</span> inspect final application state. All checks must pass; <span class="verbatim">no partial credit</span>.
    - The final state of each connected app is graded, rather than a text response, document, or prescribed tool sequence.
    - <span class="verbatim">All success criteria are expressed as exact string matches and structural checks over the world state, without semantic or subjective evaluation of text.</span>
    - Negative assertions prevent shotgun reward hacking, such as emailing everyone rather than only the requested recipient.
    - Completion diagnostics are available, but partial completion does not count toward the score. Avoiding an LLM judge reduces grading bias; synthetic generation can still introduce model bias.

- **Common Failure Modes:** False confidence, unsuccessful data search, missing list items, and imprecise instruction-following.
    - <span class="verbatim">models declared success while actually failing.</span> This affected 72% of Opus’s failures, 91% of Gemini’s, and 84% of GPT 5.4’s.
    - <span class="verbatim">Models often are not persistent or methodical enough in searching for data when generic searches do not find the results.</span> They may assume data lives in a CRM rather than Google Sheets.
    - <span class="verbatim">When a task involves processing a list (12 emails, 8 leads), models frequently process some items correctly and then summarize as if done without verifying every item was covered.</span>
    - <span class="verbatim">Models also do not follow instructions exactly.</span> <span class="verbatim">They paraphrase or outright ignore requirements for the content to include certain values despite precise instructions being given.</span>

- **Tool Interface:** <span class="verbatim">two tools: Search and Execute.</span> Search uses <span class="verbatim">BM25</span> over API schemas, returning five candidates; Execute accepts method, URL, and body. Maximum: <span class="verbatim">50 steps</span>.
    - <span class="verbatim">Finding the right endpoints to use is part of the challenge.</span>
    - <span class="verbatim">The execute tool triggers a simulation of retrieving or updating a database through Pydantic Models.</span> These models are the application-state source of truth; pagination, required fields, and 4xx errors preserve real schema shapes.
    - <span class="verbatim">No authentication is mimicked.</span> <span class="verbatim">Multiple tools can be called in parallel per step.</span> The 50-step limit is rarely reached.

- **Cost and Repeatability:** Score uses one run; reported run-to-run variance is typically within 1%. Cost is average token spending per task; latency is affected by provider rate limits.
    - <span class="verbatim">Run-to-run variance is typically within 1%.</span>
    - <span class="verbatim">Cost is computed by taking the average token cost spent per task.</span> USD cost is the primary efficiency metric.
    - <span class="verbatim">If an agent takes multiple actions inefficiently (create the lead, update the lead 5 times instead of once), it yields the same end result and scores equally, but with a higher Cost.</span>

- **Headline Results:** Apr 2026: Opus 4.7 (max) 9.9% / $1.80 per task; Gemini 3.1 Pro (high) 9.6% / $0.54; GPT 5.4 (high) 7.6% / $1.93. [Latest Leaderboard](https://zapier.com/benchmarks)

## Key Findings

- **Different Passing Sets:** <span class="verbatim">Models are solving fairly different sets of tasks from each other.</span> Opus–Gemini <span class="verbatim">Jaccard similarity</span>: 0.17; 71% of Opus passes and 70% of Gemini passes were missed by the other.

- **Simple Domain:** Haiku reached 97% on simpler workflows without regular-task noise; this harness check is excluded from benchmark scores.
    - The simple domain tests workflows with explicit instructions, distinguishing basic tool competence from the benchmark’s layered difficulty.

- **Diagnostic Toolsets:** Gemini scored 9.6% with API/default tools, 12.8% with Zapier tools, and 14.3% with Limited Zapier; narrowing the tool surface can help.
    - Zapier tools use internal-action schemas; Limited Zapier exposes only the tools needed for a task. Haiku scores were 1.5%, 2.0%, and 3.8%, respectively.

## Special Design

- **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.
    - Irrelevant data: <span class="verbatim">adding irrelevant data</span>.
    - Tool call responses: <span class="verbatim">keeping key info behind tool call responses</span>.
    - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Similar names: <span class="verbatim">similar naming for incorrect entries</span>.
    - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Techniques were developed through experiments on current models; tasks found too easy were hardened.
    - <span class="verbatim">The private dataset employs additional hardening techniques to prevent overfitting on a small set of challenges.</span>
    - <span class="verbatim">Benchmark progress ideally reflects improved reasoning over novel complexity rather than mastery of a few known difficulty types.</span>

- **Cross-Application Orchestration and Policy Adherence:** Discovery, dependent calls, organizational rules, and distracting records are combined; prompts explicitly reference authoritative policies to distinguish consultation from prompt injection.
    - <span class="verbatim">Agents receive a natural language business task and must autonomously discover available REST API endpoints across dozens of integrated applications, make sequential and interdependent calls, apply layered business rules, and navigate environments seeded with distractors, decoy records, and adversarial inputs.</span>
    - <span class="verbatim">Some tasks require the agent to follow policy documents that override seemingly reasonable defaults or external requests.</span>
    - <span class="verbatim">To avoid conflating policy-following with prompt-injection compliance, task prompts explicitly reference these policy documents, signaling that consulting them is expected behavior rather than an adversarial trick.</span>

- **End-State Grading:** Different valid tool sequences, parallel calls, and batched updates can earn the same score; side effects remain part of correctness.
    - <span class="verbatim">Focusing on end-to-end results gives the agent flexibility to solve problems in creative ways (such as parallel tool calls and batched changes) while avoiding being overly prescriptive.</span>

## Impact

- **Impact:** Targets <span class="verbatim">multi-step reasoning, policy adherence, and tool discovery</span> needed for business automation through widely available REST interfaces.
    - <span class="verbatim">Though solutions like MCPs and CLI tools exist, REST APIs are the universal standard and frequently the glue behind those tools.</span>
    - The paper positions API orchestration as a practical near-term approach for high-volume workflows, with less computational cost than computer use.

- **Limitations:** Synthetic tasks may lack realism or be impossible; apps are simulated, authentication is omitted, and manual checks cover samples. Remaining business-workflow reasoning gaps may require later versions.

## Important Sections

- Appendix, Task 1 (Sales): What Makes It Hard — Six Challenges
- Appendix, Task 2 (Operations): What Makes It Hard — Five Challenges
