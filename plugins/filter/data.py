# Copyright: (c) 2025, Robert Pufky <rpufky@gmail.com>
# GNU Affero General Public License v3 (see COPYING or https://www.gnu.org/licenses/agpl-3.0.txt)

''' Data annotations for ansible. '''


from __future__ import annotations

import typing

from ansible.errors import AnsibleFilterError


class FilterModule():
    """ Data Annotation Filters """

    def filters(self):
        return {
            'v3': self.v3_data_annotation,
            'dotted2dict': self.dotted_to_dict
        }

    def v3_data_annotation(
        self,
        annotation: dict,
        section: str = None,
        key: str = None,
        raw: typing.Any = None,
        data: typing.Any = None,
        nested_data: bool = False,
        default: typing.Any = None,
        hint: str = None,
        added: str = '0.0.0',
        sensitive: bool = False,
        deprecated: bool = False,
        keep: bool = True,
        comment: str = None,
        docstring: str = None,
        order: int = 0,
        **kwargs: typing.Any
    ) -> dict:
        '''
        Data Annotation V3.

        Annotate user supplied data with context for easier role processing.

        Args:
            annotation (dict): Data annotation dict.
            section (str): Section name. Default: ''.
            key (str): Config file key. Default: ''.
            raw: (any): Raw value from user, defaults, or role defaults.
                Default: ''.
            data: (any): Processed raw value for use in rendering. Optional.
                Default: ''.
            nested_data (bool): Create a nested dictionary using annotated data
                with dotted2dict stored in dict.nested_data:
                * "data" used for value if both "raw" and "data" are defined.
                * "keep=true" always constructs dict even with default values.
                * "keep=false" constructs dict when "raw" != "default" value.
                Otherwise returns empty dict. Default: False.
            default: (any): Role default value (testing for changed defaults).
                Default: ''.
            hint (str): Value rendering type hint (docstring types).
                Default: ''.
            role_* (any): Role specific usage. Optional.
            added (str): Release version variable added.
                Special Case:
                  0.0.0: Unknown or since role inception.
                Default: '0.0.0'.
            sensitive (bool): True for PII/SPII data that should not be logged.
                Default: False.
            deprecated (bool): True if no longer used in current role release.
                Default: False.
            keep (bool): True if data should be written to configuration
                file. Default: True.
            comment (str): Internal use comment. Default: ''.
            docstring (str): User visible documentation. Default: ''.
            order (int): Order item should appear in templated files.
                Default: 0.
            **kwargs (any): Additional data annotation attributes to set. Keys
                should be prefixed with '_'.

        Returns:
            dict: Data annotation V2 dict with defaults created.
        '''
        result = annotation
        if (kwargs is not None and not all(key.startswith('_') for key in kwargs)):
            raise AnsibleFilterError(
                'r_pufky.data.v2: additional data annotations require keys '
                'prefixed with _.\n\n'
                'e.g. r_pufky.data.v2(..., _dest="/tmp")\n\n'
                f'Received kwargs: {kwargs.keys()}'
            )
        result.update(kwargs)
        result.update({
            'section': section if section is not None else '',
            'key': key if key is not None else '',
            'raw': raw if raw is not None else '',
            'data': data if data is not None else '',
            'nested_data': {},
            'default': default if default is not None else '',
            'hint': hint if hint is not None else 'str',
            'added': added if added is not None else '0.0.0',
            'sensitive': sensitive if sensitive is not None else False,
            'deprecated': deprecated if deprecated is not None else False,
            'keep': keep if keep is not None else True,
            'comment': comment if comment is not None else '',
            'docstring': docstring if docstring is not None else '',
            'order': order if order is not None else 0
        })
        if nested_data:
            value = result['raw'] if not data else result['data']
            if result['raw'] == result['default'] and not keep:
                result.update({'nested_data': {}})
            else:
                result.update({
                    'nested_data': self.dotted_to_dict(
                        '.'.join([result['section'], result['key']]),
                        value
                    )}
                )
        return result

    def dotted_to_dict(
        self,
        dotted: str,
        data: typing.Any,
    ) -> dict:
        '''
        Return nested dictionary generated based on dotted notation.

        data_annotation: 'root_section.nested.subsection.key'

        data_annotation | r_pufky.lib.dotted2dict(data='my value'):

            result:
                root_section:
                    nested:
                        subsection:
                            key: 'my value'

        Args:
            dotted (str): Dotted string notation to nest.
            data (any): Value to set for final key.

        Raises:
            AnsibleFilterError: Input filter data is invalid.

        Returns:
          dict: Nested dict with value mapped.
        '''
        result = {}
        if dotted is None or data is None:
            raise AnsibleFilterError(
                'dotted2dict: requires dotted string and data set:'
                '  "example.key.str" | r_pufky.lib.dotted2dict(data="value")'
            )

        process_dict = result
        parts = dotted.split('.')
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                process_dict[part] = data
            else:
                process_dict = process_dict.setdefault(part, {})
        return result
