import unicodecsv
import pandas as pd
from pandas import read_excel
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from scipy import stats
from scipy.stats import norm
import statistics


###
#Import Data
# Open File
file_name ='DataInCarMusic.xlsx'

# Read Two the most important(in my opinion Sheet of music)
ContextualRating_data = pd.read_excel(file_name, sheet_name='ContextualRating')
MusicTrack_data=pd.read_excel(file_name, sheet_name='Music Track')

# The name of the factors
UserID = ContextualRating_data['UserID']
ItemID = ContextualRating_data['ItemID']
Rating = ContextualRating_data['Rating']
SongID = MusicTrack_data['ItemID']


# The data Columns which are problematic to read&open by PANDAS :|
CategoryID =[1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,1,4,10,5,4,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,4,4,8,8,8,8,8,5,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,4,8,8,8,8,8,4,8,8,10,4,8]
SongTitle = ['The Thrill is Gone', 'Crazy Blues', 'Hellhound On My Trail', 'Stormy Monday', 'Four Seasons', 'Brandenburg Concerto 3','Symphony 5', 'Trout Quintet', 'Rhapsody in Blue','The Devil Went Down to Georgia','Im So Lonesome I Could Cry', 'I Walk the Line', 'Stand By Your Man', 'Flowers On The Wall','Stayin Alive', 'Good Times', 'I Will Survive', 'Funkytown', 'YMCA','Dear Mama','Gangsta Paradise','Hypnotize','Its Like That','Rappers Delight','Moanin','Giant Steps','Potato Head Blues','So What','Straight No Chaser','Pursuit Of Vikings','Apocalypse','The Trooper','Master Of Puppets','Cemetery Gates','Dancing Queen','Toxic','Paparazzi','Like A Prayer','Billie Jean','I Shot The Sheriff','No Woman No Cry','Israelites','Satta Massagana','Pressure Drop','You Shook Me All Night Long','Highway Star','Sultans of Swing','Purple Haze','House of the Rising Sun','I Cant Quit You Baby','Disco Pogo','If Today Was Your Last Day (Album Version)','Alles wird gut - Album Version','TiK ToK','Das Geht Ab (Wir Feiern Die Ganze Nacht)','I Like - Jost and Grubert','Alors On Danse','Fireflies - Album Version','Fight For This Love','Bad Romance','Dont Tell Me That Its Over','Geboren um zu leben','I Will Love You Monday (365)','Wishing You Well - Radio Version','All The Right Moves','Monsta','If We Ever Meet Again (Featuring Katy Perry)','I Gotta Feeling - Album Version','Heavy Cross - Album Version','Rude Boy - Album Version','Rude Boy - Explicit Version','Spinner','Memories (Featuring Kid Cudi)','Whatcha Say - Main Version','Meet Me Halfway - Album Version','Bad Boys','Einer von Zweien','Undisclosed Desires - Album Version','Eiskalt','Monday Morning - Album Version','Replay (Album Version)','Morning After Dark (Featuring Nelly Furtado)','Pflaster','Russian Roulette - Album Version','Rock That Body - Album Version','Hey','Release Me','This Is My Time (Club Edit)','Morning Sun','Secrets','Halte durch','Neopolitan Dreams','Everybody Hurts','Krieger des Lichts - Single Version','One World One Flame','Try Sleeping With A Broken Heart','Hoffnung','Bad Romance - Radio Edit','Bad Influence - Main Version','Moonlight Shadow','Feels Like Im Dancin (Original Mix)','Sexy Bitch (Featuring Akon)','If We Ever Meet Again - International Radio','Alles kann besser werde','Sky And Sand','Ich bau dir ein Schloss - Wolken Mix','Empire State Of Mind [Jay-Z + Alicia Keys]','Lass mich nie mehr los - Studio Version','Eingeliebt - ausgeliebt','nemeyer','Mein Stern','Time to Wonder (Club Mix)','Hallelujah','Einer von Zweien - Radio Version','One Love (Featuring Estelle)','Into The Light','Blah Blah Blah','Alice','If A Song Could Get Me You','Foundations - Full Explicit Version','Hoffnung - Single Version','I Cant Dance Alone [feat. Ross Antony]','If You Tolerate This (Club Mix)','Youve Got The Love','Gypsy - Album Version','An deiner Seite','Go - Single Version','Rocket','Fur immer','Du bist so gut fur mich (Radio Edit)','In My Head (Album Version)','Hold My Hand (Original Version)','Young Forever [Jay-Z + Mr Hudson]','Feel It','Jein (Radio Edit)','Paparazzi','Superman Tonight - Album Version','Narcotic','Closer To Heaven' ]
###



###
#Functions is used the SongID, UserID, ItemID, Rating
# the give back how many users are voted
###
def AmountVotes(SongID, UserID, ItemID, Rating):

    val = 0
    AmountVotes = []

    for j in range(0, len(SongID), 1):
        for i in range(0, len(UserID), 1):
            if ItemID[i] == SongID[j]:
                val += 1


        AmountVotes.append(val)

        val = 0

    return(AmountVotes)


###
#Functions is used the SongID, UserID, ItemID, Rating
# the give back the mean value of ratings
###

def MeanValuesRatings(SongID, UserID, ItemID, Rating):
    SumRating = 0
    val = 0
    AmountRatings = []
    MeanValuesRatings = []
    for j in range(0, len(SongID), 1):
        for i in range(0, len(UserID), 1):
            if ItemID[i] == SongID[j]:
                val += 1
                SumRating += Rating[i]

        MeanValue = SumRating / val
        AmountRatings.append(val)
        MeanValuesRatings.append(MeanValue)
        SumRating = 0
        val = 0

    return(MeanValuesRatings)

###
#Functions is used the SongID, UserID, ItemID, Rating
# the give back the list of ratings
###
def RatingCollection(SongID, UserID, ItemID, Rating):

    RatingCollections = []
    for i in range(0, len(UserID), 1):
        if ItemID[i] == SongID:
            RatingCollections.append(Rating[i])

    return RatingCollections


###
#Functions is used the AmountVotes, SongID
# the give back the most voteable SongID
###
def SongIDMaximalAmountVotes(AmountVotes, SongID):

    SongIDMaximalAmountVotes=[]
    MaximalAmountVotes = max(AmountVotes)
    values = np.array(AmountVotes)
    searchval = MaximalAmountVotes
    ii = np.where(values == searchval)[0]

    for i in range(0, len(ii), 1):
        factork = ii[i]
        SongIDMaximalAmountVotes.append(SongID[factork])
        #print('SongID na ktore najczescie glosowano: ', SongID[factork])

    return SongIDMaximalAmountVotes


###
#Functions is used the AmountVotes
# the give back the most voteable Index of SongID
###
def SongListIndexMaximalAmountVotes(AmountVotes):

    SongListIndexMaximalAmountVotes=[]
    MaximalAmountVotes = max(AmountVotes)
    values = np.array(AmountVotes)
    searchval = MaximalAmountVotes
    ii = np.where(values == searchval)[0]

    for i in range(0, len(ii), 1):
        factork = ii[i]
        SongListIndexMaximalAmountVotes.append(factork)
        #print('indexy listy na ktore najczescie glosowano: ', factork)

    return SongListIndexMaximalAmountVotes

def SongTitleMaximalAmountVotes(AmountVotes, SongTitle):

    SongTitleMaximalAmountVotes=[]
    MaximalAmountVotes = max(AmountVotes)
    values = np.array(AmountVotes)
    searchval = MaximalAmountVotes
    ii = np.where(values == searchval)[0]

    for i in range(0, len(ii), 1):
        factork = ii[i]
        SongTitleMaximalAmountVotes.append(SongTitle[factork])
        #print('indexy listy na ktore najczescie glosowano: ', factork)
    return (SongTitleMaximalAmountVotes)

###
#Functions is used the AmountVotes, SongID
# the give back the worst voteable SongID
###
def SongIDMinimalAmountVotes(AmountVotes, SongID):

    SongIDMinimalAmountVotes=[]
    MinimalAmountVotes = min(AmountVotes)
    values = np.array(AmountVotes)
    searchval = MinimalAmountVotes
    ii = np.where(values == searchval)[0]

    for i in range(0, len(ii), 1):
        factork = ii[i]
        SongIDMinimalAmountVotes.append(SongID[factork])
        #print('SongID na ktore najrzadziej glosowano: ', SongID[factork])

    return SongIDMinimalAmountVotes

###
#Functions is used the AmountVotes
# the give back the worst voteable Index of SongID
###
def SongListIndexMinimalAmountVotes(AmountVotes):

    SongListIndexMinimalAmountVotes=[]
    MinimalAmountVotes = min(AmountVotes)
    values = np.array(AmountVotes)
    searchval = MinimalAmountVotes
    ii = np.where(values == searchval)[0]

    for i in range(0, len(ii), 1):
        factork = ii[i]
        SongListIndexMinimalAmountVotes.append(factork)
        #print('indexy listy na ktore najrzadziej glosowano: ', factork)

    return SongListIndexMinimalAmountVotes

def SongTitleMinimalAmountVotes(AmountVotes, SongTitle):

    SongTitleMinimalAmountVotes=[]
    MinimalAmountVotes = min(AmountVotes)
    values = np.array(AmountVotes)
    searchval = MinimalAmountVotes
    ii = np.where(values == searchval)[0]

    for i in range(0, len(ii), 1):
        factork = ii[i]

        SongTitleMinimalAmountVotes.append(SongTitle[factork])
        #print('indexy listy na ktore najrzadziej glosowano: ', factork)

    return(SongTitleMinimalAmountVotes)


###
#Functions is used the SongID, ItemID, CategoryID
#Function is give back list: assigned the Category of Song into in order to user
###
def UserIDCategoryAssignment(SongID, ItemID, CategoryID ):
    values = np.array(SongID)
    UserIDCategoryAssignment = []
    # len(ItemID)
    for i in range(0, len(ItemID), 1):
        searchval = ItemID[i]
        ii = np.where(values == searchval)[0]
        # print(ii)
        factor = ii[0]
        UserIDCategoryAssignment.append(CategoryID[factor])

    return(UserIDCategoryAssignment)



def SongMaximalAmountVotesMeanRatingValue(SongListIndexMaximalAmountVotes):

    SongMaximalAmountVotesMeanRatingValue = []
    for i in range(0, len(SongListIndexMaximalAmountVotes), 1):
        val = MeanValuesRatings[SongListIndexMaximalAmountVotes[i]]
        SongMaximalAmountVotesMeanRatingValue.append(val)
    #print('Song with max amount votes, the mean rating of them:')
    #print(SongMaximalAmountVotesMeanRatingValue)

    return(SongMaximalAmountVotesMeanRatingValue)

def SongMinimalAmountVotesMeanRatingValue(SongListIndexMinimalAmountVotes):
    SongMinimalAmountVotesMeanRatingValue = []
    for i in range(0, len(SongListIndexMinimalAmountVotes), 1):
        val = MeanValuesRatings[SongListIndexMinimalAmountVotes[i]]
        SongMinimalAmountVotesMeanRatingValue.append(val)
    #print('Song with minimal amount votes, the mean rating values of them:')
    #print(SongMinimalAmountVotesMeanRatingValue)
    return(SongMinimalAmountVotesMeanRatingValue)

def SongTitleBestRated(MeanValuesRatings,SongTitle):

    values = np.array(MeanValuesRatings)
    searchval = max(MeanValuesRatings)
    ii = np.where(values == searchval)[0]
    #print('nr indexu dla najbardziej lubianej piosenki wartości: ', ii)
    factork = ii[0]     #There is only one value

    SongTitleBestRated = SongTitle[factork]

    #print('Song Title dla najwyzszej wartosci sredniej Ratingu: ', SongTitleBestRated)
    return (SongTitleBestRated)


def SongTitleWorstRated(MeanValuesRatings,SongTitle):

    values = np.array(MeanValuesRatings)
    searchval = min(MeanValuesRatings)
    jj = np.where(values == searchval)[0]
    #print('nr indexu dla najmniej lubianej piosenki wartości: ', jj)
    factorkk = jj[0]     #There is only one value

    SongTitleWorstRated = SongTitle[factorkk]

    #print('Song Title dla najniższej wartosci sredniej Ratingu: ', SongTitleWorstRated)



    return(SongTitleWorstRated)


###
#Functions is used the SongID, UserID, ItemID, Rating
# the give back the list of ratings
###
def RatingCollection(SongID, UserID, ItemID, Rating):

    RatingCollections = []
    for i in range(0, len(UserID), 1):
        if ItemID[i] == SongID:
            RatingCollections.append(Rating[i])


    return (RatingCollections)


###
#Functions is used the RatingCollection
#Function is ploted the hostogram of Grades
###
def RatingCollectionHistogram(RatingCollection):

    labels, counts = np.unique(RatingCollection, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.gca().set_xticks(labels)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Grade Value')
    plt.ylabel('Amount of Votes')
    plt.title('Histogram')
    plt.text(23, 45, r'$\mu=15, b=3$')
    plt.show()

def HistogramMaximalAmountVotesRatingCollection(SongIDMaximalAmountVotes,UserID, ItemID, Rating ):

    for j in range(0, len(SongIDMaximalAmountVotes), 1):
        RatingCollection = []
        for i in range(0, len(UserID), 1):
            if ItemID[i] == SongIDMaximalAmountVotes[j]:
                RatingCollection.append(Rating[i])

        labels, counts = np.unique(RatingCollection, return_counts=True)
        plt.bar(labels, counts, align='center')
        plt.gca().set_xticks(labels)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Grade Value')
        plt.ylabel('Amount of Votes')
        plt.title('Histogram')
        plt.text(23, 45, r'$\mu=15, b=3$')
        plt.show()


def HistogramMinimalAmountVotesRatingCollection(SongIDMinimalAmountVotes,UserID, ItemID, Rating ):

    for j in range(0, len(SongIDMinimalAmountVotes), 1):
        RatingCollection = []
        for i in range(0, len(UserID), 1):
            if ItemID[i] == SongIDMinimalAmountVotes[j]:
                RatingCollection.append(Rating[i])

        labels, counts = np.unique(RatingCollection, return_counts=True)
        plt.bar(labels, counts, align='center')
        plt.gca().set_xticks(labels)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Grade Value')
        plt.ylabel('Amount of Votes')
        plt.title('Histogram')
        plt.text(23, 45, r'$\mu=15, b=3$')
        plt.show()

def BestSongInCategory(CategoryID, MeanValuesRatings, SongID, SongTitle ):

    BestSongInCategory =[]

    for item in range (1,11, 1):

        # list of Song in Category
        RatingSongsMusicCategory = []
        # list of all song with categories
        values = np.array(CategoryID)
        #search unique Category Nr
        searchval = item
        ii = np.where(values == searchval)[0]
        #print('Indeksy Piosenkim z listy,w szukanej kategorii', ii)

        for i in range (0, len(ii), 1):
            factor = ii[i]
            #print('Nazwa znalezionej piosenki: ', SongTitle[factor])
            RatingSongsMusicCategory.append(MeanValuesRatings[factor])

        #print('Wartosci srednie dla ocen piosenek: ', RatingSongsMusicCategory)

        MaxRatedMusic = max(RatingSongsMusicCategory)
        #print('Maksymalna srednia wartosc oceny: ',MaxRatedMusic )


        values = np.array(RatingSongsMusicCategory)
        searchval = MaxRatedMusic
        jj = np.where(values == searchval)[0]
        factork=jj[0]
        #print(factork)
        # BestSong = SongID[jj[0]]
        BestSong = SongTitle[ii[factork]]
        BestSongInCategory.append(BestSong)

    return (BestSongInCategory)

def MusicScoreDFExporter(SongID, CategoryID, MeanValuesRatings, SongTitle):

    data = {
            'SongID': SongID,
            'CategoryID': CategoryID,
            'SongGrade': MeanValuesRatings,
            'SongTitle': SongTitle}
    # Creating the DataFrame
    MusicScoreDF = pd.DataFrame(data, columns=['SongID', 'CategoryID', 'SongGrade', 'SongTitle'])
    print(MusicScoreDF.head())
    export_csv = MusicScoreDF.to_csv('MusicScoreDF.csv', index=False, header=True)

    return (MusicScoreDF)


def UserDataDFExporter(UserID, ItemID,Rating,UserIDCategoryAssignment):

    data = {'UserID': UserID,
             'ItemID': ItemID,
             'Rating': Rating,
             'MusicCategory': UserIDCategoryAssignment}

    UserDataDF = pd.DataFrame(data, columns=['UserID', 'ItemID', 'Rating', 'MusicCategory'])
    print(UserDataDF.head())
    export_csv = UserDataDF.to_csv('UserDataDF.csv', index=False, header=True)
    return UserDataDF



AmountVotes=AmountVotes(SongID, UserID, ItemID, Rating)
MeanValuesRatings=MeanValuesRatings(SongID, UserID, ItemID, Rating)
UserIDCategoryAssignment = UserIDCategoryAssignment(SongID, ItemID, CategoryID )

# SongID na które najczescie glosowano
SongIDMaximalAmountVotes = SongIDMaximalAmountVotes(AmountVotes,SongID )
print('SongID na ktore najczescie glosowano')
print(SongIDMaximalAmountVotes)

# SongListIndex na które najczescie glosowano
SongListIndexMaximalAmountVotes = SongListIndexMaximalAmountVotes(AmountVotes)
print('SongListIndex na ktore najczescie glosowano')
print(SongListIndexMaximalAmountVotes)

# SongID na które najrzadziej glosowano
SongIDMinimalAmountVotes = SongIDMinimalAmountVotes(AmountVotes,SongID )
print('SongID na które najrzadziej glosowano')
print(SongIDMinimalAmountVotes)

# SongListIndex na które najczescie glosowano
SongListIndexMinimalAmountVotes = SongListIndexMinimalAmountVotes(AmountVotes)
print('SongListIndex na ktore najrzadzeij glosowano')
print(SongListIndexMinimalAmountVotes)


SongMaximalAmountVotesMeanRatingValue = SongMaximalAmountVotesMeanRatingValue(SongListIndexMaximalAmountVotes)
print('Song with max amount votes, the mean rating of them:')
print(SongMaximalAmountVotesMeanRatingValue)

SongMinimalAmountVotesMeanRatingValue = SongMinimalAmountVotesMeanRatingValue(SongListIndexMinimalAmountVotes)
print('Song with minimal amount votes, the mean rating values of them:')
print(SongMinimalAmountVotesMeanRatingValue)

SongTitleMaximalAmountVotes = SongTitleMaximalAmountVotes(AmountVotes, SongTitle)
print('Titles of song with max amount votes: ')
print(SongTitleMaximalAmountVotes)

SongTitleMinimalAmountVotes = SongTitleMinimalAmountVotes(AmountVotes, SongTitle)
print('Titles of song with min amount votes: ')
print(SongTitleMinimalAmountVotes)

SongTitleBestRated = SongTitleBestRated(MeanValuesRatings,SongTitle)
print('Title of best rated song: ')
print('"', SongTitleBestRated,'"')

SongTitleWorstRated = SongTitleWorstRated(MeanValuesRatings,SongTitle)
print('Title of worst rated song: ')
print('"', SongTitleWorstRated,'"')

BestSongInCategory = BestSongInCategory(CategoryID, MeanValuesRatings, SongID, SongTitle )
print('BestSongInCategory')
print(BestSongInCategory)

print('HistogramMaximalAmountVotes')
p = HistogramMaximalAmountVotesRatingCollection(SongIDMaximalAmountVotes,UserID, ItemID, Rating)
print('HistogramMinimalAmountVotes')
r = HistogramMinimalAmountVotesRatingCollection(SongIDMinimalAmountVotes,UserID, ItemID, Rating )


MusicScoreDFExporter = MusicScoreDFExporter(SongID, CategoryID, MeanValuesRatings, SongTitle)
UserDataDFExporter = UserDataDFExporter(UserID, ItemID,Rating,UserIDCategoryAssignment)
