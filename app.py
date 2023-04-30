import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_card import card

load_keywords = pickle.load(open("keywords.pkl", 'rb'))
load_similarity = pickle.load(open("similarity.pkl",'rb'))

load_data4 = pickle.load(open("data4.pkl",'rb'))
load_data5 = pickle.load(open("data5.pkl",'rb'))

data4 = pd.DataFrame(load_data4)
data5 = pd.DataFrame(load_data5)

final_data = data5.join(data4["info"])



# st.title("Your Recommendations Displays here......")


def recommend(keyword):
    keyword = keyword.lower()
    places_index = []
    similar = np.array([])
    simi_indexs = []

    if(final_data["info"].str.contains(keyword).any()):
        places_index.append(final_data[final_data["info"].str.contains(keyword)].index[0])

        if len(places_index)==1:
            similar = load_similarity[places_index]

            simi_indexs = sorted(list(enumerate(similar[0])),reverse=True,key=lambda x:x[1])[1:11]
        else:
#             print(places_index)
            similar = load_similarity[places_index[0]]
            simi_indexs = sorted(list(enumerate(similar[0])),reverse=True,key=lambda x:x[1])[1:11]

    else:
        print("Opps ! Please try Different Keyword")


    return simi_indexs


# def get_image(img_name):
#     url=""
#     params["q"] = img_name
#     search = GoogleSearch(params)
#     res = search.get_dict()
#     if len(res["inline_images"]) ==0:
#         url= "https://www.udacity.com/blog/wp-content/uploads/2021/02/img8.png"
#     else:
#         url = res["inline_images"][0]["thumbnail"]
#     return url


def get_allkeys(keylist):
    for i in keylist:
        print("======================")
        out= recommend(i)
        # print(type(out))
        # print(out)
        # cnt =0

        # col1, col2 = st.columns(2)
        # j = 0
        # for i in out:
        #     while j<10:
        #         with col1:
        #             titl = final_data.iloc[i[0],1]
        #             txt = final_data.iloc[i[0],0] + " " + final_data.iloc[i[0],3]
        #             card(title=titl,text=txt,key=j)
        #         j =j+1
        #         with col2:
        #             titl = final_data.iloc[i[0],1]
        #             txt = final_data.iloc[i[0],0] + " " + final_data.iloc[i[0],3]
        #             card(title=titl,text=txt,key=j)
        #         j = j+1

        with st.expander(i.upper()):
            for i in out:
                titl = final_data.iloc[i[0],1]
                txt = final_data.iloc[i[0],0] + " " + final_data.iloc[i[0],3]
                card(title=titl,text=txt,key=i[0])



def pass_keywords():
    get_allkeys(sel_keywords)

st.sidebar.header("Travel Recommender System(India)")


sel_keywords = st.sidebar.multiselect("Enter Kyewords", load_keywords, default=None,key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", max_selections=None)
st.sidebar.button("Recommend", on_click=pass_keywords)

