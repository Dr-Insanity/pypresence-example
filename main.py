from pypresence import Presence
import time

client_id = '384445465454675675'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

click_me = [{"label": "first button's text", "url": "https://link-to.whatever"}, {"label": "second button's text", "url": "https://nice.cool-website.app"}]

print(RPC.update(state="text", details="text", buttons=click_me))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds



# the original developer uses a MIT license for pypresence.
# qwertyquerty's Git profile: https://github.com/qwertyquerty
# pypresence repository: https://github.com/qwertyquerty/pypresence
# pypresence's documentation: https://qwertyquerty.github.io/pypresence/html/index.html