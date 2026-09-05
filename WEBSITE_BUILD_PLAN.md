# Workshop website build plan

## Purpose and implementation handoff

Implement this plan together with `WORKSHOP_BUILD_PLAN.md`. These are build specifications, not finished course content. The implementation agent should author the lessons, examples, quiz, notebook, and supporting materials using the supplied sources and current documentation. Keep this plan's learning outline broad; do not interpret it as a request to reproduce a semester course.

The workshop serves first-year BS Management Information Systems students who are starting programming. The entire event is 70–90 minutes, including introductions and closing. Finishing a personalized Python project is the priority. Explanation, Python edits, Git practice, and execution must be interwoven.

The website is both the presenters' main teaching surface and a usable self-study guide afterward. A separate short deck handles introductions and closing. Students may type along, copy code, or recover through checkpoint branches.

### Human handoff checklist

- [x] Supply **Gabe's PMG repository**: source context about MISA clusters for quiz questions, answer associations, and result descriptions. It is not the website design template.
- [x] Supply **Yani's MISA website repository**: primarily the official icon/logo and any relevant assets. Do not copy its entire visual design.
- [x] Supply the **humanizer skill**: apply its actual instructions to all learner-facing writing, including website text and quiz prompts/results. Preserve technical accuracy, essential terminology, and executable code.

Once these are supplied, the next agent should be able to implement both plans without another planning interview. Inspect the supplied resources; do not invent cluster facts or pretend an unavailable skill was applied. Structural work can proceed with explicitly marked placeholders while inputs are missing. Resolve routine framework and tooling choices autonomously.

## Location and technical boundaries

- Build the site in `/web`, with its own dependencies and build configuration.
- Use a static documentation architecture with Markdown-based content. Choose a maintained framework appropriate to that requirement; the visual reference does not mandate Next.js.
- Students run Python in `/workshop`; they must not need Node.js or the website toolchain to participate.
- No accounts, database, saved completion tracking, or full in-browser Python IDE. Colab is the execution fallback.
- Choose suitable static hosting during implementation and document build/deployment configuration. Production deployment follows `main`, not learner checkpoint branches.

## Visual direction and navigation

Use [Next.js documentation](https://nextjs.org/docs) as the primary layout and interaction reference: straightforward documentation, restrained styling, readable prose, a section sidebar, and clear code examples. Use the supplied MISA icon/logo for identity; avoid turning this into an elaborate branded landing page.

Other supplied references are secondary inspiration:

- [Intermediate React course](https://intermediate-react-v6.holt.courses/lessons/welcome/intro)
- [ML workshop](https://fem-ml-workshop.netlify.app/docs/project-1#load-the-model)
- [Intro to Agents](https://publish.obsidian.md/agents-v2/01-Intro-to-Agents)

Required interface:

- Light and dark themes with readable code highlighting in both; initially follow system preference, provide a visible toggle, and remember manual selection.
- Ordered sidebar sections, active-section indication, heading anchors, page-level contents where useful, and previous/next navigation.
- Search across published workshop material, with helpful section labels.
- Persistent, easy-to-find setup/help, repository, checkpoint, and Colab links.
- Responsive navigation for smaller screens and legible presentation on a projector. Provide a comfortable reading width and generous code text sizes.
- Keyboard-operable controls, visible focus, sufficient contrast, semantic headings, and reduced-motion support. Do not rely on color alone to communicate state.

## Content structure and writing contract

Broad sections: welcome/destination, setup and fallback, ordered project milestones, troubleshooting, and moving forward. The exact lesson titles and number of pages belong to implementation, following the progression in the workshop plan.

Every build milestone should make the following easy to identify:

1. What the learner is about to make work.
2. The minimum explanation and essential terms needed now.
3. The file being edited and precisely where the change belongs.
4. Copyable code and how to run it.
5. Expected output or behavior and one short check when useful.
6. The matching recovery checkpoint and a link to safe recovery instructions.

Use plain, beginner-friendly English, short paragraphs, descriptive headings, and focused bullets. Format cleanly. Explain new syntax before relying on it; do not substitute vague friendly wording for a necessary explanation. Apply the supplied humanizer to website and quiz text. Use familiar analogies only when useful, and briefly explain their limits.

Git analogy: Google Docs version history helps introduce commits; a shared Drive location helps introduce GitHub. Explicitly explain that saving a file, committing locally, and pushing online are different actions, not automatic synchronization.

Code examples must favor understandable steps over brevity: descriptive variables, intermediate values, ordinary loops, and small named functions. Avoid lambdas, comprehensions, and compressed expressions in the required path. Do not require typing bulk quiz data. Introduce one example, then provide the question bank to copy.

Code blocks must identify Python versus shell, include copy controls with feedback, and copy executable text without line numbers, prompts, or diff markers. Distinguish replacement blocks from additions. Keep full working checkpoint versions available so a partial snippet never leaves students guessing about file state.

## Visualizations and analogies

Build a few focused visualizations where they materially clarify execution. They supplement runnable examples, not replace them.

- A loop stepper: highlight the current code line/item, current variable values, and accumulated output.
- A scoring stepper: show a selected answer, its associated clusters, and score changes one at a time.
- A simple static Git diagram: working files → staging → local commit, with the remote/push relationship explained when relevant.

Use explicit Step and Reset controls for interactive examples. Avoid autoplay. Include a short textual explanation or static equivalent, accessible controls, and a layout that works on a projected screen. Prefer small deterministic demonstrations over a general-purpose execution engine. Demonstration behavior must match the actual Python examples, including loop boundaries and reset state.

## Shared website/project contract

Define one checkpoint mapping with stable identifiers, lesson URLs, branch names, edited files, run commands, and expected behavior. Both README instructions and website links must derive from or be checked against that mapping. The notebook must use corresponding milestone identifiers.

- Learners clone `main`, then check out `00-start`.
- `main` contains guides and the website, not completed learner code.
- The final project lives on the final checkpoint branch.
- Checkpoints represent runnable reference states; regular participants continue their own edits rather than switching at every lesson.
- Every recovery route explains saving work first and that switching to a reference checkpoint does not carry customizations into that reference version.

Keep website source and root guidance available and consistent on published checkpoint branches. Prepare checkpoints from a common finalized website baseline so branch changes do not expose an outdated teaching guide.

## Moving forward

Create a compact roadmap for every relevant source-note topic omitted from the live path. Group related concepts; provide a brief purpose, a checked resource, and a tiny exercise or very small project where useful. End with a few more substantial project-spec ideas with clear outcomes and suggested concepts. Do not create full additional courses.

Include GitHub publishing/further Git practice, general tips, suitable videos/resources, encouragement to join MISA, and invitations to share progress with friends, organizations, and the facilitators. Keep the tone warm and natural.

## Implementation sequence

1. Read both plans and supplied reference materials; audit essential coverage and source restrictions.
2. Choose the static documentation stack, define the shared milestone mapping, and scaffold the site and themes.
3. Implement navigation, search, copyable code, lesson templates, and visualization components.
4. Author original lessons alongside executable project checkpoints and the notebook. Apply the humanizer to learner-facing text.
5. Add setup/help and the moving-forward roadmap; verify references and remove placeholders once source inputs arrive.
6. Rehearse the website as the teaching surface, correct pacing and code drift, and prepare hosting configuration.
7. Complete the private-source cleanup specified in the workshop plan before public publication.

## Acceptance checks

- Production build succeeds; direct lesson URLs, anchors, search, previous/next navigation, and repository/checkpoint links work.
- Both themes, copy controls, keyboard navigation, mobile navigation, and projector-scale readability are checked.
- Copied snippets run in the stated checkpoint/file context and agree with expected output.
- Steppers correctly show intermediate state and output; Reset restores the starting state.
- A learner can follow independently, and presenters can teach the live path without needing a second instructional slide deck.
- Site content is original, essential basics are not silently omitted, and remaining topics have a compact follow-up route.
- No supplied professor notes are bundled, indexed, published, or retained in the public repository history.
- Cluster text is grounded in PMG context, the official icon is used when supplied, and the actual humanizer skill has been applied to learner-facing prose.
