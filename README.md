# Authentication Defense Lab

A small Python security lab for comparing a deliberately weak authentication model with a stronger in-memory model that adds password-policy checks, request pacing and temporary IP-based blocking.

> **Scope:** This repository is an educational, local simulation. It does not target a real website, network service or third-party system.

## Purpose

The project is intended to demonstrate a simple defensive idea: authentication security cannot rely on password checking alone. Repeated failed attempts and unusually fast requests can be tracked and used to temporarily block a simulated client.

The implementation is intentionally compact so the behavior is easy to inspect in code.

## Repository structure

- `app_zayif.py` — deliberately weak authentication baseline
- `app_guclu.py` — stronger in-memory authentication model
- `attacker.py` — local attack/simulation driver used to exercise the models
- `veri_tabani.py` — small local credential dataset used by the simulation
- `wordlist.txt` — tiny sample word list

## Implemented controls

`app_guclu.py` currently implements:

- minimum password-complexity checks with regular expressions
- per-IP failed-attempt counters
- a maximum failed-attempt threshold
- temporary IP blocking after the threshold is reached
- a minimum interval between requests that returns a simulated `429 Too Many Requests` result when requests arrive too quickly
- counter reset after a successful login

These controls are implemented as Python objects and in-memory data structures. The project does **not** include a production web server, reverse proxy, WAF or persistent distributed rate limiter.

## Security lessons

The lab illustrates several practical limitations of simple defenses:

- rate limiting based only on request speed can be avoided by slower attempts
- per-process, in-memory counters are not sufficient for a distributed production system
- IP-based blocking alone can create false positives and does not replace MFA, secure password storage, monitoring or broader identity controls
- a string such as `429 Too Many Requests` in this simulation represents application logic; it is not evidence of an actual HTTP gateway or firewall response

## Run locally

```bash
git clone https://github.com/AtakanTas-io/Siber-Proje.git
cd Siber-Proje
python attacker.py
```

Review the scripts before changing scenarios or thresholds.

## Responsible use

Use security-testing code only in environments you own or are explicitly authorized to test. This repository is published for defensive learning and controlled local experimentation.

## Status

Educational lab / prototype. It is intentionally small and is not presented as a production authentication framework.
