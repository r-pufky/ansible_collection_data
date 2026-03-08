# Data Annotations.
Provide high-resolution, data-centric processing for roles.

Data annotations are data-centric dictionaries to reduce role implementation
complexity through standardized format, context around data use, input
sanitization, and address many shortcomings of argument spec and unit testing.

See [Documentation](https://r-pufky.github.io/ansible_docs) for development
setup, requirements, and submission practices. See Individual role
documentation for usage.

[Install from Galaxy](https://galaxy.ansible.com/ui/repo/published/r_pufky/data).

[Related Collections](https://galaxy.ansible.com/ui/namespaces/r_pufky).

## Filters

* [v3](https://github.com/r-pufky/ansible_collection_data/blob/main/plugins/filter/v3.yml) - Data annotations.
* [dotted2dict](https://github.com/r-pufky/ansible_collection_data/blob/main/plugins/filter/dotted2dict.yml) - Convert dotted strings to nested dicts.

## Development
Configure [environment](https://r-pufky.github.io/ansible_docs/ansible/environment)

Run all sanity and integration tests:
``` bash
ansible-galaxy collection build -f
ansible-galaxy collection install -f r_pufky-data-{VERSION}.tar.gz
cd ~/.ansible/collections/ansible_collections/r_pufky/data
ansible-test sanity
ansible-test integration
```
* Changes require rebuilding, installing, and re-entering test directory.

## [Versions](https://semver.org/spec/v2.0.0)

 Release | Debian | Ansible | Notes
---------|--------|---------|-------
 3.x.x   | 13     | 2.18    | Data annotations V3.

### Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://www.tldrlegal.com/license/gnu-affero-general-public-license-v3-agpl-3-0)
 [(direct link)](https://github.com/r-pufky/ansible_tests/blob/main/LICENSE)

## Author Information
PGP Fingerprint: [466EEC2B67516C7117C85CE3A0BC35D16698BAB9](https://keys.openpgp.org/vks/v1/by-fingerprint/466EEC2B67516C7117C85CE3A0BC35D16698BAB9)
| [github gist](https://gist.github.com/r-pufky/a8df36977c55b5bb20829267c4c49d22)
