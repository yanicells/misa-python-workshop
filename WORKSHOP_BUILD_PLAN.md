# Workshop project and repository build plan

## Objective and scope

Implement this plan together with `WEBSITE_BUILD_PLAN.md`. Deliver a project-based Python workshop for first-year BS MIS beginners, with a working, personalized MISA cluster personality quiz completed within a 70–90-minute event. Introductions, Python explanations, Git, coding, and closing all count toward that time. Weave explanation and immediate application together; do not teach all Python, then all Git, then assemble the project.

This document specifies structure, scope, broad progression, and verification. The implementation agent authors actual lessons, quiz content, code, and project-spec examples. Do not turn this outline into a semester syllabus.

Each participant has a laptop; Yani and Gabe present, with roughly five or more additional helpers expected. Encourage pre-event setup and provide Colab as a fallback. Learners may type along, copy complete blocks, or recover using reference branches. Completion is the priority, but essential basics remain required even when demonstrated outside the quiz.

## Required human inputs and deliverables

Handoff reminders for Yani/Gabe:

- [x] **Gabe's PMG repo:** context about MISA clusters, used to develop personality questions, answer-to-cluster associations, and result descriptions.
- [x] **Yani's MISA website repo:** primarily the official icon/logo and relevant assets, not a mandate to reproduce that site's design.
- [x] **Humanizer skill:** apply to learner-facing website writing and quiz prompts, descriptions, and results without compromising accuracy or code.

With those supplied, an agent should implement both plans using its own routine technical judgment. It may scaffold with explicit placeholders beforehand; it must not invent cluster facts or claim to apply a missing skill.

Implementation deliverables:

- Documentation website in `/web`, following the companion plan.
- Beginner-readable Python project in `/workshop`, with starter, runnable intermediate checkpoints, and final checkpoint branches.
- Root repository README and `/workshop/README.md` on `main`.
- Equivalent Google Colab notebook fallback, linked from the website and learner README.
- Pre-event setup/verification guide and short troubleshooting/recovery instructions.
- Introduction and closing material on the website. Any separate slide deck is managed outside this repository.
- Moving-forward roadmap, tiny practice activities, and a few follow-up project specifications.
- Publication-ready repository with temporary professor material removed from files and public history.

## Repository structure and branch contract

```text
/
  README.md                    # Entry point: workshop, website, setup, branch workflow
  WEBSITE_BUILD_PLAN.md
  WORKSHOP_BUILD_PLAN.md
  web/                         # Website source, content, assets, dependencies
  workshop/
    README.md                  # Concise learner commands and website/fallback links
  notes/                       # Temporary private inputs; absent before publication
```

This is the `main` layout: no completed learner Python project on `main`. After cloning, participants check out `00-start`; learner code appears under `/workshop` on that branch. Keep the root and workshop READMEs distinct. Explanations belong primarily on the website; READMEs are short navigation/run guides.

Use the checkpoint branches `00-start`, `01-welcome`, `02-question`, `03-loops`, `04-functions`, `05-results`, and `06-improve`. The final `06-improve` branch contains the complete 15-question weighted quiz. Each checkpoint is a cumulative runnable milestone, not an independent exercise folder.

Prefer a single clear entry script with only a small separate question-data file if that aids readability. Avoid package scaffolding and unnecessary abstractions. Use Python's standard library; no web server, database, accounts, APIs, or third-party Python dependencies in the required project. Keep maintainer checks outside the learner's main working files and add them to the repository only when they remain useful. Store the fallback notebook under `/workshop` on applicable checkpoint branches and link directly to the appropriate Colab version; do not place completed notebook solutions on `main`.

All branches in a repository version the whole tree, not just `/workshop`. Preserve consistent website source/guides across the published checkpoint series. If Yani later connects the site to Vercel, production should use `main`; deployment remains outside this repository. Keep complete final learner code off `main`'s current tree, while allowing the website's instructional code examples.

## Quiz behavior

Build a playful personality quiz, inspired by the idea of [UniSort](https://github.com/yanicells/UniSort), not a port of its full implementation or scoring system.

- Ask for a name or nickname, then ask 15 questions about the participant; there are no correct answers. Show a question number and use clear blank lines between terminal sections.
- Each choice awards 2 points to its closest cluster and 1 point to a related cluster. Store the point mapping as data and loop through it to update scores. Every choice awards 3 total points.
- Build and explain one question first. Use a seven-question unweighted bank while teaching the core loop, then provide the complete 15-question weighted bank for copying in the final improvement milestone. Learners can customize one question or its wording.
- Use actual cluster context from PMG. Keep total weighted scoring opportunities within one point across the seven clusters so no cluster has a structural scoring advantage.
- Validate choices with straightforward membership checks and a `while` retry. Keep answer identifiers as strings to avoid unnecessary conversion/error handling in the main flow.
- Percentage means **cluster points / all points awarded × 100**. Label it as a share of quiz points, not a scientifically measured compatibility. A complete final run awards 45 points.
- Sort scores and show the **top three distinct positive score levels** using dense ranks: ties share a rank and the next distinct score advances by one. Include every cluster tied at a displayed rank, even if more than three clusters appear. Fewer than three ranks is acceptable when fewer earned points.
- Each displayed result includes rank, cluster name, percentage, description, and a clear tie indicator when applicable. Rank by raw scores, not rounded display percentages. The displayed subset need not sum to 100%.
- Ensure valid question data always awards points; handle an empty/zero-score state simply instead of dividing by zero.

## Beginner-code constraints

Understandable code is more important than short code. Use descriptive names, explicit steps and intermediate variables, ordinary loops, and small named functions. Do not hide main behavior in a provided black-box helper.

Teach sorting and tied-rank display in the guided build. A named function returning a cluster's score can make the sorting key concrete; keep ordering, percentage calculation, and rank tracking separate. Avoid lambdas, comprehensions, compact tricks, unnecessary classes, and teaching a custom sorting algorithm just to avoid a built-in. Explain the limited new sorting syntax directly.

Supply copyable code and recovery checkpoints for learners who need them. Bulk question data is copied after one example is understood; typing repetitive content is not a learning objective.

## Rough progression and topic-to-project mapping

Use this as sequencing guidance, not a finished lesson script or proven timing schedule. Rehearse the complete required path for 70 minutes, leaving up to 20 additional minutes for troubleshooting and personalization.

| Stage | Topics / activity | Immediate application |
| --- | --- | --- |
| Welcome and destination | Introduce presenters and finished outcome; brief `import`/`random` exposure | Demonstrate the quiz; randomly select about five participants for introductions |
| Meet Python and GitHub | What Python can build; Git, GitHub, repositories, commits, branches | Understand the tools and browse the repository before entering commands |
| Get the project | Git vs. GitHub, terminal navigation, `clone`, branches, `checkout` | Clone `main`, open `/workshop`, switch to `00-start`, run the starter |
| First personal change | Running Python, comments, indentation, variables, strings, `print()`, `input()` | Ask for the player's name; use Input → Process → Output as the recurring frame |
| Save a working version | `status`, staging with `add`, local `commit` | Save the first customization; distinguish saving files from recording history |
| One personality question | `input()`, conditions, comparisons, answer validation | Read a choice and award initial points; retry invalid answers with `while` |
| Expand the quiz | Lists, indexing, dictionaries, key access, `for`, simple nested iteration, `+=` | Understand one question's data, copy the question bank, loop through questions and associated clusters |
| Organize working behavior | Functions, parameters, return values | Group behavior students already understand into small functions |
| Show results | Arithmetic, totals, floats, percentages, formatting, sorting, rank tracking | Display three score ranks with descriptions and ties |
| Improve the quiz | Nested point dictionaries and weighted addition | Expand to 15 grounded questions with 2-point primary and 1-point related matches |
| Test and personalize | Reading errors, manual checks, local commit; recovery as needed | Try answers and a tie, customize, let a neighbor try the quiz, save finished work |
| Closing / next steps | Follow-up practice, sharing, MISA; optional remote Git | Point to roadmap and project specs; push only if time permits |

### Essential-basics guarantee

The implementation agent must audit both supplied semester notes and the prior workshop reference for super-basic omissions. Cover the following even when not naturally used in the quiz, using a tiny example at a relevant moment:

- Running a file, comments, indentation, variables, and assignment.
- Strings, integers, floats, booleans, and basic type conversion.
- `print()`, `input()`, and the fact that input returns a string.
- Basic arithmetic and comparison operators; `and`, `or`, `not`.
- `if` / `elif` / `else`, `for`, `while`, and basic `range()`.
- Lists, zero-based indexing, dictionaries, and access by key.

Include project-used functions and formatting as described above. Maximize natural exposure, not syntax density. Use correct Python terminology, such as lists rather than calling every collection an array. Borrow last year's useful IPO frame and small prediction prompts, without reproducing its slide text or postponing all project assembly until the end.

Likely outside the main project: tuples as a dedicated topic, advanced slicing/formatting, collection copying, comprehensions, deeper function scope, OOP, encapsulation, inheritance, and overriding. This list is provisional: map every relevant source-note topic to live use, a tiny essential demonstration, or moving-forward material. Being present in the semester notes does not make an advanced topic mandatory live coverage.

If rehearsal overruns, reduce optional customization and repeated demonstrations first. Do not spend time typing the question bank. Preserve required essentials and a completed runnable project; report any remaining timing conflict instead of silently dropping requirements or claiming untested feasibility.

## Setup, Git, and recovery

Pre-event checklist: install VS Code, Python, and Git; create/check GitHub access; successfully clone the repository; and run a tiny Python file. Document relevant Windows/macOS differences with verified commands. Verify presenter/helper laptops fully beforehand. Students who already cloned open their existing copy while facilitators demonstrate cloning; do not require duplicate clones into the same folder.

Introduce Git near the start through familiar analogies: Google Docs version history for commits and a shared Drive location for GitHub. Explain limits: local commits and online pushes are explicit, separate operations. Practice `clone`, `checkout`, `status`, `add`, and `commit` when needed. Explain branches in the checkpoint context; creating personal recovery branches may support safe work preservation. `push` and `pull` belong in optional time or moving forward.

Recovery must preserve personal work. Teach committing relevant learner files before switching, use local branch names that avoid detached-HEAD confusion, and record how to return to earlier work. Make clear that the reference checkpoint does not merge in personal edits. Never use force checkout, hard reset, or cleanup commands as routine beginner recovery. Helpers handle conflicts through explicit preservation steps, not deletion of student work.

Colab follows the same Python milestones and behavior but does not require local Git practice. Document how to open/save a personal notebook copy and run cells in order. Keep the fallback useful if the local environment fails; do not teach a second parallel course.

## Moving forward and presentation

For remaining source-note concepts, provide a compact roadmap with purpose, checked resources, tiny examples or very small practice projects. Finish with a few achievable project specifications describing the outcome, scope, and concepts to practice. Include optional publishing/further Git, general tips, videos/resources, joining MISA, and sharing progress with friends, organizations, and facilitators.

Keep presenter introductions, motivation/destination, instruction, hands-on steps, and closing available through the website. If the workshop team creates a separate deck, manage it outside this repository and do not duplicate all lessons into slides.

## Temporary sources and publication cleanup

The existing `/notes` files are professor course material received through another person. Use them privately to understand boundaries and essential terminology; author original explanations, examples, and assets. Do not publish the supplied notes.

Before public release, remove `/notes` and any copies from the working tree **and all history/branches/tags included in the public repository**. Deleting current files alone is insufficient. Inspect the remote state first; preserve needed private reference access while preparing a clean publication history. Verify checkpoint branches do not reintroduce the material. A history rewrite affects commit IDs and collaborators, so coordinate any necessary remote replacement rather than blindly force-pushing. This is an implementation/release requirement, not an instruction to rewrite history while committing these plans.

## Implementation and verification

1. Inspect the supplied repos, skill, private notes, and any available prior workshop material; produce a concise coverage map.
2. Finalize question-data shape, original content, runnable milestones, and shared website/checkpoint mapping.
3. Build the simplest working quiz, then develop learner checkpoints and website explanations together.
4. Add the notebook, setup/recovery guides, moving-forward material, and introduction/closing website content.
5. Apply the humanizer to all user-facing prose; verify cluster grounding and branding inputs.
6. Rehearse from a fresh clone and each recovery checkpoint, using the website as the presenter guide.
7. Prepare clean public history and validate every release branch before publication.

Acceptance checks:

- Fresh clone → `00-start` → documented run succeeds without website dependencies.
- `main` has the two READMEs and no completed learner project; final code is on the named final checkpoint branch.
- Every checkpoint runs and matches its lesson, expected behavior, notebook milestone, and recovery instructions.
- Validate name input, question numbering, weighted awards, percentages, invalid input retry, ties spanning third rank, fewer positive ranks, and zero-score handling. Use small maintainer fixtures or manual checks; do not burden beginners with a test framework.
- Validate all 15 questions, confirm that each choice awards 3 points, keep cluster opportunities within one point, and confirm descriptions against PMG context.
- Test notebook execution from a clean runtime and local execution on supported workshop platforms.
- Exercise recovery after a student's customization and confirm earlier work remains recoverable.
- Record actual rehearsal duration and any scope adjustments; do not label the time target verified without a rehearsal.
- Verify both website themes, readable/copyable code, visualizations, links, and all companion-plan acceptance checks.
- Audit all public refs and build artifacts for the temporary professor material before release.
