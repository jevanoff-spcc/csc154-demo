# Known issues and limitations

Checked against `tracker.py` and the open Issues on 2026-10-21.

## Limitations

- There is no command-line interface yet. Tasks can only be added by calling `add_task` from Python. See [#5](https://github.com/jevanoff-spcc/csc154-demo/issues/5).
- Only `add_task` exists. Listing, completing, editing and deleting tasks are not built. No Issue yet.
- Tasks are kept in memory and are lost when the program stops. No Issue yet.
- Optional due dates are not built. See [#10](https://github.com/jevanoff-spcc/csc154-demo/issues/10), planned for Milestone 2.

## Known bugs

- Leading and trailing spaces are kept in task titles. Fix in review: [#8](https://github.com/jevanoff-spcc/csc154-demo/issues/8) and PR [#9](https://github.com/jevanoff-spcc/csc154-demo/pull/9).
- A blank title returns `None`, so code that uses the result crashes. Fix in review: [#13](https://github.com/jevanoff-spcc/csc154-demo/issues/13) and PR [#14](https://github.com/jevanoff-spcc/csc154-demo/pull/14).
