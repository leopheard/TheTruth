from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://feeds.thetruthpodcast.com/thetruthapm"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://github.com/leopheard/Audio-Podcasts/blob/master/resources/media/1.jpg?raw=true"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://f.prxu.org/97/images/7cba013c-58c6-470f-bd34-a9e603d54af9/The_Truth_2000x2000.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup1)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

if __name__ == '__main__':
    plugin.run()
