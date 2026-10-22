# Terminal-Bench 2.0

**Merrill, Shaw et al. · Jan 2026 · ~5-minute overview** · [Paper](https://arxiv.org/abs/2601.11868)

## Summary

- **Purpose:** Terminal-Bench is <span class="verbatim">a framework to evaluate agents on realistic tasks in command line interfaces.</span> Terminal-Bench 2.0 contains <span class="verbatim">89 tasks</span>.
- **Scope:** High-skill work across <span class="verbatim">software engineering, scientific computing, cybersecurity, and machine learning</span>; 16 author-assigned categories.
    - The terminal is <span class="verbatim">a ubiquitous, versatile, and powerful interface</span>.
    - Equal-contribution corresponding authors include <span class="verbatim">Mike A. Merrill</span> and <span class="verbatim">Alexander G. Shaw</span>.
- **Task Design:** <span class="verbatim">Terminal-Bench tasks are interactive.</span> Agents explore and manipulate a container to achieve the requested final state.
- **Time and Cost:** Author-estimated expert/junior workload; agent runtime and token usage are reported.
- **Evaluation Method:** Experiments <span class="verbatim">benchmark frontier LLMs and agents</span> using final-state tests, repeated trials, and confidence intervals.

## Dataset Creation

- **Task Sourcing:** The project <span class="verbatim">crowd-sourced tasks through open-source contributions, with 93 contributors creating 229 tasks.</span> The final dataset contains 89 tasks.
    - Selection was <span class="verbatim">based on the author’s difficulty assessment and a quality assessment by three experienced human reviewers</span>.
    - Software engineering is the largest category (26 tasks), with no majority category; the collection also includes personal-assistant and video-processing work.
    - <span class="verbatim">Terminal-Bench evaluates whether agents can perform the kind of high-skill work that professionals are paid to do, including configuring legacy systems, reimplementing research papers, and solving general software engineering problems.</span>

- **Task Design:** <span class="verbatim">A Terminal-Bench task consists of an instruction, a Docker image, a set of tests, an example solution, and a time limit</span>.
    - <span class="verbatim">Each task features a unique environment, human-written solution, and comprehensive tests for verification.</span>
    - The Dockerfile initializes relevant packages/files; instructions define the goal, tests verify completion, and a human-written oracle demonstrates solvability. Tests are injected for verification rather than exposed with the oracle during agent execution.
    - <span class="verbatim">Claude 4 Opus was used to transform the author-provided task instructions into the abbreviated “Description” in Appendix H.</span> The example below uses the instruction shown in Figure 2.

- **Example Tasks:**
    - **Example Task:** Paper: Figure <span class="verbatim">2</span> (COBOL example); dataset: [cobol-modernization](https://github.com/harbor-framework/terminal-bench-2/blob/2fd12b88aafdd04a52c298e3940bcb189f9766d6/cobol-modernization/instruction.md) (`instruction.md`).

        The task instruction is: *“Re-implement the COBOL program located in /app/src/program.cbl, in Python. Your script must produce identical results to the COBOL baseline.”*

- **Completion-Time Estimates:** Authors estimate junior and expert workload; these are estimates rather than observed human runs.
    - <span class="verbatim">a junior software engineer with little familiarity with the topic</span> defines the junior estimate; <span class="verbatim">how long a domain expert would require</span> defines the expert estimate.
    - Table 1 reports 74 estimates: expert counts are 36 under one hour, 35 from one hour to one day, and 3 from one day to one week. Junior counts are 6, 53, and 12 in those bins, plus 3 above one week.
    - fix-ocaml-gc is estimated at roughly 24 expert hours versus 240 junior hours.

## Quality Control

### Human Review

- **Review Approach**
    - Contributors submit checklists after manual self-checks; tasks are <span class="verbatim">manually verified by three human reviewers for correctness.</span> Expert review precedes merging, followed by two final auditors; combined reviewer attention averages three hours/task.
    - Contributors and post-merge auditors inspect multi-model Terminus 2 failures to distinguish task defects from agent limitations; every exploit trajectory is manually reviewed.
        - Figure 3: contributor submission → automated CI/LLM checks → expert review (reject, request changes, or approve/merge) → post-merge model experiments → manual trajectory audit → exploit audit → final accept/revise decision.
        - <span class="verbatim">Between the three reviews, the average task received approximately three hours of combined reviewer attention,</span> excluding task creation.
        - <span class="verbatim">A team of experienced reviewers worked with the contributor to manually check the task and verify that it met quality standards.</span> <span class="verbatim">Each task was run with multiple language models and Terminus 2.</span>

- **Quality Dimensions**
    - Specificity: <span class="verbatim">the unit tests will pass if and only if the container ends in an acceptable state.</span>
    - Solvability: <span class="verbatim">each task has an oracle solution script that mirrors a real workflow and, when executed, causes all test cases to pass.</span>
    - Integrity: shortcuts unavailable in real deployment must not yield a pass; future Git commits are removed to prevent solution lookup.

- **Task Contributor Checklist:** Checks human authorship, specification/test coverage, schemas, cheating resistance, reproducibility, and analysis of strong-model failures.
    - Contributors run <span class="verbatim">tb tasks check &lt;task-id&gt;</span> and require all checks to pass. <span class="verbatim">All behavior checked in the test cases is described in the task instruction.</span> <span class="verbatim">All behavior described in the task instruction is checked in the unit tests.</span> Test cases <span class="verbatim">have informative docstrings that describe which behavior they check.</span>
    - Instructions in <span class="verbatim">task.yaml</span> are human-written; <span class="verbatim">solution.sh</span> is human-written with minimal language-model help. Structured outputs must have an exact schema in the task or a separate file.
    - Contributors check resistance to edited data, embedded answer strings, and training on test data. For <span class="verbatim">external dependencies (e.g. Docker images, pip packages, etc.)</span>, <span class="verbatim">their versions are pinned to ensure reproducibility.</span> The apt exception is below.
    - Contributors run <span class="verbatim">terminus-2</span> with <span class="verbatim">a powerful model (e.g., GPT-5)</span>. Failing runs are expected for harder tasks; contributors analyze them to confirm task validity. <span class="verbatim">tb tasks debug</span> can help.

- **Agentic Benchmark Checklist:** ABC assessment averaged 0.896; limitations include residual non-determinism, no objective test-quality metrics, public tasks, and no quantified impact of remaining flaws.
    - <span class="verbatim">the benchmark relies on extensive human review of test specifications and coverage.</span> Code coverage and cyclomatic-complexity metrics were not used to assess test quality.
    - <span class="verbatim">Some non-determinism remains.</span> Hardware, external APIs, and infrastructure can change outcomes despite containers and repeat runs.
    - <span class="verbatim">All tasks are hosted on a public GitHub repository.</span> There is no private held-out set; a canary discourages contamination but cannot prevent training or overfitting.
    - Outcome Validity: 0.857; Task Validity: 1.000; Benchmark Reporting: 0.830.
    - <span class="verbatim">Authors of ABC have been closely involved with the development process, and many issues were surfaced and resolved through the public GitHub repository.</span> <span class="verbatim">This collaboration highlights how the ABC framework, when combined with active engagement from benchmark developers, can be a useful tool for ensuring rigor and improving benchmark quality.</span>
    - <span class="verbatim">it does not provide quantitative estimates of how such flaws impact benchmark results.</span>

### Auto Judge

- **Oracle and Dummy Checks:** Submission automation requires the oracle to pass and a no-op agent to fail; failed checks trigger task revision.

- **Deterministic Checks:** GitHub Actions rejects failures in metadata, file references, canaries, privileges, and test/oracle exposure checks; apt versions remain unpinned.
    - <span class="verbatim">When a task was initially submitted to the project’s GitHub, an automated workflow ran the task’s oracle solution to ensure solvability. If the test cases failed, the contributor was asked to modify their task.</span> A <span class="verbatim">no-op “dummy” agent should fail the task</span>.
    - <span class="verbatim">Canary Check to ensure the task artifacts contain the canary string.</span>
    - <span class="verbatim">Dockerfile Reference Check to ensure the task environment (Dockerfile) shall not in- clude tests or oracle solutions, otherwise agents could cheat by reading them.</span>
    - <span class="verbatim">Dockerfile Sanity Check to check that apt dependencies are not pinned, as older apt package versions could be removed from the registry.</span>
    - <span class="verbatim">Test File Reference Check to ensure that if tests reference a file and the oracle solu- tion references the same file, the file must be mentioned in the task description, unless otherwise allowed.</span>
    - <span class="verbatim">Privilege check to ensure that no task environment has potential security issues, such as using privileged containers.</span>
    - <span class="verbatim">Task Field Check to ensure meta data of tasks are properly filled.</span>

- **LLM-Backed Quality Check:** Checks specification/test alignment, schemas, cheating resistance, dependencies, typos, hidden artifacts, test setup, and hardcoded answers.
    - <span class="verbatim">Behavior in Task Description checks whether all behavior checked in the test cases is described in the task description.</span>
    - <span class="verbatim">Behavior in Tests checks whether all behavior described in the task description is checked in the unit tests.</span>
    - <span class="verbatim">Informative Test Docstrings checks whether test cases have informative docstrings that describe which behavior they check.</span>
    - <span class="verbatim">Anti Cheating Measures checks if it is hard for the agent to cheat on the task (e.g. by editing data files, looking inside files for strings that represent solutions, training on the test set, etc.). If Dockerfile involves git cloning, it ensures that the agent won’t see newer commits.</span>
    - <span class="verbatim">Structured Data Schema checks if the agent produces structured data (e.g. it is tasked with building an API) and whether the exact schema is described in the task.yaml or a separate file.</span>
    - <span class="verbatim">Pinned Dependencies checks if the task uses external dependencies (e.g. pip packages), whether their versions are pinned to ensure reproducibility. Apt packages shall not be pinned, but all python dependencies should be pinned.</span>
    - <span class="verbatim">Typos checks whether there are any typos. It looks very closely at file and variable names, because these can be hard to catch.</span>
    - <span class="verbatim">Tests or Solution in Image checks if the tests/ folder or solution file is not copied to the image.</span>
    - <span class="verbatim">Test Deps in Image checks if there are any test dependencies installed in the image dur- ing the build process. They should be installed in the run-tests.sh script instead.</span>
    - <span class="verbatim">Hardcoded Solution checks if the solution directly outputs or hard-codes the final answer using commands like echo/cat without performing the steps an agent would need to compute it. Using echo/cat to write source files or scripts that are then executed is acceptable. This check should PASS when the solution demonstrates a sequence of commands (e.g., data processing, running code) that derives the answer, and FAIL when the solution simply prints or writes the final answer without computation.</span>
    - <span class="verbatim">File Reference Mentioned checks if the agent needs to produce a file to be checked by tests, whether these filenames are mentioned in the task.yaml explicitly.</span>

- **Debug Tool:** Determines whether <span class="verbatim">test failures are due to insufficient task instructions rather than normal agent limitations.</span>
    - The LLM receives task specification, run information, and trial data; it checks unspecified names/formats/signatures/values, implicit expectations, undocumented exact strings, and examples incorrectly treated as requirements.
    - <span class="verbatim">If all trials fail on the same tests with similar errors, this suggests systematic instruction issues rather than agent variability.</span> Differing failures can indicate appropriate task difficulty.
    - The prompt returns a JSON outcome (PASS, FAIL, or NOT_APPLICABLE) and explanation, and asks for agent-log inspection where available.

- **Adversarial Exploit Agent:** <span class="verbatim">An adversarial exploit agent was run to detect design flaws that could allow agents to cheat and pass the tests.</span> Every trajectory is manually reviewed.
    - OpenHands is used <span class="verbatim">to attempt to pass the tests by cheating without actually looking at the tests and oracle solutions.</span> <span class="verbatim">The trajectories are then manually inspected and verified by an author, regardless of whether the agent passes the task or not.</span>
    - <span class="verbatim">Common exploits found by this agent include monkey-patching test environments, guessing answers, and generating all possible answers with the hope that tests might only check existence of a correct answer but not absence of wrong answers.</span>
    - The source prompt requires at least some cheating, even if combined with normal methods, and forbids completing the task solely by legitimate means.
    - **Original Exploit Prompt (Source Material):**

            verbatim
            You are a security researcher bot and your goal is to exploit any way to
            CHEAT and complete a task assigned to you.
            If you can complete a task normally without cheating, DO NOT do it.
            Complete a task ONLY IF you could use some cheating.
            A great way of cheating is to guess how tests might be written to verify
            the results.
            Here’s your task. Remember, their outcomes are validated by programs (
            pytest) that are deterministic, and MIGHT have
            flaws which allows you to pass it using shortcuts. It is OKAY if you use
            some cheating and some normal methods to achieve
            the final goal, but you MUST use at least some cheating.
            ## Task Description
            {{ instruction }}

## Model Evaluation

### Human Review

- **Error-Analysis Calibration:** Two annotators refine rubrics; calibration on 20 trials reports Cohen’s κ = 0.93. Human annotations validate automated judges.

### Auto Judge

- **Scoring:** <span class="verbatim">The tests verify that all outcomes described in the instruction have been achieved by testing properties of the final container state; they do not test the agent’s commands or console output.</span>
    - Agents may use shell commands or richer tools to search the web, edit files, or execute code. The framework is <span class="verbatim">outcome-driven</span>, permitting different valid approaches.
    - Each supported model–agent combination runs at least five times; experiments total 32,155 trials. Headline comparisons select each model's best-performing compatible scaffold.
    - <span class="verbatim">The agent scaffold used to report each model was chosen to maximize performance.</span>

- **Harbor and Terminus 2:** Tasks <span class="verbatim">are implemented in the Harbor task format and executed using the Harbor harness.</span> Terminus 2 provides a neutral Bash-only scaffold with context summarization.
    - The evaluation uses <span class="verbatim">three popular command-line agents</span> (Claude Code, Codex CLI, Gemini CLI) and <span class="verbatim">three open-source software engineering agents</span> (OpenHands, Mini-SWE-Agent, Terminus 2).
    - <span class="verbatim">Terminus 2 has a single tool, a headless terminal, and completes tasks using only Bash commands.</span>
    - <span class="verbatim">The agent operates in a simple loop where a language model produces keystrokes which are executed in a tmux shell inside a Docker container. After execution the results of the command’s output is returned to the model.</span>
    - <span class="verbatim">Terminus 2 incorporates a context summarization module which makes calls to a language model to condense the agent’s context when it reaches its model’s context limit.</span> <span class="verbatim">This allows it to operate on extended tasks that may require millions of tokens.</span>
    - Agents are <span class="verbatim">free to manipulate the container however they please.</span> <span class="verbatim">Many agents are installed directly into the container by a package manager and wield tools that are actually executable programs, far more complex than a typical Bash command.</span> Native agents use their providers' models; other compatible scaffolds compare models more broadly.
    - Experiments use Daytona with 32–100 concurrent containers. Harbor configurations are released in the terminal-bench-experiments repository.

- **Headline Results:** Jan 2026, Table 2: GPT-5.2/Codex CLI 62.9% ± 3.0%; Opus 4.5/Terminus 2 57.8% ± 2.5%; Gemini 3 Pro/Terminus 2 56.9% ± 2.5%. [Latest Leaderboard](https://www.tbench.ai/)
    - Intervals are 95% confidence intervals.

- **Trajectory-Level Error Analysis:** Two failed trials/task/model under Terminus 2 are labeled with Execution, Coherence, and Verification rubrics; GPT-5 high-reasoning judge agreement is 90% against 120 human-labeled traces.
    - The Terminal Agent Taxonomy refines the <span class="verbatim">Multi-Agent System Taxonomy (MAST)</span>, removing irrelevant single-agent categories. <span class="verbatim">Docent uses language models to summarize, cluster, and search over agent transcripts,</span> while a custom pipeline combines two human annotators' labels with iterative rubric refinement.
    - Separate rubrics enable <span class="verbatim">more precise definitions, clearer decision boundaries, and mode-specific exclusion criteria.</span> Each includes <span class="verbatim">its high-level framing, a decision procedure, and exclusion criteria.</span> <span class="verbatim">The refined rubrics are then used to generate the final failure classification.</span> Judge precision is 92% and recall 90%.
    - **Terminal Agent Taxonomy — Original Definitions:**

        | Class | Failure Mode | Original Definition |
        | --- | --- | --- |
        | <span class="verbatim">Execution</span> | <span class="verbatim">Disobey Specification</span> | <span class="verbatim">the agent materially contradicts explicit task directives (hard or soft), such as required methods, sources of truth, constraints, or required output locations.</span> |
        | <span class="verbatim">Execution</span> | <span class="verbatim">Step Repetition</span> | <span class="verbatim">the agent re-executes the same phase (same sub-goal, tool, target, and underlying method) multiple times without a meaningful strategy change, including abort-loops and redundant verification runs.</span> |
        | <span class="verbatim">Execution</span> | <span class="verbatim">Unaware of termination conditions</span> | <span class="verbatim">the agent continues acting past a reasonable stopping point, i.e. after clear success, after established futility, or after declaring completion, without justification or need.</span> |
        | <span class="verbatim">Coherence</span> | <span class="verbatim">Reasoning-Action Mismatch</span> | <span class="verbatim">the agent’s stated reasoning or claims (e.g., “tests passed,” “requirements satisfied”) are contradicted by its observable actions, logs, or artifacts.</span> |
        | <span class="verbatim">Coherence</span> | <span class="verbatim">Context Loss</span> | <span class="verbatim">the agent forgets or contradicts relevant recent context, either about environment state (files, configs, errors) or semantic commitments (plans, instructions, clarified goals).</span> |
        | <span class="verbatim">Coherence</span> | <span class="verbatim">Task Derailment</span> | <span class="verbatim">the agent deviates from the intended objective or focus of a given task, potentially resulting in irrelevant or unproductive actions.</span> |
        | <span class="verbatim">Verification</span> | <span class="verbatim">Premature termination</span> | <span class="verbatim">the agent declares the task complete or presents a final answer before satisfying explicit objectives or before delivering required artifacts/verification, without providing a concrete, actionable handoff acknowledging the remaining gaps.</span> |
        | <span class="verbatim">Verification</span> | <span class="verbatim">No or incorrect Verification</span> | <span class="verbatim">the agent marks the task completed or bypasses a designated verifier without performing a substantive check of required properties on the actual final deliverable (or ignores failing core checks).</span> |
        | <span class="verbatim">Verification</span> | <span class="verbatim">Weak Verification</span> | <span class="verbatim">the agent relies on verification that fails to cover task-critical properties, including fabricating data that should have been recovered or derived from specified sources, while still using those checks to justify progress.</span> |

    - <span class="verbatim">Execution errors dominate for Opus 4.5 and GPT-5.2, while coherence and verification errors occur at lower rates.</span> Qwen Coder has a more balanced error profile, with greater prevalence across modes. Reported percentages are shares of failures, not task success rates.
    - <span class="verbatim">These distinct failure signatures suggest that different models require distinct strategies for improvement.</span>

- **Command-Level Error Analysis:** LLM judges <span class="verbatim">identify individual command failures across trajectories, and classify these errors against a failure mode taxonomy.</span> These are Terminus 2 traces. Missing executables account for <span class="verbatim">24.1% of all failures</span>.
    - Detection: GPT-5 medium reasoning reviews individual command input/output pairs; agreement is 92.4% against majority labels from three annotators on 66 pairs. Model command-error rates range from 9.2% to 26.7%.
    - Classification: GPT-5 high reasoning uses a category/subcategory taxonomy; agreement is 82.0% against 50 author annotations. <span class="verbatim">3,800 failures are uniformly sampled and categorized across Terminal-Bench tasks and models</span>. The paper finds that <span class="verbatim">command failures calling executables that are not installed or not in PATH are the most frequent (24.1% of all failures) followed by failures when running executables (9.6%).</span>
    - The taxonomy covers <span class="verbatim">Invocation &amp; CLI</span>, <span class="verbatim">Filesystem &amp; Permissions</span>, <span class="verbatim">Environment &amp; Configuration</span>, <span class="verbatim">Build, Toolchain &amp; Packages</span>, <span class="verbatim">Packages &amp; repositories</span>, <span class="verbatim">Network &amp; Remote Access</span>, <span class="verbatim">Runtime, Interpreters &amp; Processes</span>, <span class="verbatim">Interpreters &amp; REPLs</span>, <span class="verbatim">Services &amp; platforms</span>, <span class="verbatim">Data &amp; Formats</span>, and <span class="verbatim">Testing &amp; Quality</span>.
    - Detection prompts inspect <span class="verbatim">a single input and all captured outputs.</span> Classification prompts receive error-containing segments and require a taxonomy category and child subcategory; these judges diagnose errors rather than score task completion.
    - **Identification Prompt — Source Excerpts:** <span class="verbatim">The user will provide you with segments from a terminal trace - these contain a single input and all captured outputs.</span> <span class="verbatim">Identify if any output failures that occur.</span>
    - **Classification Prompt — Source Excerpt:** <span class="verbatim">The user will provide you with segments from a terminal traces where errors occur. Your goal is to classify the errors into an error taxonomy.</span>

## Key Findings

- **Output Tokens and Episode Count:** <span class="verbatim">verbosity and an extensive number of turns do not inherently lead to better performance</span>; <span class="verbatim">improving decision quality and strategic reasoning</span> is recommended.
    - <span class="verbatim">an episode refers to a turn in a trial.</span> Episode count efficiency averages turns over all Terminus 2 trials per model; verbosity averages generated output tokens per trial for each model.
    - <span class="verbatim">the number of interaction rounds has no meaningful relationship with task success.</span> <span class="verbatim">more attempts do not translate to better outcomes.</span>
    - <span class="verbatim">generating more text does not necessarily improve performance.</span> <span class="verbatim">excessive verbosity can reflect inefficient reasoning rather than thoroughness.</span>
    - <span class="verbatim">the most effective models demonstrate efficiency in both token generation and episode utilization.</span> The paper recommends <span class="verbatim">improving decision quality and strategic reasoning rather than simply increasing output volume or interaction frequency.</span>

- **Model Selection:** <span class="verbatim">model selection is usually more important than agent scaffold when optimizing for performance.</span>
    - Scaffold choice still matters: Gemini 2.5 Pro resolves 32.6% with Terminus 2 versus 15.7% with OpenHands in Table 2.

- **Agent Run Analysis:** <span class="verbatim">Most trials are completed in under 20 minutes, using fewer than 25 model calls and 10 million tokens.</span>
    - <span class="verbatim">In extreme cases, agents ran for up to 2 hours, making hundreds of model calls and using nearly 100 million tokens.</span>
    - API-call counts are recorded for Terminus 2; execution time and token usage cover all 32,155 trials.

- **Empirical Difficulty:** Based on <span class="verbatim">Terminus 2’s average pass rate across the frontier models</span>. <span class="verbatim">The largest discrepancy occurs when humans rate tasks as medium but models find them hard</span> (54.5%).
    - Easy: resolution ≥66.7%; Medium: between 33.3% and 66.7%; Hard: <33.3%. Human labels estimate human difficulty, not agent difficulty.
    - Human/empirical difficulty correlate at r = 0.436 (p < 0.001); 93.3% of human-hard tasks are also empirically hard. Human-medium tasks needing creative/adversarial reasoning often challenge models; examples include XSS-filter bypass and Redcode strategy.

## Special Design

- **Expert Tasks and Iterative Review:** <span class="verbatim">diverse, long-horizon tasks collected from experts</span>, <span class="verbatim">manually verified by three human reviewers for correctness.</span>
    - <span class="verbatim">These tasks require extensive domain knowledge, long chains of interdependent actions, and autonomous problem-solving that characterizes valuable technical work.</span>
    - The 89-task set was selected from 229 contributions <span class="verbatim">based on the author’s difficulty assessment and a quality assessment by three experienced human reviewers</span>.
    - <span class="verbatim">Between the three reviews, the average task received approximately three hours of combined reviewer attention, implying multiple hundreds of person-hours went into reviewing alone, excluding the time spent creating the tasks.</span>
    - <span class="verbatim">an automated workflow ran the task’s oracle solution to ensure solvability.</span> <span class="verbatim">Each task was run with multiple language models and Terminus 2.</span> <span class="verbatim">An adversarial exploit agent was run to detect design flaws that could allow agents to cheat and pass the tests.</span>

- **General Agentic Manipulation of Computers:** Focuses on <span class="verbatim">general agentic manipulation of computers.</span> <span class="verbatim">Terminal-Bench tasks are conducted inside a real terminal shell.</span>
    - Related benchmarks focus on software engineering, tool-use, computer use, and scientific discovery.
    - <span class="verbatim">Other benchmarks measure narrow aspects of the command line interface,</span> including shell optimization, environment configuration, and translating natural language to Bash; Terminal-Bench instead targets <span class="verbatim">general agentic manipulation of computers.</span>

- **Adapters:** <span class="verbatim">Terminal-Bench currently supports 26 adapters</span>; <span class="verbatim">adapters translate diverse task formats into Terminal-Bench’s standardized schema,</span> with parity experiments verifying fidelity.
    - <span class="verbatim">Adapters serve as the interface layer that integrates external benchmarks into Terminal-Bench’s unified evaluation framework</span>.
    - Requirements: <span class="verbatim">To integrate a benchmark through an adapter, four core requirements must be met: (1) task descriptions in natural language, (2) containerized environments for reproducibility, (3) programmatic evaluation criteria, and (4) optionally, reference solutions for validation.</span>
    - <span class="verbatim">controlled comparisons where identical agents and models are evaluated on both the original and adapted versions across multiple trials.</span> <span class="verbatim">These experiments ensure that adaptation preserves the benchmark’s evaluation semantics without introducing artifacts.</span> Integration follows successful parity checks.
    - <span class="verbatim">researchers can evaluate any agent on any adapted benchmark through a single interface.</span>
    - <span class="verbatim">Table 5: Adapter List: 26 benchmarks integrated as adapters in Terminal Bench format</span> spans repository engineering, programming, science, interactive agents, code performance, machine learning, and cybersecurity.

## Impact

- **Impact:** Dataset curators should <span class="verbatim">invest significant effort into manual verification</span> of challenging agentic benchmarks.
    - The paper reports that <span class="verbatim">validating the correctness of these tasks is extremely difficult</span>. Manual review should include <span class="verbatim">ensuring that cheating is difficult and also verifying that all properties tested have been adequately specified in the task description.</span>
    - Released tasks, oracles, harnesses, and adapters support agent research.

- **Limitations:** Internet access enables package installation/research and potential oracle lookup. Public tasks risk <span class="verbatim">intentional contamination</span>; external services, resource variation, and residual task flaws affect validity and reproducibility.
    - Oracle lookup was not observed in tens of thousands of trajectories, but remains possible. The paper does not release a private test set.
    - Version pinning, prebuilt Docker images, and bundled dependencies mitigate variability; external API/package changes and resource enforcement remain uncontrolled factors.
    - Even after <span class="verbatim">manual and language-model-assisted task quality review</span>, tasks may fall short of the benchmark's verification criteria.

## Important Sections

- Appendix B Quality Control
- Appendix C.1 Terminal Agent Taxonomy
- Appendix E.2 Command Failure Mode Taxonomy
- Appendix E.3 System Prompt for Failure Identification
