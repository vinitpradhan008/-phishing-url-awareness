
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for selected phishing warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: URL length
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IP address hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Many hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 50)
    print("EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 50)

    print("Text checks only - this program does not open URLs.")

    # Improvement 1: Check multiple URLs
    while True:
        raw_url = input(
            "\nEnter a sample URL (or q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")

        for item in findings:
            print("- " + item)

        # Improvement 2: Warning summary
        warning_messages = [
            "Contains an @ symbol",
            "Unusually long URL",
            "Uses an IP address",
            "Contains many hostname segments",
            "Contains a punycode-style hostname",
            "Uses HTTP."
        ]

        warning_count = sum(
            any(item.startswith(message) for message in warning_messages)
            for item in findings
        )

        if warning_count > 0:
            print(
                f"\nREVIEW CAREFULLY: {warning_count} warning sign(s) found."
            )

        print("\nNever enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
