from wit import Wit
from flask import session
from ..settings import WIT_AI_KEY



client = Wit(access_token=WIT_AI_KEY)