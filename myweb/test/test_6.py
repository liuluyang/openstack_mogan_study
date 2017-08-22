import traceback
import sys
from oslo_utils import importutils

def import_class(import_str):
    """Returns a class from a string including module and class.

    .. versionadded:: 0.3
    """
    mod_str, _sep, class_str = import_str.rpartition('.')
    print mod_str
    print _sep
    print class_str
    __import__(mod_str)
    try:
        return getattr(sys.modules[mod_str], class_str)
    except AttributeError:
        raise ImportError('Class %s cannot be found (%s)' %
                          (class_str,
                           traceback.format_exception(*sys.exc_info())))

importutils.import_object('myweb.test.test_2.DD')
print '#'*30
import_class('myweb.test.test_2.DD')

