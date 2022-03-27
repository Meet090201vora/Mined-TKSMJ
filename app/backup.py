import streamlit as st
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set_style("darkgrid")
#plt.style.use("dark_background")

st.title("Netflix for Researcher")
st.sidebar.title("OPTIONS")


# st.subheader("This application shows graphs for the given algorithms ")
# st.sidebar.markdown("This application is a ML algo dashboard ")
# show = st.sidebar.checkbox("SHOW")
# st.sidebar.subheader("ACCURACY OF MODELS")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
    width:50%;
    padding: 4%;
    margin-left:20%;
    corn
}
div.stButton > button:hover {
    background-color: #ff0000;
    # color:#ff0000;
}
#the-title {
  text-align: center;
}
# div.stTitle > title:first-child{
#     # font-size:10cm
#     text-align: centre;
# }
div.stTextInput>div>div>input {
    color: #ff0000;
}
</style>""", unsafe_allow_html=True)

# st.sidebar.title("ALGORITHMS")
button1 = st.sidebar.button("IEEE")
button2 = st.sidebar.button("Elsevier")
button4 = st.sidebar.button("Springer")
button3 = st.sidebar.button("IJSER")
button4 = st.sidebar.button("IJISRT")
button5 = st.sidebar.button("IJIRE")
button6 = st.sidebar.button("IJSRET")


# st.text("Search ")
# submit_search = st.form_submit_button(label='Search')

with st.form(key='searchform'):
    nav1,nav2,nav3,nav4 = st.columns(4)

    with nav1:
        search_title = st.text_input("Search Title")
    with nav2:
        search_author = st.text_input("Author")
    with nav3:
        search_date = st.date_input("Published After")#,datetime.date(2019, 7, 6))
    with nav4:
        st.text("Search ")
        submit_search = st.form_submit_button(label='Search')

    # st.success("You searched for {} in {}".format(search_term,location))
st.success("You searched for {} by {} published on {}".format(search_title,search_author,search_date))


if submit_search:
    st.write("Pressed Submit")









with st.form(key='searchform2'):
    # row1,row2,row3,row4 = st.rows(4)
    option=["Select one","AI","Computer Vision","xyz","xyz"]
    search_field = st.selectbox("Select one",option)
    search_input = st.text_input("Search")
    search_title = st.form_submit_button(label='Search Title')
    search_author = st.form_submit_button(label='Search Author')
    search_date = st.form_submit_button(label='Search Date')