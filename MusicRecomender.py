import numpy as np
import pandas as pd
from statistics import mode


class MusicRecomender(object):
    #def __init__(self):

    def ImportUserData(self, file_name):
        UserData = pd.read_csv(file_name)
        return(UserData)

    def ImportMusicScoreData(self, file_name):
        MusicScore = pd.read_csv(file_name)
        return(MusicScore)

    def UserDominantMusicCategory(self, UserUniqueNr, UserData):
        #UserID, UserIDCategoryAssignment

        UserID = UserData.iloc[:, 0]
        UserIDCategory = UserData.iloc[:, 3]

        UserMusicCategory = []
        values = np.array(UserID)
        searchval = UserUniqueNr
        ii = np.where(values == searchval)[0]
        # print('Indesy danego Usera', ii)
        for i in range(0, len(ii), 1):
            factor = ii[i]
            UserMusicCategory.append(UserIDCategory[factor])

        # print('Kategorie muzyczne danego usera',UserMusicCategory)
        UserDominantMusicCategory = mode(UserMusicCategory)
        # print('Dominujacy nr kateroi Muzycznej u Usera',UserDominantMusicCategory)

        if UserDominantMusicCategory == 1:
            print('Blues Music')
        elif UserDominantMusicCategory == 2:
            print('Classical Music')
        elif UserDominantMusicCategory == 3:
            print('Country Music')
        elif UserDominantMusicCategory == 4:
            print('Disco Music')
        elif UserDominantMusicCategory == 5:
            print('Hip Hop Music')
        elif UserDominantMusicCategory == 6:
            print('Jazz Music')
        elif UserDominantMusicCategory == 7:
            print('Metal Music')
        elif UserDominantMusicCategory == 8:
            print('Pop Music')
        elif UserDominantMusicCategory == 9:
            print('Reggae Music')
        elif UserDominantMusicCategory == 10:
            print('Rock Music')
        else: print('this category is not recognised!!!')

        return (UserDominantMusicCategory)

    def BestSongInCategory(self, CategoryUniqueNr, MusicScore  ):
            # CategoryID, MeanValuesRatings, SongID, SongTitle

        CategoryID = MusicScore.iloc[:, 1]
        MeanValuesRatings = MusicScore.iloc[:, 2]
        SongID = MusicScore.iloc[:, 0]
        SongTitle=MusicScore.iloc[:, 3]

        # list of Song in Category
        RatingSongsMusicCategory = []
        # list of all song with categories
        values = np.array(CategoryID)
        # search unique Category Nr
        searchval = CategoryUniqueNr
        ii = np.where(values == searchval)[0]
        # print('Indeksy Piosenkim z listy,w szukanej kategorii', ii)

        for i in range(0, len(ii), 1):
            factor = ii[i]
            # print('Nazwa znalezionej piosenki: ', SongTitle[factor])
            RatingSongsMusicCategory.append(MeanValuesRatings[factor])

        # print('Wartosci srednie dla ocen piosenek: ', RatingSongsMusicCategory)

        MaxRatedMusic = max(RatingSongsMusicCategory)
        # print('Maksymalna srednia wartosc oceny: ',MaxRatedMusic )

        values = np.array(RatingSongsMusicCategory)
        searchval = MaxRatedMusic
        jj = np.where(values == searchval)[0]
        factork = jj[0]
        # print(factork)
        # BestSong = SongID[jj[0]]
        BestSong = SongTitle[ii[factork]]
        return (BestSong)

    def SongInCategory(self, CategoryUniqueNr, MusicScore):
        CategoryID = MusicScore.iloc[:, 1]
        MeanValuesRatings = MusicScore.iloc[:, 2]
        SongID = MusicScore.iloc[:, 0]
        SongTitle=MusicScore.iloc[:, 3]

        # list of Song in Category
        RatingSongsMusicCategory = []

        RatingSongsMusicCategoryTitle = []
        # list of all song with categories
        values = np.array(CategoryID)
        # search unique Category Nr
        searchval = CategoryUniqueNr
        ii = np.where(values == searchval)[0]
        # print('Indeksy Piosenkim z listy,w szukanej kategorii', ii)

        for i in range(0, len(ii), 1):
            factor = ii[i]
            # print('Nazwa znalezionej piosenki: ', SongTitle[factor])
            RatingSongsMusicCategory.append(MeanValuesRatings[factor])
            RatingSongsMusicCategoryTitle.append(SongTitle[factor])

        Songs = {'RatingSongsMusicCategory': RatingSongsMusicCategory,
                 'RatingSongsMusicCategoryTitle': RatingSongsMusicCategoryTitle}
        df = pd.DataFrame(Songs, columns=['RatingSongsMusicCategory', 'RatingSongsMusicCategoryTitle'])

        # sort Brand - ascending order
        df.sort_values(by=['RatingSongsMusicCategory'], inplace=True, ascending=False)

        return(df)


MR = MusicRecomender()
UserData = MR.ImportUserData('UserDataDF.csv')
MusicScore = MR.ImportMusicScoreData('MusicScoreDF.csv')

### Asking for user number:
print('Please, give the UserID to choose the most suitable song for him,')
var = int(input('it has to be number between 1001-1042: '))
print('you enetered: ', str(var))
UserNR=var
#UserNR=1001
UserDominantMusicCategory = MR.UserDominantMusicCategory(UserNR, UserData)
print('is User Dominan category - nr: ')
print(UserDominantMusicCategory)

BestSongInCategory = MR.BestSongInCategory(UserDominantMusicCategory,MusicScore)
print('Best Suitable for User Music Song: ')
print(BestSongInCategory)

SongInCategory = MR.SongInCategory(UserDominantMusicCategory, MusicScore)
print('the List of also preafale by User Music Songs in ored of rating: ')
print(SongInCategory)
