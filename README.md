# Slug Generator

## What it does
A small HTTP service that turns text into URL slugs, with Cyrillic
transliteration (`Актау Город` -> `aktau-gorod`).

## Run
    ./scripts/run.sh

Listens on port 8080 by default. Set the `PORT` environment variable to change it.

## Test
    ./scripts/test.sh

Prints `TESTS: n/n`.

## Endpoints
- `GET /healthz` returns 200
- `GET /slug?text=Hello World` returns `hello-world`