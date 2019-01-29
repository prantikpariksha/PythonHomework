"""
This includes three functions.When someone calls these functions
it will return the corresponding value defined under the three 
global variables
"""

Artist="Bob Marley"                  #This is the singer name
Title="No Woman No Cry"              #This is the Song name
Album="Raga Music"                   #this is the Album name
var1=True
var2=False                  

def GetArtistName(name):
    return name
ArtistName=GetArtistName(Artist)
print(ArtistName)

def GetTitleName(name):
    return name
TitleName=GetTitleName(Title)
print(TitleName)

def GetAlbumName(name):
    return name
AlbumName=GetAlbumName(Album)
print(AlbumName)

def Booleans(name):
    return name
var3=Booleans(var1)
var4=Booleans(var2)
print (var3,var4)
