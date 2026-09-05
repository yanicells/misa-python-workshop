# Verification record

Checked locally on macOS, 2026-09-05. This is a release candidate; the GitHub repository and production site have not been replaced or published by this implementation.

## Passed

- Astro type checking: zero errors, warnings, or hints. Static production build succeeds with 13 HTML pages, including the default 404 page, and a Pagefind search index.
- Dependency installation with Node.js 24: npm reports zero known vulnerabilities. Students need only Python and Git.
- Seven Python behavior tests: input retry and normalization, one/two-cluster awards, dense ties including every third-rank tie, fewer positive ranks, zero totals, raw-score ranking despite rounded percentages, and balanced/valid question data.
- Six checkpoint scripts execute from a fresh clone and match their documented expected output.
- Each notebook checkpoint cell executes in a fresh Python namespace with simulated answers. All notebook milestone identifiers match the shared mapping. Execution outputs are absent from distributed notebooks.
- A saved learner customization survives switching to a recovery branch and returning to the original named branch.
- Every checkpoint has the same website tree as main. Main has no learner quiz files or completed notebook under workshop.
- Clean release refs have no notes directory or temporary professor-source history. The original private working checkout remains separate from the clean release.
- Both deterministic stepper state tests pass, including assignment/body boundaries, completion, the retained loop variable, and reset.
- Headless Chromium: theme selection and persistence, search results with section labels, both steppers through completion and reset, keyboard Space activation, clipboard code contents, mobile menu navigation at 390px, and no page JavaScript errors.
- Visual review of desktop light/dark views, mobile lesson layout, code highlighting/copy feedback, and all four rendered deck slides. PPTX structural, geometry, font-policy, and re-import checks pass.
- Static link audit: 423 internal links and heading anchors across 13 generated HTML files resolve. The Colab sidebar link and repository/deck links target the planned release refs.
- Humanizer pass over original learner prose and quiz data, including a scan for leftover drafting placeholders and unwanted dash/stock wording.

## Still needs a human or published environment

- Owner coordination before replacing remote main's old history; inspect remote refs again and use an explicit expected-SHA lease for an approved replacement.
- Publication of main and all six checkpoint branches, GitHub Pages settings/deployment, and verification of public checkpoint, deck, and Colab links.
- An actual Google Colab session with Google sign-in and Drive copy/save, and a Windows laptop. Local notebook execution is not a claim of testing Google's UI.
- A timed 70-to-90-minute teaching rehearsal with helpers and a projector. The schedule is a target, not measured classroom timing.
- The earlier workshop slide reference was unavailable; the agreed plans supply the IPO frame and essential-basics requirements.

The default Starlight build emits notices for its empty optional i18n collection and default 404 content fallback. It still generates the 404 page and all lesson routes successfully.
