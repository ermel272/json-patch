"""
Module:     json_patch.py
Author:     Chris Ermel
Purpose:    Implements a utility for administering the JSON Patch standard (IETF RFC 6902)
            defined at https://tools.ietf.org/html/rfc6902
"""

#########################
#
# String Constants
#
#########################
__ADD = "add"
__REPLACE = "replace"
__REMOVE = "remove"
__COPY = "copy"
__MOVE = "move"
__TEST = "test"


#########################
#
# Interface
#
#########################
def apply_patch(patch, obj):
    pass


class JsonPatch(object):

    def __init__(self, patches):
        self.patches = patches

    def __apply_test(self, patch):


#########################
#
# Helper Functions
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
