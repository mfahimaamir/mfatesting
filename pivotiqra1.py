import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
import matplotlib.pyplot as plt
import numpy
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
import pandas as pd
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
st.html("""
    <style>
        .stMainBlockContainer {
            max-width:350rem;
            max-hight:10rem;
        }
    </style>
    """
)



#url12 = "https://docs.google.com/spreadsheets/d/1TrljfQUEw2cEiYUOyXXfH7u0VF0IDARZ/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
#url12 = "https://docs.google.com/spreadsheets/d/1j4zRBnAb1nXi4NMMC8NEnEZMBVTW2oje/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
url12 = "https://docs.google.com/spreadsheets/d/1j4zRBnAb1nXi4NMMC8NEnEZMBVTW2oje/edit?pli=1&gid=92713901#gid=92713901"
file_id122 = url12.split("/")[-2]
path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
            #sce = pd.read_excel(path1)
iqradata = pd.read_excel(path1122)

        #st.write(st.session_state.df92 )
        #datag = st.session_state.df92


#@st.cache_data()
def load_data():
    #data = pd.read_excel("C:/mfa/exportpv.xlsx")
    #data = pd.read_excel('c:\mfa\iqradata.xlsx')
    data= iqradata
    #data = pd.read_csv("./data.csv", parse_dates=["referenceDate"])
    return data

data = load_data()



shouldDisplayPivoted = st.checkbox("Pivot data on Reference Date",True)
tab1, tab2, tab3, tab4 , tab5, tab6= st.tabs(["View-1", "View-2", "View-3", "View-4", "View-5", "View-6"])
#tab1, tab2, tab3, tab4 = st.tabs(["View-1", "View-2", "View-3", "View-4"])

with tab1:
#with st.expander("Pivot -1 "):
    gb = GridOptionsBuilder()

    gb.configure_default_column(
        resizable=True,
        filterable=True,
        sortable=True,
        editable=False,
    )
    gb.configure_column(
        field="Campus", header_name="Campus", width=80, rowGroup=shouldDisplayPivoted
    )

    gb.configure_column(
        field="Faculty",
        header_name="Faculty",
        flex=1,
        tooltipField="Faculty",
        rowGroup=shouldDisplayPivoted,
        #rowGroup=True if shouldDisplayPivoted else False,
    )
    gb.configure_column(
        field="Career",
        header_name="Career",
        width=110,
        rowGroup=shouldDisplayPivoted,
    )

    #Campus	Faculty	Career	Program	ctype	semister	credithh		
    gb.configure_column(
        field="Program",
        header_name="Program",
        width=150,
        tooltipField="Program",
        rowGroup=shouldDisplayPivoted,
    )
    gb.configure_column(
        field="ctype",
        header_name="ctype",
        width=150,
        tooltipField="ctype",
        rowGroup=shouldDisplayPivoted,
    )

    #field="dat32 ReferenceDate",
    #valueGetter="new Date(data.referenceDate).getFullYear()",
    gb.configure_column(
        field="semister",
        header_name="semister",
        #valueGetter="ctype",
        valueGetter="(data.semister)",
        pivot=True,
        hide=True,
    )


    #valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",

    gb.configure_column(
        field="credithh",
        #header_name="Volume [MWh]",
        header_name="credithh",
        width=100,
        type=["numericColumn"],
        aggFunc="sum",
        valueFormatter="value.toLocaleString()",
    )

    gb.configure_grid_options(
        tooltipShowDelay=0,
        pivotMode=shouldDisplayPivoted,
    )

    gb.configure_grid_options(
        autoGroupColumnDef=dict(
            minWidth=300, 
            pinned="left", 
            cellRendererParams=dict(suppressCount=True)
        )
    )
    go = gb.build()

    AgGrid(data, gridOptions=go, width =1900 ,height=400)
    
with tab2:
    gb = GridOptionsBuilder()

    gb.configure_default_column(
        resizable=True,
        filterable=True,
        sortable=True,
        editable=False,
    )
    gb.configure_column(
        field="Campus", header_name="Campus", width=80, rowGroup=shouldDisplayPivoted
    )

    gb.configure_column(
        field="Faculty",
        header_name="Faculty",
        flex=1,
        tooltipField="Faculty",
        rowGroup=shouldDisplayPivoted,
        #rowGroup=True if shouldDisplayPivoted else False,
    )
    gb.configure_column(
        field="Career",
        header_name="Career",
        width=110,
        rowGroup=shouldDisplayPivoted,
    )

    #Campus	Faculty	Career	Program	ctype	semister	credithh		
    gb.configure_column(
        field="Program",
        header_name="Program",
        width=150,
        tooltipField="Program",
        rowGroup=shouldDisplayPivoted,
    )
    
    #field="dat32 ReferenceDate",
    #valueGetter="new Date(data.referenceDate).getFullYear()",
    gb.configure_column(
        field="semister",
        header_name="semister",
        #valueGetter="ctype",
        valueGetter="(data.semister)",
        pivot=True,
        hide=True,
    )

    gb.configure_column(
            field="ctype",
            header_name="ctype",
            #valueGetter="ctype",
            valueGetter="(data.ctype)",
            pivot=True,
            hide=True,
        )

    #valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",

    gb.configure_column(
        field="credithh",
        #header_name="Volume [MWh]",
        header_name="credithh",
        width=100,
        type=["numericColumn"],
        aggFunc="sum",
        valueFormatter="value.toLocaleString()",
    )

    gb.configure_grid_options(
        tooltipShowDelay=0,
        pivotMode=shouldDisplayPivoted,
    )

    gb.configure_grid_options(
        autoGroupColumnDef=dict(
            minWidth=300, 
            pinned="left", 
            cellRendererParams=dict(suppressCount=True)
        )
    )
    go = gb.build()

    AgGrid(data, gridOptions=go, width =1900 ,height=400)
with tab3:
    t = pivot_ui(data)

    with open(t.src) as t:
        components.html(t.read(), width=900, height=1000, scrolling=True)


with tab4:
    st.write(iqradata)
    table = pd.pivot_table(iqradata, values ='credithh', index =['Campus',	'Faculty',	'Career',	'Program'], 
                         columns =['ctype',	'semister'], aggfunc = np.sum) 
    st.header("=================Pivot -1=================== ")
    st.write(table)
    table1 = pd.pivot_table(iqradata, values ='credithh', index =['Campus',	'Faculty',	'Career',	'Program'], 
                         columns =['semister','ctype'], aggfunc = np.sum) 
    st.header("=================Pivot -2=================== ")
    st.write(table1)
    table2 = pd.pivot_table(iqradata, values ='credithh', index =['Campus',	'Faculty',	'Career',	'Program','ctype'], 
                         columns =['semister'], aggfunc = np.sum) 
    st.header("=================Pivot -3=================== ")
    st.write(table2)


with tab5:
#        'Campus',	'Faculty',	'Career',	'Program',	'ctype',	'semister'	credithh

    table3 = iqradata.groupby(['Campus',	'Faculty',	'Career',	'Program']).apply(lambda sub_df:
    sub_df.pivot_table(index=['ctype'],columns =['semister'], values=['credithh'], aggfunc='sum', margins=True))
    st.write(table3)
with tab6:
    dfg = pd.DataFrame(dict(
        Business='MUHAMMAD;FAHIM;AAMIR;Beauty & Spas;Burgers-Restaurants;Pizza;Mexican Restaurants;Modern European-Restaurants;Chineese'.split(';'),
        aniticipation=[0] * 9,
        enjoyment=[6., 1., 6., 33.,150., 19.5, 9, 43, 81],
        sad=[1., 2., 1., 3., 13.5, 3, 4, 2, 11],
        disgust=[1, 1, 0, 3, 37, 3, 89, 32, 41],
        anger=[1.5, 2.1, 4.2, 9.4, 19.3, 3.5, 3.8, 3, 1.7],
        surprise=[3, 0, 0, 2, 12, 1, 29, 32, 11],
        fear=[0, 1, 1, 9, 22, 1, 19, 52, 21],
        trust=[0] * 9
    ))

    st.write(dfg)
    fig, axes = plt.subplots(3, 3, figsize=(10, 6))
    #fig, axes = plt.subplots(2, 3, figsize=(10, 6))

    for i, (idx, row) in enumerate(dfg.set_index('Business').iterrows()):
        ax = axes[i // 3, i % 3]
        row = row[row.gt(row.sum() * .01)]
        ax.pie(row, labels=row.index, autopct='%1.1f%%',startangle=30)
        ax.set_title(idx)
        #plt.legend()
        

    fig.subplots_adjust(wspace=.2)

    st.pyplot(plt)


