import sys


class NRELError(Exception):
    """
    """

    def __init__(self, message):
        """
        """
        Exception.__init__(self, message)
        self.message = message

    def __unicode__(self):
        return unicode(repr(self.message))

    if sys.version_info[0] >= 3:  # Python 3
        def __str__(self):
            return self.__unicode__()
    else:  # Python 2
        def __str__(self):
            return self.__unicode__().encode('utf8')


class NRELFail(Exception):

    def __init__(self):
        Exception.__init__(self)


class NRELNoResults(Exception):

    def __init__(self):
        Exception.__init__(self)
