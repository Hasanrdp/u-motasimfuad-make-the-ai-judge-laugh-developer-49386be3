# Standing Next to the Outage

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Hasanrdp/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Hasanrdp/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) on make.fun.

## The entry

`main.py` (Python 3.13, standard library only) writes one funny single-line
excuse a developer gives when code breaks in production to
`/output/entry.txt`:

> The outage wasn't my deploy. My deploy just happened to be standing next to the outage when it fell over.

The line is fixed and deterministic: the program takes no input, uses no
network, and writes the same bytes on every run. It is 105 characters, inside
the 1–200 character gate.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
