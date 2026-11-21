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
## Deploy
Argo CD deploys `k8s/` from `main` (see `argocd/application.yaml`). CI only builds
and publishes the image; to deploy a new version, change the image SHA in
`k8s/deployment.yaml` in a pull request and merge it.

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s` folder.
To roll back, undo the commit that deployed the bad version, with a new commit:

    git log --oneline -- k8s/
    git revert <commit>
    git push

Argo CD deploys the previous version within three minutes. Do not use
`kubectl rollout undo`: self-heal would put the bad version back.
