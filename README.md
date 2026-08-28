# CI/CD Performance Lab

This repository is a hands-on learning project for building a CI/CD pipeline
from zero and later triggering performance tests with Apache JMeter and
LoadRunner Enterprise (LRE).

## Learning path

1. **Source control:** make a small application change and commit it with Git.
2. **Continuous integration (CI):** run automated checks on every change.
3. **Continuous delivery (CD):** package and deploy only changes that passed CI.
4. **Performance testing:** run JMeter in the pipeline and publish its results.
5. **Enterprise performance testing:** trigger an LRE test run and make the
   pipeline wait for its result.

We will build each stage in small, verifiable steps. `LEARNING_LOG.md` is the
durable record of decisions, commands, and discoveries.

## Current lesson

Lesson 1 is setting up Git and creating a tiny Python service with one test.
See the journal for the exact exercise.
