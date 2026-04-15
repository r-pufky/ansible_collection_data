# Data Annotations.
Provide high-resolution, data-centric processing for roles.

Data annotations are data-centric dictionaries to reduce role implementation
complexity through standardized format, context around data use, input
sanitization, and address many shortcomings of argument spec and unit testing.

> Always use a **static** version.

See [Documentation][a] for development setup, requirements, and submission
practices. See Individual role documentation for usage.

[Install from Galaxy][g].

[Related Collections][h].

## Filters

* [v3][j] - Data annotations.
* [dotted2dict][k] - Convert dotted strings to nested dicts.

## Development
Configure [environment][a].

``` bash
# Run all sanity and integration tests.
ansible-galaxy collection build -f
ansible-galaxy collection install -f r_pufky-data-{VERSION}.tar.gz
# Changes require rebuilding, installing, and re-entering test directory.
cd ~/.ansible/collections/ansible_collections/r_pufky/data
ansible-test sanity
ansible-test integration
```

### [Releases][b]

 Release | Debian | Ansible | Notes
---------|--------|---------|-------
 3.x.x   | 13     | 2.20    | Data annotations V3.

## License
[AGPL-3.0 License][c] | [direct link][f]

## Author Information
PGP: [466EEC2B67516C7117C85CE3A0BC35D16698BAB9][d] | [github gist][e]

[a]: https://r-pufky.github.io/ansible_docs
[b]: https://semver.org/spec/v2.0.0
[c]: https://www.tldrlegal.com/license/gnu-affero-general-public-license-v3-agpl-3-0
[d]: https://keys.openpgp.org/vks/v1/by-fingerprint/466EEC2B67516C7117C85CE3A0BC35D16698BAB9
[e]: https://gist.github.com/r-pufky/a8df36977c55b5bb20829267c4c49d22

[f]: https://github.com/r-pufky/ansible_collection_data/blob/main/LICENSE
[g]: https://galaxy.ansible.com/ui/repo/published/r_pufky/data
[h]: https://galaxy.ansible.com/ui/namespaces/r_pufky
[j]: https://github.com/r-pufky/ansible_collection_data/blob/main/plugins/filter/v3.yml
[k]: https://github.com/r-pufky/ansible_collection_data/blob/main/plugins/filter/dotted2dict.yml