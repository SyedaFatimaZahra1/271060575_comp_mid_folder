print("question 3")
                   
class Song:
    def __init__(self,title,artist,album,duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
    def display_info(self):
        print(f" title : {self.title} artist: {self.artist} album: {self.album} duration: {self.duration}")
class Playlist:
    def __init__(self,pl_title,descrip):
        self.pl_title = pl_title
        self.descrip = descrip
        self.song_list = []
    def add_song(self,obj_song):
        if obj_song not in self.song_list:
            self.song_list.append(obj_song)
            print("song has been added")
        else:
            print("song already exists")
    def remove_song(self,obj_song):
        if obj_song in self.song_list:
            self.song_list.remove(obj_song)
        else:
            print("song does not exist in playlist")
    def display_all_song(self):
        for i in self.song_list:
            print(i.display_info())
          
class Library:
    def __init__(self):
        self.pl_list = []
    def add_pl(self,obj_pl):
        if obj_pl not in self.pl_list:
            self.pl_list.append(obj_pl)
            print("playlist added")
        else:
            print("song already exists")
    def remove_pl(self,obj_pl):
        if obj_pl in self.pl_list:
            self.pl_list.remove(obj_pl)
            print("playlist removed")
        else:
            print("song already deleted")
        for i in self.pl_list:
            print(i.display_all_song())               
