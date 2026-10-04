"""Write a Markdown summary of a JUnit XML test report to the GitHub job summary."""

import os
import sys
import xml.etree.ElementTree as ET


def main(report_path):
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    out = open(summary_path, "a") if summary_path else sys.stdout

    if not os.path.exists(report_path):
        out.write(f"### Test results\n\nNo report found at `{report_path}`.\n")
        return

    rows = []
    passed = failed = skipped = 0
    for case in ET.parse(report_path).getroot().iter("testcase"):
        name = f"{case.get('classname')}.{case.get('name')}"
        duration = float(case.get("time", 0))
        if case.find("failure") is not None or case.find("error") is not None:
            status = "❌ Failed"
            failed += 1
        elif case.find("skipped") is not None:
            status = "⏭️ Skipped"
            skipped += 1
        else:
            status = "✅ Passed"
            passed += 1
        rows.append(f"| `{name}` | {status} | {duration:.3f}s |")

    out.write("### Test results\n\n")
    out.write(f"**{passed} passed, {failed} failed, {skipped} skipped**\n\n")
    out.write("| Test | Status | Time |\n|---|---|---|\n")
    out.write("\n".join(rows) + "\n\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pytest-report.xml")
