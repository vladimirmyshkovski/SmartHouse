from wit import Wit
from flask import session
import settings as s



client = Wit(access_token=s.WIT_AI_KEY)