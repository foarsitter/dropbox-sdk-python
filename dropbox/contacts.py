# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# @generated
# flake8: noqa
# pylint: skip-file
from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

from dropbox import common

class DeleteManualContactsArg(bb.Struct):
    """
    :ivar contacts.DeleteManualContactsArg.email_addresses: List of manually
        added contacts to be deleted.
    """

    __slots__ = [
        '_email_addresses_value',
    ]

    _has_required_fields = True

    def __init__(self,
                 email_addresses=None):
        self._email_addresses_value = bb.NOT_SET
        if email_addresses is not None:
            self.email_addresses = email_addresses

    # Instance attribute type: list of [str] (validator is set below)
    email_addresses = bb.Attribute("email_addresses")

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(DeleteManualContactsArg, self)._process_custom_annotations(annotation_type, field_path, processor)

DeleteManualContactsArg_validator = bv.Struct(DeleteManualContactsArg)

class DeleteManualContactsError(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar list of [str] contacts.DeleteManualContactsError.contacts_not_found:
        Can't delete contacts from this list. Make sure the list only has
        manually added contacts. The deletion was cancelled.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    other = None

    @classmethod
    def contacts_not_found(cls, val):
        """
        Create an instance of this class set to the ``contacts_not_found`` tag
        with value ``val``.

        :param list of [str] val:
        :rtype: DeleteManualContactsError
        """
        return cls('contacts_not_found', val)

    def is_contacts_not_found(self):
        """
        Check if the union tag is ``contacts_not_found``.

        :rtype: bool
        """
        return self._tag == 'contacts_not_found'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def get_contacts_not_found(self):
        """
        Can't delete contacts from this list. Make sure the list only has
        manually added contacts. The deletion was cancelled.

        Only call this if :meth:`is_contacts_not_found` is true.

        :rtype: list of [str]
        """
        if not self.is_contacts_not_found():
            raise AttributeError("tag 'contacts_not_found' not set")
        return self._value

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(DeleteManualContactsError, self)._process_custom_annotations(annotation_type, field_path, processor)

DeleteManualContactsError_validator = bv.Union(DeleteManualContactsError)

DeleteManualContactsArg.email_addresses.validator = bv.List(common.EmailAddress_validator)
DeleteManualContactsArg._all_field_names_ = set(['email_addresses'])
DeleteManualContactsArg._all_fields_ = [('email_addresses', DeleteManualContactsArg.email_addresses.validator)]

DeleteManualContactsError._contacts_not_found_validator = bv.List(common.EmailAddress_validator)
DeleteManualContactsError._other_validator = bv.Void()
DeleteManualContactsError._tagmap = {
    'contacts_not_found': DeleteManualContactsError._contacts_not_found_validator,
    'other': DeleteManualContactsError._other_validator,
}

DeleteManualContactsError.other = DeleteManualContactsError('other')

delete_manual_contacts = bb.Route(
    'delete_manual_contacts',
    1,
    False,
    bv.Void(),
    bv.Void(),
    bv.Void(),
    {'auth': u'user',
     'host': u'api',
     'style': u'rpc'},
)
delete_manual_contacts_batch = bb.Route(
    'delete_manual_contacts_batch',
    1,
    False,
    DeleteManualContactsArg_validator,
    bv.Void(),
    DeleteManualContactsError_validator,
    {'auth': u'user',
     'host': u'api',
     'style': u'rpc'},
)

ROUTES = {
    'delete_manual_contacts': delete_manual_contacts,
    'delete_manual_contacts_batch': delete_manual_contacts_batch,
}

