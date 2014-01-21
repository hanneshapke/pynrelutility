class NRELError(Exception):
    """
    """

    def __init__(self, status):
        """

        """
        Exception.__init__(self, message)        
        self.message = message

    def __str__(self):
        return repr(self.message) 

    def __unicode__(self):
        return unicode(self.__str__())


class NRELFail(Exception):

    def __init__(self):
        Exception.__init__(self)


class NRELNoResults(Exception):

    def __init__(self):
        Exception.__init__(self)