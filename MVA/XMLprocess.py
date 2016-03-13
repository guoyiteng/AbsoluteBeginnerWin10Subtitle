import srt

class DefaultSaxHandler(object):
    def __init__(self):
        self._subs = []
        self._subIdx = -1
    def start_element(self, name, attrs):
        if name == 'p':
            subLine = {'start': srt.srt_timestamp_to_timedelta(dict(attrs)['begin'].replace('.', ',')),
                       'end': srt.srt_timestamp_to_timedelta(dict(attrs)['end'].replace('.', ',')),
                       'content': ''}
            self._subs.append(subLine)
            self._subIdx += 1

    def char_data(self, text):
        if self._subIdx > -1:
            self._subs[self._subIdx]['content'] += text

    @property
    def subs(self):
        return self._subs
