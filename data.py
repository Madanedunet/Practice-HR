# import streamlit as st
# import numpy as np
# import pandas as pd
import json

# df = pd.DataFrame(
#     np.random.randn(50, 20),
#     columns=["cold" + str(i) for i in range(20)])
# # st.write(df)
# st.dataframe(df, width=200 , height=1000)
# # st.dataframe( np.random.randn(50, 20))

# # st.table(df)
# st.metric("TCS stock", value = "3220.70", delta = "19.10", delta_color= "off")

import random
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)


df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))


df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(12, 5), columns=["a", "b", "c", "d", "e"]
    )

event = st.dataframe(
    st.session_state.df,
    key="data",
    on_select="rerun",
    selection_mode=["multi-row", "multi-column"],
)

event.selection


df1 = pd.DataFrame(np.random.randn(50, 5), columns=("col %d" % i for i in range(5)))

my_table = st.table(df1)

df2 = pd.DataFrame(np.random.randn(50, 5), columns=("col %d" % i for i in range(5)))

my_table.add_rows(df2)
# Now the table shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
# Now the chart shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

st.vega_lite_chart({
    'mark': 'line',
    'encoding': {'x': {'field': 'a', 'type': 'quantitative'}, 'y': {'field': 'b', 'type': 'quantitative'}},
    'datasets': {
      'some_fancy_name': df1,  # <-- named dataset
    },
    'data': {'name': 'some_fancy_name'},
})

# To add rows, use the correct approach for Vega-Lite
# Streamlit currently does not support dynamic updates to Vega-Lite charts directly like this
# You might need to re-render the chart with the updated data
df_combined = pd.concat([df1, df2])
st.vega_lite_chart({
    'mark': 'line',
    'encoding': {'x': {'field': 'a', 'type': 'quantitative'}, 'y': {'field': 'b', 'type': 'quantitative'}},
    'data': {'values': df_combined.to_dict(orient='records')}
})

