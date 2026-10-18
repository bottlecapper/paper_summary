# AutomationBench Highlight Audit

All 63 included highlights are mapped to the revised summary. Topics are ordered by their highest highlight priority; selections within each topic are ordered by priority, then paper order.

Prior-coverage judgments are a manual semantic review. Annotation accounting is checked programmatically. Raw selections retain PDF extraction artifacts; mathematical selections are explained in context in the summary.

Previous statuses: **Covered**, **Partial**, **Title only**, or **Missing**. New coverage means the highlighted information is represented by a topic lead, source excerpt, definition, or merged equivalent passage—not that every duplicate fragment is repeated verbatim.

## Policy Design

**Priority 2 · Special Design**

- **Cross-Application Orchestration and Policy Adherence:** Discovery, dependent calls, organizational rules, and distracting records are combined; prompts explicitly reference authoritative policies to distinguish consultation from prompt injection.

- **H032 · Bright green · Before: Not assessed**
    - Selected text: `prompt injection.`
    - Now represented under **Special Design → Policy Design**.

    - Summary evidence:     - <span class="verbatim">To avoid conflating policy-following with prompt-injection compliance, task prompts explicitly reference these policy documents, signaling that consulting them is expected behavior rather than an adversarial trick.</span>
    - Meaning: prompt injection.

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H012 · Light green · Before: Not assessed**
    - Selected text: `Agents receive a natural language business task and must autonomously discover available REST API endpoints across dozens of integrated applications, make sequential and interdependent calls, apply layered business rules, and navigate environments seeded with distractors, decoy records, and adversarial inputs.`
    - Now represented under **Special Design → Policy Design**.

    - Summary evidence:     - <span class="verbatim">Agents receive a natural language business task and must autonomously discover available REST API endpoints across dozens of integrated applications, make sequential and interdependent calls, apply layered business rules, and navigate environments seeded with distractors, decoy records, and adversarial inputs.</span>
    - Meaning: Agents receive a natural language business task and must autonomously discover available REST API endpoints across dozens of integrated applications, make sequential and interdependent calls, apply layered business rules, and navigate environments seeded with distractors, decoy records, and adversarial inputs.

- **H030 · Light green · Before: Not assessed**
    - Selected text: `Some tasks require the agent to follow policy documents that override seem- ingly reasonable defaults or external requests.`
    - Now represented under **Special Design → Policy Design**.

    - Summary evidence:     - <span class="verbatim">Some tasks require the agent to follow policy documents that override seemingly reasonable defaults or external requests.</span>
    - Meaning: Some tasks require the agent to follow policy documents that override seem- ingly reasonable defaults or external requests.

- **H031 · Light green · Before: Not assessed**
    - Selected text: `task prompts explicitly reference these policy documents, signaling that consulting them is expected behavior rather than an adversarial trick.`
    - Now represented under **Special Design → Policy Design**.

    - Summary evidence:     - <span class="verbatim">To avoid conflating policy-following with prompt-injection compliance, task prompts explicitly reference these policy documents, signaling that consulting them is expected behavior rather than an adversarial trick.</span>
    - Meaning: task prompts explicitly reference these policy documents, signaling that consulting them is expected behavior rather than an adversarial trick.

## Solvability

**Priority 2 · Quality Control · Auto Judge**

- **Solvability Checks:** A separate hint-assisted mode guides endpoint selection without giving parameter values; smaller models achieved approximately 80–100%.

- **H036 · Bright green · Before: Not assessed**
    - Selected text: `solvable,`
    - Now represented under **Quality Control → Auto Judge → Solvability**.

    - Summary evidence: - **Solvability Checks:** A separate hint-assisted mode guides endpoint selection without giving parameter values; smaller models achieved approximately 80–100%.
    - Meaning: solvable,

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H035 · Light green · Before: Not assessed**
    - Selected text: `a separate hint sheet`
    - Now represented under **Quality Control → Auto Judge → Solvability**.

    - Summary evidence:     - A <span class="verbatim">separate hint sheet</span> supplies <span class="verbatim">instructions on which endpoints to call and clues on parameters but not the parameters themselves.</span>
    - Meaning: a separate hint sheet

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H037 · Light green · Before: Not assessed**
    - Selected text: `instructions on which endpoints to call and clues on parameters`
    - Now represented under **Quality Control → Auto Judge → Solvability**.

    - Summary evidence:     - A <span class="verbatim">separate hint sheet</span> supplies <span class="verbatim">instructions on which endpoints to call and clues on parameters but not the parameters themselves.</span>
    - Meaning: instructions on which endpoints to call and clues on parameters

- **H038 · Light green · Before: Not assessed**
    - Selected text: `Hints deliberately exclude actual parameter values,`
    - Now represented under **Quality Control → Auto Judge → Solvability**.

    - Summary evidence:     - <span class="verbatim">Hints deliberately exclude actual parameter values, as including them could bypass tool calls entirely and mask discoverability issues.</span>
    - Meaning: Hints deliberately exclude actual parameter values,

## Scoring

**Priority 2 · Model Evaluation · Auto Judge**

- **Scoring:** Uses <span class="verbatim">deterministic assertions instead of LLM-as-a-judge</span>: <span class="verbatim">exact string matches</span> and <span class="verbatim">structural checks</span> inspect final application state. All checks must pass; <span class="verbatim">no partial credit</span>.

- **H047 · Bright green · Before: Not assessed**
    - Selected text: `instead of grading a text response or document, we consider only the end state of each connected app.`
    - Now represented under **Model Evaluation → Auto Judge → Scoring**.

    - Summary evidence:     - The final state of each connected app is graded, rather than a text response, document, or prescribed tool sequence.
    - Meaning: instead of grading a text response or document, we consider only the end state of each connected app.

    - Transformation reason: Grading object and excluded response/trajectory criteria are restated without author framing.

- **H053 · Bright green · Before: Not assessed**
    - Selected text: `We use deterministic assertions instead of LLM-as-a-judge.`
    - Now represented under **Model Evaluation → Auto Judge → Scoring**.

    - Summary evidence: - **Scoring:** Uses <span class="verbatim">deterministic assertions instead of LLM-as-a-judge</span>: <span class="verbatim">exact string matches</span> and <span class="verbatim">structural checks</span> inspect final application state. All checks must pass; <span class="verbatim">no partial credit</span>.
    - Meaning: We use deterministic assertions instead of LLM-as-a-judge.

    - Transformation reason: Deterministic scoring is stated without author framing; exact success criteria are quoted underneath.

- **H054 · Bright green · Before: Not assessed**
    - Selected text: `We include negative assertions to prevent shotgun approach reward hacking`
    - Now represented under **Model Evaluation → Auto Judge → Scoring**.

    - Summary evidence:     - Negative assertions prevent shotgun reward hacking, such as emailing everyone rather than only the requested recipient.
    - Meaning: We include negative assertions to prevent shotgun approach reward hacking

    - Transformation reason: Negative assertions and the shotgun-email example are summarized without author framing.

- **H055 · Bright green · Before: Not assessed**
    - Selected text: `We give no partial credit`
    - Now represented under **Model Evaluation → Auto Judge → Scoring**.

    - Summary evidence:     - Completion diagnostics are available, but partial completion does not count toward the score. Avoiding an LLM judge reduces grading bias; synthetic generation can still introduce model bias.
    - Meaning: We give no partial credit

    - Transformation reason: No-partial-credit policy is restated neutrally with diagnostics separated from headline scoring.

- **H056 · Light green · Before: Not assessed**
    - Selected text: `exact string matches`
    - Now represented under **Model Evaluation → Auto Judge → Scoring**.

    - Summary evidence:     - <span class="verbatim">All success criteria are expressed as exact string matches and structural checks over the world state, without semantic or subjective evaluation of text.</span>
    - Meaning: exact string matches

- **H057 · Light green · Before: Not assessed**
    - Selected text: `structural checks`
    - Now represented under **Model Evaluation → Auto Judge → Scoring**.

    - Summary evidence:     - <span class="verbatim">All success criteria are expressed as exact string matches and structural checks over the world state, without semantic or subjective evaluation of text.</span>
    - Meaning: structural checks

## Failure Modes

**Priority 2 · Model Evaluation · Auto Judge**

- **Common Failure Modes:** False confidence, unsuccessful data search, missing list items, and imprecise instruction-following.

- **H065 · Bright green · Before: Not assessed**
    - Selected text: `models declared success while actually failing.`
    - Now represented under **Model Evaluation → Auto Judge → Failure Modes**.

    - Summary evidence:     - <span class="verbatim">models declared success while actually failing.</span> This affected 72% of Opus’s failures, 91% of Gemini’s, and 84% of GPT 5.4’s.
    - Meaning: models declared success while actually failing.

- **H068 · Bright green · Before: Not assessed**
    - Selected text: `Models also do not follow instructions exactly.`
    - Now represented under **Model Evaluation → Auto Judge → Failure Modes**.

    - Summary evidence:     - <span class="verbatim">Models also do not follow instructions exactly.</span> <span class="verbatim">They paraphrase or outright ignore requirements for the content to include certain values despite precise instructions being given.</span>
    - Meaning: Models also do not follow instructions exactly.

- **H070 · Bright green · Before: Not assessed**
    - Selected text: `Another failure mode is missing items.`
    - Now represented under **Model Evaluation → Auto Judge → Failure Modes**.

    - Summary evidence:     - <span class="verbatim">When a task involves processing a list (12 emails, 8 leads), models frequently process some items correctly and then summarize as if done without verifying every item was covered.</span>
    - Meaning: Another failure mode is missing items.

    - Transformation reason: Missing-items error is represented by the complete highlighted list-processing sentence.

- **H066 · Light green · Before: Not assessed**
    - Selected text: `Models often are not persistent or methodical enough in searching for data when generic searches do not find the results.`
    - Now represented under **Model Evaluation → Auto Judge → Failure Modes**.

    - Summary evidence:     - <span class="verbatim">Models often are not persistent or methodical enough in searching for data when generic searches do not find the results.</span> They may assume data lives in a CRM rather than Google Sheets.
    - Meaning: Models often are not persistent or methodical enough in searching for data when generic searches do not find the results.

- **H067 · Light green · Before: Not assessed**
    - Selected text: `When a task involves processing a list (12 emails, 8 leads), models frequently process some items correctly and then summarize as if done without verifying every item was covered.`
    - Now represented under **Model Evaluation → Auto Judge → Failure Modes**.

    - Summary evidence:     - <span class="verbatim">When a task involves processing a list (12 emails, 8 leads), models frequently process some items correctly and then summarize as if done without verifying every item was covered.</span>
    - Meaning: When a task involves processing a list (12 emails, 8 leads), models frequently process some items correctly and then summarize as if done without verifying every item was covered.

- **H069 · Light green · Before: Not assessed**
    - Selected text: `They paraphrase or outright ignore requirements for the content to include certain values despite precise instructions being given.`
    - Now represented under **Model Evaluation → Auto Judge → Failure Modes**.

    - Summary evidence:     - <span class="verbatim">Models also do not follow instructions exactly.</span> <span class="verbatim">They paraphrase or outright ignore requirements for the content to include certain values despite precise instructions being given.</span>
    - Meaning: They paraphrase or outright ignore requirements for the content to include certain values despite precise instructions being given.

## Scope

**Priority 3 · Summary**

- **Purpose:** Zapier benchmark for <span class="verbatim">evaluating AI agents on cross-application workflow orchestration via REST APIs.</span>

- **H001 · Light green · Before: Not assessed**
    - Selected text: `evaluating AI agents on cross-application workflow orches- tration via REST APIs.`
    - Now represented under **Summary → Scope**.

    - Summary evidence: - **Purpose:** Zapier benchmark for <span class="verbatim">evaluating AI agents on cross-application workflow orchestration via REST APIs.</span>
    - Meaning: evaluating AI agents on cross-application workflow orches- tration via REST APIs.

- **H002 · Light green · Before: Not assessed**
    - Selected text: `tasks span Sales, Marketing, Operations, Support, Finance, and HR domains.`
    - Now represented under **Summary → Scope**.

    - Summary evidence: - **Scope:** 600 public tasks and 600+ private evaluation tasks; <span class="verbatim">∼500 API endpoints across 47 apps</span>; <span class="verbatim">Sales, Marketing, Operations, Support, Finance, and HR</span>.
    - Meaning: tasks span Sales, Marketing, Operations, Support, Finance, and HR domains.

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H003 · Light green · Before: Not assessed**
    - Selected text: `Grading is programmatic and end-state only:`
    - Now represented under **Summary → Scope**.

    - Summary evidence: - **Evaluation Method:** <span class="verbatim">Grading is programmatic and end-state only:</span> all required final-state assertions must pass.
    - Meaning: Grading is programmatic and end-state only:

- **H004 · Light green · Before: Not assessed**
    - Selected text: `The agent iteratively discovers and calls API endpoints to complete a task.`
    - Now represented under **Summary → Scope**.

    - Summary evidence:     - <span class="verbatim">The agent iteratively discovers and calls API endpoints to complete a task.</span>
    - Meaning: The agent iteratively discovers and calls API endpoints to complete a task.

- **H017 · Light green · Before: Not assessed**
    - Selected text: `A pool of ∼500 API endpoints across 47 apps`
    - Now represented under **Summary → Scope**.

    - Summary evidence: - **Scope:** 600 public tasks and 600+ private evaluation tasks; <span class="verbatim">∼500 API endpoints across 47 apps</span>; <span class="verbatim">Sales, Marketing, Operations, Support, Finance, and HR</span>.
    - Meaning: A pool of ∼500 API endpoints across 47 apps

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H018 · Light green · Before: Not assessed**
    - Selected text: `six distinct domains: Sales, Marketing, Opera- tions, Support, Finance, and HR.`
    - Now represented under **Summary → Scope**.

    - Summary evidence: - **Scope:** 600 public tasks and 600+ private evaluation tasks; <span class="verbatim">∼500 API endpoints across 47 apps</span>; <span class="verbatim">Sales, Marketing, Operations, Support, Finance, and HR</span>.
    - Meaning: six distinct domains: Sales, Marketing, Opera- tions, Support, Finance, and HR.

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H019 · Light green · Before: Not assessed**
    - Selected text: `100 public tasks per domain`
    - Now represented under **Summary → Scope**.

    - Summary evidence:     - Each domain has <span class="verbatim">100 public tasks per domain</span>; at least half the corpus is private, with additional hardening. Official scores use private tasks.
    - Meaning: 100 public tasks per domain

## Impact

**Priority 3 · Impact**

- **Impact:** Targets <span class="verbatim">multi-step reasoning, policy adherence, and tool discovery</span> needed for business automation through widely available REST interfaces.

- **H013 · Light green · Before: Not assessed**
    - Selected text: `REST APIs are the uni- versal standard and frequently the glue behind those tools.`
    - Now represented under **Impact**.

    - Summary evidence:     - <span class="verbatim">Though solutions like MCPs and CLI tools exist, REST APIs are the universal standard and frequently the glue behind those tools.</span>
    - Meaning: REST APIs are the uni- versal standard and frequently the glue behind those tools.

- **H014 · Light green · Before: Not assessed**
    - Selected text: `multi-step reasoning,`
    - Now represented under **Impact**.

    - Summary evidence: - **Impact:** Targets <span class="verbatim">multi-step reasoning, policy adherence, and tool discovery</span> needed for business automation through widely available REST interfaces.
    - Meaning: multi-step reasoning,

- **H015 · Light green · Before: Not assessed**
    - Selected text: `policy adherence,`
    - Now represented under **Impact**.

    - Summary evidence: - **Impact:** Targets <span class="verbatim">multi-step reasoning, policy adherence, and tool discovery</span> needed for business automation through widely available REST interfaces.
    - Meaning: policy adherence,

- **H016 · Light green · Before: Not assessed**
    - Selected text: `tool discovery`
    - Now represented under **Impact**.

    - Summary evidence: - **Impact:** Targets <span class="verbatim">multi-step reasoning, policy adherence, and tool discovery</span> needed for business automation through widely available REST interfaces.
    - Meaning: tool discovery

## Task Sourcing

**Priority 3 · Dataset Creation**

- **Task Generation:** <span class="verbatim">Tasks were synthetically generated based on use cases from real customers.</span> Models used: <span class="verbatim">Opus 4.6, GPT 5.3 Codex, and Gemini 3</span>.

- **H020 · Light green · Before: Not assessed**
    - Selected text: `Tasks were synthetically generated based on use cases from real customers.`
    - Now represented under **Dataset Creation → Task Sourcing**.

    - Summary evidence: - **Task Generation:** <span class="verbatim">Tasks were synthetically generated based on use cases from real customers.</span> Models used: <span class="verbatim">Opus 4.6, GPT 5.3 Codex, and Gemini 3</span>.
    - Meaning: Tasks were synthetically generated based on use cases from real customers.

- **H021 · Light green · Before: Not assessed**
    - Selected text: `We used Opus 4.6, GPT 5.3 Codex, and Gemini 3 in task generation.`
    - Now represented under **Dataset Creation → Task Sourcing**.

    - Summary evidence: - **Task Generation:** <span class="verbatim">Tasks were synthetically generated based on use cases from real customers.</span> Models used: <span class="verbatim">Opus 4.6, GPT 5.3 Codex, and Gemini 3</span>.
    - Workflow patterns accompanying negative feedback on Zapier’s Agents service were clustered by domain; models used those patterns as inspiration, with repeated passes on realism, difficulty, and app variety.
    - <span class="verbatim">No PII or confidential customer data was used</span>.
    - Meaning: We used Opus 4.6, GPT 5.3 Codex, and Gemini 3 in task generation.

    - Transformation reason: Original model names are retained; author-voice framing is removed.

## Hardening

**Priority 3 · Special Design**

- **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.

- **H022 · Light green · Before: Not assessed**
    - Selected text: `a variety of hardening techniques,`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence: - **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.
    - Irrelevant data: <span class="verbatim">adding irrelevant data</span>.
    - Tool call responses: <span class="verbatim">keeping key info behind tool call responses</span>.
    - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Similar names: <span class="verbatim">similar naming for incorrect entries</span>.
    - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Techniques were developed through experiments on current models; tasks found too easy were hardened.
    - <span class="verbatim">The private dataset employs additional hardening techniques to prevent overfitting on a small set of challenges.</span>
    - <span class="verbatim">Benchmark progress ideally reflects improved reasoning over novel complexity rather than mastery of a few known difficulty types.</span>
    - Meaning: a variety of hardening techniques,

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H023 · Light green · Before: Not assessed**
    - Selected text: `adding irrelevant data,`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence: - **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.
    - Irrelevant data: <span class="verbatim">adding irrelevant data</span>.
    - Tool call responses: <span class="verbatim">keeping key info behind tool call responses</span>.
    - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Similar names: <span class="verbatim">similar naming for incorrect entries</span>.
    - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Techniques were developed through experiments on current models; tasks found too easy were hardened.
    - <span class="verbatim">The private dataset employs additional hardening techniques to prevent overfitting on a small set of challenges.</span>
    - <span class="verbatim">Benchmark progress ideally reflects improved reasoning over novel complexity rather than mastery of a few known difficulty types.</span>
    - Meaning: adding irrelevant data,

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H024 · Light green · Before: Not assessed**
    - Selected text: `keeping key info behind tool call responses,`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence: - **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.
    - Irrelevant data: <span class="verbatim">adding irrelevant data</span>.
    - Tool call responses: <span class="verbatim">keeping key info behind tool call responses</span>.
    - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Similar names: <span class="verbatim">similar naming for incorrect entries</span>.
    - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Techniques were developed through experiments on current models; tasks found too easy were hardened.
    - <span class="verbatim">The private dataset employs additional hardening techniques to prevent overfitting on a small set of challenges.</span>
    - <span class="verbatim">Benchmark progress ideally reflects improved reasoning over novel complexity rather than mastery of a few known difficulty types.</span>
    - Meaning: keeping key info behind tool call responses,

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H025 · Light green · Before: Not assessed**
    - Selected text: `ambiguity of`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence:     - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Meaning: ambiguity of

- **H026 · Light green · Before: Not assessed**
    - Selected text: `where info can be found,`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence: - **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.
    - Irrelevant data: <span class="verbatim">adding irrelevant data</span>.
    - Tool call responses: <span class="verbatim">keeping key info behind tool call responses</span>.
    - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Similar names: <span class="verbatim">similar naming for incorrect entries</span>.
    - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Techniques were developed through experiments on current models; tasks found too easy were hardened.
    - <span class="verbatim">The private dataset employs additional hardening techniques to prevent overfitting on a small set of challenges.</span>
    - <span class="verbatim">Benchmark progress ideally reflects improved reasoning over novel complexity rather than mastery of a few known difficulty types.</span>
    - Meaning: where info can be found,

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H027 · Light green · Before: Not assessed**
    - Selected text: `similar naming for incorrect entries,`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence: - **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.
    - Irrelevant data: <span class="verbatim">adding irrelevant data</span>.
    - Tool call responses: <span class="verbatim">keeping key info behind tool call responses</span>.
    - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Similar names: <span class="verbatim">similar naming for incorrect entries</span>.
    - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Techniques were developed through experiments on current models; tasks found too easy were hardened.
    - <span class="verbatim">The private dataset employs additional hardening techniques to prevent overfitting on a small set of challenges.</span>
    - <span class="verbatim">Benchmark progress ideally reflects improved reasoning over novel complexity rather than mastery of a few known difficulty types.</span>
    - Meaning: similar naming for incorrect entries,

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H028 · Light green · Before: Not assessed**
    - Selected text: `strict business policy rules with overriding priorities.`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence:     - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Meaning: strict business policy rules with overriding priorities.

- **H060 · Light green · Before: Not assessed**
    - Selected text: `We used various hardening techniques to realistically increase the difficulty of the tasks.`
    - Now represented under **Special Design → Hardening**.

    - Summary evidence: - **Hardening:** Combines irrelevant data, information behind tool calls, ambiguous information locations, similar names, and overriding business policies. Private tasks use additional hardening to reduce overfitting.
    - Irrelevant data: <span class="verbatim">adding irrelevant data</span>.
    - Tool call responses: <span class="verbatim">keeping key info behind tool call responses</span>.
    - Information location: <span class="verbatim">ambiguity of</span> <span class="verbatim">where info can be found</span>.
    - Similar names: <span class="verbatim">similar naming for incorrect entries</span>.
    - Business policies: <span class="verbatim">strict business policy rules with overriding priorities.</span>
    - Techniques were developed through experiments on current models; tasks found too easy were hardened.
    - <span class="verbatim">The private dataset employs additional hardening techniques to prevent overfitting on a small set of challenges.</span>
    - <span class="verbatim">Benchmark progress ideally reflects improved reasoning over novel complexity rather than mastery of a few known difficulty types.</span>
    - Meaning: We used various hardening techniques to realistically increase the difficulty of the tasks.

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

## Task Design

**Priority 3 · Dataset Creation**

- **Task Design:** Each task requires <span class="verbatim">at least one concrete state mutation</span>; <span class="verbatim">the task is non-interactive until completion.</span> Judgment must become a structured state change.

- **H029 · Light green · Before: Not assessed**
    - Selected text: `We limit subjectivity in this benchmark, but some degree is supported in these tasks by requiring the agent to record its decision as a structured state change (e.g., updating a status field, assigning a score, routing to a queue) rather than producing free-form text.`
    - Now represented under **Dataset Creation → Task Design**.

    - Summary evidence:     - <span class="verbatim">requiring the agent to record its decision as a structured state change (e.g., updating a status field, assigning a score, routing to a queue) rather than producing free-form text.</span>
    - Meaning: We limit subjectivity in this benchmark, but some degree is supported in these tasks by requiring the agent to record its decision as a structured state change (e.g., updating a status field, assigning a score, routing to a queue) rather than producing free-form text.

    - Transformation reason: Original clause preserves every structured-decision example; author framing is removed.

- **H033 · Light green · Before: Not assessed**
    - Selected text: `at least one concrete state mutation`
    - Now represented under **Dataset Creation → Task Design**.

    - Summary evidence: - **Task Design:** Each task requires <span class="verbatim">at least one concrete state mutation</span>; <span class="verbatim">the task is non-interactive until completion.</span> Judgment must become a structured state change.
    - Meaning: at least one concrete state mutation

- **H034 · Light green · Before: Not assessed**
    - Selected text: `the task is non-interactive until completion.`
    - Now represented under **Dataset Creation → Task Design**.

    - Summary evidence: - **Task Design:** Each task requires <span class="verbatim">at least one concrete state mutation</span>; <span class="verbatim">the task is non-interactive until completion.</span> Judgment must become a structured state change.
    - Meaning: the task is non-interactive until completion.

## Reward Hardening

**Priority 3 · Quality Control · Auto Judge**

- **Reward-Hacking Checks:** Reinforcement-learning experiments exposed strategies used to strengthen the reward function.

- **H040 · Light green · Before: Not assessed**
    - Selected text: `These runs identified some common reward-hacking strategies that we used to strengthen the reward function.`
    - Now represented under **Quality Control → Auto Judge → Reward Hardening**.

    - Summary evidence: - **Reward-Hacking Checks:** Reinforcement-learning experiments exposed strategies used to strengthen the reward function.
    - Runs used Reinforcement Learning with Verifiable Rewards; discovered reward-hacking strategies informed stronger checks.
    - Meaning: These runs identified some common reward-hacking strategies that we used to strengthen the reward function.

    - Transformation reason: RL reward-hacking experiments and resulting reward improvements are merged in neutral wording.

## Tool Interface

**Priority 3 · Model Evaluation · Auto Judge**

- **Tool Interface:** <span class="verbatim">two tools: Search and Execute.</span> Search uses <span class="verbatim">BM25</span> over API schemas, returning five candidates; Execute accepts method, URL, and body. Maximum: <span class="verbatim">50 steps</span>.

- **H041 · Light green · Before: Not assessed**
    - Selected text: `two tools: Search and Execute.`
    - Now represented under **Model Evaluation → Auto Judge → Tool Interface**.

    - Summary evidence: - **Tool Interface:** <span class="verbatim">two tools: Search and Execute.</span> Search uses <span class="verbatim">BM25</span> over API schemas, returning five candidates; Execute accepts method, URL, and body. Maximum: <span class="verbatim">50 steps</span>.
    - Meaning: two tools: Search and Execute.

- **H042 · Light green · Before: Not assessed**
    - Selected text: `No authentication is mimicked.`
    - Now represented under **Model Evaluation → Auto Judge → Tool Interface**.

    - Summary evidence:     - <span class="verbatim">No authentication is mimicked.</span> <span class="verbatim">Multiple tools can be called in parallel per step.</span> The 50-step limit is rarely reached.
    - Meaning: No authentication is mimicked.

- **H043 · Light green · Before: Not assessed**
    - Selected text: `Finding the right endpoints to use is part of the challenge.`
    - Now represented under **Model Evaluation → Auto Judge → Tool Interface**.

    - Summary evidence:     - <span class="verbatim">Finding the right endpoints to use is part of the challenge.</span>
    - Meaning: Finding the right endpoints to use is part of the challenge.

- **H044 · Light green · Before: Not assessed**
    - Selected text: `The execute tool triggers a simulation of retrieving or updating a database through Pydantic Models.`
    - Now represented under **Model Evaluation → Auto Judge → Tool Interface**.

    - Summary evidence:     - <span class="verbatim">The execute tool triggers a simulation of retrieving or updating a database through Pydantic Models.</span> These models are the application-state source of truth; pagination, required fields, and 4xx errors preserve real schema shapes.
    - Meaning: The execute tool triggers a simulation of retrieving or updating a database through Pydantic Models.

- **H045 · Light green · Before: Not assessed**
    - Selected text: `Multiple tools can be called in parallel per step.`
    - Now represented under **Model Evaluation → Auto Judge → Tool Interface**.

    - Summary evidence:     - <span class="verbatim">No authentication is mimicked.</span> <span class="verbatim">Multiple tools can be called in parallel per step.</span> The 50-step limit is rarely reached.
    - Meaning: Multiple tools can be called in parallel per step.

- **H046 · Light green · Before: Not assessed**
    - Selected text: `maximum of 50 steps.`
    - Now represented under **Model Evaluation → Auto Judge → Tool Interface**.

    - Summary evidence: - **Tool Interface:** <span class="verbatim">two tools: Search and Execute.</span> Search uses <span class="verbatim">BM25</span> over API schemas, returning five candidates; Execute accepts method, URL, and body. Maximum: <span class="verbatim">50 steps</span>.
    - Meaning: maximum of 50 steps.

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

## Cost And Repeatability

**Priority 3 · Model Evaluation · Auto Judge**

- **Cost and Repeatability:** Score uses one run; reported run-to-run variance is typically within 1%. Cost is average token spending per task; latency is affected by provider rate limits.

- **H048 · Light green · Before: Not assessed**
    - Selected text: `If an agent takes multiple actions inefficiently (create the lead, update the lead 5 times instead of once), it yields the same end result and scores equally, but with a higher Cost.`
    - Now represented under **Model Evaluation → Auto Judge → Cost And Repeatability**.

    - Summary evidence:     - <span class="verbatim">If an agent takes multiple actions inefficiently (create the lead, update the lead 5 times instead of once), it yields the same end result and scores equally, but with a higher Cost.</span>
    - Meaning: If an agent takes multiple actions inefficiently (create the lead, update the lead 5 times instead of once), it yields the same end result and scores equally, but with a higher Cost.

- **H050 · Light green · Before: Not assessed**
    - Selected text: `Run-to-run variance is typically within 1%.`
    - Now represented under **Model Evaluation → Auto Judge → Cost And Repeatability**.

    - Summary evidence:     - <span class="verbatim">Run-to-run variance is typically within 1%.</span>
    - Meaning: Run-to-run variance is typically within 1%.

- **H051 · Light green · Before: Not assessed**
    - Selected text: `Cost (USD per run)`
    - Now represented under **Model Evaluation → Auto Judge → Cost And Repeatability**.

    - Summary evidence:     - <span class="verbatim">Cost is computed by taking the average token cost spent per task.</span> USD cost is the primary efficiency metric.
    - Meaning: Cost (USD per run)

    - Transformation reason: Related fragments are merged with their subject and context; edited wording, punctuation, counts, or capitalization stay in the default color. The selected meaning is retained in the bound passage.

- **H052 · Light green · Before: Not assessed**
    - Selected text: `Cost is computed by taking the average token cost spent per task.`
    - Now represented under **Model Evaluation → Auto Judge → Cost And Repeatability**.

    - Summary evidence:     - <span class="verbatim">Cost is computed by taking the average token cost spent per task.</span> USD cost is the primary efficiency metric.
    - Meaning: Cost is computed by taking the average token cost spent per task.

## Outcome Flexibility

**Priority 3 · Special Design**

- **End-State Grading:** Different valid tool sequences, parallel calls, and batched updates can earn the same score; side effects remain part of correctness.

- **H049 · Light green · Before: Not assessed**
    - Selected text: `Focusing on end-to-end results gives the agent flexibility to solve problems in creative ways (such as parallel tool calls and batched changes) while avoiding being overly prescriptive.`
    - Now represented under **Special Design → Outcome Flexibility**.

    - Summary evidence:     - <span class="verbatim">Focusing on end-to-end results gives the agent flexibility to solve problems in creative ways (such as parallel tool calls and batched changes) while avoiding being overly prescriptive.</span>
    - Meaning: Focusing on end-to-end results gives the agent flexibility to solve problems in creative ways (such as parallel tool calls and batched changes) while avoiding being overly prescriptive.

## Human Validation

**Priority 3 · Quality Control · Human Review**

- **Review Approach**

- **H058 · Light green · Before: Not assessed**
    - Selected text: `We manually inspected samples of tasks to reduce this risk.`
    - Now represented under **Quality Control → Human Review → Human Validation**.

    - Summary evidence:     - Authors inspected task samples and repeated audits; hints were audited against rules to exclude actual parameter values.
    - Meaning: We manually inspected samples of tasks to reduce this risk.

    - Transformation reason: Sample-based manual inspection and repeated audits are restated without author framing.

- **H059 · Light green · Before: Not assessed**
    - Selected text: `risk of lack of realism and impossibility.`
    - Now represented under **Quality Control → Human Review → Human Validation**.

    - Summary evidence:         - <span class="verbatim">there is a risk of lack of realism and impossibility.</span>
    - Meaning: risk of lack of realism and impossibility.

## Complementary Successes

**Priority 3 · Key Findings**

- **Different Passing Sets:** <span class="verbatim">Models are solving fairly different sets of tasks from each other.</span> Opus–Gemini <span class="verbatim">Jaccard similarity</span>: 0.17; 71% of Opus passes and 70% of Gemini passes were missed by the other.

- **H061 · Light green · Before: Not assessed**
    - Selected text: `Models are solving fairly different sets of tasks from each other.`
    - Now represented under **Key Findings → Complementary Successes**.

    - Summary evidence: - **Different Passing Sets:** <span class="verbatim">Models are solving fairly different sets of tasks from each other.</span> Opus–Gemini <span class="verbatim">Jaccard similarity</span>: 0.17; 71% of Opus passes and 70% of Gemini passes were missed by the other.
    - Meaning: Models are solving fairly different sets of tasks from each other.

- **H062 · Light green · Before: Not assessed**
    - Selected text: `Jaccard similarity`
    - Now represented under **Key Findings → Complementary Successes**.

    - Summary evidence: - **Different Passing Sets:** <span class="verbatim">Models are solving fairly different sets of tasks from each other.</span> Opus–Gemini <span class="verbatim">Jaccard similarity</span>: 0.17; 71% of Opus passes and 70% of Gemini passes were missed by the other.
    - Meaning: Jaccard similarity

## Simple Baseline

**Priority 3 · Key Findings**

- **Simple Domain:** Haiku reached 97% on simpler workflows without regular-task noise; this harness check is excluded from benchmark scores.

- **H063 · Light green · Before: Not assessed**
    - Selected text: `We also created a simple domain as a baseline to signal how well models do with simpler workflows without the noise and difficulty of regular tasks.`
    - Now represented under **Key Findings → Simple Baseline**.

    - Summary evidence: - **Simple Domain:** Haiku reached 97% on simpler workflows without regular-task noise; this harness check is excluded from benchmark scores.
    - The simple domain tests workflows with explicit instructions, distinguishing basic tool competence from the benchmark’s layered difficulty.
    - Meaning: We also created a simple domain as a baseline to signal how well models do with simpler workflows without the noise and difficulty of regular tasks.

    - Transformation reason: Simple-domain purpose, score, and exclusion from benchmark scoring are merged without author framing.

## Important Sections

**Priority 3 · Important Sections**

- Appendix, Task 1 (Sales): What Makes It Hard — Six Challenges

- **H071 · Light green · Before: Not assessed**
    - Selected text: `What Makes It Hard Six challenges the model must navigate:`
    - Now represented under **Important Sections**.

    - Summary evidence: - Appendix, Task 1 (Sales): What Makes It Hard — Six Challenges
    - Meaning: What Makes It Hard Six challenges the model must navigate:

    - Transformation reason: Highlighted appendix subsection and six-challenge count retained; Title Case and contextual identifier are edited. All six challenges also appear under Task Design.

- **H072 · Light green · Before: Not assessed**
    - Selected text: `What Makes It Hard Five challenges the model must navigate:`
    - Now represented under **Important Sections**.

    - Summary evidence: - Appendix, Task 2 (Operations): What Makes It Hard — Five Challenges
    - Meaning: What Makes It Hard Five challenges the model must navigate:

    - Transformation reason: Highlighted appendix subsection and five-challenge count retained; Title Case and contextual identifier are edited. All five challenges also appear under Task Design.

## Excluded and Unclassified

- H005: Dark green highlight, excluded by your color preferences.
- H006: Dark green highlight, excluded by your color preferences.
- H007: Dark green highlight, excluded by your color preferences.
- H008: Dark green highlight, excluded by your color preferences.
- H009: Dark green highlight, excluded by your color preferences.
- H010: Dark green highlight, excluded by your color preferences.
- H011: Dark green highlight, excluded by your color preferences.
- H039: Yellow highlight, excluded by your color preferences.
- H064: Yellow highlight, excluded by your color preferences.
