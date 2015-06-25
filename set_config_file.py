__author__ = 'luishoracio'
import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.
config.add_section('Log')
config.set('Log', 'pop3', 'mail.basipesa.com')
config.set('Log', 'mail_user', 'hmb@basipesa.com')
config.set('Log', 'mail_pass', '250215hmb')
config.set('Log', 'rangeLow', '6739')

config.add_section('SMTP')
config.set('SMTP', 'smtp_server', 'smtp.basipesa.com')
config.set('SMTP', 'smtp_port', '587')
config.set('SMTP', 'smtp_user', 'hmb@basipesa.com')
config.set('SMTP', 'smtp_pass', '250215hmb')
# config.set('Section1', 'baz', 'fun')
# config.set('Section1', 'bar', 'Python')
# config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('config.cfg', 'wb') as configfile:
    config.write(configfile)
