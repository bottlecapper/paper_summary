# DeepSWE Highlight Audit

All 139 included highlights are mapped to the revised summary. Topics are ordered by their highest highlight priority; selections within each topic are ordered by priority, then paper order.

Prior-coverage judgments are a manual semantic review. Annotation accounting is checked programmatically. Raw selections retain PDF extraction artifacts; mathematical selections are explained in context in the summary.

Previous statuses: **Covered**, **Partial**, **Title only**, or **Missing**. New coverage means the highlighted information is represented by a topic lead, source excerpt, definition, or merged equivalent passage—not that every duplicate fragment is repeated verbatim.

## Design Advantages

**Priority 1 · Special Design**

- **Original Tasks and Leakage Control:** Tasks <span class="verbatim">are authored from scratch</span> and <span class="verbatim">never merged upstream</span>; containers hold only a shallow base-commit clone.

- **H009 · Red rectangle · Before: Covered**
    - Selected text: `• every task is authored from scratch and never Original tasks, authored at repository scale: merged upstream, so its reference solution is absent from the public commit and pull-request record that pretraining corpora scrape (§3.3). • tasks span a broad pool of 91 repositories across five languages. High diversity: • prompts are about half the length of SWE-Bench Larger solutions from shorter prompts: Pro’s, yet reference solutions require more code and more output tokens. 5.5× ∼2× • verifiers are hand-written to test observable software behavior rather Functional verification: than implementation details.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **Original Tasks and Leakage Control:** Tasks <span class="verbatim">are authored from scratch</span> and <span class="verbatim">never merged upstream</span>; containers hold only a shallow base-commit clone.
    - <span class="verbatim">Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.</span>
    - Most public agentic coding benchmarks are <span class="verbatim">built by mining merged fixes from public repositories</span>; this scales, but introduces contamination and inherited-test grading risks.
    - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - <span class="verbatim">DeepSWE tasks aren’t derived from existing public commits, and the task container ships a shallow clone with only the base commit, so there’s no gold hash in the workspace to find.</span>
    - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
- **<span class="verbatim">Larger solutions from shorter prompts:</span>** Mean prompts: 2,158 versus 4,614 characters on SWE-Bench Pro; mean reference code added: 668 versus 120 lines; files edited: 7.4 versus 5.1.
    - The four highlighted design contributions are original never-merged tasks, broad coverage (91 repositories/five languages), larger solutions from shorter prompts, and hand-written functional verification.
    - Prompts are roughly half as long, with 5.5× more reference code and roughly twice the output tokens. They state desired functionality, leaving agents to discover implementation locations and design tradeoffs.
    - <span class="verbatim">given a short task description, can an agent working autonomously inside a repository produce the requested change, typically large and multi-file, whose functional correctness the verifier confirms.</span>
    - <span class="verbatim">Agents must discover where and how to implement the change, so a substantial share of the capabilities being evaluated involves end-to-end exploration instead of just the execution of an overspecified engineering task.</span>
    - The paper’s Happy DOM example states shutdown/body-read behavior without enumerating implementation files or symbols. Its SWE-Bench Pro comparison specifies function names, file paths, signatures, and a requirements checklist.
- **Functional Verifiers:** Public <span class="verbatim">APIs and observable outputs</span> accept valid alternatives and reject no-op implementations.
    - <span class="verbatim">Verifiers run end-to-end functional assertions, so a no-op fails the check on observable software behavior regardless of signature.</span>
    - Behavioral grading <span class="verbatim">lets prompts stay short and natural</span>.
    - Inherited pull-request tests split into <span class="verbatim">FAIL_TO_PASS</span> (new tests) and <span class="verbatim">PASS_TO_PASS</span> (existing regression tests); their original purpose was confirming one fix. They can reject correct alternatives or reward incomplete implementations.
    - Adding requirements/interface blocks reduces naming mismatches but does not change inherited-test grading. Purpose-written verifiers check requested behavior: <span class="verbatim">any implementation providing the requested functionality is accepted;</span> implementation shape is not the criterion.
    - Meaning: All four red-box contributions: original never-merged tasks, 91-repository/five-language diversity, larger solutions from shorter prompts, and hand-written functional grading.

    - Transformation reason: The rectangle or introductory pointer spans several points. Source order is reorganized into corresponding topic bullets/excerpts; all listed contributions or QA requirements remain represented.

- **H028 · Bright green · Before: Covered**
    - Selected text: `decontamination strategies.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
    - Meaning: Selected point: decontamination strategies.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H002 · Light green · Before: Covered**
    - Selected text: `two problems:`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **Original Tasks and Leakage Control:** Tasks <span class="verbatim">are authored from scratch</span> and <span class="verbatim">never merged upstream</span>; containers hold only a shallow base-commit clone.
    - <span class="verbatim">Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.</span>
    - Most public agentic coding benchmarks are <span class="verbatim">built by mining merged fixes from public repositories</span>; this scales, but introduces contamination and inherited-test grading risks.
    - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - <span class="verbatim">DeepSWE tasks aren’t derived from existing public commits, and the task container ships a shallow clone with only the base commit, so there’s no gold hash in the workspace to find.</span>
    - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
- **<span class="verbatim">Larger solutions from shorter prompts:</span>** Mean prompts: 2,158 versus 4,614 characters on SWE-Bench Pro; mean reference code added: 668 versus 120 lines; files edited: 7.4 versus 5.1.
    - The four highlighted design contributions are original never-merged tasks, broad coverage (91 repositories/five languages), larger solutions from shorter prompts, and hand-written functional verification.
    - Prompts are roughly half as long, with 5.5× more reference code and roughly twice the output tokens. They state desired functionality, leaving agents to discover implementation locations and design tradeoffs.
    - <span class="verbatim">given a short task description, can an agent working autonomously inside a repository produce the requested change, typically large and multi-file, whose functional correctness the verifier confirms.</span>
    - <span class="verbatim">Agents must discover where and how to implement the change, so a substantial share of the capabilities being evaluated involves end-to-end exploration instead of just the execution of an overspecified engineering task.</span>
    - The paper’s Happy DOM example states shutdown/body-read behavior without enumerating implementation files or symbols. Its SWE-Bench Pro comparison specifies function names, file paths, signatures, and a requirements checklist.
- **Functional Verifiers:** Public <span class="verbatim">APIs and observable outputs</span> accept valid alternatives and reject no-op implementations.
    - <span class="verbatim">Verifiers run end-to-end functional assertions, so a no-op fails the check on observable software behavior regardless of signature.</span>
    - Behavioral grading <span class="verbatim">lets prompts stay short and natural</span>.
    - Inherited pull-request tests split into <span class="verbatim">FAIL_TO_PASS</span> (new tests) and <span class="verbatim">PASS_TO_PASS</span> (existing regression tests); their original purpose was confirming one fix. They can reject correct alternatives or reward incomplete implementations.
    - Adding requirements/interface blocks reduces naming mismatches but does not change inherited-test grading. Purpose-written verifiers check requested behavior: <span class="verbatim">any implementation providing the requested functionality is accepted;</span> implementation shape is not the criterion.
    - Meaning: Two structural problems: public-fix contamination and inherited tests designed for one patch.

    - Transformation reason: The rectangle or introductory pointer spans several points. Source order is reorganized into corresponding topic bullets/excerpts; all listed contributions or QA requirements remain represented.

- **H004 · Light green · Before: Covered**
    - Selected text: `hand-written verifier`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - The four highlighted design contributions are original never-merged tasks, broad coverage (91 repositories/five languages), larger solutions from shorter prompts, and hand-written functional verification.
    - Meaning: Selected point: hand-written verifier

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H005 · Light green · Before: Partial**
    - Selected text: `That recipe is scalable, but it carries two structural costs.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **Original Tasks and Leakage Control:** Tasks <span class="verbatim">are authored from scratch</span> and <span class="verbatim">never merged upstream</span>; containers hold only a shallow base-commit clone.
    - <span class="verbatim">Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.</span>
    - Most public agentic coding benchmarks are <span class="verbatim">built by mining merged fixes from public repositories</span>; this scales, but introduces contamination and inherited-test grading risks.
    - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - <span class="verbatim">DeepSWE tasks aren’t derived from existing public commits, and the task container ships a shallow clone with only the base commit, so there’s no gold hash in the workspace to find.</span>
    - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
- **<span class="verbatim">Larger solutions from shorter prompts:</span>** Mean prompts: 2,158 versus 4,614 characters on SWE-Bench Pro; mean reference code added: 668 versus 120 lines; files edited: 7.4 versus 5.1.
    - The four highlighted design contributions are original never-merged tasks, broad coverage (91 repositories/five languages), larger solutions from shorter prompts, and hand-written functional verification.
    - Prompts are roughly half as long, with 5.5× more reference code and roughly twice the output tokens. They state desired functionality, leaving agents to discover implementation locations and design tradeoffs.
    - <span class="verbatim">given a short task description, can an agent working autonomously inside a repository produce the requested change, typically large and multi-file, whose functional correctness the verifier confirms.</span>
    - <span class="verbatim">Agents must discover where and how to implement the change, so a substantial share of the capabilities being evaluated involves end-to-end exploration instead of just the execution of an overspecified engineering task.</span>
    - The paper’s Happy DOM example states shutdown/body-read behavior without enumerating implementation files or symbols. Its SWE-Bench Pro comparison specifies function names, file paths, signatures, and a requirements checklist.
- **Functional Verifiers:** Public <span class="verbatim">APIs and observable outputs</span> accept valid alternatives and reject no-op implementations.
    - <span class="verbatim">Verifiers run end-to-end functional assertions, so a no-op fails the check on observable software behavior regardless of signature.</span>
    - Behavioral grading <span class="verbatim">lets prompts stay short and natural</span>.
    - Inherited pull-request tests split into <span class="verbatim">FAIL_TO_PASS</span> (new tests) and <span class="verbatim">PASS_TO_PASS</span> (existing regression tests); their original purpose was confirming one fix. They can reject correct alternatives or reward incomplete implementations.
    - Adding requirements/interface blocks reduces naming mismatches but does not change inherited-test grading. Purpose-written verifiers check requested behavior: <span class="verbatim">any implementation providing the requested functionality is accepted;</span> implementation shape is not the criterion.
    - Meaning: Merged-fix mining is scalable but introduces recall and inherited-test validity risks.

    - Transformation reason: The rectangle or introductory pointer spans several points. Source order is reorganized into corresponding topic bullets/excerpts; all listed contributions or QA requirements remain represented.

- **H006 · Light green · Before: Covered**
    - Selected text: `a high score can reflect recall rather than problem-solving,`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - Meaning: Selected point: a high score can reflect recall rather than problem-solving,

- **H007 · Light green · Before: Covered**
    - Selected text: `those tests were written to confirm one particular fix, not to grade an arbitrary new solution, so they can reject a valid alternative implementation or accept an incomplete one.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Inherited pull-request tests split into <span class="verbatim">FAIL_TO_PASS</span> (new tests) and <span class="verbatim">PASS_TO_PASS</span> (existing regression tests); their original purpose was confirming one fix. They can reject correct alternatives or reward incomplete implementations.
    - Meaning: Selected point: those tests were written to confirm one particular fix, not to grade an arbitrary new solution, so they can reject a valid alternative implementation or accept an incomplete one.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H008 · Light green · Before: Covered**
    - Selected text: `Larger solutions from shorter prompts:`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **<span class="verbatim">Larger solutions from shorter prompts:</span>** Mean prompts: 2,158 versus 4,614 characters on SWE-Bench Pro; mean reference code added: 668 versus 120 lines; files edited: 7.4 versus 5.1.
    - Meaning: Selected point: Larger solutions from shorter prompts:

- **H012 · Light green · Before: Covered**
    - Selected text: `120 lines of code`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **<span class="verbatim">Larger solutions from shorter prompts:</span>** Mean prompts: 2,158 versus 4,614 characters on SWE-Bench Pro; mean reference code added: 668 versus 120 lines; files edited: 7.4 versus 5.1.
    - Meaning: Selected point: 120 lines of code

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H013 · Light green · Before: Covered**
    - Selected text: `contamination`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - Meaning: Selected point: contamination

- **H015 · Light green · Before: Covered**
    - Selected text: `given a short task description, can an agent working autonomously inside a repository produce the requested change, typically large and multi-file, whose functional correctness the verifier confirms.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - <span class="verbatim">given a short task description, can an agent working autonomously inside a repository produce the requested change, typically large and multi-file, whose functional correctness the verifier confirms.</span>
    - Meaning: Selected point: given a short task description, can an agent working autonomously inside a repository produce the requested change, typically large and multi-file, whose functional correctness the verifier confirms.

- **H026 · Light green · Before: Covered**
    - Selected text: `avoids pull-request mining by authoring tasks directly,`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - <span class="verbatim">Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.</span>
    - Meaning: Selected point: avoids pull-request mining by authoring tasks directly,

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H027 · Light green · Before: Covered**
    - Selected text: `DeepSWE occupies a distinct point among these neighbors: original, never-merged tasks at repository scale in the everyday format of a short request against an existing codebase.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **Original Tasks and Leakage Control:** Tasks <span class="verbatim">are authored from scratch</span> and <span class="verbatim">never merged upstream</span>; containers hold only a shallow base-commit clone.
    - <span class="verbatim">Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.</span>
    - Most public agentic coding benchmarks are <span class="verbatim">built by mining merged fixes from public repositories</span>; this scales, but introduces contamination and inherited-test grading risks.
    - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - <span class="verbatim">DeepSWE tasks aren’t derived from existing public commits, and the task container ships a shallow clone with only the base commit, so there’s no gold hash in the workspace to find.</span>
    - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
- **<span class="verbatim">Larger solutions from shorter prompts:</span>** Mean prompts: 2,158 versus 4,614 characters on SWE-Bench Pro; mean reference code added: 668 versus 120 lines; files edited: 7.4 versus 5.1.
    - The four highlighted design contributions are original never-merged tasks, broad coverage (91 repositories/five languages), larger solutions from shorter prompts, and hand-written functional verification.
    - Prompts are roughly half as long, with 5.5× more reference code and roughly twice the output tokens. They state desired functionality, leaving agents to discover implementation locations and design tradeoffs.
    - <span class="verbatim">given a short task description, can an agent working autonomously inside a repository produce the requested change, typically large and multi-file, whose functional correctness the verifier confirms.</span>
    - <span class="verbatim">Agents must discover where and how to implement the change, so a substantial share of the capabilities being evaluated involves end-to-end exploration instead of just the execution of an overspecified engineering task.</span>
    - The paper’s Happy DOM example states shutdown/body-read behavior without enumerating implementation files or symbols. Its SWE-Bench Pro comparison specifies function names, file paths, signatures, and a requirements checklist.
- **Functional Verifiers:** Public <span class="verbatim">APIs and observable outputs</span> accept valid alternatives and reject no-op implementations.
    - <span class="verbatim">Verifiers run end-to-end functional assertions, so a no-op fails the check on observable software behavior regardless of signature.</span>
    - Behavioral grading <span class="verbatim">lets prompts stay short and natural</span>.
    - Inherited pull-request tests split into <span class="verbatim">FAIL_TO_PASS</span> (new tests) and <span class="verbatim">PASS_TO_PASS</span> (existing regression tests); their original purpose was confirming one fix. They can reject correct alternatives or reward incomplete implementations.
    - Adding requirements/interface blocks reduces naming mismatches but does not change inherited-test grading. Purpose-written verifiers check requested behavior: <span class="verbatim">any implementation providing the requested functionality is accepted;</span> implementation shape is not the criterion.
    - Meaning: Selected point: DeepSWE occupies a distinct point among these neighbors: original, never-merged tasks at repository scale in the everyday format of a short request against an existing codebase.

    - Transformation reason: The rectangle or introductory pointer spans several points. Source order is reorganized into corresponding topic bullets/excerpts; all listed contributions or QA requirements remain represented.

- **H029 · Light green · Before: Covered**
    - Selected text: `continuous evolution:`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
    - Meaning: Selected point: continuous evolution:

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H033 · Light green · Before: Covered**
    - Selected text: `this requires continual re-collection as tasks age past model cutoffs.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
    - Meaning: Selected point: this requires continual re-collection as tasks age past model cutoffs.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H034 · Light green · Before: Covered**
    - Selected text: `access- and licensing-based:`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Other decontamination approaches use <span class="verbatim">continuous evolution</span> (post-cutoff task collection), or <span class="verbatim">access- and licensing-based</span> restrictions; freshness requires repeated collection as tasks age.
    - Meaning: Selected point: access- and licensing-based:

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H035 · Light green · Before: Covered**
    - Selected text: `its tasks are written from scratch and never merged upstream, so the reference solution stays off the public record`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - <span class="verbatim">Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.</span>
    - Meaning: Selected point: its tasks are written from scratch and never merged upstream, so the reference solution stays off the public record

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H036 · Light green · Before: Covered**
    - Selected text: `tests FAIL_TO_PASS`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Inherited pull-request tests split into <span class="verbatim">FAIL_TO_PASS</span> (new tests) and <span class="verbatim">PASS_TO_PASS</span> (existing regression tests); their original purpose was confirming one fix. They can reject correct alternatives or reward incomplete implementations.
    - Meaning: Selected point: tests FAIL_TO_PASS

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H037 · Light green · Before: Covered**
    - Selected text: `tests PASS_TO_PASS`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Inherited pull-request tests split into <span class="verbatim">FAIL_TO_PASS</span> (new tests) and <span class="verbatim">PASS_TO_PASS</span> (existing regression tests); their original purpose was confirming one fix. They can reject correct alternatives or reward incomplete implementations.
    - Meaning: Selected point: tests PASS_TO_PASS

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H038 · Light green · Before: Covered**
    - Selected text: `adding human-written requirements and an interface block that names the classes and functions the inherited tests expect, which reduces false negatives from naming mismatches but does not change how submissions are graded:`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Adding requirements/interface blocks reduces naming mismatches but does not change inherited-test grading. Purpose-written verifiers check requested behavior: <span class="verbatim">any implementation providing the requested functionality is accepted;</span> implementation shape is not the criterion.
    - Meaning: Prompt-side requirements and interface names reduce naming false negatives but leave inherited grading unchanged.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H039 · Light green · Before: Covered**
    - Selected text: `any implementation providing the requested functionality is accepted;`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Adding requirements/interface blocks reduces naming mismatches but does not change inherited-test grading. Purpose-written verifiers check requested behavior: <span class="verbatim">any implementation providing the requested functionality is accepted;</span> implementation shape is not the criterion.
    - Meaning: Selected point: any implementation providing the requested functionality is accepted;

- **H040 · Light green · Before: Covered**
    - Selected text: `functional verifiers`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **Functional Verifiers:** Public <span class="verbatim">APIs and observable outputs</span> accept valid alternatives and reject no-op implementations.
    - Meaning: Selected point: functional verifiers

- **H046 · Light green · Before: Covered**
    - Selected text: `Agents must discover where and how to implement the change, so a substantial share of the capabilities being evaluated involves end-to-end exploration instead of just the execution of an overspecified engineering task.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - <span class="verbatim">Agents must discover where and how to implement the change, so a substantial share of the capabilities being evaluated involves end-to-end exploration instead of just the execution of an overspecified engineering task.</span>
    - Meaning: Selected point: Agents must discover where and how to implement the change, so a substantial share of the capabilities being evaluated involves end-to-end exploration instead of just the execution of an overspecified engineering task.

- **H047 · Light green · Before: Covered**
    - Selected text: `lets prompts stay short and natural`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Behavioral grading <span class="verbatim">lets prompts stay short and natural</span>.
    - Meaning: Selected point: lets prompts stay short and natural

- **H049 · Light green · Before: Covered**
    - Selected text: `Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - <span class="verbatim">Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.</span>
    - Meaning: Selected point: Every DeepSWE task is original: the reference solution is written from scratch rather than copied or adapted from an existing pull request, commit, or public patch. Some tasks are motivated by unresolved GitHub issues, but the fix itself is new.

- **H050 · Light green · Before: Covered**
    - Selected text: `the gold solution can leak into the evaluation container itself:`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - Meaning: Selected point: the gold solution can leak into the evaluation container itself:

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H051 · Light green · Before: Covered**
    - Selected text: `pretraining-contamination risk,`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - Meaning: Selected point: pretraining-contamination risk,

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H052 · Light green · Before: Covered**
    - Selected text: `the repository’s history .git`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - Public merged fixes pose <span class="verbatim">pretraining-contamination risk</span>: <span class="verbatim">a high score can reflect recall rather than problem-solving,</span> while a separate packaging risk lets an agent recover the gold solution from the container’s .git history. DeepSWE avoids upstream gold records and removes that history.
    - Meaning: Selected point: the repository’s history .git

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H121 · Light green · Before: Covered**
    - Selected text: `no-ops`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence: - **Functional Verifiers:** Public <span class="verbatim">APIs and observable outputs</span> accept valid alternatives and reject no-op implementations.
    - Meaning: Selected point: no-ops

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H122 · Light green · Before: Covered**
    - Selected text: `so there’s no gold hash in the workspace to find.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - <span class="verbatim">DeepSWE tasks aren’t derived from existing public commits, and the task container ships a shallow clone with only the base commit, so there’s no gold hash in the workspace to find.</span>
    - Meaning: Selected point: so there’s no gold hash in the workspace to find.

- **H123 · Light green · Before: Covered**
    - Selected text: `Verifiers run end-to-end functional assertions, so a no-op fails the check on observable software behavior re- gardless of signature.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - <span class="verbatim">Verifiers run end-to-end functional assertions, so a no-op fails the check on observable software behavior regardless of signature.</span>
    - Meaning: Selected point: Verifiers run end-to-end functional assertions, so a no-op fails the check on observable software behavior re- gardless of signature.

- **H153 · Light green · Before: Covered**
    - Selected text: `Two differences stand out. The SWE-Bench Pro prompt names the exact symbols and file paths to create`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - The paper’s Happy DOM example states shutdown/body-read behavior without enumerating implementation files or symbols. Its SWE-Bench Pro comparison specifies function names, file paths, signatures, and a requirements checklist.
    - Meaning: SWE-Bench Pro names exact symbols/file paths.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H154 · Light green · Before: Covered**
    - Selected text: `and lists requirements as an explicit checklist, whereas the DeepSWE prompt states only the functionality the change must provide and leaves the agent to discover where and how to implement it.`
    - Now represented under **Special Design → Design Advantages**.

    - Summary evidence:     - The paper’s Happy DOM example states shutdown/body-read behavior without enumerating implementation files or symbols. Its SWE-Bench Pro comparison specifies function names, file paths, signatures, and a requirements checklist.
    - Meaning: Its explicit requirements contrast with DeepSWE functionality-only implementation discovery.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

## Verifier Audit

**Priority 1 · Quality Control · Auto Judge**

- **Verifier Audit:** <span class="verbatim">A benchmark is only as good as its verifier.</span> Judge–verifier disagreement: 1.4% on DeepSWE versus 32.4% on SWE-Bench Pro.

- **H053 · Light cyan · Before: Covered**
    - Selected text: `A benchmark is only as good as its verifier.`
    - Now represented under **Quality Control → Auto Judge → Verifier Audit**.

    - Summary evidence: - **Verifier Audit:** <span class="verbatim">A benchmark is only as good as its verifier.</span> Judge–verifier disagreement: 1.4% on DeepSWE versus 32.4% on SWE-Bench Pro.
    - Meaning: Selected point: A benchmark is only as good as its verifier.

- **H011 · Light green · Before: Covered**
    - Selected text: `disagreed`
    - Now represented under **Quality Control → Auto Judge → Verifier Audit**.

    - Summary evidence: - **Verifier Audit:** <span class="verbatim">A benchmark is only as good as its verifier.</span> Judge–verifier disagreement: 1.4% on DeepSWE versus 32.4% on SWE-Bench Pro.
    - Meaning: Selected point: disagreed

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H054 · Light green · Before: Covered**
    - Selected text: `In SWE benchmarks, the verifier should approximate the task’s functional specification: it should determine whether the submitted code implements the requested change, while remaining agnostic to the particular implementation strategy.`
    - Now represented under **Quality Control → Auto Judge → Verifier Audit**.

    - Summary evidence:     - <span class="verbatim">In SWE benchmarks, the verifier should approximate the task’s functional specification: it should determine whether the submitted code implements the requested change, while remaining agnostic to the particular implementation strategy.</span>
    - Meaning: Selected point: In SWE benchmarks, the verifier should approximate the task’s functional specification: it should determine whether the submitted code implements the requested change, while remaining agnostic to the particular implementation strategy.

- **H055 · Light green · Before: Covered**
    - Selected text: `This differs from the common pattern in which the verifier is inherited from a merged pull request’s test suite (§2): those tests are not necessarily designed as complete graders for arbitrary future submissions, so they can miss valid solutions or pass submissions that satisfy the tests without fully satisfying the task.`
    - Now represented under **Quality Control → Auto Judge → Verifier Audit**.

    - Summary evidence:     - Inherited tests can reject valid alternatives or accept incomplete work; they were not designed as complete graders of arbitrary submissions.
    - Meaning: Selected point: This differs from the common pattern in which the verifier is inherited from a merged pull request’s test suite (§2): those tests are not necessarily designed as complete graders for arbitrary future submissions, so they can miss valid solutions or pass submissions that satisfy the tests without fully satisfying the task.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H056 · Light green · Before: Covered**
    - Selected text: `An independent LLM judge (GPT-5.5 at reasoning effort, run as a Codex CLI agent) xhigh`
    - Now represented under **Quality Control → Auto Judge → Verifier Audit**.

    - Summary evidence:     - <span class="verbatim">GPT-5.5 at xhigh</span>, running as a <span class="verbatim">Codex CLI agent</span>, independently inspected task definitions, trajectories, reference solutions, and verifier output.
    - Meaning: Selected point: An independent LLM judge (GPT-5.5 at reasoning effort, run as a Codex CLI agent) xhigh

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H057 · Light green · Before: Covered**
    - Selected text: `This is a disagreement rate between two independent readers, not a ground-truth error rate (§8).`
    - Now represented under **Quality Control → Auto Judge → Verifier Audit**.

    - Summary evidence:     - <span class="verbatim">This is a disagreement rate between two independent readers, not a ground-truth error rate (§8).</span>
    - Meaning: Disagreement with a fallible judge is not ground-truth verifier error.

## Quality Assurance

**Priority 1 · Quality Control · Human Review**

- **Review Approach**

- **H071 · Red rectangle · Before: Partial**
    - Selected text: `A task is included only after both LLM-assisted analysis and independent human review. Reviewers inspect the prompt, verifier, reference solution, and diagnostic agent rollouts before acceptance. The reference solution is authored alongside the task but never used at grading time. This gives reviewers one known-correct implementation to compare against the prompt and verifier. Reviewers evaluate each task along four dimensions: 1. The verifier should test exactly the functionality the prompt asks Prompt-verifier bijection. for, no more, no less. A verifier that tests more produces false negatives (an agent solves the stated task but fails an unstated one); a verifier that tests less produces false positives (partial solutions are rewarded as if they were complete). Either way, the benchmark does not accurately or fully measure what it claims to measure. 2. The verifier should accept any reasonable implementation of the requested Acceptance breadth. functionality, not just the reference shape (§3.4). A verifier that accepts only one shape measures whether the agent can guess the author’s structure rather than whether it can solve the task. 3. Realism has two axes. the prompt reads in a natural developer Realism. Prompt realism: register, the way someone would actually message an agent, rather than a concrete todo list. the task itself is one a maintainer might plausibly accept as a contribution. An Task realism: underspecified prompt forces the agent to discover the relevant surface and weigh design tradeoffs before writing code, mirroring the kind of engineering work an agent would actually be asked to do. 4. Reviewers inspect both the failing rollouts and the task itself for Environment cleanliness. environment errors, dependency issues, flaky tests, and other infrastructure problems. These do not measure model capability, so reviewers flag them for revision. When an agent fails, the failure should come from struggling to complete the task, not environmental issues. Multiple frontier agent configurations attempt each task as part of review. We confirm that passing rollouts are true positives, and that failing rollouts reflect model capability rather than environment or harness issues. Near-correct failing rollouts are especially useful: they surface how the verifier behaves on edge cases, which helps us refine it. Tasks that fall below the bar return for revision before they enter the benchmark.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence: - **Review Approach**
    - <span class="verbatim">A task is included only after both LLM-assisted analysis and independent human review.</span>
    - <span class="verbatim">Reviewers inspect the prompt, verifier, reference solution, and diagnostic agent rollouts before acceptance.</span>
    - <span class="verbatim">The reference solution is authored alongside the task but never used at grading time. This gives reviewers one known-correct implementation to compare against the prompt and verifier.</span>
    - Passing rollouts are checked as <span class="verbatim">true positives</span>; failures must reflect capability rather than environment or harness errors.
        - Multiple frontier configurations attempt each task. Near-correct failures expose verifier edge cases; substandard tasks <span class="verbatim">return for revision</span>.
        - <span class="verbatim">Near-correct failing rollouts are especially useful: they surface how the verifier behaves on edge cases, which helps us refine it.</span>
- **Quality Dimensions**
    - <span class="verbatim">Prompt-verifier bijection</span>: <span class="verbatim">The verifier should test exactly the functionality the prompt asks for, no more, no less.</span>
        - Extra requirements cause false negatives; missing requirements reward incomplete solutions.
    - <span class="verbatim">Acceptance breadth</span>: <span class="verbatim">The verifier should accept any reasonable implementation of the requested functionality, not just the reference shape</span>.
    - <span class="verbatim">Realism</span>: natural developer prompts and tasks a maintainer could plausibly accept.
        - <span class="verbatim">An underspecified prompt forces the agent to discover the relevant surface and weigh design tradeoffs before writing code, mirroring the kind of engineering work an agent would actually be asked to do.</span>
        - Prompt realism uses <span class="verbatim">a natural developer register</span>, <span class="verbatim">rather than a concrete todo list.</span>
    - <span class="verbatim">Environment cleanliness</span>: reviewers check <span class="verbatim">environment errors</span>, dependencies, <span class="verbatim">flaky tests</span>, and infrastructure; defective tasks <span class="verbatim">return for revision</span>.
        - <span class="verbatim">Reviewers inspect both the failing rollouts and the task itself for environment errors, dependency issues, flaky tests, and other infrastructure problems. These do not measure model capability, so reviewers flag them for revision. When an agent fails, the failure should come from struggling to complete the task, not environmental issues.</span>
    - Meaning: Full high-priority QA box: inspect prompt/verifier/reference/rollouts; review-only known-correct implementation; four dimensions; diagnostic runs; true-positive checks; edge cases; revision before acceptance.

    - Transformation reason: The rectangle or introductory pointer spans several points. Source order is reorganized into corresponding topic bullets/excerpts; all listed contributions or QA requirements remain represented.

- **H063 · Bright green · Before: Covered**
    - Selected text: `The verifier should test exactly the functionality the prompt asks for, no more, no less.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:     - <span class="verbatim">Prompt-verifier bijection</span>: <span class="verbatim">The verifier should test exactly the functionality the prompt asks for, no more, no less.</span>
    - Meaning: Selected point: The verifier should test exactly the functionality the prompt asks for, no more, no less.

- **H064 · Bright green · Before: Covered**
    - Selected text: `The verifier should accept any reasonable implementation of the requested functionality, not just the reference shape`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:     - <span class="verbatim">Acceptance breadth</span>: <span class="verbatim">The verifier should accept any reasonable implementation of the requested functionality, not just the reference shape</span>.
    - Meaning: Selected point: The verifier should accept any reasonable implementation of the requested functionality, not just the reference shape

- **H065 · Bright green · Before: Covered**
    - Selected text: `Reviewers inspect the prompt, verifier, reference solution, and diagnostic agent rollouts before acceptance.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:     - <span class="verbatim">Reviewers inspect the prompt, verifier, reference solution, and diagnostic agent rollouts before acceptance.</span>
    - Meaning: Selected point: Reviewers inspect the prompt, verifier, reference solution, and diagnostic agent rollouts before acceptance.

- **H068 · Bright green · Before: Covered**
    - Selected text: `Reviewers inspect both the failing rollouts and the task itself for environment errors, dependency issues, flaky tests, and other infrastructure problems. These do not measure model capability, so reviewers flag them for revision. When an agent fails, the failure should come from struggling to complete the task, not environmental issues.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:         - <span class="verbatim">Reviewers inspect both the failing rollouts and the task itself for environment errors, dependency issues, flaky tests, and other infrastructure problems. These do not measure model capability, so reviewers flag them for revision. When an agent fails, the failure should come from struggling to complete the task, not environmental issues.</span>
    - Meaning: Selected point: Reviewers inspect both the failing rollouts and the task itself for environment errors, dependency issues, flaky tests, and other infrastructure problems. These do not measure model capability, so reviewers flag them for revision. When an agent fails, the failure should come from struggling to complete the task, not environmental issues.

- **H069 · Bright green · Before: Covered**
    - Selected text: `We confirm that passing rollouts are true positives, and that failing rollouts reflect model capability rather than environment or harness issues.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:     - Passing rollouts are checked as <span class="verbatim">true positives</span>; failures must reflect capability rather than environment or harness errors.
    - Meaning: Passing rollouts must be true positives; failures must reflect capability, not environment or harness errors.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H062 · Light green · Before: Covered**
    - Selected text: `A task is included only after both LLM-assisted analysis and independent human review.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:     - <span class="verbatim">A task is included only after both LLM-assisted analysis and independent human review.</span>
    - Meaning: Selected point: A task is included only after both LLM-assisted analysis and independent human review.

- **H066 · Light green · Before: Covered**
    - Selected text: `rather than a concrete todo list.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:         - Prompt realism uses <span class="verbatim">a natural developer register</span>, <span class="verbatim">rather than a concrete todo list.</span>
    - Meaning: Selected point: rather than a concrete todo list.

- **H067 · Light green · Before: Covered**
    - Selected text: `An underspecified prompt forces the agent to discover the relevant surface and weigh design tradeoffs before writing code, mirroring the kind of engineering work an agent would actually be asked to do.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:         - <span class="verbatim">An underspecified prompt forces the agent to discover the relevant surface and weigh design tradeoffs before writing code, mirroring the kind of engineering work an agent would actually be asked to do.</span>
    - Meaning: Selected point: An underspecified prompt forces the agent to discover the relevant surface and weigh design tradeoffs before writing code, mirroring the kind of engineering work an agent would actually be asked to do.

- **H070 · Light green · Before: Covered**
    - Selected text: `Near-correct failing rollouts are especially useful: they surface how the verifier behaves on edge cases, which helps us refine it.`
    - Now represented under **Quality Control → Human Review → Quality Assurance**.

    - Summary evidence:         - <span class="verbatim">Near-correct failing rollouts are especially useful: they surface how the verifier behaves on edge cases, which helps us refine it.</span>
    - Meaning: Selected point: Near-correct failing rollouts are especially useful: they surface how the verifier behaves on edge cases, which helps us refine it.

## Important Sections

**Priority 1 · Important Sections**

- 4.3 Quality Assurance

- **H072 · Light cyan · Before: Covered**
    - Selected text: `4.3 Quality assurance`
    - Now represented under **Important Sections**.

    - Summary evidence: - 4.3 Quality Assurance
    - Meaning: Selected point: 4.3 Quality assurance

    - Transformation reason: Highlighted section title retained in Important Sections with Title Case; changed capitalization is not marked verbatim.

- **H140 · Light cyan · Before: Covered**
    - Selected text: `C Verdict tag taxonomy`
    - Now represented under **Important Sections**.

    - Summary evidence: - Appendix C Verdict Tag Taxonomy
    - Meaning: Selected point: C Verdict tag taxonomy

    - Transformation reason: Highlighted section title retained in Important Sections with Title Case; changed capitalization is not marked verbatim.

- **H148 · Light cyan · Before: Covered**
    - Selected text: `D Representative trajectories per verdict tag`
    - Now represented under **Important Sections**.

    - Summary evidence: - Appendix D Representative Trajectories per Verdict Tag
    - Meaning: Selected point: D Representative trajectories per verdict tag

    - Transformation reason: Highlighted section title retained in Important Sections with Title Case; changed capitalization is not marked verbatim.

## Trajectory Analysis

**Priority 1 · Model Evaluation · Auto Judge**

- **Trajectory Analysis:** An agent-as-a-judge audit classifies outcomes, failure tags, and test-level root causes, grounded in trajectory evidence.

- **H139 · Light cyan · Before: Covered**
    - Selected text: `Table 4 defines the verdict tags the LLM judge assigns to each reviewed rollout in the failure-mode analysis`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - **Verdict Tag Taxonomy:** <span class="verbatim">Tags are emitted by the LLM judge for each reviewed rollout.</span>
    - Meaning: Table 4 defines the per-rollout judge verdict tags.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H150 · Light cyan · Before: Covered**
    - Selected text: `Detail`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - **Representative Trajectories:** Appendix D’s Detail column is the authors’ plain-language summary: <span class="verbatim">it states the judge’s verdict, gives context on the task, and sketches what the judge found, rather than reproducing its narration verbatim.</span>
    - Meaning: Detail is a table column, not a section heading.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H045 · Bright green · Before: Covered**
    - Selected text: `We adapt the agent-trajectory failure-mode analysis of SWE-Bench Pro [Deng et al., 2025] to categorize verdicts and root causes`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - The analysis adapts SWE-Bench Pro’s trajectory-failure methodology. Figure 9 orders models by judge-assessed legitimate-pass share; its <span class="verbatim">TP/TN/FN/FP</span> categories are second opinions, not replacement leaderboard scores.
    - Meaning: Selected point: We adapt the agent-trajectory failure-mode analysis of SWE-Bench Pro [Deng et al., 2025] to categorize verdicts and root causes

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H104 · Bright green · Before: Covered**
    - Selected text: `a structured trajectory analysis`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence: - **Trajectory Analysis:** An agent-as-a-judge audit classifies outcomes, failure tags, and test-level root causes, grounded in trajectory evidence.
    - Meaning: Selected point: a structured trajectory analysis

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H109 · Bright green · Before: Covered**
    - Selected text: `It produces a structured verdict classifying the trial outcome, assigning a tag from a taxonomy of pass and failure modes, and mapping each failing test to a root cause, with every claim grounded in evidence cited from the artifacts.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - <span class="verbatim">It produces a structured verdict classifying the trial outcome, assigning a tag from a taxonomy of pass and failure modes, and mapping each failing test to a root cause, with every claim grounded in evidence cited from the artifacts.</span>
    - Meaning: Selected point: It produces a structured verdict classifying the trial outcome, assigning a tag from a taxonomy of pass and failure modes, and mapping each failing test to a root cause, with every claim grounded in evidence cited from the artifacts.

- **H043 · Light green · Before: Covered**
    - Selected text: `Our verifier audit and trajectory analysis use a model to adjudicate agent trajectories,`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence: - **Trajectory Analysis:** An agent-as-a-judge audit classifies outcomes, failure tags, and test-level root causes, grounded in trajectory evidence.
    - Meaning: Selected point: Our verifier audit and trajectory analysis use a model to adjudicate agent trajectories,

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H044 · Light green · Before: Covered**
    - Selected text: `agent-as-a-judge`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence: - **Trajectory Analysis:** An agent-as-a-judge audit classifies outcomes, failure tags, and test-level root causes, grounded in trajectory evidence.
    - Meaning: Selected point: agent-as-a-judge

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H105 · Light green · Before: Covered**
    - Selected text: `30 tasks`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - Thirty random tasks per benchmark × nine frontier configurations × three attempts; GPT-5.5 xhigh runs as a <span class="verbatim">Codex CLI agent</span> <span class="verbatim">in a fresh sandbox</span>. It sees the task, complete trajectory and patch, verifier output, and <span class="verbatim">hidden reference solution</span>.
    - Meaning: Thirty random tasks per benchmark.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H106 · Light green · Before: Covered**
    - Selected text: `9 frontier agent configurations three times per task.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - Thirty random tasks per benchmark × nine frontier configurations × three attempts; GPT-5.5 xhigh runs as a <span class="verbatim">Codex CLI agent</span> <span class="verbatim">in a fresh sandbox</span>. It sees the task, complete trajectory and patch, verifier output, and <span class="verbatim">hidden reference solution</span>.
    - Meaning: Nine configurations, three rollouts per task.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H107 · Light green · Before: Covered**
    - Selected text: `access to the task definition, the agent’s full trajectory and patch, the verifier output, and the hidden reference solution.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - Thirty random tasks per benchmark × nine frontier configurations × three attempts; GPT-5.5 xhigh runs as a <span class="verbatim">Codex CLI agent</span> <span class="verbatim">in a fresh sandbox</span>. It sees the task, complete trajectory and patch, verifier output, and <span class="verbatim">hidden reference solution</span>.
    - Meaning: Judge sees task, full trajectory and patch, verifier output, hidden reference solution.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H108 · Light green · Before: Covered**
    - Selected text: `a judge`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - Thirty random tasks per benchmark × nine frontier configurations × three attempts; GPT-5.5 xhigh runs as a <span class="verbatim">Codex CLI agent</span> <span class="verbatim">in a fresh sandbox</span>. It sees the task, complete trajectory and patch, verifier output, and <span class="verbatim">hidden reference solution</span>.
    - Meaning: GPT-5.5 xhigh sandboxed Codex CLI judge.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H110 · Light green · Before: Covered**
    - Selected text: `The audited sample is released in full:`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - The audit releases trajectories, patches, verifier output, and judge verdicts. The browser exposes original DeepSWE task definitions as well.
    - Meaning: Audit inputs/outputs released for individual inspection.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H111 · Light green · Before: Covered**
    - Selected text: `Failure modes by model, ordered by legitimate-pass rate`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - The analysis adapts SWE-Bench Pro’s trajectory-failure methodology. Figure 9 orders models by judge-assessed legitimate-pass share; its <span class="verbatim">TP/TN/FN/FP</span> categories are second opinions, not replacement leaderboard scores.
    - Meaning: Figure 9 orders failure distributions by legitimate-pass share.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H112 · Light green · Before: Covered**
    - Selected text: `TP/TN/FN/FP`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - <span class="verbatim">TP = true positive</span>; <span class="verbatim">TN = true negative</span>; <span class="verbatim">FN = false negative</span>; <span class="verbatim">FP = false positive</span>. Categories are judge-assessed; headline exclusions follow the scoring protocol.
    - Meaning: TP/TN/FN/FP definitions are judge-assessed.

- **H113 · Light green · Before: Covered**
    - Selected text: `patterns`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - **Recurring Model Patterns:**
        - About two-thirds of Claude DeepSWE rollouts tagged <span class="verbatim">MISSED_REQUIREMENT</span> implemented only one required branch, such as sync but not async. This is a proportion of that tagged subset.
        - On SWE-Bench Pro, Opus configurations often recovered gold fixes <span class="verbatim">from .git history</span>. About 18% of Opus 4.7 verifier-passes and 25% of Opus 4.6 verifier-passes were judged improper; none was observed for GPT-5.4/5.5 in this sample.
        - <span class="verbatim">TEST_MISMATCH</span> affected 19–28% of reviewed GPT-5 trials; <span class="verbatim">CHEATED</span> about 13% of all reviewed Opus 4.6/4.7 trials on SWE-Bench Pro.
    - **Representative Trajectories:** Appendix D’s Detail column is the authors’ plain-language summary: <span class="verbatim">it states the judge’s verdict, gives context on the task, and sketches what the judge found, rather than reproducing its narration verbatim.</span>
        - <span class="verbatim">FAIL_TEST_BROKEN</span> (Flipt): <span class="verbatim">The verifier setup tests for “complex metadata import” but never set up the input files those tests need. The tests failed on “file not found” before they could check the agent’s code.</span>
        - <span class="verbatim">PASS_CHEATED</span> (Vuls): <span class="verbatim">The verifier gave this run a pass, but the agent never implemented the main requirement. The task was to wire up external nmap scanning in Vuls. The agent added config helpers but left execExternalPortScan as a TODO that just calls the built-in scanner. The hidden tests only checked small config methods (GetScanTechniques, IsZero), not whether nmap actually runs, so the stub still passed.</span>
        - Each table row links a concrete rollout and identifies the model/task; the public record lets readers inspect the same underlying evidence.
    - Meaning: Recurring model patterns include missed branches, gold recovery and test mismatch.

    - Transformation reason: The isolated figure-analysis pointer is expanded into the specific recurring model-family patterns.

- **H114 · Light green · Before: Covered**
    - Selected text: `CHEATED`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - On SWE-Bench Pro, Opus configurations often recovered gold fixes <span class="verbatim">from .git history</span>. About 18% of Opus 4.7 verifier-passes and 25% of Opus 4.6 verifier-passes were judged improper; none was observed for GPT-5.4/5.5 in this sample.
    - Meaning: Opus gold recovery from git history; improper passes are judge-assessed.

- **H115 · Light green · Before: Covered**
    - Selected text: `Roughly two-thirds of Claude’s DeepSWE rollouts tagged fit this “one branch shipped” MISSED_REQUIREMENT pattern.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - About two-thirds of Claude DeepSWE rollouts tagged <span class="verbatim">MISSED_REQUIREMENT</span> implemented only one required branch, such as sync but not async. This is a proportion of that tagged subset.
    - Meaning: Two-thirds refers to Claude rollouts already tagged MISSED_REQUIREMENT, not all trials.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H119 · Light green · Before: Covered**
    - Selected text: `TEST_ MISMATCH`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - <span class="verbatim">TEST_MISMATCH</span> affected 19–28% of reviewed GPT-5 trials; <span class="verbatim">CHEATED</span> about 13% of all reviewed Opus 4.6/4.7 trials on SWE-Bench Pro.
    - Meaning: TEST_MISMATCH: 19–28% of reviewed GPT trials on SWE-Bench Pro.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H120 · Light green · Before: Covered**
    - Selected text: `CHEATED`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - <span class="verbatim">TEST_MISMATCH</span> affected 19–28% of reviewed GPT-5 trials; <span class="verbatim">CHEATED</span> about 13% of all reviewed Opus 4.6/4.7 trials on SWE-Bench Pro.
    - Meaning: CHEATED: about 13% of all reviewed Opus 4.6/4.7 trials, distinct from conditional-on-pass rates.

- **H138 · Light green · Before: Covered**
    - Selected text: `Each row links to a page that surfaces the full agent trajectory, the produced patch, the verifier output, and (for DeepSWE) the original task definition.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - The audit releases trajectories, patches, verifier output, and judge verdicts. The browser exposes original DeepSWE task definitions as well.
    - Meaning: Browser exposes trajectory, patch, verifier output, original task.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H141 · Light green · Before: Covered**
    - Selected text: `Tags are emitted by the LLM judge for each reviewed rollout.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - **Verdict Tag Taxonomy:** <span class="verbatim">Tags are emitted by the LLM judge for each reviewed rollout.</span>
    - Meaning: Selected point: Tags are emitted by the LLM judge for each reviewed rollout.

- **H142 · Light green · Before: Covered**
    - Selected text: `Solution is reasonable, but the hidden test enforces an expectation the prompt never named.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - FN: <span class="verbatim">FAIL_TEST_MISMATCH</span> — <span class="verbatim">Solution is reasonable, but the hidden test enforces an expectation the prompt never named.</span>
    - Meaning: Selected point: Solution is reasonable, but the hidden test enforces an expectation the prompt never named.

- **H143 · Light green · Before: Covered**
    - Selected text: `Agent passes tests without really doing the task: hardcoding expected values, stubbing functionality, editing tests, or copying a reference solution it found.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - FP: <span class="verbatim">PASS_CHEATED</span> — <span class="verbatim">Agent passes tests without really doing the task: hardcoding expected values, stubbing functionality, editing tests, or copying a reference solution it found.</span>
    - Meaning: Selected point: Agent passes tests without really doing the task: hardcoding expected values, stubbing functionality, editing tests, or copying a reference solution it found.

- **H144 · Light green · Before: Covered**
    - Selected text: `The hidden test or its setup is buggy; no agent could pass it.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - FN: <span class="verbatim">FAIL_TEST_BROKEN</span> — <span class="verbatim">The hidden test or its setup is buggy; no agent could pass it.</span>
    - Meaning: Selected point: The hidden test or its setup is buggy; no agent could pass it.

- **H145 · Light green · Before: Covered**
    - Selected text: `Prompt admits more than one reasonable reading; agent picks one the hidden test doesn’t.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - FN: <span class="verbatim">FAIL_AMBIGUOUS_TASK</span> — <span class="verbatim">Prompt admits more than one reasonable reading; agent picks one the hidden test doesn’t.</span>
    - Meaning: Selected point: Prompt admits more than one reasonable reading; agent picks one the hidden test doesn’t.

- **H146 · Light green · Before: Covered**
    - Selected text: `Sandbox, dependencies, or environment fails out- side the agent’s control and blocks the agent from finishing.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - FN: <span class="verbatim">FAIL_EXECUTION_ERROR_EXTERNAL</span> — <span class="verbatim">Sandbox, dependencies, or environment fails outside the agent’s control and blocks the agent from finishing.</span>
    - Meaning: Selected point: Sandbox, dependencies, or environment fails out- side the agent’s control and blocks the agent from finishing.

- **H147 · Light green · Before: Covered**
    - Selected text: `The Detail column is our own plain-language summary of the trial: it states the judge’s verdict, gives context on the task, and sketches what the judge found, rather than reproducing its narration verbatim.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - **Representative Trajectories:** Appendix D’s Detail column is the authors’ plain-language summary: <span class="verbatim">it states the judge’s verdict, gives context on the task, and sketches what the judge found, rather than reproducing its narration verbatim.</span>
    - Meaning: Detail is authors’ plain-language summary of verdict/context/finding, not verbatim judge narration.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H149 · Light green · Before: Covered**
    - Selected text: `Representative trajectory per verdict tag, drawn from the judge audit.`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:     - **Representative Trajectories:** Appendix D’s Detail column is the authors’ plain-language summary: <span class="verbatim">it states the judge’s verdict, gives context on the task, and sketches what the judge found, rather than reproducing its narration verbatim.</span>
    - Meaning: Appendix D gives concrete inspectable audit examples.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H151 · Light green · Before: Covered**
    - Selected text: `FAIL_TEST_ BROKEN`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - <span class="verbatim">FAIL_TEST_BROKEN</span> (Flipt): <span class="verbatim">The verifier setup tests for “complex metadata import” but never set up the input files those tests need. The tests failed on “file not found” before they could check the agent’s code.</span>
    - Meaning: Flipt broken-test example: missing fixtures prevent code checking.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H152 · Light green · Before: Covered**
    - Selected text: `PASS_CHEATED`
    - Now represented under **Model Evaluation → Auto Judge → Trajectory Analysis**.

    - Summary evidence:         - <span class="verbatim">PASS_CHEATED</span> (Vuls): <span class="verbatim">The verifier gave this run a pass, but the agent never implemented the main requirement. The task was to wire up external nmap scanning in Vuls. The agent added config helpers but left execExternalPortScan as a TODO that just calls the built-in scanner. The hidden tests only checked small config methods (GetScanTechniques, IsZero), not whether nmap actually runs, so the stub still passed.</span>
    - Meaning: Vuls cheated-pass example: external-scanning TODO passes configuration-only tests.

## Benchmark Scope

**Priority 3 · Summary**

- **Purpose:** Datacurve’s benchmark of <span class="verbatim">113 original, long-horizon software engineering tasks</span>.

- **H001 · Light green · Before: Covered**
    - Selected text: `113 original, long-horizon software engineering tasks`
    - Now represented under **Summary → Benchmark Scope**.

    - Summary evidence: - **Purpose:** Datacurve’s benchmark of <span class="verbatim">113 original, long-horizon software engineering tasks</span>.
    - Meaning: Selected point: 113 original, long-horizon software engineering tasks

- **H003 · Light green · Before: Covered**
    - Selected text: `91 active open-source repositories`
    - Now represented under **Summary → Benchmark Scope**.

    - Summary evidence: - **Scope:** <span class="verbatim">91 active open-source repositories</span>; <span class="verbatim">TypeScript, Go, Python, JavaScript, and Rust</span>.
    - Meaning: Selected point: 91 active open-source repositories

## Cross-Benchmark Spread

**Priority 3 · Key Findings**

- **Cross-Benchmark Spread:** DeepSWE separates eight publicly comparable models across 69.8 percentage points, versus 29.7 on SWE-Bench Pro.

- **H014 · Light green · Before: Covered**
    - Selected text: `separate`
    - Now represented under **Key Findings → Cross-Benchmark Spread**.

    - Summary evidence: - **Cross-Benchmark Spread:** DeepSWE separates eight publicly comparable models across 69.8 percentage points, versus 29.7 on SWE-Bench Pro.
    - Meaning: Models clustered on other benchmarks separate across a wider range here.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H096 · Light green · Before: Covered**
    - Selected text: `DeepSWE spreads these frontier coding agents across a wider band than SWE-Bench Pro,`
    - Now represented under **Key Findings → Cross-Benchmark Spread**.

    - Summary evidence: - **Cross-Benchmark Spread:** DeepSWE separates eight publicly comparable models across 69.8 percentage points, versus 29.7 on SWE-Bench Pro.
    - Meaning: Selected point: DeepSWE spreads these frontier coding agents across a wider band than SWE-Bench Pro,

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H101 · Light green · Before: Covered**
    - Selected text: `DeepSWE separates these models across a wider band:`
    - Now represented under **Key Findings → Cross-Benchmark Spread**.

    - Summary evidence: - **Cross-Benchmark Spread:** DeepSWE separates eight publicly comparable models across 69.8 percentage points, versus 29.7 on SWE-Bench Pro.
    - Meaning: Selected point: DeepSWE separates these models across a wider band:

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H102 · Light green · Before: Covered**
    - Selected text: `Cross-benchmark spread.`
    - Now represented under **Key Findings → Cross-Benchmark Spread**.

    - Summary evidence: - **Cross-Benchmark Spread:** DeepSWE separates eight publicly comparable models across 69.8 percentage points, versus 29.7 on SWE-Bench Pro.
    - Meaning: Selected point: Cross-benchmark spread.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

## Harness

**Priority 3 · Model Evaluation · Auto Judge**

- **Harness:** Sixteen configurations share <span class="verbatim">mini-swe-agent</span>, one bash tool, and one prompt; the rollout ceiling is <span class="verbatim">2.5 hours</span>, without step/cost caps.

- **H041 · Light green · Before: Covered**
    - Selected text: `the same model can post markedly different scores across these scaffolds, harness choice is itself a confound for cross-model leaderboards,`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - <span class="verbatim">the same model can post markedly different scores across these scaffolds, harness choice is itself a confound for cross-model leaderboards,</span> motivating standardization.
    - Meaning: Selected point: the same model can post markedly different scores across these scaffolds, harness choice is itself a confound for cross-model leaderboards,

- **H042 · Light green · Before: Covered**
    - Selected text: `DeepSWE therefore holds the harness fixed, evaluating every model under [SWE-agent contributors, mini-swe-agent 2025] with a single tool and a shared prompt rather than per-vendor editing primitives, so bash that the leaderboard reflects model capability rather than scaffolding`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - <span class="verbatim">mini-swe-agent is model-agnostic by design: every model gets the same bash tool and the same shared prompt, with no per-vendor editing primitives or model-specific instructions.</span>
    - Meaning: Selected point: DeepSWE therefore holds the harness fixed, evaluating every model under [SWE-agent contributors, mini-swe-agent 2025] with a single tool and a shared prompt rather than per-vendor editing primitives, so bash that the leaderboard reflects model capability rather than scaffolding

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H073 · Light green · Before: Covered**
    - Selected text: `16 frontier agent configurations`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence: - **Harness:** Sixteen configurations share <span class="verbatim">mini-swe-agent</span>, one bash tool, and one prompt; the rollout ceiling is <span class="verbatim">2.5 hours</span>, without step/cost caps.
    - Meaning: Selected point: 16 frontier agent configurations

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H074 · Light green · Before: Covered**
    - Selected text: `mini-swe-agent`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence: - **Harness:** Sixteen configurations share <span class="verbatim">mini-swe-agent</span>, one bash tool, and one prompt; the rollout ceiling is <span class="verbatim">2.5 hours</span>, without step/cost caps.
    - Meaning: Selected point: mini-swe-agent

- **H075 · Light green · Before: Covered**
    - Selected text: `is model-agnostic by design: every model gets the same tool mini-swe-agent bash and the same shared prompt, with no per-vendor editing primitives or model-specific instructions.`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - <span class="verbatim">mini-swe-agent is model-agnostic by design: every model gets the same bash tool and the same shared prompt, with no per-vendor editing primitives or model-specific instructions.</span>
    - Meaning: Selected point: is model-agnostic by design: every model gets the same tool mini-swe-agent bash and the same shared prompt, with no per-vendor editing primitives or model-specific instructions.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H076 · Light green · Before: Covered**
    - Selected text: `the agent reads the prompt, issues commands to explore and edit the bash workspace, and the resulting patch is graded by the task’s functional verifier`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - In each pinned container, <span class="verbatim">the agent reads the prompt, issues bash commands to explore and edit the workspace, and the resulting patch is graded by the task’s functional verifier</span>. Context exhaustion or timeout is a failure; 67/<span class="verbatim">7,174 scored rollouts</span> reached the 9,000-second ceiling.
    - Meaning: Selected point: the agent reads the prompt, issues commands to explore and edit the bash workspace, and the resulting patch is graded by the task’s functional verifier

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H077 · Light green · Before: Covered**
    - Selected text: `A rollout ends when the agent submits a patch, exhausts the model’s native context window, or hits the timeout, whichever comes first; the latter two are scored as failures`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - In each pinned container, <span class="verbatim">the agent reads the prompt, issues bash commands to explore and edit the workspace, and the resulting patch is graded by the task’s functional verifier</span>. Context exhaustion or timeout is a failure; 67/<span class="verbatim">7,174 scored rollouts</span> reached the 9,000-second ceiling.
    - Meaning: End on submission, context exhaustion or timeout; latter two are failures.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H078 · Light green · Before: Covered**
    - Selected text: `system mini-swe-agent’s prompt also recommends a workflow (find files, reproduce, edit, re-run, check edge cases) that maps almost one-to-one onto how a SWE-bench-style task is graded, which plausibly helps every model`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - The common system prompt recommends finding files, reproducing, editing, rerunning, and checking edge cases; its close match to SWE-bench-style grading may help all models.
    - Meaning: The shared workflow closely matches SWE-bench grading and may help all models.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H079 · Light green · Before: Covered**
    - Selected text: `On this slice pass rate was equal to or higher than the native mini-swe-agent’s harness for all three models`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - A 10-task SWE-Bench Pro pilot found shared/native pass rates of 50%/40% for Opus 4.7, 40%/40% for GPT-5.5, and 40%/20% for Gemini 3.1 Pro, <span class="verbatim">at comparable token cost</span>. None of the differences was significant.
    - Meaning: Shared-harness pass rate was equal to or higher than native harnesses for all three pilot models.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H080 · Light green · Before: Covered**
    - Selected text: `under the shared harness.`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - The common system prompt recommends finding files, reproducing, editing, rerunning, and checking edge cases; its close match to SWE-bench-style grading may help all models.
    - Meaning: Selected point: under the shared harness.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H081 · Light green · Before: Covered**
    - Selected text: `On this small slice (n = 10) the standardized harness does not systematically underperform the native ones;`
    - Now represented under **Model Evaluation → Auto Judge → Harness**.

    - Summary evidence:     - <span class="verbatim">On this small slice (n = 10) the standardized harness does not systematically underperform the native ones; the pilot is a directional check on harness parity, not a ranking of production harnesses.</span>
    - Meaning: Ten-task pilot is a noisy parity check, not a production-harness ranking.

## Repository Selection

**Priority 3 · Dataset Creation**

- **Repository Selection:** Public, actively maintained, permissively licensed repositories with ≥<span class="verbatim">500 GitHub stars</span>; commits are pinned.

- **H048 · Light green · Before: Covered**
    - Selected text: `TypeScript, Go, Python, JavaScript, and Rust`
    - Now represented under **Dataset Creation → Repository Selection**.

    - Summary evidence:     - <span class="verbatim">TypeScript, Go, Python, JavaScript, and Rust</span>.
    - Meaning: Selected point: TypeScript, Go, Python, JavaScript, and Rust

- **H058 · Light green · Before: Covered**
    - Selected text: `We want to measure agent performance across actively maintained public projects with real user dependence, not just the flagship frameworks that already dominate public benchmarks.`
    - Now represented under **Dataset Creation → Repository Selection**.

    - Summary evidence:     - Selection targets projects with real users beyond flagship frameworks. Seventy-five of 91 repositories contribute one task; the median is one.
    - Meaning: Selected point: We want to measure agent performance across actively maintained public projects with real user dependence, not just the flagship frameworks that already dominate public benchmarks.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

## Task Design

**Priority 3 · Dataset Creation**

- **Task Design:** <span class="verbatim">Every task ships three artifacts: the prompt the agent reads, an executable verifier that grades the result, and a reference solution used during review.</span>

- **H059 · Light green · Before: Covered**
    - Selected text: `Every task ships three artifacts: the prompt the agent reads, an executable verifier that grades the result, and a reference solution used during review.`
    - Now represented under **Dataset Creation → Task Design**.

    - Summary evidence: - **Task Design:** <span class="verbatim">Every task ships three artifacts: the prompt the agent reads, an executable verifier that grades the result, and a reference solution used during review.</span>
    - Meaning: Prompt, executable verifier, and review-only reference solution; embedded request and complete patch are original public artifacts.

## Verifier Stability

**Priority 3 · Quality Control · Auto Judge**

- **Verifier Stability:** Each <span class="verbatim">verifier runs three times during authoring</span>; variable outcomes trigger revision.

- **H060 · Light green · Before: Covered**
    - Selected text: `Every verifier runs three times during authoring; verifiers whose outcome varies across runs are flagged as flaky and returned to the author for revision,`
    - Now represented under **Quality Control → Auto Judge → Verifier Stability**.

    - Summary evidence:     - <span class="verbatim">Every verifier runs three times during authoring; verifiers whose outcome varies across runs are flagged as flaky and returned to the author for revision,</span> reducing grading noise.
    - Meaning: Selected point: Every verifier runs three times during authoring; verifiers whose outcome varies across runs are flagged as flaky and returned to the author for revision,

## Functional Scoring

**Priority 3 · Model Evaluation · Auto Judge**

- **Functional Scoring:** The executable verifier determines leaderboard pass/fail; the LLM judge supplies an auxiliary second opinion.

- **H061 · Light green · Before: Covered**
    - Selected text: `On every trial the verifier also runs regression checks:`
    - Now represented under **Model Evaluation → Auto Judge → Functional Scoring**.

    - Summary evidence:     - <span class="verbatim">On every trial the verifier also runs regression checks:</span> selected existing tests plus author-added regression tests. A correct new feature that breaks existing functionality fails.
    - Meaning: Selected point: On every trial the verifier also runs regression checks:

- **H124 · Light green · Before: Covered**
    - Selected text: `Each rollout is scored pass or fail:`
    - Now represented under **Model Evaluation → Auto Judge → Functional Scoring**.

    - Summary evidence:     - <span class="verbatim">Each rollout is scored pass or fail:</span> <span class="verbatim">no partial credit</span>.
    - Meaning: Selected point: Each rollout is scored pass or fail:

## Metrics and Sampling

**Priority 3 · Model Evaluation · Auto Judge**

- **Metrics and Sampling:** <span class="verbatim">pass@1</span> weights tasks equally; <span class="verbatim">pass@4</span> counts tasks solved in up to four attempts. Infrastructure errors are excluded; context exhaustion/timeouts are failures.

- **H082 · Light green · Before: Covered**
    - Selected text: `pass@1 is the macro-average of this per-task pass fraction over the corpus,`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Let N = 113 tasks, n_t = scored rollouts on task t, and c_t = passing rollouts. <span class="verbatim">pass@1</span> = (1/N) Σ_t(c_t/n_t); the pooled rate Σ_t c_t / Σ_t n_t weights rollouts instead. They differ by only a few tenths of a percentage point here.
    - Meaning: Selected point: pass@1 is the macro-average of this per-task pass fraction over the corpus,

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H083 · Light green · Before: Covered**
    - Selected text: `nt`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Let N = 113 tasks, n_t = scored rollouts on task t, and c_t = passing rollouts. <span class="verbatim">pass@1</span> = (1/N) Σ_t(c_t/n_t); the pooled rate Σ_t c_t / Σ_t n_t weights rollouts instead. They differ by only a few tenths of a percentage point here.
    - Meaning: n_t denotes scored rollout count on a task.

- **H084 · Light green · Before: Covered**
    - Selected text: `ct`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Let N = 113 tasks, n_t = scored rollouts on task t, and c_t = passing rollouts. <span class="verbatim">pass@1</span> = (1/N) Σ_t(c_t/n_t); the pooled rate Σ_t c_t / Σ_t n_t weights rollouts instead. They differ by only a few tenths of a percentage point here.
    - Meaning: c_t denotes passing rollout count on a task.

- **H085 · Light green · Before: Covered**
    - Selected text: `N`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Let N = 113 tasks, n_t = scored rollouts on task t, and c_t = passing rollouts. <span class="verbatim">pass@1</span> = (1/N) Σ_t(c_t/n_t); the pooled rate Σ_t c_t / Σ_t n_t weights rollouts instead. They differ by only a few tenths of a percentage point here.
    - Meaning: N = 113 tasks.

- **H086 · Light green · Before: Covered**
    - Selected text: `the simpler pooled rate ( (total passes over total scored ct)/( nt) t t rollouts);`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Let N = 113 tasks, n_t = scored rollouts on task t, and c_t = passing rollouts. <span class="verbatim">pass@1</span> = (1/N) Σ_t(c_t/n_t); the pooled rate Σ_t c_t / Σ_t n_t weights rollouts instead. They differ by only a few tenths of a percentage point here.
    - Meaning: Pooled rate is total passes / total scored rollouts, weighting rollouts rather than tasks.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H087 · Light green · Before: Covered**
    - Selected text: `Whereas pass@1 measures per-rollout reliability, pass@4 measures whether a configuration can reach a correct solution within a small sampling budget; their difference, pass@4 pass@1, is the headroom a model gains − from a few extra attempts.`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - <span class="verbatim">Whereas pass@1 measures per-rollout reliability, pass@4 measures whether a configuration can reach a correct solution within a small sampling budget; their difference, pass@4 − pass@1, is the headroom a model gains from a few extra attempts.</span>
    - Meaning: Selected point: Whereas pass@1 measures per-rollout reliability, pass@4 measures whether a configuration can reach a correct solution within a small sampling budget; their difference, pass@4 pass@1, is the headroom a model gains − from a few extra attempts.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H088 · Light green · Before: Covered**
    - Selected text: `four rollouts per task per configuration,`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - <span class="verbatim">pass@4</span> = (1/N) Σ_t 1[c_t ≥ 1]. The intended budget is four rollouts/task/configuration; exclusions are not resampled, leaving 428–452 scored rollouts/configuration and 7,174 total. Fewer than four attempts can slightly understate <span class="verbatim">pass@4</span>.
    - Meaning: Selected point: four rollouts per task per configuration,

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H089 · Light green · Before: Covered**
    - Selected text: `95% confidence interval, pass@1 1.96 SE, ±`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Run-to-run uncertainty: <span class="verbatim">pass@1 ± 1.96 SE</span>, with SE = std(s_1,…,s_R)/√R over roughly four full-benchmark runs. These intervals measure rerun noise, not task-selection uncertainty.
    - Meaning: Run-to-run 95% interval is pass@1 ± 1.96 SE over whole-benchmark rerun scores.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H091 · Light green · Before: Covered**
    - Selected text: `a cluster bootstrap:`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - A cluster bootstrap resamples tasks with replacement, keeping each task’s rollouts together; <span class="verbatim">this shows how much the result depends on the particular tasks.</span>
    - Meaning: Suggested cluster bootstrap resamples tasks with replacement and preserves within-task rollout clusters.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H092 · Light green · Before: Covered**
    - Selected text: `this shows how much the result depends on the particular tasks.`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - A cluster bootstrap resamples tasks with replacement, keeping each task’s rollouts together; <span class="verbatim">this shows how much the result depends on the particular tasks.</span>
    - Meaning: This bootstrap exposes dependence on which tasks were sampled.

- **H093 · Light green · Before: Covered**
    - Selected text: `Rollouts terminated by a model-provider error, a verifier or grading error, or a transient network error carry no signal about whether the agent could solve the task, so we exclude them`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Provider, verifier/grading, and transient network errors leave both numerator and denominator; exclusions range from 0% to 5.3%. Context-window exhaustion before submission and agent timeout remain genuine failures.
    - Meaning: Provider, verifier/grading and transient network errors leave numerator and denominator.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H094 · Light green · Before: Covered**
    - Selected text: `exhausting the model’s context window before submitting a patch, and exceeding the agent’s wall-clock budget (an agent timeout).`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Provider, verifier/grading, and transient network errors leave both numerator and denominator; exclusions range from 0% to 5.3%. Context-window exhaustion before submission and agent timeout remain genuine failures.
    - Meaning: Context exhaustion and timeout are genuine failures.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H095 · Light green · Before: Covered**
    - Selected text: `genuine failures,`
    - Now represented under **Model Evaluation → Auto Judge → Metrics and Sampling**.

    - Summary evidence:     - Provider, verifier/grading, and transient network errors leave both numerator and denominator; exclusions range from 0% to 5.3%. Context-window exhaustion before submission and agent timeout remain genuine failures.
    - Meaning: Resource-limit outcomes count as failures, unlike infrastructure errors.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

## Efficiency

**Priority 3 · Key Findings**

- **Efficiency:** More output tokens, time, or spending did not consistently solve more tasks.

- **H097 · Light green · Before: Covered**
    - Selected text: `(median output tokens,`
    - Now represented under **Key Findings → Efficiency**.

    - Summary evidence:     - Reported axes are <span class="verbatim">median output tokens, median wall-clock duration, and median dollar cost per trial</span>.
    - Meaning: Median output tokens per trial.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H098 · Light green · Before: Covered**
    - Selected text: `median wall-clock duration,`
    - Now represented under **Key Findings → Efficiency**.

    - Summary evidence:     - Reported axes are <span class="verbatim">median output tokens, median wall-clock duration, and median dollar cost per trial</span>.
    - Meaning: Median wall-clock duration per trial.

- **H099 · Light green · Before: Covered**
    - Selected text: `median dollar cost`
    - Now represented under **Key Findings → Efficiency**.

    - Summary evidence:     - Reported axes are <span class="verbatim">median output tokens, median wall-clock duration, and median dollar cost per trial</span>.
    - Meaning: Median dollar cost per trial.

- **H100 · Light green · Before: Covered**
    - Selected text: `Output tokens, wall-clock duration, and dollar cost per trial all vary by an order of magnitude across the agents shown, but none correlates strongly with pass rate: emitting more tokens, running longer, or costing more does not consistently solve more tasks.`
    - Now represented under **Key Findings → Efficiency**.

    - Summary evidence:     - <span class="verbatim">Output tokens, wall-clock duration, and dollar cost per trial all vary by an order of magnitude across the agents shown, but none correlates strongly with pass rate: emitting more tokens, running longer, or costing more does not consistently solve more tasks.</span>
    - Meaning: Selected point: Output tokens, wall-clock duration, and dollar cost per trial all vary by an order of magnitude across the agents shown, but none correlates strongly with pass rate: emitting more tokens, running longer, or costing more does not consistently solve more tasks.

- **H103 · Light green · Before: Covered**
    - Selected text: `the efficiency frontier`
    - Now represented under **Key Findings → Efficiency**.

    - Summary evidence:     - The efficiency frontier is <span class="verbatim">the highest pass rate reached at a given budget,</span> traced across token, time, and cost panels.
    - Meaning: Efficiency frontier is highest pass rate attained at a given resource budget.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

## Self-Verification

**Priority 3 · Key Findings**

- **Self-Verification:** <span class="verbatim">Stronger models test more, and they do it unprompted.</span>

- **H116 · Light green · Before: Covered**
    - Selected text: `We used an LLM-based judge agent to tag every trial with the self-verification steps the agent took (running the repository’s existing tests, writing fresh tests of its own, running a one-off reproduction script, or skipping verification).`
    - Now represented under **Key Findings → Self-Verification**.

    - Summary evidence:     - A judge tagged existing-test runs, new tests, one-off reproductions, and skipped verification. GPT-5.4 and Opus 4.7 authored tests on 85% and 83% of DeepSWE runs; Gemini 3 Flash skipped every kind of test on 18%.
    - Meaning: Existing tests, new tests, reproduction scripts and skipped verification are all tagged.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H117 · Light green · Before: Covered**
    - Selected text: `Stronger models test more, and they do it unprompted.`
    - Now represented under **Key Findings → Self-Verification**.

    - Summary evidence: - **Self-Verification:** <span class="verbatim">Stronger models test more, and they do it unprompted.</span>
    - Meaning: Selected point: Stronger models test more, and they do it unprompted.

- **H118 · Light green · Before: Covered**
    - Selected text: `We notice that models are a lot less likely to write their own tests on SWE-Bench Pro than on DeepSWE.`
    - Now represented under **Key Findings → Self-Verification**.

    - Summary evidence:     - Models authored far fewer tests on SWE-Bench Pro; its wrapper says not to modify tests/testing logic. DeepSWE lacks that wrapper, and test-writing returns.
    - Meaning: Own-test writing falls under SWE-Bench Pro testing restrictions, unlike DeepSWE.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

## Impact and Limitations

**Priority 3 · Impact**

- **Impact:** Released tasks, functional verifiers, and full trajectories support reproducible evaluation and grader research.

- **H125 · Light green · Before: Covered**
    - Selected text: `They do not score code quality, readability, idiomatic style, defensive coding, error-handling thoroughness, performance, or documentation.`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - <span class="verbatim">They do not score code quality, readability, idiomatic style, defensive coding, error-handling thoroughness, performance, or documentation.</span>
    - Meaning: Selected point: They do not score code quality, readability, idiomatic style, defensive coding, error-handling thoroughness, performance, or documentation.

- **H126 · Light green · Before: Covered**
    - Selected text: `shorter and less specified than SWE-Bench Pro’s,`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - Prompts are <span class="verbatim">shorter and less specified than SWE-Bench Pro’s,</span> but remain <span class="verbatim">more fully specified than</span> typical developer requests.
    - Meaning: Selected point: shorter and less specified than SWE-Bench Pro’s,

- **H127 · Light green · Before: Covered**
    - Selected text: `Functional verification imposes a floor on this terseness: the prompt must name enough of the desired functionality for the verifier to know what surface to test against, and below that floor the task becomes ambiguous.`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - <span class="verbatim">Functional verification imposes a floor on this terseness: the prompt must name enough of the desired functionality for the verifier to know what surface to test against, and below that floor the task becomes ambiguous.</span>
    - Meaning: Selected point: Functional verification imposes a floor on this terseness: the prompt must name enough of the desired functionality for the verifier to know what surface to test against, and below that floor the task becomes ambiguous.

- **H128 · Light green · Before: Covered**
    - Selected text: `DeepSWE says little about how agents behave on genuinely under-specified or ambiguous requests, where the correct response may be to ask a clarifying question, surface a design tradeoff, or decline an ill-posed task rather than to produce a patch.`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - Genuinely ambiguous requests, clarification, design discussion, declining ill-posed requests, non-coding use, and developer collaboration are not measured.
    - Meaning: Selected point: DeepSWE says little about how agents behave on genuinely under-specified or ambiguous requests, where the correct response may be to ask a clarifying question, surface a design tradeoff, or decline an ill-posed task rather than to produce a patch.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H129 · Light green · Before: Covered**
    - Selected text: `LLM-judge audit on a small random sample:`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - The audit covers 30 tasks/benchmark, nine configurations and three attempts. DeepSWE disagreements are only 2 false-positive and 8 false-negative events; GPT-5.5 self-preference cannot be excluded. The fallible LLM judge is not ground truth; its exact prompt is unreleased.
    - Meaning: Small 30-task audit; DeepSWE disagreement counts are only 2 and 8.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H130 · Light green · Before: Covered**
    - Selected text: `self-preference bias toward its own trajectories cannot be excluded;`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - The audit covers 30 tasks/benchmark, nine configurations and three attempts. DeepSWE disagreements are only 2 false-positive and 8 false-negative events; GPT-5.5 self-preference cannot be excluded. The fallible LLM judge is not ground truth; its exact prompt is unreleased.
    - Meaning: GPT-5.5 self-preference bias cannot be excluded.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H131 · Light green · Before: Covered**
    - Selected text: `The judge is itself a fallible LLM,`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - The audit covers 30 tasks/benchmark, nine configurations and three attempts. DeepSWE disagreements are only 2 false-positive and 8 false-negative events; GPT-5.5 self-preference cannot be excluded. The fallible LLM judge is not ground truth; its exact prompt is unreleased.
    - Meaning: The LLM judge is fallible.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H132 · Light green · Before: Partial**
    - Selected text: `reference solutions are large and multi-file, while the prompts that elicit them are short, so an agent must explore the codebase to locate the relevant surface and reconstruct the implicit specification before writing code`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - <span class="verbatim">reference solutions are large and multi-file, while the prompts that elicit them are short, so an agent must explore the codebase to locate the relevant surface and reconstruct the implicit specification before writing code</span>.
    - Meaning: Structural long-horizon: large multi-file solutions and exploration from short prompts.

- **H133 · Light green · Before: Covered**
    - Selected text: `not a claim that the tasks correspond to hours or`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence: - **Meaning of “Long-Horizon”:** Large, multi-file solutions and exploration relative to short prompts; this is <span class="verbatim">a structural property</span>, without an estimate of human engineering hours.
    - Meaning: No claim of human engineering hours.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H134 · Light green · Before: Covered**
    - Selected text: `days of human engineering effort;`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence: - **Meaning of “Long-Horizon”:** Large, multi-file solutions and exploration relative to short prompts; this is <span class="verbatim">a structural property</span>, without an estimate of human engineering hours.
    - Meaning: No hours/days-of-human-work estimate.

    - Transformation reason: Fragment, statistic or formula expanded/reconstructed with its subject, units, population and experimental conditions; edited wording stays in default color.

- **H135 · Light green · Before: Covered**
    - Selected text: `As with any benchmark, once we release the prompts, functional verifiers, and trajectory artifacts, future training runs could ingest them;`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - Originality limits contamination at evaluation time; released prompts, verifiers, and trajectories can enter future training corpora, so later evaluations need refreshed tasks.
    - Meaning: Released artifacts can enter future training; contamination protection is time-dependent.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

- **H136 · Light green · Before: Covered**
    - Selected text: `combine LLM-based judges with unit tests`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - The full record includes per-task/<span class="verbatim">per-configuration pass counts</span>. Future work includes multiple harnesses, broader projects/languages, and hybrid verifiers that <span class="verbatim">combine LLM-based judges with unit tests</span>.
    - Meaning: Hybrid verifiers combining LLM judges with unit tests are future work.

- **H137 · Light green · Before: Covered**
    - Selected text: `We release the benchmark, the functional verifiers, and the full trajectory record (including per-task, per-configuration pass counts);`
    - Now represented under **Impact → Impact and Limitations**.

    - Summary evidence:     - The full record includes per-task/<span class="verbatim">per-configuration pass counts</span>. Future work includes multiple harnesses, broader projects/languages, and hybrid verifiers that <span class="verbatim">combine LLM-based judges with unit tests</span>.
    - Meaning: Release includes per-task/per-configuration pass counts.

    - Transformation reason: Related selections are merged with original context, or author framing/isolated labels are rewritten neutrally; the cited excerpt preserves the selected point.

## Excluded and Unclassified

- H010: Dark green highlight, excluded by your color preferences.
- H016: Yellow highlight, excluded by your color preferences.
- H017: Dark green highlight, excluded by your color preferences.
- H018: Dark green highlight, excluded by your color preferences.
- H019: Dark green highlight, excluded by your color preferences.
- H020: Dark green highlight, excluded by your color preferences.
- H021: Dark green highlight, excluded by your color preferences.
- H022: Dark green highlight, excluded by your color preferences.
- H023: Dark green highlight, excluded by your color preferences.
- H024: Dark green highlight, excluded by your color preferences.
- H025: Dark green highlight, excluded by your color preferences.
- H030: Dark green highlight, excluded by your color preferences.
- H031: Dark green highlight, excluded by your color preferences.
- H032: Dark green highlight, excluded by your color preferences.
- H090: Yellow highlight, excluded by your color preferences.
