#
# 检测DNS

import re
def validate_service_record_data(data):
    # valid _sip._tls
    # invalid _sip._tls.
    # invalid sip.tls.
    # (\.[\w\d\.-]+\.)
    regex = re.compile(r'_[a-z\d-]{1,63}\._[a-z\d-]{1,63}?$', re.IGNORECASE)
    m = regex.match(data)
    if m is not None:
        return True
    else:
        raise ValidationError('Service record is not valid.')
