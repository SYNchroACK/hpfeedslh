from lib.event import Event
from lib.hpfeeds import HPFeeds

print('\n')


###
print('> Create an event')
e = Event()
e.add('source.ip', '192.168.1.20')
e.add('source.port', '61432')
e.add('destination.ip', '192.168.1.200')
e.add('destination.port', '22')
print('Event: {}'.format(e))
print('--------\n')


###
print('> Test: value already defined')
e.add('destination.port', '23')
print('Event: {}'.format(e))
print('--------\n')


###
# print('> Test: invalid key')
# e.add('destination.xxx', 'whatever')
# print('Event: {}'.format(e))
# print('--------\n')


###
# print('> HPFeeds: connect to hpfeed server')
#
# hpfeeds = HPFeeds(host='xxx.xxx.xxx.xxx',
#                   port='2000',
#                   ident='zZzZzZ',
#                   secret='sHsHshhhHHh'
#                   max_retries=10
#                  )
# hpfeeds.connect()
# hpfeeds.send(e.serialize())
#
# print('--------\n')


print('\n')
