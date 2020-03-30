from functools import namedtuple
from GcMessageProtocol import BanProtocol
from GcMessageProtocol import Protocol
import datetime

def on_message(message):
    if message.author.bot:
        protocol = Protocol.identifyProtocol(message.content)
        print(protocol.toMessage())
    else:
        print("Não é bot >:[")
        
Member = namedtuple('Member', 'id bot')
Message = namedtuple('Message', 'content author')

protocol = BanProtocol(bot=123456789012345678, user_id=30, target_id=10, reason='sla', timestamp=datetime.datetime.now())

message = Message(protocol.toMessage() , author=Member(id=123456789012345678,bot=True))
on_message(message)