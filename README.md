# orbit-api

A FastAPI service, scaffolded with [Protostar](https://github.com/JacksonFergusonDev/protostar).

Run it with `uv run orbit-api`, then open <http://127.0.0.1:8000/health>.

## About this example

This project was created from the [`service` template](https://github.com/JacksonFergusonDev/protostar-example-templates/tree/main/service) with:

```bash
protostar init --from https://github.com/JacksonFergusonDev/protostar-example-templates/tree/v1.0.0/service \
  --tier production --option database=postgres --var SERVICE_PORT=8000
```

[`.github/workflows/protostar-sync.yml`](.github/workflows/protostar-sync.yml) runs `protostar sync --to latest` every week, using the Protostar release recorded in `protostar.lock`, and opens a pull request when the template has a new release. See [Automating Updates](https://protostar.jacksonferguson.me/usage/automating-updates/).
