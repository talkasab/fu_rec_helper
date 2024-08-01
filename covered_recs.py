import streamlit as st

st.header("Covered Recommendations", divider=True)

"""
The tool and the program are best-suited to creating and managing recommendations
for follow-up imaging exams. However, the tool can be used to create other kinds of 
recommendations, such as:
"""

col1, col2 = st.columns([3, 1])
with col1:
    """
    - Specific use of contrast (“With Contrast” report code) or arthrogram (“Arthrogram” report code)
    - Specialized protocols (“CT Abdomen Pelvis Hypervascular Tumor Protocol”, “MR Pituitary”)
    - Special handling for recommendations that shouldn’t be semi-automatically ordered but require human management
    """
col2.page_link(
    "vid_report_code.py", label="Adding a Report Code", icon=":material/movie:"
)
col2.page_link(
    "recommendables.py", label="All Recommendable Exams", icon=":material/table:"
)

col1, col2 = st.columns([3, 1])
with col1:
    """
      - Interventional procedures such as biopsies (use “Image-guided biopsy” modality), 
        echocardiography, endoscopy, etc.
      - Consults (use “Consult” modality)
    """
col2.page_link(
    "vid_recommend_consult.py", label="Recommending a Consult", icon=":material/movie:"
)

"""
It is not expected that radiologists will create structured recommendations for 
lab values, suggestions for comparison with other previous imaging, or other 
clinical correlations. These recommendations can still be included in the text of
the report, but they do not need to be formalized with the Follow-up Recommendations 
tool.
"""
