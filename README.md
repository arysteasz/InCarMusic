# InCarMusic
1.	Music Recomnder system
The MusicRecomender is one class program, responsible for recommendation of music for user.
Firstly, when you run the program, the Application will ask you for User number. Provide, the integer User number from the 1001-1042 and press Enter. The application will analyse the User past history of ratings. In the category in which the most often User voted will be choose the best rated song - song with best mean value rating.  Next, the list of the songs , ordered of mean value ratings will by suggested too.

2.	Function Description
ImportUserData the function which import data of user prepared by the InCarMusic.py stored in UserDataDF.csv The file contains the UserID, ItemID, Rating, Music Category   


ImportMusicScoreData the function which import data of user prepared by the InCarMusic.py stored in MusicScoreDF.csv The file contains SongID, CategoryID, SongGrade, SongTitle. 


UserDominantMusicCategory the function which collect amount of songs rated by User. The dominant song category is suggested to looking for the best rated song. 

BestSongInCategory the function which collect amount of song ratings by all Users. The best ratings songs in the category is suggested to the User.
 
 
SongInCategory the function which collected the song from the dominant music category and ordered the in the increased mean values ratings order.
