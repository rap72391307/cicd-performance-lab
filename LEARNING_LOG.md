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
- 2026-08-29: Pull-request CI passed for the default-greeting change. GitHub
  warned that `actions/checkout@v4` and `actions/setup-python@v5` use the
  deprecated Node.js 20 action runtime, so they will be upgraded to `v6`
  (Node.js 24). This action runtime is separate from the Python application
  version used by the tests.
- 2026-08-29: PR #1 ("Add default greeting") squash-merged into `main` as
  `f342e1e`. Local `main` fast-forwarded to match, and the merged
  `feature/default-greeting` branch was deleted both locally and on GitHub.
- 2026-08-29: SSH auth to GitHub failed locally with "Permission denied
  (publickey)" even though the registered key was correct. Root cause: the
  private key (`~/.ssh/id_ed25519_rap72391307`) is passphrase-protected and
  had never been loaded into the macOS ssh-agent, so signing the auth
  challenge silently failed with no TTY available to prompt for it. Fixed by
  running `ssh-add --apple-use-keychain ~/.ssh/id_ed25519_rap72391307` in an
  interactive terminal.

## Lesson 2 — Merging a pull request

### Concepts

- A **pull request (PR)** proposes merging one branch into another and gives
  CI a chance to verify the change before it lands on `main`.
- **Squash and merge** collapses every commit on the feature branch into one
  commit on the target branch — useful when the branch's own history (typos,
  fixups) isn't worth preserving permanently.
- `git fetch` downloads new history from the remote without touching your
  current branch; `git pull` does `fetch` + `merge` in one step.
- A **fast-forward** merge just slides a branch pointer forward with no new
  merge commit, possible only when the local branch has no commits that
  diverged from what's being merged in.

- 2026-08-29: Decided to build the minimal HTTP service with Python's
  built-in `http.server` (zero new dependencies) rather than Flask, to stay
  consistent with the project's minimal-setup philosophy.

## Lesson 3 — Minimal HTTP service

### Concepts

- Keep routing/response logic as a plain function (`handle_request`) separate
  from the code that opens a socket. The plain function is easy to unit test
  with pytest; the socket-handling class (`GreetingHandler`) just calls it.
- `BaseHTTPRequestHandler` / `HTTPServer` are the standard-library building
  blocks for a bare-bones HTTP server — no new dependency needed.
- CI didn't need a workflow change: `python -m pytest` already auto-discovers
  any `test_*.py` file under `tests/`, so a new test file runs on the next
  push/PR for free.

- 2026-08-29: PR #2 ("feat: add minimal HTTP greeting service") passed CI and
  was squash-merged into `main` as `5cb7633`. Local `main` fast-forwarded to
  match, and the `feature/greeting-http-service` branch was deleted locally
  and on GitHub. `python -m pytest` on `main` afterward: `5 passed`.

## Lesson 4 — JMeter load test

### Concepts

- A JMeter Test Plan (`.jmx`, XML) is realistically always built via JMeter's
  GUI rather than hand-typed, unlike the project's Python/YAML files — so it
  was generated directly rather than typed into an editor.
- **Headless mode** (`jmeter -n -t <plan> -l <results>`) runs JMeter from the
  CLI with no GUI — the only mode that works in CI, which has no display.
- In CI, the app under test and JMeter run in the same job: start the app in
  the background, poll it with `curl` until it responds (so JMeter doesn't
  race a server that isn't up yet), run JMeter, then grep the `.jtl` results
  for a `false` success column and fail the build on any hit.
- Generated/output files (`jmeter/results.jtl`, `jmeter.log`) are gitignored
  — only the test plan itself is source.

- 2026-08-30: `jmeter/greet-test.jmx` (2 virtual users x 5 loops against
  `GET /greet?name=Rahul`, with a response assertion) run locally: all 10
  requests succeeded. PR #3 ("Feature/jmeter load test") added the CI steps
  (Java + JMeter install, background app + curl-poll + headless run) and
  passed CI; squash-merged into `main` as `4cce836`. Local `main` synced and
  the `feature/jmeter-load-test` branch deleted locally and on GitHub.
  `python -m pytest` on `main` afterward: `5 passed`.

## Next lesson (do not start yet)

Add LoadRunner Enterprise (LRE) to the pipeline, per the original stack plan.
