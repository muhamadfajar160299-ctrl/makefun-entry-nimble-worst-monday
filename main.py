"""Write one worst-Monday one-liner to entry.txt.

The line is embedded below and written verbatim to the output
directory (MAKEFUN_OUTPUT_DIR, default /output). The program writes
exactly one line, at most 140 characters, and refuses to write an
empty line: an empty or whitespace-only line raises instead of
producing an invalid entry.
"""

import os

LINE = "Monday: I fixed the bug I shipped on Friday, then stand-up asked me to explain in one sentence why Monday keeps happening to me."

def main():
    if not LINE or not LINE.strip():
        raise ValueError("entry line must not be empty")
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError as exc:
        raise RuntimeError("could not write entry.txt: %s" % exc) from exc

if __name__ == "__main__":
    main()
