"""String checks for the Why Topfaith page in index.html. Run: python3 -I docs/superpowers/plans/check_why.py"""
import pathlib, re, sys

s = (pathlib.Path(__file__).resolve().parents[3] / "index.html").read_text()
fails = []
def check(cond, msg):
    if not cond: fails.append(msg)

check('id="tpl-Why"' in s, "tpl-Why template missing")
check('"Why": {"id": "why"' in s, "ROUTES entry missing")
check('<option value="why">' in s, "Jump-to option missing")
check(re.search(r'<a href="Why\.dc\.html" style="color: #B9C3CB[^>]*>Why Topfaith</a>', s), "footer link missing")
check(re.search(r'<a href="Why\.dc\.html"[^>]*>Read all 25</a>', s), '"Read all 25" not pointing at Why')
check('1:7' not in s, "1:7 ratio still present")
m = re.search(r'REG\["Why"\] = \(function\(\)\{(.*?)return Component;\}\)\(\);', s, re.S)
check(m, 'REG["Why"] missing')
if m:
    block = m.group(1)
    check(len(re.findall(r"^\s*'[^']+',?\s*$", block, re.M)) == 25, "expected 25 reason strings")
    for gid in ("teaching", "care", "campus", "values"):
        check(f"id: '{gid}'" in block, f"group {gid} missing")
    check("1:8" in block, "1:8 ratio missing from reasons")

print("\n".join(fails) or "PASS: all checks")
sys.exit(1 if fails else 0)
