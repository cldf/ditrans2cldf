Releasing ditrans2cldf
======================

- Do platform test via tox:
```
tox -r
```

- Make sure flake8 passes:
```
flake8 src
```

- Update the version number, by removing the trailing `.dev0` in:
  - `pyproject.toml`

- Create the release commit:
```shell
git commit -a -m "release <VERSION>"
```

- Create a release tag:
```
git tag -a v<VERSION> -m"<VERSION> release"
```

- Release to PyPI:
```shell
# requires `pip install build twine`
test -d ./dist/ && rm -r ./dist/
python -m build
twine upload ./dist/*
```

- Push to github:
```
git push origin
git push --tags
```

- Increment version number and append `.dev0` to the version number for the new development cycle:
  - `pyproject.toml`

- Commit/push the version change:
```shell
git commit -a -m "bump version for development"
git push origin
```
