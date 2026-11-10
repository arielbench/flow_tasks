# Flow-cytometry tasks: visualizer

A browsable view of the flow-cytometry evaluation tasks built from archived experimental data:
what each task asks, the answer key, how it is scored, the results, and the full step-by-step trace of every run.

## View it

```bash
git clone git@github.com:arielbench/flow_tasks.git && cd flow_tasks && python3 view.py
```

That's it. It opens the visualizer in your browser (needs only Python 3, no installs). Press **Ctrl+C** in the terminal to stop.
Already cloned? Just run `python3 view.py` from this folder.

## What's inside

- **Start here** – the two task types (A: redo the analysis; B: be the scientist), what they are given, what they hand in, and how they are scored.
- **Results** – scores per task and model, item by item, with heatmaps; FlowKit versions next to the Cytoflow versions.
- **Rubrics** and **What the LLM judge sees** – the scoring items, weights and the exact text the judge receives.
- **Tasks** (left sidebar) – A1–A3 and B1–B4 (Cytoflow GUI versions) and A1_flowkit … B4_flowkit (Python + FlowKit versions). Each task has tabs for the plain-language summary, the exact prompt and inputs, the golden solution, the rubric, and **Traces**.
- **Traces** – one row per run (5 per model per task: Opus 5.5, GPT-6 Astra and Fable 5.2). Each opens a page with every step the system took: what it said, each command, the output, and the screenshots it looked at.

Batches shown: Task A Cytoflow tb6/tb7 (rescored with the 6-item rubric), Task B Cytoflow tb8 (6-item rubric), FlowKit fk1 (Opus 5.5 and GPT-6 Astra, effort xhigh); Fable 5.2 fb1 + fb2 on all tasks (effort high).

## Contents

```
view.py      one-command local viewer
site/        the visualizer (index.html, judge.html) and traces/ (one page per run + screenshots)
```

Confidential: contains experimental data, answer keys and model traces. Keep this repository private.

To refresh after new runs (from the eval workspace): `visualizer/build_traces.py`, `visualizer/build.py`, then
`visualizer/export_site.py <path to this repo>/site`.
