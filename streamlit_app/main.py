import streamlit as st
from streamlit_option_menu import option_menu
import db
from queries import *
import auth_lib
from db_schema_helpers import *
# horizontal Menu
# selected2 is the page the user goes to
data_url = 'https://cdn.dribbble.com/users/4567683/screenshots/9244379/media/1879a9614122f80d5cd6d1b315974fa3.gif'
#st.markdown(f"![Alt Text]({data_url})")
selected2 = option_menu(None, ["Search", "Popular Recipes", "About", "Login/SignUp"],
icons=['search', 'star', 'cloud-upload', 'user'],
menu_icon="cast", default_index=0, orientation="horizontal")
res_list = []
# check logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['user_obj'] = {}
if 'posts' not in st.session_state:
    st.session_state['posts'] = []
if not(st.session_state['logged_in']):
    st.info('Please login to rate the recipes!', icon="ℹ️")
if selected2 == "Home":
    st.write('you are at Home')
elif selected2 == "About":
    # prints out the md file
    with open('../README.md') as f:
        st.markdown(f.read())
elif selected2 == "Search":
    query = st.text_input('Keywords', placeholder = "chicken, salt, pepper")
    genre = st.radio("Type", ('By Ingredients', 'By Recipe'))
    restrictions = st.multiselect("Restrictions", ('Alcohol-Cocktail', 'Alcohol-Free', 'Celery-Free', 'Crustacean-Free', 'Dairy-Free', 'DASH', 'Egg-Free', 'Fish-Free', 'FODMAP-Free', 'Gluten-Free', 'Immuno-Supportive', 'Keto-Friendly', 'Kidney-Friendly', 'Kosher', 'Low Potassium', 'Low Sugar', 'Lupine-Free', 'Mediterranean', 'Mollusk-Free', 'Mustard-Free', 'No Oil Added', 'Paleo', 'Peanut-Free', 'Pecatarian', 'Pork-Free', 'Red-Meat-Free', 'Sesame-Free', 'Shellfish-Free', 'Soy-Free', 'Sugar-Conscious', 'Sulfite-Free', 'Tree-Nut-Free', 'Vegan', 'Vegetarian', 'Wheat-Free'))
    count = st.slider('Number of Recipes', 1, 25, 5)
    if st.button('refresh'):
        st.experimental_rerun()
    #st.write(f'you searched for {query}')
    search_items = list(map(lambda x: x.strip(), query.split(',')))
    query_string = ''
    resp = []
    # create restrictions string
    restriction_params = []
    # create restrictions string
    restriction_filters = ''
    for c, r in enumerate(restrictions):
        if(c == 0):
            restriction_filters += f"AND (D.name = %s "
        else:
            restriction_filters += f"OR D.name = %s "
        restriction_params.append(r)
    if(len(restrictions)):
        restriction_filters += ")"
        
    if genre == 'By Ingredients':
        # search by ingredient
        # construct query
        query_string = ''
        res_list = []
        added = False
        if search_items[0] == '':
            st.error('You must search for something!')
        else:
            for item in search_items:
                sub_q_params = [f'%{item}%']
                sub_q = food_to_recipe_id
                query_string = recipe_from_id.format(f'({sub_q})', restriction_filters) 
                if len(restrictions):
                    query_string += f' AND P.cnt = %s'
                    sub_q_params.extend(restriction_params)
                    sub_q_params.append(len(restrictions))
                resp = db.query(query_string, sub_q_params)
                if added:
                    res_list = list(set(res_list) & set(resp))
                else:
                    res_list = resp
                    added = True
    else:
        # construct query
        if search_items[0] == '':
            st.error('You must search for something!')
        elif len(search_items) > 1:
            st.error('Multiple recipe searches: This feature is not supported.')
            st.stop()
        else:  
            sub_q_params = [f'%{search_items[0]}%']
            sub_q = recipe_to_recipe_id
            # get recipe objects
            query_string = recipe_from_id.format(f'({sub_q})', restriction_filters) 
            if len(restrictions):
                query_string += f' AND P.cnt = %s'
                sub_q_params.extend(restriction_params)
                sub_q_params.append(len(restrictions))
            res_list = db.query(query_string, sub_q_params)
    ###PRINT POSTS###
    st.write(f"{min(len(res_list), count)} recipes found.")
    rec_table_to_posts(res_list[:count])
elif selected2 == "Login/SignUp":
    if st.session_state['logged_in']:
        st.write('You are logged in as {}.'.format(
            (st.session_state['user_obj'])['username']
        ))
        if st.button('Logout'):
            st.session_state['logged_in'] = False
            st.session_state['user_obj'] = {}
            st.experimental_rerun()
    else:
        LoginSignUpT = st.radio("Type", ('Login', 'SignUp'))      
        if LoginSignUpT == 'Login':
            with st.form("search_form"):
                username = st.text_input('Username')
                password = st.text_input("Password", type="password", key="password", max_chars=71)
                submitted = st.form_submit_button("Sign In")
            if submitted:
                user_obj = auth_lib.validatePassword(username, password)
                if user_obj:
                    st.session_state['logged_in'] = True
                    st.session_state['user_obj'] = user_obj
                    st.success('Done!')
                    st.experimental_rerun()
                else:
                    st.error('Invalid Credentials')
        elif LoginSignUpT == 'SignUp':
            with st.form("detail_form"):
                username = st.text_input('Username')
                email = st.text_input('email')
                password = st.text_input("Password", type="password", key="password")
                password2 = st.text_input("Re-enter Password", type="password", key="password2")
                submitted = st.form_submit_button("Sign Up")
            if submitted:
                # verify
                if password != password2:
                    st.error('Passwords do not match!')
                else:
                    u_obj = auth_lib.createUser(username, email, password, 'test.url')

                    if u_obj != []:
                        st.session_state['logged_in'] = True
                        st.session_state['user_obj'] = u_obj
                        print(st.session_state['user_obj'])
                        st.success('Done, You are logged in!')
                        st.experimental_rerun()
                    else:
                        st.error('Error In Account Creation')
elif selected2 == "Popular Recipes":
    count = st.slider('Browse the top recipes:', 1, 25, 5)
    tresp = db.query(get_top_n_recipes, (count))
    remaining = count - len(tresp)
    tresp2 = db.query(get_unrated_recipes, (remaining))
    resp = tresp + tresp2
    ###PRINT POSTS### MIGHT BE UNORDERED
    rec_table_to_posts(resp, popr=True, add_index=True)