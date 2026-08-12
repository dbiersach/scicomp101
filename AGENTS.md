# SCICOMP101 Python and Jupyter Notebook Style Guide

These instructions define the expected coding and documentation style for all Python scripts (`.py`) and Jupyter notebooks (`.ipynb`) in this repository.

The goal is clarity, consistency, and strong pedagogical value.

---

## General Principles

- Code should be **clear, explicit, and readable**.
- Prefer **teaching-oriented explanations** over compact or clever code.
- Write as if the reader is a **student learning the concept for the first time**.
- Avoid unnecessary abstraction unless it improves understanding.

---

## File Naming

- Use lowercase `snake_case` for all files.
- File names should be **descriptive and topic-based**.

Examples:

- `continued_fractions.ipynb`
- `conic_sections.py`
- `scicomp101_utils.py`

---

## Jupyter Notebook Structure

### First Code Cell

The first code cell must begin with a short docstring containing the notebook filename:

```python
"""example_notebook.ipynb"""
```

If the notebook imports matplotlib anywhere, an inline backend must be
selected after the docstring and the cell-label comment, before any import:

```python
"""example_notebook.ipynb"""

# Cell 01 - Import packages

%matplotlib inline

import matplotlib.pyplot as plt
```

This is required, not optional, and it must be in the **first** code cell so
that it runs before any plot is made. Without it the kernel inherits the
venv's `qtagg` backend, `plt.show()` opens a window that blocks the kernel,
and the cell spins forever. A notebook that needs a live animation uses
`%matplotlib widget` instead. `nb_check.py` enforces this, and
`githooks/pre-commit` refuses a commit that violates it.

---

### Cell Labeling

Each code cell should be labeled with a structured comment:

```python
# Cell 01 - Import packages
# Cell 02 - Define helper functions
# Cell 03 - Run simulation
```

Guidelines:

- Use two-digit numbering (`01`, `02`, etc.)
- Keep descriptions short and meaningful

---

### Markdown Cell Structure

Every markdown cell after the first one in a notebook must begin with a
horizontal rule on its own line, followed by a `###` header:

```markdown
---
### Setup: simulation parameters

The simulation runs from ...
```

The rule draws a visible line between the cell and the output of the code cell
above it, which otherwise run together in the notebook view.

Header rules:

- Start at `###`. Never use `#` or `##`, which render so large that a short
  heading eats a disproportionate amount of vertical space.
- `###` is the only level used for section headers. Sub-points inside a section
  are made with bold lead-ins or lists, not `####`.
- The very first cell of the notebook is the only exception to the rule: it
  opens directly with its `###` title, since there is no output above it to
  separate.
- A markdown cell that follows another markdown cell still takes the rule. The
  separator doubles as a section break, so it stays even where there is no code
  output above it.

Do not open a markdown cell with a bolded run-in sentence such as
`**Simulation parameters.**`. Write a real `###` header instead.

---

### Every Code Cell Must Display Output

Never write a code cell that produces no visible output. A cell containing
only imports, constants, or function definitions gives the student no feedback
that they ran it. It is easy to skip a silent cell and then hit a `NameError`
in the next one.

When a cell exists mainly to define things, end it with a short check that
exercises what was just defined. Call the new functions on a simple case and
`print()` or `display()` the result next to the expected answer:

```python
# Quick check that the convergent matches the known value
p, q = convergent(golden_ratio_cf, 10)
print(f"convergent 10 = {p}/{q} = {p / q:.6f}  (expected 1.618034)")
```

This doubles as a worked example and as proof the cell ran.

Stale saved output is the related hazard. A cell whose code was edited but
never rerun still shows its old result, which reads as if it passed. Rerun
the notebook after editing it.

---

### Markdown + Code Balance

- Use markdown cells to explain:
  - What the code does
  - Why the method is used
  - What the results mean
- Keep explanations **plain, direct, and instructional**
- Avoid overly formal or verbose writing

---

## Python Code Style

### Type Hints

- Use type hints for all reusable functions and classes
- Prefer modern Python 3.14 syntax:

```python
float | np.ndarray
list[str]
tuple[np.ndarray, ...]
```

---

### Docstrings

- Use **NumPy-style docstrings** for reusable functions in `.py` files

Example:

```python
def compute_energy(x: np.ndarray) -> float:
    """
    Compute the total energy of the system.

    Parameters
    ----------
    x : np.ndarray
        Input state vector.

    Returns
    -------
    float
        Computed energy value.
    """
```

- Short helper functions may use one-line docstrings:

```python
def square(x: float) -> float:
    """Return x squared."""
```

---

## Imports

Use standard aliases:

```python
import numpy as np
import matplotlib.pyplot as plt
```

---

## Comments and Writing Style

- Comments must be **functional and explanatory**
- Focus on:
  - Purpose of the code
  - Mathematical meaning
  - Instructions to the reader/student

### Avoid

- Decorative or stylistic comments
- Redundant comments that restate obvious code
- Em dashes or long dashes

Instead:

- Use normal hyphens `-`
- Or rewrite the sentence for clarity

---

## American English Only

Use American spelling everywhere you write prose or identifiers: comments,
docstrings, markdown cells, variable and function names, plot titles, axis
labels, and printed output. British spellings are treated as errors, and the
workspace spell checker flags them.

The differences that come up most often:

| Use | Not |
| --- | --- |
| color, coloring, colored | colour, colouring, coloured |
| behavior, favor, labor | behaviour, favour, labour |
| center, meter, liter, fiber | centre, metre, litre, fibre |
| normalize, initialize, analyze | normalise, initialise, analyse |
| labeled, labeling, modeled | labelled, labelling, modelled |
| gray | grey |
| license, defense | licence, defence |

This applies to text **you** write. Do not rewrite British spellings that are
already inside third-party data files, quoted sources, proper nouns, or library
APIs. Data files carrying Wikipedia text with "aluminium" and "colourless" in
them, and organization names like "GSI Helmholtz Centre", stay exactly as they
are.

---

## Notebook Teaching Style

When writing notebooks:

- Break work into logical steps
- Explain transitions between steps
- Clearly interpret results

Good pattern:

1. Introduce concept
2. Show implementation
3. Run code
4. Interpret output

---

## Environment Notes

These are properties of the development machine, not style rules.

### Force the inline matplotlib backend in notebooks

The venv's default backend is `qtagg`, because PySide6 and PyQt6 are installed
so that standalone `.py` scripts can open an interactive plot window. That
default is wrong inside a Jupyter kernel: `plt.show()` opens a Qt window that
blocks the kernel, and the cell never returns.

Two layers guard against this, and both should stay in place:

- Every notebook that imports matplotlib puts `%matplotlib inline` in its
  first code cell, right after the docstring and cell-label comment. This
  travels with the `.ipynb` file, so it works for students on any machine.
- `nb_check.py` enforces that rule, so a notebook cannot quietly ship
  without it. `githooks/pre-commit` runs the check against staged
  notebooks and refuses the commit if one is missing the magic. Register
  the hook directory once per clone:

      git config core.hooksPath githooks

  Run the same check over the whole repository at any time with
  `uv run --no-project python nb_check.py`.

A VS Code setting cannot serve as the backstop here. `jupyter.runStartupCommands`
is declared by the Jupyter extension with `"scope": "application"`, which means
VS Code reads it only from user settings and ignores it in a workspace or folder
file, where it renders grayed out.

Standalone scripts are unaffected and keep their interactive Qt window. A
notebook that genuinely needs a live animation uses `%matplotlib widget`
instead, never the Qt backend.

---

## Reference Material Loaded On Demand

Two longer references are skills under `.claude/skills/`, so Claude Code loads
them only when the task calls for them instead of on every session. Other tools
should read the files directly.

- `.claude/skills/office-latex/SKILL.md` - Office-compatible LaTeX for the
  Microsoft 365 Equation Editor (PowerPoint and Word), including Dirac
  bra-ket notation.
- `.claude/skills/machine-environment-notes/SKILL.md` - diagnosing a notebook
  cell that hangs or never finishes, clearing orphaned kernel processes,
  reloading VS Code after a `uv sync`, and why quantum chemistry packages
  cannot be installed on this machine.
