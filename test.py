import kissanimedl

s = kissanimedl.Scraper()
d = s.GetEpisodeLinks("http://kissanime.to/Anime/Sword-Art-Online-Dub")
if not len(d) > 0:
    raise "Couldn't get individual a list of episodes from show link"
