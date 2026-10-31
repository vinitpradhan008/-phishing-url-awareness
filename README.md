
# EWB Phishing URL Awareness Checker

## Overview

Phishing is a cyber attack where attackers use fake links
or messages to steal personal information.

This Python project checks URL text for selected phishing
warning signs. It is designed for beginner cybersecurity
learning.

## Features

- Detects @ symbols in URLs.
- Detects unusually long URLs.
- Detects IP address hostnames.
- Detects multiple hostname segments.
- Detects punycode-style hostnames.
- Detects HTTP scheme.
- Supports checking multiple URLs.
- Displays a warning summary.
- Handles malformed URL input.

## Requirements

- Python 3.10 or later.
- No additional Python packages required.

## How to Run

Windows:

python phishing_checker.py

Mac/Linux:

python3 phishing_checker.py

## Example Input

http://192.0.2.10/account

## Example Output

Uses an IP address instead of a familiar domain.
Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.

## Testing

Five sample URLs are tested.

See tests/test_samples.md for the testing table.

## Screenshots

![Sample Run](screenshots/sample_run.png)

![Test Results](screenshots/test_results.png)

## Improvements

1. Added a loop to check multiple URLs without restarting.
2. Added a warning summary to show the number of warning signs.

## Limitations

This is an educational tool.

It only reads URL text. It does not visit websites,
scan for malware or prove that a URL is safe.

No warning signs found does NOT mean a URL is safe.

## Ethical Use

- Use sample URLs only.
- Never collect passwords or credentials.
- Do not scan websites without permission.
- Use this project for defensive cybersecurity learning.

## Author

Name: [Your Name]

Course: EWB Cybersecurity Mini Project
