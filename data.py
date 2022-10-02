import pandas as pd
import  numpy as np


athlete_events=pd.read_csv('athlete_events.csv')
noc_regions=pd.read_csv('noc_regions.csv')


# data preprcesing 


df=pd.merge(athlete_events,noc_regions,on="NOC")
m=pd.get_dummies(df['Medal'],).astype(int)
df=pd.concat([df,m],axis=1)
summer_df=df[df['Season']=='Summer']
summer_df['total']=summer_df['Gold']+summer_df['Silver']+summer_df['Bronze']
summer_df.drop_duplicates(inplace=True)
summer_df.drop_duplicates(subset=['Team','NOC','Games','City','Sport','Event','Medal'],inplace=True)
a=summer_df.drop_duplicates(subset=['Name','Year'])
ab=a[['Name','Sport','Year','Gold','Silver','Bronze','total']]



    
# side bar menu funcation
# for total madel ---

def medal():
    
    # summer_df['total']=summer_df['Gold']+summer_df['Silver']+summer_df['Bronze']
    return summer_df.groupby('region').sum()[['Gold','Silver','Bronze','total']].sort_values('Gold',ascending=False,).reset_index()
    

def year():
    years=summer_df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Over All Years')
   
    return years
def country():
   
    country=np.unique(summer_df['region'].dropna()).tolist()
    country.sort()
    country.insert(0,"Over All Country's")

    return country

def athlete():
    b=a['Name'].unique().tolist()
    b.sort()
    b.insert(0,'Over All Athlete')
    return b

# ---------END--------------

def y_c(text):
    a=summer_df[summer_df['Year']==int(text)]
    return a.groupby('region').sum()[['Gold','Silver','Bronze','total']].reset_index()


def c_y(text):
    a=summer_df[summer_df['region']==str(text)]
    return a.groupby('Year').sum()[['Gold','Silver','Bronze','total']].reset_index()

def cc_yy(text,text1):

    a=summer_df[(summer_df['Year']==int(text)) &  (summer_df['region']==str(text1))]
    return a.groupby('Year').sum()[['Gold','Silver','Bronze','total']].reset_index()


# ----------End-----------------


# over all analysis option
def overall_country(text):
    a=summer_df[summer_df['Year']==int(text)]
    event=a['Event'].unique().shape[0]
    city=a['City'].unique().shape[0]
    county=a['region'].unique().shape[0]
    plyer=a['Name'].shape[0]
    sport=a['Sport'].unique().shape[0]
    edtions=a['Year'].unique().shape[0]
    return event,city,county,plyer,sport,edtions

def overall_year(text):
    a=summer_df[summer_df['region']==str(text)]
    event=a['Event'].unique().shape[0]
    city=a['City'].unique().shape[0]
    county=a['region'].unique().shape[0]
    plyer=a['Name'].shape[0]
    sport=a['Sport'].unique().shape[0]
    edtions=a['Year'].unique().shape[0]
    return event,city,county,plyer,sport,edtions

def overall_year_county(text,text1):
    a=summer_df[(summer_df['region']==str(text)) & (summer_df['Year']==int(text1))]
    event=a['Event'].unique().shape[0]
    city=a['City'].unique().shape[0]
    county=a['region'].unique().shape[0]
    plyer=a['Name'].shape[0]
    sport=a['Sport'].unique().shape[0]
    edtions=a['Year'].unique().shape[0]
    return event,city,county,plyer,sport,edtions


# def char():
#     year_region=summer_df.drop_duplicates(subset=['Year','region'])['Year'].value_counts().reset_index()
#     year_region.rename(columns={'index':'year','Year':'country'},inplace=True)
#     return (year_region['country'],year_region['year']


# Analysis Athlete_wise


   
def grup_year(text):
    
    year=ab[ab['Year']==int(text)]
    
    return year[['Name','Sport','Year','Gold','Silver','Bronze','total']]

def grup_country(text):
    
    country=a[a['region']==str(text)]
    
    return country[['Name','region','Sport','Year','Gold','Silver','Bronze','total']]

def  grup_c_y (text,text1):
    country_year=a[(a['region']==str(text)) & (a['Year']==int(text1))]
    return country_year[['Name','Sport','region','Year','Gold','Silver','Bronze','total']]

def grup_c_y_a(text3):
    cn=a[(['Name']==str(text3))]
    
    return cn[['Name','region','Sport','Year','Gold','Silver','Bronze','total']]

def grup_c_y_aa(text,text1,text3):
    cn=a[(a['region']==str(text)) & (a['Year']==int(text1)) & (a['Name']==str(text3))]
    
    return cn[['Name','region','Sport','Year','Gold','Silver','Bronze','total']]
