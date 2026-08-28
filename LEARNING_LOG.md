# CI/CD learning journal

## Goal

Build a CI/CD pipeline that validates an application and can eventually
trigger JMeter and LoadRunner Enterprise (LRE) performance tests.

## Chosen starter stack

| Area | Choice | Why |
| --- | --- | --- |
| Source control | Git + GitHub | Standard foundation for CI/CD workflows |
| CI runner | GitHub Actions | Clear YAML and a free hosted starting point |
| Demo application | Python | Small amount of setup and readable tests |
| Unit tests | pytest | Widely used Python test runner |
| Load testing | Apache JMeter | Can run locally and headlessly in CI |
| Enterprise load testing | LRE | Added once CI and JMeter are working |

## Lesson 1 — Git foundation and a tested application

### Concepts

- A **repository** is a tracked history of a project.
- A **commit** is a named snapshot of a coherent change.
- CI runs checks against commits or pull requests. A pipeline is useful only
  when it can prove a commit is safe enough to move forward.

### Your hands-on exercise

Run these commands from this folder, one at a time. Read the output after each
one; paste any error here rather than trying to work around it blindly.

```bash
git init
git add README.md LEARNING_LOG.md
git commit -m "docs: start CI/CD performance learning lab"
```

If Git asks who you are before it can commit, configure your identity (replace
the values with yours) and retry the commit:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Success check

```bash
git log --oneline -1
git status
```

Expected: one commit appears, and Git reports a clean working tree.

## Findings and decisions

- 2026-08-28: The workspace began empty and was not a Git repository.
- 2026-08-28: We chose GitHub Actions, Python, pytest, JMeter, then LRE as the
  progressive learning stack.
- 2026-08-28: Lesson 1 completed. Initial commit `fc01f32` exists on `main`;
  `git status` confirmed a clean working tree.
- 2026-08-28: Lesson 2 application check completed locally with Python 3.9.6
  and pytest 8.4.2: `1 passed`.
- 2026-08-28: CI workflow committed as `0ed11c3` and the project remote was
  configured with a dedicated SSH identity for GitHub account `rap72391307`.
- 2026-08-28: GitHub Actions CI passed after correcting YAML indentation. The
  successful workflow commit was `8295dee`.

## Next lesson (do not start yet)

Create a minimal HTTP service and a pytest test; then make CI run that test on
every push and pull request.
