from NEXIOMUSIC.core.bot import NEXIO
from NEXIOMUSIC.core.dir import dirr
from NEXIOMUSIC.core.git import git
from NEXIOMUSIC.core.userbot import Userbot
from NEXIOMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = NEXIO()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
