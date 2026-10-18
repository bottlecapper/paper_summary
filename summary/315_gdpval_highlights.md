# GDPval Highlight Audit

All 117 included highlights are mapped to the revised summary. Topics are ordered by their highest highlight priority; selections within each topic are ordered by priority, then paper order.

Prior-coverage judgments are a manual semantic review. Annotation accounting is checked programmatically. Raw selections retain PDF extraction artifacts; mathematical selections are explained in context in the summary.

Previous statuses: **Covered**, **Partial**, **Title only**, or **Missing**. New coverage means the highlighted information is represented by a topic lead, source excerpt, definition, or merged equivalent passage—not that every duplicate fragment is repeated verbatim.

## Quality Dimensions

**Priority 1 · Quality Control · Human Review · Quality Dimensions**

Quality Dimensions

- **H080 · Light cyan · Before: Title only**
    - Selected text: `A.4.4 TASK REPRESENTATIVENESS`
    - Now represented under **Quality Control → Human Review → Quality Dimensions**.

- **H021 · Light green · Before: Missing**
    - Selected text: `To assess task quality, we asked occupational experts to rate each task on its difficulty, representativeness, time to complete, and overall quality against real-world standards for their occupation.`
    - Now represented under **Quality Control → Human Review → Quality Dimensions**.

- **H075 · Light green · Before: Missing**
    - Selected text: `Avg time to complete (hrs) 9.49`
    - Now represented under **Quality Control → Human Review → Quality Dimensions**.

- **H076 · Light green · Before: Missing**
    - Selected text: `Avg time to complete (hrs) 8.63`
    - Now represented under **Quality Control → Human Review → Quality Dimensions**.

## Model-in-the-Loop Task Review

**Priority 1 · Quality Control · Auto Judge**

Automated screening flags possible errors or omissions in task submissions.

- **H099 · Light cyan · Before: Covered**
    - Selected text: `Because models can make mistakes, experts were instructed to take model feedback as a suggestion rather than a direction. Experts retained final responsibility for task accuracy and completeness; the model did not autonomously alter tasks.`
    - Now represented under **Quality Control → Auto Judge → Model-in-the-Loop Task Review**.

- **H094 · Bright green · Before: Covered**
    - Selected text: `automatically screen each task submission`
    - Now represented under **Quality Control → Auto Judge → Model-in-the-Loop Task Review**.

- **H095 · Light green · Before: Covered**
    - Selected text: `if there were no deliverable and reference files attached.`
    - Now represented under **Quality Control → Auto Judge → Model-in-the-Loop Task Review**.

- **H096 · Light green · Before: Covered**
    - Selected text: `if the task complexity was too simple`
    - Now represented under **Quality Control → Auto Judge → Model-in-the-Loop Task Review**.

- **H097 · Light green · Before: Covered**
    - Selected text: `ensuring the task is relevant to the selected O*NET occupation,`
    - Now represented under **Quality Control → Auto Judge → Model-in-the-Loop Task Review**.

- **H098 · Light green · Before: Missing**
    - Selected text: `tasks performed primarily on a computer,`
    - Now represented under **Quality Control → Auto Judge → Model-in-the-Loop Task Review**.

## Review Approach

**Priority 1 · Quality Control · Human Review · Review Approach**

<span class="verbatim">Each task received an average of five human reviews (with a minimum of three reviews).</span>

- **H104 · Light cyan · Before: Title only**
    - Selected text: `A.5.2 HUMAN EXPERT REVIEWERS`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H022 · Bright green · Before: Covered**
    - Selected text: `an iterative review pipeline involving both automated model-based screening and multiple stages of human expert review.`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H023 · Bright green · Before: Covered**
    - Selected text: `Each task received an average of five human reviews (with a minimum of three reviews).`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H100 · Bright green · Before: Partial**
    - Selected text: `Initially, our researchers manually reviewed all tasks to identify experts who produced consistently high- quality tasks; these individuals were trained and promoted to reviewers.`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H024 · Light green · Before: Partial**
    - Selected text: `Across all stages of review, experts provided detailed comments, and tasks were iteratively revised before subsequent reviews to enhance quality and representativeness,`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H101 · Light green · Before: Missing**
    - Selected text: `The most skilled reviewers were further trained to become lead reviewers, responsible for identifying, mentoring, and promoting additional qualified reviewers from within the expert pool.`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H102 · Light green · Before: Missing**
    - Selected text: `Throughout the review process, the research team regularly performed quality-control checks on tasks signed off by reviewers, ensuring ongoing alignment and quality standards.`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H103 · Light green · Before: Covered**
    - Selected text: `Human reviewers conducted multiple rounds of review on each task.`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H105 · Light green · Before: Covered**
    - Selected text: `occupation-specific reviewer`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H106 · Light green · Before: Covered**
    - Selected text: `generalist reviewer`
    - Now represented under **Quality Control → Human Review → Review Approach**.

- **H107 · Light green · Before: Covered**
    - Selected text: `third expert reviewer`
    - Now represented under **Quality Control → Human Review → Review Approach**.

## Under-Contextualized GDPval

**Priority 2 · Key Findings**

GPT-5 performs worse on under-specified prompts that require it to find the necessary inputs, choose an approach, and determine formatting requirements.

- **H069 · Bright green · Before: Partial**
    - Selected text: `To assess how models handle task ambiguity, we created a modified version of GDPval with de- liberately lower-context prompts.`
    - Now represented under **Key Findings → Under-Contextualized GDPval**.

- **H070 · Light green · Before: Partial**
    - Selected text: `These shorter prompts omitted additional context such as where to locate specific data within reference files, how to approach the problem, or detailed formatting expectations for the final deliverable; the models had to “figure it out.”`
    - Now represented under **Key Findings → Under-Contextualized GDPval**.

- **H071 · Light green · Before: Partial**
    - Selected text: `navigating ambiguity by figuring out what to work on and where to get the necessary inputs.`
    - Now represented under **Key Findings → Under-Contextualized GDPval**.

- **H072 · Light green · Before: Covered**
    - Selected text: `model’s performance was worse on under-specified prompts. In particular, the models struggled to figure out context.`
    - Now represented under **Key Findings → Under-Contextualized GDPval**.

## Expert Sourcing

**Priority 2 · Dataset Creation**

Experts are recruited from the highest-earning knowledge work occupations in the selected sectors; occupation-specific experience and selective screening ground tasks in professional work.

- **H093 · Bright green · Before: Partial**
    - Selected text: `Experts for each occupation were required to have previous experience in that specific occupation and sector`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H002 · Light green · Before: Covered**
    - Selected text: `industry professionals with an average of 14 years of experience.`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H016 · Light green · Before: Covered**
    - Selected text: `highest-earning knowledge work occupations`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H017 · Light green · Before: Partial**
    - Selected text: `We recruited expert industry professionals to create realistic tasks based on their professional work experience.`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H018 · Light green · Before: Covered**
    - Selected text: `The average expert had 14 years of experience.`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H019 · Light green · Before: Missing**
    - Selected text: `pass a video interview, a background check, a training and a quiz to partici- pate in the project.`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H081 · Light green · Before: Missing**
    - Selected text: `15+ years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H082 · Light green · Before: Missing**
    - Selected text: `18+ years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H083 · Light green · Before: Missing**
    - Selected text: `15 years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H084 · Light green · Before: Missing**
    - Selected text: `20+ years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H085 · Light green · Before: Missing**
    - Selected text: `25 years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H086 · Light green · Before: Missing**
    - Selected text: `5+ years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H087 · Light green · Before: Missing**
    - Selected text: `teams of 10+ engineers`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H088 · Light green · Before: Missing**
    - Selected text: `15+ years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H089 · Light green · Before: Missing**
    - Selected text: `10 years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H090 · Light green · Before: Missing**
    - Selected text: `20 years`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H091 · Light green · Before: Missing**
    - Selected text: `Less than 10% of applicants were selected to con- tribute tasks to our full set.`
    - Now represented under **Dataset Creation → Expert Sourcing**.

- **H092 · Light green · Before: Missing**
    - Selected text: `Each occupation had a minimum of 5 quali- fied professionals.`
    - Now represented under **Dataset Creation → Expert Sourcing**.

## Dataset Scope

**Priority 3 · Summary**

The full dataset contains <span class="verbatim">1,320 tasks</span> spanning <span class="verbatim">44 occupations across the top 9 sectors contributing to U.S. GDP (Gross Domestic Product).</span> The public gold subset has <span class="verbatim">220 tasks</span>. There are <span class="verbatim">at least 30 tasks per occupation in the full set</span> and <span class="verbatim">5 tasks per occupation in the gold subset</span>.

- **H001 · Light green · Before: Covered**
    - Selected text: `44 occupations across the top 9 sectors contributing to U.S. GDP (Gross Domestic Product).`
    - Now represented under **Summary → Dataset Scope**.

- **H003 · Light green · Before: Covered**
    - Selected text: `220 tasks`
    - Now represented under **Summary → Dataset Scope**.

- **H005 · Light green · Before: Missing**
    - Selected text: `at least 30 tasks per occupation in the full set (and 5 tasks per occupation in the gold subset), across 44 occupations.`
    - Now represented under **Summary → Dataset Scope**.

- **H010 · Light green · Before: Covered**
    - Selected text: `1,320 tasks`
    - Now represented under **Summary → Dataset Scope**.

## Automated Grading

**Priority 3 · Model Evaluation · Auto Judge**

<span class="verbatim">average human-automated grader agreement was 65.7% and human inter-rater agreement was 70.8%.</span>

- **H004 · Light green · Before: Missing**
    - Selected text: `a pub- lic automated grading service`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H007 · Light green · Before: Partial**
    - Selected text: `an experimental automated grader`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H028 · Light green · Before: Partial**
    - Selected text: `we trained an experimental grading model`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H029 · Light green · Before: Covered**
    - Selected text: `achieves 66% agreement with human expert graders, only 5% below human expert inter-rating agreement of 71%.`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H048 · Light green · Before: Partial**
    - Selected text: `we make an automated grader proxy available, but do not consider it a full substitute for industry expert graders.`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H108 · Light green · Before: Missing**
    - Selected text: `the empirical mean over all pairs of ratings`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H109 · Light green · Before: Missing**
    - Selected text: `H human score`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H110 · Light green · Before: Missing**
    - Selected text: `au- A tomated grader score`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H111 · Light green · Before: Missing**
    - Selected text: `human scores and H1 H2`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H113 · Light green · Before: Missing**
    - Selected text: `three automated grader`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H114 · Light green · Before: Covered**
    - Selected text: `average human-automated grader agreement was 65.7% and human inter-rater agreement was 70.8%.`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H115 · Light green · Before: Missing**
    - Selected text: `models often favor their own responses`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H116 · Light green · Before: Missing**
    - Selected text: `Both agreement metrics are highest for less capable models, since their outputs are easier to distinguish from human deliverables and are less likely to be preferred.`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

- **H117 · Light green · Before: Covered**
    - Selected text: `12 out of 220 tasks as ungradable due to limitations of the automated grader.`
    - Now represented under **Model Evaluation → Auto Judge → Automated Grading**.

## Human Expert Grading

**Priority 3 · Model Evaluation · Human Review**

<span class="verbatim">In addition to correctness, expert graders often consider subjective factors such as structure, style, format, aesthetics, and relevance.</span>

- **H006 · Light green · Before: Covered**
    - Selected text: `our primary evaluation metric is head-to-head human expert comparison.`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

- **H012 · Light green · Before: Covered**
    - Selected text: `In addition to correctness, expert graders often consider subjective factors such as structure, style, format, aesthetics, and relevance.`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

- **H013 · Light green · Before: Partial**
    - Selected text: `our primary metric is win rate,`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

- **H015 · Light green · Before: Covered**
    - Selected text: `compare model outputs against a human expert baseline,`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

- **H025 · Light green · Before: Missing**
    - Selected text: `blinded expert pairwise comparisons,`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

- **H026 · Light green · Before: Missing**
    - Selected text: `rank two or more unlabeled work deliverables.`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

- **H027 · Light green · Before: Missing**
    - Selected text: `over an hour.`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

- **H030 · Light green · Before: Missing**
    - Selected text: `stylistic differences.`
    - Now represented under **Model Evaluation → Human Review → Human Expert Grading**.

## Economic Relevance

**Priority 3 · Impact**

<span class="verbatim">AI capability evaluations can provide clearer, more directly attributable evidence about model abilities, allowing us to assess economic relevance ahead of widespread adoption.</span>

- **H008 · Light green · Before: Partial**
    - Selected text: `how increasingly capable AI models could affect the labor market—`
    - Now represented under **Impact → Economic Relevance**.

## Files and Attachments

**Priority 3 · Special Design**

<span class="verbatim">GDPval tasks incorporate a broad range of real-world file types (such as spreadsheets, documents, presentations, images, audio, video, and specialized formats like CAD).</span>

- **H009 · Light green · Before: Covered**
    - Selected text: `tasks are based on actual work product from industry experts,`
    - Now represented under **Special Design → Files and Attachments**.

- **H077 · Light green · Before: Partial**
    - Selected text: `Many traditional evaluations rely on text-in/text-out task formats. GDPval tasks incorporate a broad range of real-world file types (such as spreadsheets, documents, presentations, images, audio, video, and specialized formats like CAD). 67.7% of tasks required interaction with at least one reference file.`
    - Now represented under **Special Design → Files and Attachments**.

## Representative Breadth

**Priority 3 · Special Design**

The benchmark builds on production AI usage analyses to cover areas where model adoption is still emerging.

- **H011 · Light green · Before: Missing**
    - Selected text: `production AI usage analyses`
    - Now represented under **Special Design → Representative Breadth**.

## Time to Complete

**Priority 3 · Key Findings**

Reported task-time averages differ across the introduction, task-statistics tables, and economic analysis.

- **H014 · Light green · Before: Missing**
    - Selected text: `average of 7 hours of work`
    - Now represented under **Key Findings → Time to Complete**.

## Task Design

**Priority 3 · Dataset Creation**

<span class="verbatim">Each GDPval task consists of two primary components: a request (often with reference files) and a deliverable (work product).</span>

- **H020 · Light green · Before: Covered**
    - Selected text: `Each GDPval task consists of two primary components: a request (often with reference files) and a deliverable (work product).`
    - Now represented under **Dataset Creation → Task Design**.

## Speed and Cost Comparison

**Priority 3 · Key Findings**

<span class="verbatim">When incorporating time to review and redo work, the payoff from using a model shrinks.</span>

- **H031 · Light green · Before: Covered**
    - Selected text: `In the scenarios analyzed, incorporating frontier AI models into expert workflows showed the potential to save time and money relative to unaided experts.`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H032 · Light green · Before: Covered**
    - Selected text: `“try using the model and if still unsat- isfactory, fix it yourself”`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H033 · Light green · Before: Missing**
    - Selected text: `Here, an expert human samples from a model, reviews outputs, and if unsatisfactory, resamples and repeats.`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H049 · Light green · Before: Missing**
    - Selected text: `HT`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H050 · Light green · Before: Missing**
    - Selected text: `HC,`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H051 · Light green · Before: Missing**
    - Selected text: `= 404 HT`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H052 · Light green · Before: Missing**
    - Selected text: `= $361. HC`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H053 · Light green · Before: Missing**
    - Selected text: `RT`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H054 · Light green · Before: Missing**
    - Selected text: `= 109 RT`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H055 · Light green · Before: Missing**
    - Selected text: `RC`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H056 · Light green · Before: Missing**
    - Selected text: `$86,`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H057 · Light green · Before: Missing**
    - Selected text: `MT`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H058 · Light green · Before: Missing**
    - Selected text: `MC`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H059 · Light green · Before: Missing**
    - Selected text: `w`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H060 · Light green · Before: Missing**
    - Selected text: `HT /MT`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H061 · Light green · Before: Missing**
    - Selected text: `HC/MC.`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H062 · Light green · Before: Missing**
    - Selected text: `(1 wi) −`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H063 · Light green · Before: Missing**
    - Selected text: `human completion time for any fixes needed`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H064 · Light green · Before: Covered**
    - Selected text: `a human tries using GPT-5 for a task, assesses its quality, and then does the task themselves if the deliverable quality is below their quality bar.`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H065 · Light green · Before: Partial**
    - Selected text: `without accounting for any quality differences`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H066 · Light green · Before: Missing**
    - Selected text: `n a human tries rounds of using GPT-5 for a task, then assesses its quality each time, and then does the task themselves if the model quality is below their quality bar after all attempts.`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

- **H067 · Light green · Before: Covered**
    - Selected text: `When incorporating time to review and redo work, the payoff from using a model shrinks.`
    - Now represented under **Key Findings → Speed and Cost Comparison**.

## Model Strengths and Weaknesses

**Priority 3 · Model Evaluation · Human Review**

<span class="verbatim">Claude, Grok, and Gemini most often lost due to instruction-following failures, while GPT-5 high lost mainly from formatting errors and had the fewest instruction-following issues.</span>

- **H034 · Light green · Before: Missing**
    - Selected text: `5Samples were clustered using expert justifications;`
    - Now represented under **Model Evaluation → Human Review → Model Strengths and Weaknesses**.

- **H035 · Light green · Before: Partial**
    - Selected text: `We built a clustering pipeline to analyze why experts preferred or rejected GPT-5 high,`
    - Now represented under **Model Evaluation → Human Review → Model Strengths and Weaknesses**.

- **H036 · Light green · Before: Covered**
    - Selected text: `instruction-following failures,`
    - Now represented under **Model Evaluation → Human Review → Model Strengths and Weaknesses**.

- **H037 · Light green · Before: Covered**
    - Selected text: `formatting errors`
    - Now represented under **Model Evaluation → Human Review → Model Strengths and Weaknesses**.

- **H038 · Light green · Before: Covered**
    - Selected text: `ignored reference data,`
    - Now represented under **Model Evaluation → Human Review → Model Strengths and Weaknesses**.

- **H039 · Light green · Before: Covered**
    - Selected text: `failed to provide deliverables,`
    - Now represented under **Model Evaluation → Human Review → Model Strengths and Weaknesses**.

- **H040 · Light green · Before: Covered**
    - Selected text: `used the wrong format.`
    - Now represented under **Model Evaluation → Human Review → Model Strengths and Weaknesses**.

## Increasing Reasoning Effort and Scaffolding

**Priority 3 · Key Findings**

Increased reasoning effort, prompt-tuning, and agent scaffolding, including best-of-N sampling, improve performance and deliverable quality.

- **H041 · Light green · Before: Covered**
    - Selected text: `We found that additional reasoning effort improved performance.`
    - Now represented under **Key Findings → Increasing Reasoning Effort and Scaffolding**.

- **H042 · Light green · Before: Partial**
    - Selected text: `improved agent scaffolding`
    - Now represented under **Key Findings → Increasing Reasoning Effort and Scaffolding**.

- **H043 · Light green · Before: Covered**
    - Selected text: `improve model capabilities with prompts.`
    - Now represented under **Key Findings → Increasing Reasoning Effort and Scaffolding**.

- **H073 · Light green · Before: Missing**
    - Selected text: `best-of-N sampling`
    - Now represented under **Key Findings → Increasing Reasoning Effort and Scaffolding**.

- **H074 · Light green · Before: Missing**
    - Selected text: `GPT-5 grader`
    - Now represented under **Key Findings → Increasing Reasoning Effort and Scaffolding**.

## Limitations

**Priority 3 · Impact**

GDPval focuses on self-contained knowledge work; tasks are precisely-specified and one-shot, with the full task context provided.

- **H045 · Light green · Before: Partial**
    - Selected text: `knowledge work that can be performed on a computer, particularly around digital deliver- ables.`
    - Now represented under **Impact → Limitations**.

- **H046 · Light green · Before: Partial**
    - Selected text: `we provide the full context of the task in the prompt,`
    - Now represented under **Impact → Limitations**.

- **H047 · Light green · Before: Covered**
    - Selected text: `one-shot, not interactive:`
    - Now represented under **Impact → Limitations**.

## Task Duration

**Priority 3 · Model Evaluation · Human Review**

<span class="verbatim">Win rates are highest for shorter tasks (0–2 hours) and decline steadily as completion time increases.</span>

- **H068 · Light green · Before: Covered**
    - Selected text: `Win rates are highest for shorter tasks (0–2 hours) and decline steadily as completion time increases. This indicates that models perform best on faster, less time-intensive tasks.`
    - Now represented under **Model Evaluation → Human Review → Task Duration**.

## Prompt Specificity

**Priority 3 · Quality Control · Human Review · Quality Dimensions**

<span class="verbatim">Occupational experts conducting human grading rated the specificity of instructions provided in each prompt.</span>

- **H078 · Light green · Before: Missing**
    - Selected text: `the specificity of instructions provided in each prompt.`
    - Now represented under **Quality Control → Human Review → Quality Dimensions → Prompt Specificity**.

- **H079 · Light green · Before: Missing**
    - Selected text: `human grading`
    - Now represented under **Quality Control → Human Review → Quality Dimensions → Prompt Specificity**.

## Validating the Digital Tasks Measure

**Priority 3 · Dataset Creation**

The digital tasks measure aligns with established economic measures of work: higher non-routine cognitive content and lower routine and manual content.

- **H118 · Light green · Before: Missing**
    - Selected text: `The patterns are clear: occupations with higher digital-task shares score systematically higher on the non-routine cognitive dimensions and lower on the manual dimensions. In other words, the more an occupation relies on digital tasks, the more it resembles cognitive, non-routine work.`
    - Now represented under **Dataset Creation → Validating the Digital Tasks Measure**.

- **H119 · Light green · Before: Missing**
    - Selected text: `The pattern is again clear– knowledge-work occupations cluster at the top of the non-routine cognitive distributions and at the bottom of the routine and manual distributions. Taken together, these results suggest that our digital- task classification is closely aligned with the economic literature on cognitive/manual work.`
    - Now represented under **Dataset Creation → Validating the Digital Tasks Measure**.

## Excluded and Unclassified

- H112: Yellow highlight, excluded by your color preferences.
- H044: Squiggly annotation (#4B99FF); meaning unclassified, not included in the highlight count.
