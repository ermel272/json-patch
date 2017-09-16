"""
Module:     json_patch.py
Author:     Chris Ermel
Purpose:    Implements a utility for administering the JSON Patch standard (IETF RFC 6902)
            defined at https://tools.ietf.org/html/rfc6902
"""


#########################
#
# Convenience Functions
#
#########################
def apply_patch(patch, obj):
    pass


#########################
#
# Classes
#
#########################
class JsonPatch(object):

    def __init__(self, patches):
        self.patches = patches

        #########################
        #
        # Interface
        #
        #########################

        #########################
        #
        # Helper Functions
        #
        #########################


class JsonPatchException(Exception):
    """
    Class for exceptions raised within the json_patch module.
    """
    pass
