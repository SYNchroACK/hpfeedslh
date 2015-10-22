# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json
import six


def load_configuration(filepath):
    with open(filepath, 'r') as fpconfig:
        config = json.loads(fpconfig.read())
    return config

harm_config = load_configuration('./conf/harmonization.conf')  # FIXME


class Event(dict):

    def __init__(self, message=()):
        try:
            self.harmonization_config = harm_config
        except:
            print('FIXME: cannot load harmonization')

    def __setitem__(self, key, value):
        self.add(key, value)

    def add(self, key, value, force=False, ignore=()):

        if not force and key in self:
            print('key already exists')  # FIXME
            return

        if not self.__is_valid_key(key):
            print('invalid key, exiting... bye\n')  # FIXME
            exit(-1)  # FIXME

        ''' Value validation '''

        if value is None or value == "":
            return

        for invalid_value in ["-", "N/A"]:
            if value == invalid_value:
                return

        if value in ignore:
            return

        ''' Save key/value '''

        super(Event, self).__setitem__(key, value)

    def value(self, key):
        return self.__getitem__(key)

    def update(self, key, value):
        if key not in self:
            print('cannot update inexistent key')  # FIXME
        self.add(key, value, force=True)

    def clear(self, key):
        self.__delitem__(key)

    def contains(self, key):
        return key in self

    def finditems(self, keyword):
        for key, value in super(Message, self).items():
            if key.startswith(keyword):
                yield key, value

    def __is_valid_key(self, key):
        if key in self.harmonization_config:
            return True
        return False

    def __hash__(self):
        event_hash = hashlib.sha256()

        for key, value in sorted(self.items()):
            event_hash.update(self.encode(key))
            event_hash.update(b"\xc0")
            event_hash.update(self.encode(repr(value)))
            event_hash.update(b"\xc0")

        return int(event_hash.hexdigest(), 16)

    def __unicode__(self):
        return self.serialize()

    def __str__(self):
        return self.serialize()

    def serialize(self):
        json_dump = self.decode(json.dumps(self, ensure_ascii=False))
        return json_dump

    @staticmethod
    def unserialize(message_string):
        message = json.loads(message_string)
        return message

    def decode(self, text, encodings=("utf-8", ), force=False):
        """
        Decode given string to UTF-8 (default).

        Parameters:
        -----------
        text : bytes string
            if unicode string is given, same object is returned
        encodings : iterable of strings
            list/tuple of encodings to use, default ('utf-8')
        force : boolean
            Ignore invalid characters, default: False

        Returns
        -------
        text : unicode string
            unicode string is always returned, even when encoding is ascii
            (Python 3 compat)
        """
        if isinstance(text, six.text_type):
            return text

        for encoding in encodings:
            try:
                return six.text_type(text.decode(encoding))
            except ValueError:
                pass

        if force:
            for encoding in encodings:
                try:
                    return six.text_type(text.decode(encoding, 'ignore'))
                except ValueError:
                    pass

        raise ValueError("Could not decode string with given encodings{!r}"
                         ".".format(encodings))

    def encode(self, text, encodings=("utf-8", ), force=False):
        """
        Encode given string from UTF-8 (default).

        Parameters:
        -----------
        text : unicode string
            if bytes string is given, same object is returned
        encodings : iterable of strings
            list/tuple of encodings to use, default ('utf-8')
        force : boolean
            Ignore invalid characters, default: False
        """
        if isinstance(text, six.binary_type):
            return text

        for encoding in encodings:
            try:
                return text.encode(encoding)
            except ValueError:
                pass

        if force:
            for encoding in encodings:
                try:
                    return text.encode(encoding, 'ignore')
                except ValueError:
                    pass

        raise ValueError("Could not encode string with given encodings{!r}"
                         ".".format(encodings))
