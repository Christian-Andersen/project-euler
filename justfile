set dotenv-load

alias c := check

[private]
default:
    @just --list

check:
    uv run -- prek run --all-files

audit:
    uv run -- prek run audit

ci:
    uv run -- prek run --all-files --stage manual
