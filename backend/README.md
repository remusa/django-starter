# README

## pip-tools

```bash
# compile
pip-compile
pip-compile dev-requirements.in

# install requirements in production stage
pip-sync requirements.txt
# install requirements in development stage
pip-sync requirements.txt dev-requirements.txt
```
