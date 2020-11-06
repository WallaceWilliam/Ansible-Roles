__author__ = 'WallaceWilliam'

import re
#from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text

class FilterModule(object):
    ''' Custom filters are loaded by FilterModule objects '''

    def filters(self):
        ''' Filter Module objects return a dict mapping filter names to filter functions. '''
        return {
            'regex_search_groupdict': self.regex_search_groupdict,
            'list_regex_search_groupdict': self.list_regex_search_groupdict,
        }

    def regex_search_groupdict(self, value, regex, *args, **kwargs):
        ''' Perform re.search and return the list of matches or a backref '''

        value = to_text(value, errors='surrogate_or_strict', nonstring='simplerepr')

        flags = 0
        if kwargs.get('ignorecase'):
             flags |= re.I
        if kwargs.get('multiline'):
             flags |= re.M

        match = re.search(regex, value, flags)
        if match:
            return match.groupdict()
        return {}

    def list_regex_search_groupdict(self, lines, regex, *args, **kwargs):
        ''' Perform re.search and return the list of matches or a backref '''
        ret = list()
        for value in lines:
            match = self.regex_search_groupdict(value, regex, *args, **kwargs)
            if match:
                ret.append(match)
        return ret

