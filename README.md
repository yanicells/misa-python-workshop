# MISA Python workshop

Build a MISA cluster personality quiz with Python and Git. This workshop is for first-year BS MIS students starting programming.

[Website source](web/) · [Setup and Colab](web/src/content/docs/setup.mdx) · [Recovery](web/src/content/docs/checkpoints.mdx)

## Get started

```bash
git clone https://github.com/yanicells/misa-python-workshop.git
cd misa-python-workshop
git checkout 00-start
git checkout -b my-quiz
cd workshop
```

Run `python3 quiz.py` on macOS or `py quiz.py` on Windows. You should see `Your MISA quiz starts here.` You need Python 3.10 or newer and Git. Students do not need Node.js.

`main` contains the guide and website examples. The learner files start on `00-start`; the finished quiz is on `05-results`. Stay on your own branch as you edit. Save and commit your work before using a reference checkpoint.

<!-- CHECKPOINTS:START -->
| Checkpoint | Lesson |
| --- | --- |
| [00-start](https://github.com/yanicells/misa-python-workshop/tree/00-start/workshop) | [Guide](web/src/content/docs/setup.mdx) |
| [01-welcome](https://github.com/yanicells/misa-python-workshop/tree/01-welcome/workshop) | [Guide](web/src/content/docs/build/welcome.mdx) |
| [02-question](https://github.com/yanicells/misa-python-workshop/tree/02-question/workshop) | [Guide](web/src/content/docs/build/question.mdx) |
| [03-loops](https://github.com/yanicells/misa-python-workshop/tree/03-loops/workshop) | [Guide](web/src/content/docs/build/loops.mdx) |
| [04-functions](https://github.com/yanicells/misa-python-workshop/tree/04-functions/workshop) | [Guide](web/src/content/docs/build/functions.mdx) |
| [05-results](https://github.com/yanicells/misa-python-workshop/tree/05-results/workshop) | [Guide](web/src/content/docs/build/results.mdx) |
<!-- CHECKPOINTS:END -->

[Open the matching notebook in Colab](https://colab.research.google.com/github/yanicells/misa-python-workshop/blob/05-results/workshop/misa-quiz.ipynb) and save a copy in Drive. It follows the same Python milestones without local Git setup.

## Work on the website

Use Node.js 24 or newer:

```bash
cd web
npm ci
npm run dev
npm run check
npm run build
```

The Markdown and MDX lessons are under `web/src/content/docs`. `web/src/examples` holds text sources displayed as instructional code and used to generate checkpoints; students edit only `workshop` files. `checkpoints.json` defines checkpoint names, routes, files, run commands, and expected behavior.

The workshop website is intended for Vercel, but this repository does not deploy it automatically. Yani will connect and deploy the project separately. When that happens, use `web` as the Vercel project root and add the final public URL to these guides.
