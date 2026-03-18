# Control Flow & Operators — Assignment

---

## Problem 1 — Transaction Aggregator & Anomaly Detector

Context
: You receive a chronological stream of financial transactions for multiple accounts. Each transaction is represented as a line in a text block with an account identifier and an amount separated by whitespace. Positive amounts are credits, negative amounts are debits.

Task
: Implement a function `aggregate_transactions(transactions_text)` that:
- Aggregates total balance change per `account_id` (sum of amounts).
- Detects accounts with an anomalous single debit that exceeds 50% of the absolute value of that account's total debits (i.e., an unusually large single withdrawal).

Input
: `transactions_text` — a multi-line string where each line is of the form: `account_id amount` (for example: `acct-1 120.0` or `acct-2 -50.0`). Lines may be separated by newlines.

Output
: A tuple `(balances, anomalies)` where:
- `balances` is a dict mapping account_id -> float (net balance change).
- `anomalies` is a list of account_id values that meet the anomaly condition.

Constraints & Notes
- A single-pass algorithm using loops is sufficient.
- If an account has no debits, it cannot be flagged as anomalous.
- Do not use external libraries.

Example

Input text:

```text
transactions_text = """
acct-1 120.0
acct-2 -50.0
acct-1 -20.0
acct-2 -150.0
acct-1 -10.0
"""
```

Output:

```text
(
    {"acct-1": 90.0, "acct-2": -200.0},
    ["acct-2"]
)
```

Acceptance criteria
- Correct totals per account.
- `acct-2` flagged because a single debit (-150.0) > 50% of total debits (|-200.0| * 0.5 = 100.0).

Hints
- Use a dict for running totals and another for tracking total debits and maximum single debit magnitude.
- Use `abs()` when comparing debit magnitudes.
- Use string methods and simple splitting to parse the input text.

---

## Problem 2 — Log Level Summary

Context
: You have an in-memory log represented as a block of text. Each log line starts with a level token like `INFO`, `WARN`, `ERROR`, or `DEBUG`, followed by a colon and a message.

Task
: Implement `summarize_logs(log_text)` that returns a dict with counts per level and a list of the first 3 unique ERROR messages (in order of appearance).

Input
: `log_text` — a multi-line string where each line is `LEVEL: message` (for example `ERROR: Disk full`).

Output
: `{"counts": {level: int, ...}, "first_errors": [str, ...]}`

Constraints
- Recognize levels: INFO, WARN, ERROR, DEBUG (case-sensitive). Lines that don't start with one of these should be ignored.
- `first_errors` must contain distinct messages only (no duplicates), up to 3.
- Use loops and conditionals; do not rely on collections helper utilities.

Example

Input text:

```text
log_text = """
INFO: Starting job
ERROR: Disk full
WARN: High memory usage
ERROR: Disk full
ERROR: Network timeout
DEBUG: Verbose output
ERROR: Permission denied
"""
```

Output:

```text
{
  "counts": {"INFO": 1, "ERROR": 4, "WARN": 1, "DEBUG": 1},
  "first_errors": ["Disk full", "Network timeout", "Permission denied"]
}
```

Hints
- Use `str.split(':', 1)` to separate level and message.
- Normalize spacing on messages with `.strip()`.
- Iterate through each line in the text using simple loops.

---

## Problem 3 — Prime Gaps Scanner

Context
: For performance-sensitive checks you must avoid expensive operations inside nested loops where possible.

Task
: Implement `first_prime_gap(n, gap)` that finds the first pair of consecutive prime numbers (p1, p2) such that p2 - p1 == gap and p2 <= n. Return the tuple `(p1, p2)` or `None` if not found.

Input
: `n` (int, n >= 2), `gap` (int, gap >= 2)

Output
: `(p1, p2)` or `None`.

Constraints & Hints
- Use simple primality test (trial division up to sqrt) inside a loop and reuse results where possible.
- Efficient looping and early continues/breaks will be evaluated.

Example

```text
first_prime_gap(50, 6)  # -> (23, 29)
```

---

## Problem 4 — Robust Retry with Exponential Backoff (simulation)

Context
: You are writing a retry mechanism for an unstable external call. We will simulate attempts using a simple sequence encoded as text where each token represents success or failure.

Task
: Implement `attempt_with_backoff(attempts_text, max_attempts, base_backoff)` where `attempts_text` is a whitespace- or newline-separated sequence of tokens `1` (success) or `0` (failure). The function should:
- Read tokens from `attempts_text` in order to simulate consecutive attempts.
- Stop and return `True` immediately on the first success token (`1`).
- If an attempt fails (`0`), increment an attempt counter and compute simulated backoff as `base_backoff * (2 ** (attempt_count - 1))` seconds.
- Stop and return `False` if `max_attempts` is reached or there are no more tokens.

Output
: A tuple `(result: bool, attempts_made: int, total_backoff_seconds: int)`.

Example

If `attempts_text` is `"0 0 1"` with `max_attempts=5`, `base_backoff=1`, result should be `(True, 3, 3)` because backoffs were 1 and 2 seconds (total 3) before succeeding on attempt 3.

Hints
- Use a `while` loop and simple token iteration using string splitting.
- Use `continue` to skip unnecessary work on immediate success/failure checks.

---

## Testing & Submission

- Implement each problem as a pure function in a `.py` file under `learning/control_flow/` (suggested filename: `assignments.py`).
- Include `if __name__ == "__main__"` examples or a small test harness demonstrating the sample inputs and outputs.
- Prefer small, focused helper functions where useful.

Grading checklist (automated tests will check these):
- Correctness on sample inputs (required).
- Reasonable efficiency (no obviously quadratic waste where a linear solution is expected).
- Clear docstrings and readable code.

---

If you'd like, I can also create a starter `assignments.py` with function skeletons and basic unit tests to get you started. Tell me if you want that and I will add it to the same folder.
