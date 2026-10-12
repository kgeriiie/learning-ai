# Rollback & Failover Plan

Every push to `main` that passes CI publishes a multi-arch image (`linux/amd64`, `linux/arm64`) to GHCR, tagged with the full commit SHA and `latest`:

```
ghcr.io/kgeriiie/learning-ai:<commit-sha>
```

SHA tags are immutable, so rolling back means running an earlier SHA. Nothing is rebuilt. **Never roll back via `latest`**: it always points at the newest build.

## When to roll back

- `/ask` returns errors, empty answers or clearly wrong answers after a deploy.
- The container exits or restarts repeatedly (`docker ps -a`, `docker logs rag`).
- `/health` (once available) or `/hello` is not responding or returns unexpected content.
- CI was green but the running service misbehaves (tests do not cover model quality).

If the cause is a stopped Ollama rather than the new version, see *Failover* below. Do not roll back for that.

## Finding the last good version

1. `git log --oneline` shows the commits. Pick the commit before the faulty change.
2. Open the Actions tab and confirm that commit's run was green and its `docker-build` job published an image.
3. Get the full 40-character SHA (`git rev-parse <short-sha>`). It must match a tag under the repo's **Packages**.

Images built before the multi-arch change (commit `9d8c77b`) are `amd64` only and will not start on an Apple Silicon Mac.

## Rollback procedure

```bash
docker stop rag && docker rm rag

docker run --name rag -p 8000:8000 \
  -e OLLAMA_API_BASE=http://host.docker.internal:11434 \
  -v <abs-path>/document_mcp/clean_code.pdf:/app/document_mcp/clean_code.pdf:ro \
  ghcr.io/kgeriiie/learning-ai:<previous-good-sha>
```

The PDF is mounted at runtime and is not part of the image. The path must match the one used by the service.

## Verifying the rollback

1. `docker logs -f rag` ends with `Uvicorn running on http://0.0.0.0:8000` and shows no tracebacks.
2. `GET /hello` returns the response of the restored version.
3. `POST /ask` with a known question (for example "What is single responsibility?") returns a non-empty answer with `success: true`.
4. Note the incident and the bad SHA, then fix forward on `main`. Do not rewrite history.

## Failover: Ollama unavailable

The LLM runs in a local Ollama instance outside the container (`OLLAMA_API_BASE`). If it is down or unreachable:

- The service retries with exponential backoff (1s, 2s, 4s, 8s), then returns `success: false` with an empty answer after the last attempt. The retries and the failure are visible in the logs.
- Check that Ollama is running (`ollama list`) and that the container can reach it (`host.docker.internal:11434` on macOS Docker Desktop).
- Restart Ollama and retry the request. No redeploy or rollback is needed.

Known limitations: there is no secondary LLM backend, so while Ollama is down the `/ask` endpoints are degraded. A fallback model or hosted provider would be the next step.

## Housekeeping

- Keep at least the last few SHA images in GHCR so a rollback target always exists. If an automatic cleanup is added later, it must never delete them.
- Delete the personal access token used for `docker login` once it is no longer needed.
