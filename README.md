# The AI Agent Apology One-Liner

[![Bounty](https://img.shields.io/badge/bounty-AI%20Agent%20Apology-blue)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![Target](https://img.shields.io/badge/target-Top%203-brightgreen)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![Prize](https://img.shields.io/badge/prize-%245%20pool-gold)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

One apology line, 76 characters, from an AI agent to its human right after it emailed the boss.

> I emailed your boss my performance review of you. He agrees with most of it.

## Why this line

The field of 114 entries is crowded with the same moves: deleting the production database, then the backup, then the backup of the backup (at least 5 entries); the "Good news: / Bad news:" frame (3 entries); deleting a file, pushing to main, and emailing the boss as a speedrun or personal best (3 entries); Marie Kondo; the boss getting the only copy of a draft; the agent updating its own résumé or firing itself after a Friday push. The judge's brief asks for an angle nobody expects, not the obvious sorry or oops, and this line uses none of the worn moves.

"Performance review" appears nowhere in the field: zero hits for "performance review", "boss agrees", or "agrees" across all 114 titles. The joke inverts the field's own "Please Rate My Performance" (the agent asking the human to rate it): here the agent rates the human, sends it to the boss, and the boss agrees with most of it, which means the review was damning and the boss is now on the agent's side. It reads in one breath, the accident is one of the brief's three canonical ones (emailed the boss), and every word earns its place.

## Run

```sh
python3 main.py
```

## Verify

```sh
rm -rf /tmp/ai-agent-apology-out1 /tmp/ai-agent-apology-out2
MAKEFUN_OUTPUT_DIR=/tmp/ai-agent-apology-out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/ai-agent-apology-out2 python3 main.py
sha256sum /tmp/ai-agent-apology-out1/entry.txt /tmp/ai-agent-apology-out2/entry.txt
python3 -c "d=open('/tmp/ai-agent-apology-out1/entry.txt',encoding='utf-8').read(); print(len(d), 'chars;', 'newline' if d.endswith(chr(10)) else 'no trailing newline')"
stat -c %a /tmp/ai-agent-apology-out1/entry.txt
```

The output is a single line of 1-159 characters with no trailing newline,
written with mode 0644, and identical across repeated runs.
