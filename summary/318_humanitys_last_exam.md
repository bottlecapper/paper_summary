# Humanity’s Last Exam

**Center for AI Safety and Scale AI · Oct 2026 · ~4-minute overview** · [Paper](https://arxiv.org/abs/2501.14249v12)

## Summary

- **Purpose:** HLE measures advanced academic knowledge and reasoning through closed-ended questions, extending measurement beyond saturated benchmarks.

- **Scope:** <span class="verbatim">2,500</span> public questions span <span class="verbatim">over a hundred subjects</span>. Around <span class="verbatim">14%</span> require images; <span class="verbatim">24%</span> are multiple-choice. A private set checks overfitting; its size is not reported.

- **Task Design:** Experts write original questions or non-trivial syntheses with known answers. Candidate questions must defeat frontier models, then pass iterative expert review.

- **Time and Cost:** The prize pool is <span class="verbatim">$500,000 USD</span>. Estimated question-review effort is <span class="verbatim">3-5 minutes</span>; human solving time and highest-scoring-model wall-clock runtime are not reported.

- **Evaluation Method:** An o3-mini judge compares final answers with reference answers, accepting equivalent forms. Scoring is binary, without partial credit; report accuracy and root-mean-square (RMS) error between stated confidence and empirical accuracy.

## Dataset Creation

- **Expert Sourcing:** Nearly <span class="verbatim">1000</span> experts from <span class="verbatim">over 500 institutions across 50 countries</span> contribute; most are professors, researchers, or graduate degree holders.
    - <span class="verbatim">HLE is a global collaborative effort, with questions from nearly 1000 subject expert contributors affiliated with over 500 institutions across 50 countries – comprised mostly of professors, researchers, and graduate degree holders.</span>

- **Incentives:** Accepted questions earn co-authorship; prizes encourage expert participation.
    - The <span class="verbatim">$500,000 USD</span> pool awards <span class="verbatim">$5,000 USD for each of the top 50 questions and $500 USD for each of the next 500 questions, as determined by organizers.</span>

- **Task Design:**

    - **Coverage:** Questions cover mathematics, sciences, humanities, and specialized fields.
        - <span class="verbatim">HUMANITY’S LAST EXAM (HLE) consists of 2,500 challenging questions across over a hundred subjects.</span>
        - The abstract describes <span class="verbatim">2,500 questions across dozens of subjects, including mathematics, humanities, and the natural sciences.</span> Section B.4 introduces its list as <span class="verbatim">the top fifty most popular subjects in HLE</span>: <span class="verbatim">Economies, Ecology, Artificial Intelligence, Musicology, Philosophy, Neuroscience, Law, Art History, Biochemistry, Astronomy, Classics, Chess, Chemical Engineering, Microbiology, Classical Ballet, Materials Science, Poetry, Quantum Mechanics, Aerospace Engineering, Civil Engineering, Mechanical Engineering, Geography, Robotics, Data Science, Molecular Biology, Statistics, Immunology, Education, Logic, Computational Biology, Psychology, English Literature, Machine Learning, Puzzle, Cultural Studies, Marine Biology, Archaeology, and Biophysics.</span>

    - **Answer Formats:** Use short exact-match answers or at least <span class="verbatim">five</span> multiple-choice options; questions usually require <span class="verbatim">graduate-level expertise</span>.
        - HLE is <span class="verbatim">multi-modal, featuring questions that are either text-only or accompanied by an image reference, and includes both multiple-choice and exact-match questions for automated answer verification.</span>
        - <span class="verbatim">Answers are kept short and easily verifiable for exact-match questions to support automatic grading.</span> Both formats are <span class="verbatim">suitable for automated grading.</span>

    - **Submission Contents:** Submit the question, answer specification, detailed solution, subject, and contributor identity.
        - <span class="verbatim">Each question submission includes several required components: the question text itself, answer specifications (either an an exact-match answer, or multiple-choice options with the correct answer marked), detailed rationale explaining the solution, academic subject, and contributor name and institutional affiliation to maintain accountability and accuracy.</span>

- **Example Tasks:**
    - **Example Task:** Figure 2 – Ecology (hummingbird sesamoid).

        The task instruction is: *“Hummingbirds within Apodiformes uniquely have a bilaterally paired oval bone, a sesamoid embedded in the caudolateral portion of the expanded, cruciate aponeurosis of insertion of m. depressor caudae. How many paired tendons are supported by this sesamoid bone? Answer with a number.”*

## Quality Control

### Human Review

- **Review Approach:**

    - First-round refinement: Graduate-qualified experts use standardized rubrics, provide feedback, and iteratively revise questions; each receives <span class="verbatim">1-3 reviews</span>. Scores range from <span class="verbatim">0</span> to <span class="verbatim">5</span>, with an unsure option.
        - Reviewers <span class="verbatim">possess a graduate degree (eg. Master’s, PhD, JD, etc.) in their fields.</span> They <span class="verbatim">select submissions in their domain, grading them against standardized rubrics and offering feedback when applicable.</span>
        - The first round focuses <span class="verbatim">on iteratively refining submissions, with each question receiving between 1-3 reviews.</span> Experts score questions, provide feedback, and help authors improve them, similar to academic peer review. Round-one scores run from <span class="verbatim">0</span> (discard) to <span class="verbatim">5</span> (top-notch), with an unsure option.
    - Second-round approval: Organizers and trained reviewers consider questions and prior feedback, then approve the best submissions. Scores range from <span class="verbatim">0</span> to <span class="verbatim">6</span>.
        - <span class="verbatim">In the second round, good and outstanding questions from the first round are identified and approved by organizers and reviewers to be included in the final HLE dataset.</span> Organizers train reviewers selected for thorough first-round feedback; <span class="verbatim">reviewers are asked to grade both the question and look at feedback from round 1 reviewers.</span> Round-two scores run from <span class="verbatim">0</span> to <span class="verbatim">6</span>.
        - Figure 4 summarizes model-failure filtering, iterative expert refinement, and individual manual approval.
    - Community feedback: A public review and bug bounty identify label and major question-statement errors; organizers verify reports with author input.
        - Following release, public review solicits community corrections. Initial reviewers <span class="verbatim">were not expected to verify the full accuracy of each provided solution rationale if it would take more than five minutes, instead focusing on whether the question aligns with guidelines.</span>

    - Sample-solving audits: Students solve questions fully; organizers, authors, and auditors resolve flagged errors by consensus.
        - Students from top US universities fully solve a sample. Flagged errors are routed among organizers, original question authors, and auditors until consensus. These audits inform dataset refinement. Search-flagged questions are manually checked and removed if easily found online.
    - Expert disagreement: Two samples of <span class="verbatim">200 questions</span> each, with author rebuttals, support revisions. Estimated public-set disagreement is <span class="verbatim">15.4%</span>; a targeted biology/chemistry/health review finds approximately <span class="verbatim">18%</span>.
        - The audits involve <span class="verbatim">expert reviewers from leading research universities in the United States, with a rebuttal phase from the original question authors for any disagreements.</span> The first audit identifies patterns of imprecision; similar questions are revised or removed before a new sample is audited.
        - The highlighted <span class="verbatim">The Need for Multiple Experts:</span> explains why multiple reviewers and author rebuttals matter: specialized evidence, such as an old paper, can resolve a dissent. On the health-focused subset, flagging any single dissent raises disagreement from <span class="verbatim">18% to 25%</span>. Disagreement is not a confirmed error rate.

- **Quality Dimensions:**

    - Validity and Clarity: <span class="verbatim">Questions should be precise, unambiguous, solvable, and non-searchable, ensuring models cannot rely on memorization or simple retrieval methods.</span>
        - For psychology/philosophy, reviewers check whether <span class="verbatim">the rationale contains some reference to a book, paper or standard theories.</span> <span class="verbatim">Make sure questions about law are time-bounded.</span> An example is <span class="verbatim">“as of 2024”</span>. <span class="verbatim">If there is some non-standard jargon for the topic/field, it needs to be explained.</span>
        - Open-ended prompts such as <span class="verbatim">“Give a proof of. . . ”; “Explain why. . . ”; “Provide a theory that explains. . . ”</span> are generally unsuitable. Subjective interpretation and morality/ethics questions are excluded.
        - <span class="verbatim">Question with numerical answers should have results approximated to max 2-3 decimals.</span> <span class="verbatim">Questions that can be converted to text should be</span> converted; clear LaTeX formatting can reveal that a model actually knows the answer. <span class="verbatim">Explanations should include at least some details or reference. If the rationale is unclear or not detailed, ask in the review to expand a bit.</span>

    - Multiple-Choice Interpretation: Judge the most plausible provided option, rather than demand an open-ended perfect solution.
        - Researchers <span class="verbatim">leverage the multiple-choice format with the objective of identifying the most plausible answer among the provided options.</span> Reviewers compare relative merits <span class="verbatim">rather than treating the task as an open-ended search for a perfect solution.</span>

    - Genuine Difficulty: Reject easy questions missed by models and artificial difficulty caused by unavailable calculator/code tools.
        - The second rubric labels a category <span class="verbatim">Easy questions models got wrong</span>. It includes basic/searchable questions and questions that are <span class="verbatim">artificially difficult</span> because of large calculator-dependent computations or running/rendering code. Evaluated models lack those tools, creating an artificial difficulty bar. Research papers, journals, and books are acceptable sources; simple online lookup is the exclusion criterion.

### Auto Judge

- **Difficulty Screening:** Exact-match candidates must stump all screening models; multiple-choice candidates may be solved by at most one. GPT-4o judges screening answers; search-assisted successes trigger manual searchability checks.
    - Section B.1 specifies that <span class="verbatim">exact-match questions must stump all models, while multiple-choice questions must stump all but one model to account for potential lucky guesses.</span> Section 3.2 describes the multiple-choice goal as models averaging below random guessing.
    - Screening uses <span class="verbatim">“Reasoning” and “Final Answer”</span> response formatting and an <span class="verbatim">automated GPT-4O judge</span> against submitted answers. More than <span class="verbatim">70,000 attempts</span> yield approximately <span class="verbatim">13,000 questions</span> for human review.
    - <span class="verbatim">A question is potentially searchable if a model with search tools answered correctly, but answered incorrectly without search.</span> GPT-4o mini/GPT-4o search and Perplexity Sonar supply this signal; human auditors make removal decisions.

## Model Evaluation

### Human Review

- **Role:** Humans review reference questions and answers; no separate human scoring of model responses or judge–human agreement study is reported.

### Auto Judge

- **Answer Judge:** o3-mini checks answer equivalence against the supplied reference.
    - The evaluation prompt requests explanation, final answer, and confidence. Models without system-prompt support receive it as a separate user prompt. The judge is <span class="verbatim">o3-mini-2025-01-31</span> with structured decoding; it extracts <span class="verbatim">extracted_final_answer,</span> reasoning, correctness, and confidence.
    - The judge accounts for <span class="verbatim">equivalent formats (e.g., decimals vs. fractions or estimations).</span> It compares answers rather than independently re-solving the problem. Correctness is yes/no, allowing small numerical error; no final answer extracts as None, and missing confidence defaults to <span class="verbatim">100</span>.
    - The structured-response example in Section C.1.1 uses a half-angle identity to establish equivalence between two trigonometric forms and returns yes.

- **Headline Results:** In the paper’s early-2025 text-only evaluation, o3-mini (high) scores <span class="verbatim">13.4</span>% accuracy, DeepSeek-R1 <span class="verbatim">8.5</span>%, o1 <span class="verbatim">7.8</span>%, and GPT-4o <span class="verbatim">2.3</span>%. [Current leaderboard](https://huggingface.co/datasets/cais/hle#leaderboard).
    - Table 1 accuracy / RMS calibration error (%): GPT-4o <span class="verbatim">2.7</span> / <span class="verbatim">89</span>; Grok 2 <span class="verbatim">3.0</span> / <span class="verbatim">87</span>; Claude 3.5 Sonnet <span class="verbatim">4.1</span> / <span class="verbatim">84</span>; Gemini 1.5 Pro <span class="verbatim">4.6</span> / <span class="verbatim">88</span>; Gemini 2.0 Flash Thinking <span class="verbatim">6.6</span> / <span class="verbatim">82</span>; o1 <span class="verbatim">8.0</span> / <span class="verbatim">83</span>. Text-only DeepSeek-R1 scores <span class="verbatim">8.5</span> / <span class="verbatim">73</span>; text-only o3-mini (high) scores <span class="verbatim">13.4</span> / <span class="verbatim">80</span>. The text-only rows use a different population from full-dataset rows.
    - Table 2 gives the shared text-only population used in the visible comparison; its remaining baselines are Grok 2 <span class="verbatim">3.2</span>%, Claude 3.5 Sonnet <span class="verbatim">4.3</span>%, Gemini 1.5 Pro <span class="verbatim">4.6</span>%, and Gemini 2.0 Flash Thinking <span class="verbatim">6.6</span>%.

- **Confidence Calibration:** <span class="verbatim">Models frequently provide incorrect answers with high confidence on HLE, failing to recognize when questions exceed their capabilities.</span>
    - Models give confidence <span class="verbatim">from 0% to 100%</span>. <span class="verbatim">A well-calibrated model’s stated confidence should match its actual accuracy – for example, achieving 50% accuracy on questions where it claims 50% confidence.</span>

## Key Findings

- **Guessing and Variability:** Small score changes near zero need caution.
    - <span class="verbatim">models can inconsistently guess the right answer or guess worse than random chance for multiple choice questions.</span> Such questions remain rather than being repeatedly filtered; low non-zero accuracy partly reflects inference randomness and the multiple-choice floor.

- **Evaluation Landscape:** HLE combines broad coverage with expert authorship and difficult questions.
    - Related work spans <span class="verbatim">scientific</span> and <span class="verbatim">mathematical reasoning</span>, <span class="verbatim">code generation</span>, and <span class="verbatim">general-purpose human assistance</span>. HLE complements open-ended evaluations. Reasoning models improve accuracy using substantially more completion tokens; token counts measure compute, not wall-clock time.

## Special Design

- **Closed-Ended Frontier:** Known, verifiable answers permit automated grading at unusually advanced knowledge levels.
    - HLE is designed as <span class="verbatim">a multi-modal benchmark at the frontier of human knowledge, designed to be the final closed-ended academic benchmark of its kind with broad subject coverage.</span> <span class="verbatim">Each question has a known solution that is unambiguous and easily verifiable, but cannot be quickly answered</span> via internet retrieval.

- **Research Experience:** Contributor experiments supply knowledge beyond easily indexed sources.
    - <span class="verbatim">HLE is intentionally designed to include questions based on insights from the direct, hands-on experiments of its contributors. This design captures knowledge gained from direct research experiences, which is often difficult to verify through standard literature searches or by external reviewers.</span>

- **Discouraging Lucky Answers:** Adjust question parameters to reduce correct guesses with faulty reasoning.
    - <span class="verbatim">When LLMs provide correct answers with faulty reasoning, authors are encouraged to modify question parameters, such as the number of answer choices, to discourage false positives.</span>

## Impact

- **Implications:** A shared academic benchmark can support capability tracking and research/policy discussion. Iterative expert review and held-out questions help maintain its measurement value.

- **Limitations:** <span class="verbatim">HLE tests structured academic problems rather than open-ended research or creative problem-solving abilities, making it a focused measure of technical knowledge and reasoning.</span>
    - High performance alone does not establish autonomous research or artificial general intelligence. The initial review’s limited solution verification and substantial expert disagreement also constrain interpretation.

- **Continued Refinement:** The paper proposes <span class="verbatim">HLE-ROLLING</span> as a dynamic fork.
    - <span class="verbatim">This version will be regularly updated to address community feedback and integrate new questions.</span>

## Important Sections

- C.7 Human Review Instructions
