# Ansible Collection - r_pufky.data

Data Annotations.

Provide high-resolution, data-centric processing for roles.

Data annotations are data-centric dictionaries to reduce role implementation
complexity through standardized format, context around data use, input
sanitization, and address many of the shortcomings of argument spec.

[Install from Galaxy](https://galaxy.ansible.com/ui/repo/published/r_pufky/data).

[Data annotations](https://github.com/r-pufky/ansible_collection_data/blob/main/plugins/filter/data.yml)

[dotted2dict](https://github.com/r-pufky/ansible_collection_data/blob/main/plugins/filter/dotted2dict.yml)

## Releases
Release format: **{ANNOTATION}-{MAJOR}-{MINOR}**

Release versions track data annotation versions. Previous data annotation
versions are included in new versions (e.g. a V4 annotation release includes
pre-existing V3 annotations - r_pufky.data.v3, r_pufky.data.v4).

* **[3.x.x](https://github.com/r-pufky/ansible_collection_data)**: V3.

## Development
See [Documentation](https://github.com/r-pufky/ansible_collection_docs) for
development setup, requirements, and submission practices.

Configure [environment](https://github.com/r-pufky/ansible_collection_data/blob/main/docs/dev/environment/README.md)

Run all sanity, integration tests:
``` bash
ansible-galaxy collection build -f
ansible-galaxy collection install -f r_pufky-data-{VERSION}.tar.gz
cd ~/.ansible/collections/ansible_collections/r_pufky/data
ansible-test sanity
ansible-test integration
```
* Changes require rebuilding, installing, and re-entering test directory.

### Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://www.tldrlegal.com/license/gnu-affero-general-public-license-v3-agpl-3-0)
 [(direct link)](https://github.com/r-pufky/ansible_tests/blob/main/LICENSE)

## Author Information
PGP Fingerprint: [466EEC2B67516C7117C85CE3A0BC35D16698BAB9](https://keys.openpgp.org/vks/v1/by-fingerprint/466EEC2B67516C7117C85CE3A0BC35D16698BAB9)
| [github gist](https://gist.github.com/r-pufky/a8df36977c55b5bb20829267c4c49d22)
