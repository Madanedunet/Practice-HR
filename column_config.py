import pandas as pd
import streamlit as st

# data_df = pd.DataFrame(
#     {
#         "widgets":["st.selectbox","st.number_input","st.text_area","st.button"],
#     }
# )

# st.data_editor(
#     data_df,
#     column_config={
# column
        # "widgets":st.column_config.Column(
        #     "Streamlit Widgets",
        #    help="Streamlit **widget** commands 🎈",
        # #    help="Streamlit **widget** commands \U0001F388",
        #    width="medium",
        #    required=True,
        # )
    #     },
    #         hide_index=True,
    #         num_rows="dynamic",
    #  )

# Text Column
    #         "widgets": st.column_config.TextColumn(
    #             "widgets",
    #             help="Streamlt **widget** commands 🎈",
    #             default ="st.",
    #             max_chars=50,
    #             validate="^st\.[a-z_]+$",

    #         )
    # },
    #      hide_index=True,
        
    #  )

# NUMBER COLUMN

# data_df = pd.DataFrame(
#     {
#         "price":[20, 950, 250,500],
#     }
# )

# st.data_editor(
#     data_df,
#     column_config={
#         "price":st.column_config.NumberColumn(
#        "Price (in USD)",
#              help="The price of the product in USD",
#              min_value=0,
#              max_value=1000,
#              step=1,
#              format="$%d",
#          )
#      },
#      hide_index=True,
#  )



# st.column_config.CheckboxColumn

data_df = pd.DataFrame(
      {
        "widgets":["st.selectbox","st.number_input","st.text_area","st.button"],
        "favorite":[False, False, False, False],

    }
    
)

def update_favorites(selected_widget):
    data_df["favorite"] = data_df["widgets"] == selected_widget
  
selected_widget = st.radio(
    "Select your favorite widget",
    options=data_df["widgets"],
    index=data_df["favorite"].idxmax() if data_df["favorite"].any() else 0
)

# Update the DataFrame based on the selected widget
update_favorites(selected_widget)  
    
st.data_editor(
     data_df,
    column_config={
        "favorite":st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorute** widgets",
            default=False,
        )
    },
    disabled=["widgets"],
    hide_index=True,
)
   





# import pandas as pd
# import streamlit as st

# # Sample DataFrame with questions, options, and correct answers
# data_df = pd.DataFrame(
#     {
#         "question": [
#             "What is the capital of France?",
#             "What is 2 + 2?",
#             "Which language is primarily spoken in Brazil?",
#             "What color is the sky on a clear day?"
#         ],
#         "option_1": ["Berlin", "3", "Spanish", "Red"],
#         "option_2": ["Madrid", "4", "Portuguese", "Blue"],
#         "option_3": ["Paris", "5", "French", "Green"],
#         "option_4": ["Lisbon", "6", "English", "Yellow"],
#         "correct_answer": ["Paris", "4", "Portuguese", "Blue"]
#     }
# )

# # Function to display questions and get answers
# def display_questions():
#     user_answers = []
#     for index, row in data_df.iterrows():
#         st.write(row["question"])
#         answer = st.radio(
#             label="",
#             options=[row["option_1"], row["option_2"], row["option_3"], row["option_4"]],
#             key=f"question_{index}"
#         )
#         user_answers.append(answer)
#     return user_answers

# # Function to check answers
# def check_answers(user_answers):
#     score = 0
#     for i, row in data_df.iterrows():
#         if user_answers[i] == row["correct_answer"]:
#             score += 1
#     return score

# # Display the questions
# user_answers = display_questions()

# # Submit button to check answers
# if st.button("Submit"):
#     score = check_answers(user_answers)
#     st.write(f"Your score is {score}/{len(data_df)}")
#     st.write("Correct Answers:")
#     for index, row in data_df.iterrows():
#         st.write(f"Q{index + 1}: {row['correct_answer']}")

