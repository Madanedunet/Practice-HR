import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(menu_title="main menu",
        options=[
            'home',
            'spam exploration',
            'word cloud analysis',
            
        ],
        icons=['house-fill',
               'journal',
               'rocket takeoff'
               ],

               default_index=0,

    )

    if(selected == 'home'):
        st.title('home')

    if(selected == 'spam exploration'):
        st.title('spam exploration')

    if(selected == 'word cloud analysis'):
        st.title('word cloud analysis')