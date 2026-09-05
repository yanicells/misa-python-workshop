# Release preparation

The release builder creates a new repository with a clean root commit and six runnable checkpoint branches. It does not rewrite or push the source checkout. The existing remote originally had professor material in its history; deleting files in a normal commit would leave that history reachable.

## Build and verify locally

From the implementation repository root, choose a new destination outside it:

```bash
python3 facilitator/prepare_release.py ../misa-release
cd ../misa-release
python3 facilitator/verify_release.py
cd web
npm ci
npm run check
npm run build
```

Use Node.js 24 or newer for the website. Python 3.10 or newer runs the workshop and release checks. The generator uses `checkpoints.json` to update both READMEs and creates each checkpoint from the same finalized main baseline. The notebook on a checkpoint contains only the milestones up to that checkpoint. The final notebook contains them all.

## Coordinate remote replacement

Before replacing main, get the repository owner's approval and check the current remote heads and tags. The inspected remote main was `fa8af1443303a03c22194dabfd6dc1ea7cc7b461`, with no other advertised heads or tags. Recheck before acting; if it changed, review and preserve the new work before rebuilding the clean baseline.

Use an explicit expected-SHA lease for any approved main replacement. Do not use a blind force push. Publish the six checkpoint refs from the clean repository together with main, then verify remote refs and test a fresh remote clone. Do not push the original source checkout or a backup ref containing the temporary notes. Keep any private backup outside the published repository.

Changing main's ancestry affects existing clones. Tell collaborators to preserve their work before they fetch and reconcile with the clean history. A ref rewrite removes the old material from reachable public branches, but it may not erase cached GitHub pages, forks, or already downloaded copies. If full removal of sensitive material is required, follow GitHub's sensitive-data removal process with the repository owner.

GitHub Pages uses the committed Actions workflow and main only. Enable GitHub Actions as the Pages source. Verify production routes, search, assets, Colab, and all checkpoint links after publication. The website URL in the guide is the expected Pages URL, not proof of deployment.

## Before workshop day

Record a timed rehearsal with an actual beginner/helper. Check supported Windows and macOS commands on real laptops and a real Colab runtime. Check projector readability. Automated execution verifies code and notebook cell equivalence, not classroom pacing or Google sign-in.
