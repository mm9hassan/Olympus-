import streamlit as st
# helper filer for funcaions
import data

# ----------------

# -----main title-----------------

st.header('Olympics Games Analysis')

# ----------------------------------------------------
# side bar options 
st.sidebar.title('Analysis Filter')
user_selection=st.sidebar.radio(label='Select for Analysis',options=["Total Medal's", 'Over all Analysis','Country_wise Analysis','Athlete_wise'],)


# --side box---------------
select_year=st.sidebar.selectbox('Select Year',data.year())
select_county=st.sidebar.selectbox('Select Country',data.country())
select_player=st.sidebar.selectbox('Select Athlete',data.athlete())


# for year and country and Total madels
if user_selection == "Total Medal's" and select_year=='Over All Years' and select_county =="Over All Country's":
        st.title('Over All Perform')
        st.dataframe(data.medal(),width=550)
elif select_year != 'Over All Years' and select_county== "Over All Country's" and user_selection == "Total Medal's":
    st.title(str(select_year) +  ' performing '+ select_county)
    st.table(data.y_c(select_year),)
elif select_year == 'Over All Years' and select_county!= "Over All Country's" and user_selection == "Total Medal's":
    st.title(str(select_year)+ ' performing '+ select_county)
    st.table(data.c_y(select_county),)
elif select_year != 'Over All Years' and select_county!= "Over All Country's" and user_selection == "Total Medal's":
    st.title(str(select_year)+ ' Performing ' + select_county)
    st.table(data.cc_yy(select_year,select_county),)

# ------------end-----------------

# over all analysis option
if user_selection=='Over all Analysis':
    st.title("Over all Analysis by Years & Country's")

    event=data.summer_df['Event'].unique().shape[0]
    city=data.summer_df['City'].unique().shape[0]
    county=data.summer_df['region'].unique().shape[0]
    plyer=data.summer_df['Name'].shape[0]
    sport=data.summer_df['Sport'].unique().shape[0]
    edtions=data.summer_df['Year'].unique().shape[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Total Events")
        st.title(event)
    with col2:
        st.header("Country")
        st.title(county)
    with col3:
        st.header("City")
        st.title(city)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.header("Players")
        st.title(plyer)
    with col5:
        st.header("Sport")
        st.title(sport)
    
    with col6:
        st.header("Edtions")
        st.title(edtions)
# -----------End--------------------


# for Country_wise Analysis 


if user_selection=='Country_wise Analysis'and select_year=='Over All Years' and select_county =="Over All Country's":
    st.title("Country_wise Analysis🌎")

    event=data.summer_df['Event'].unique().shape[0]
    city=data.summer_df['City'].unique().shape[0]
    county=data.summer_df['region'].unique().shape[0]
    plyer=data.summer_df['Name'].shape[0]
    sport=data.summer_df['Sport'].unique().shape[0]
    edtions=data.summer_df['Year'].unique().shape[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Total Events")
        st.title(event)
    with col2:
        st.header("Country")
        st.title(county)
    with col3:
        st.header("City")
        st.title(city)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.header("Players")
        st.title(plyer)
    with col5:
        st.header("Sport")
        st.title(sport)
    
    with col6:
        st.header("Edtions")
        st.title(edtions)
    
elif user_selection=='Country_wise Analysis' and select_year!='Over All Years' and select_county =="Over All Country's":
    st.title("Analysis by " + str(select_year) + ' '+ str(select_county))
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Total Events")
        st.title(data.overall_country(select_year)[0])
    with col2:
        st.header("Country")
        st.title(data.overall_country(select_year)[2])
    with col3:
        st.header("City")
        st.title(data.overall_country(select_year)[1])

    col4, col5, col6 = st.columns(3)

    with col4:
        st.header("Players")
        st.title(data.overall_country(select_year)[3])
    with col5:
        st.header("Sport")
        st.title(data.overall_country(select_year)[4])
    
    with col6:
        st.header("Edtions")
        st.title(data.overall_country(select_year)[5])

elif user_selection=='Country_wise Analysis' and select_year=='Over All Years' and select_county !="Over All Country's":
    st.title("Analysis by " + str(select_year) + ' '+ str(select_county))
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Total Events")
        st.title(data.overall_year(select_county)[0])
    with col2:
        st.header("Country")
        st.title(data.overall_year(select_county)[2])
    with col3:
        st.header("City")
        st.title(data.overall_year(select_county)[1])

    col4, col5, col6 = st.columns(3)

    with col4:
        st.header("Players")
        st.title(data.overall_year(select_county)[3])
    with col5:
        st.header("Sport")
        st.title(data.overall_year(select_county)[4])
    
    with col6:
        st.header("Edtions")
        st.title(data.overall_year(select_county)[5])

elif user_selection=='Country_wise Analysis' and select_year!='Over All Years' and select_county !="Over All Country's":
    st.title("Analysis by " + str(select_year) + ' and ' +  str(select_county))
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Total Events")
        st.title(data.overall_year_county(select_county,select_year)[0])
    with col2:
        st.header("Country")
        st.title(data.overall_year_county(select_county,select_year)[2])
    with col3:
        st.header("City")
        st.title(data.overall_year_county(select_county,select_year)[1])

    col4, col5, col6 = st.columns(3)

    with col4:
        st.header("Players")
        st.title(data.overall_year_county(select_county,select_year)[3])
    with col5:
        st.header("Sport")
        st.title(data.overall_year_county(select_county,select_year)[4])
    
    with col6:
        st.header("Edtions")
        st.title(data.overall_year_county(select_county,select_year)[5])

# ---------End-----------

if user_selection=='Athlete_wise' and select_year=='Over All Years' and select_county =="Over All Country's" and select_player=='Over All Athlete':
    st.title('Analysis Athlete_wise 🏃‍♂️🏃‍♀️')

    st.dataframe(data.a[['Name','Sport','Year','Gold','Silver','Bronze','total']])

elif user_selection=='Athlete_wise' and select_year!='Over All Years' and select_county =="Over All Country's" and select_player=='Over All Athlete':
    st.dataframe(data.grup_year(select_year),width=550)
elif user_selection=='Athlete_wise' and select_year =='Over All Years' and select_county !="Over All Country's" and select_player=='Over All Athlete':
    st.dataframe(data.grup_country(select_county),width=550)
elif user_selection=='Athlete_wise' and select_year !='Over All Years' and select_county !="Over All Country's" and select_player=='Over All Athlete':
    st.dataframe(data.grup_c_y(select_county,select_year),width=550)
elif user_selection=='Athlete_wise' and select_year =='Over All Years' and select_county =="Over All Country's" and select_player!='Over All Athlete':
    st.dataframe(data.grup_c_y_a(select_player),width=550)
elif user_selection=='Athlete_wise' and select_year !='Over All Years' and select_county !="Over All Country's" and select_player!='Over All Athlete':
     st.dataframe(data.grup_c_y_aa(select_county,select_year,select_player),width=550)
