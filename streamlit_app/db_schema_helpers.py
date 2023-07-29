import streamlit as st
from PIL import Image
import random
import db
from queries import *
import requests
from io import BytesIO

# This function is used to output each of the recipe cards given a db response of a recipe table resp.
# add_index is a boolean flag if we want to have some sort of order mentioned on the card (eg. most popular recipes in order).
def rec_table_to_posts(resp, popr = False, add_index=False):
    user_signed_in = st.session_state['logged_in']
    for c, item in enumerate(resp):
            image_container, description_container = st.columns([2, 2])
            with image_container:
                # col_name: image
                # change this later.. need to fetch the file first
                #req = requests.get('https://edamam-product-images.s3.amazonaws.com/web-img/4d9/4d9084cbc170789caa9e997108b595de.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLWVhc3QtMSJIMEYCIQD89Ju68aFuhrgk%2BH4kkSuMZbBl2vpwu9swq2hPZafnLQIhAJBLSHhxSs9ojFw%2FXkZwii0jcSWmjwowzeTSMJ0hBrfTKswECGQQABoMMTg3MDE3MTUwOTg2IgwGz1sQPrzGhYIiYdIqqQRMZQjSzXBYs4QuwzzRI0KiqGIfPNIT1QG8oUVDnVyQS1Ew%2BA%2F2IgoJWAtx0%2BN9TI%2BiKvTL19BB6Z2EkapLEZCNDagbdGF02rE4dN0czpcZfXc0%2B%2BKJ4C35Bvv154Jgbc7n%2B8tdPkqtrnNI4torKN%2BZVPyNn2mq81vUIz4z%2Ba71n4w%2Bh4%2FF%2FBuI2DpW41bZu7QM1JhRG3jwZpHbs%2Bru8wnsijJWewMtUTiqLeGFKyCZt16DIpsuwsSkYLjmQUc3EvrlkA2UodQyIsbrNWqTnsyjlfQ3Or44D3U%2FOdx18gLd4A2zfWMU9i%2B9NyvVF%2BGm4sH15ZYDBqqaWyHflsBep7iLzMOF%2FdQ4ZQrVCEGNnSoYOuXXLP0Rdk3br5nPt5BA80B%2BIbC4mrTYZ5iMRjoFgaL4lLys4tnLkk5gHFUofmascJqwYsflF%2FRuNh7OaOouUHy1dr5Bo53OQy9t%2B7S88Z9RTzsmzVsF%2BUt0DTvtc7Sz4iNlL6srF3%2FrsX30L3AtWytxpXdD53hacyuYOe2k4eSlycuK4efzBAUDx2AvnQNtEkHVAfHyUJ4%2BcLILtV6Lc7ZFx3B6Md3DAP4aF7RbFNECGK7AxB8bb3J35YI4U8cljOJ%2FuWnnihV0at2nU83NDOWqoRWsQpGNHaeTyFmOWFB2EXrwggV05khayS0XYd38H0gCuA2WptRdxzg58pv2a3Mx5C71EOBAKnFqG1WbS5ku1At4bp7KY%2FQ4MKL5r5sGOqgBQLZw8G4rQyWC56XWxYdMs1p6vcUEDQsSogL5HT2peNsloDmscfA2oIF4MCrRFFs3wviDL9bdsI1vbt1qvAVg3QgYd7Set3hQlQo3BWSzmGvl1GGZ7Y9TiTIVV54r%2F%2B4i5Xaf2YZ1YIQAICNaQojtwBJ%2BEUMix5kpqT9Bdpwf0ouFXg73ipn9jpTt%2FafKWaiucMts68WrVdSiK%2Bq0v2L6E4kbCvMgMHkB&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221109T210457Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFP3RPKWZZ%2F20221109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a0b247f550a9f74483005df3aeb55a63ad3bc9fc12c3a185839b0d28bc12aff6')
                 #print(item[6])
                #image = Image.open(BytesIO(req.content))
                image = Image.open(f'../data/images/{item[6]}')#item[6])
                new_image = image.resize((600, 400))
                st.image(new_image)
            with description_container:
                # col_name: name
                if add_index:
                    st.text(f'#{c + 1}. {item[1]}')
                else:
                    st.text(item[1])
                # col_name: time
                #st.text(f'Prep Time: {item[4]} minutes')
                # col_name: calories
                st.text(f'Calories: {item[3]}')
                # col_name: cuisine
                st.text(f'Cuisine: {item[2].title()}')
                # col_name: rating
                if(popr):
                    if(len(item) > 8 and int(item[8])):
                        st.text(f'Average Rating: {round(item[8], 1)}')
                    else:
                        st.text(f'Average Rating: Not Rated')
                else:
                    if(len(item) > 7 and int(item[7])):
                        st.text(f'Average Rating: {round(item[7], 1)}')
                    else:
                        st.text(f'Average Rating: Not Rated')
                # query the rating of the recipe since it is in a different table
                check_rating = recipe_id_to_rating.format(item[0])
                res = db.query(check_rating)
                if res == []:
                    st.text('Number of Ratings: Not Rated Yet')
                else:
                    st.text(f'Number of Ratings: {res[0][0]}')
                st.write(f'[View Recipe Instructions]({item[5]})')
                # IF a user has signed in, provide them functionality to edit ratings.
                if user_signed_in:
                    with st.form('Rate' + str(c)):
                        number = st.number_input('Rate 1-5', min_value=1, max_value=5, value=5)
                        submitted = st.form_submit_button("Rate")
                        if submitted:
                            query_string = user_add_rating.format(st.session_state['user_obj']['id'], item[0], number, number)
                            print(query_string)
                            db.query(query_string, insert=True)
                            st.write("Thanks for your rating!")
                            #st.experimental_rerun()