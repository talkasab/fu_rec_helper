import streamlit as st

st.header("Recommending MR Pelvis")

"""
Recommending MR Pelvis requires extra attention. There are three types of MRI pelvis
that can be ordered (GIGU, GYN, or Bone). Please pick the appropriate body part in the
PowerScribe Follow-up Recommendations tool when creating the recommendation. While 
your report text can have the wording that you think is helpful to the clinician, 
specific body parts must be picked in the Follow-up Recommendations dialog to lead 
to the correct downstream Epic order for the patient.  
 
For instance, if you would like your patient to obtain a MRI bony pelvis, you can 
state so in your report. However, in PowerScribe Follow-up Recommendations tool, pick 
"sacroiliac joints" or "coccyx".
"""

col1, col2 = st.columns([3, 1])
with col1:
    """ We suggest referring to the Recommendables page when making recommendations given 
that this process is still new."""

with col2:
    st.page_link(
        "recommendables.py",
        label="Recommendables",
        icon=":material/help:",
    )

st.divider()

st.subheader("MRI GIGU Pelvis")
col1, col2 = st.columns(2)
with col1:
    """
    To recommend a MR Pelvis GIGU, please use the following body parts 
    in the PowerScribe Follow-up Recommendations tool:"""

with col2:
    """
    Modality | Body Part
    --- | ---
    MR | Bladder
    MR | Pelvis - Lymph Node
    MR | Testis
    """

st.subheader("MRI Bony Pelvis")
col1, col2 = st.columns(2)
with col1:
    """
    To recommend a MR Pelvis Bone, please use the following body parts 
    in the PowerScribe Follow-up Recommendations tool:"""

with col2:
    """
    Modality | Body Part
    --- | ---
    MR | Coccyx
    MR | Sacroiliac Joints
    """

st.subheader("MR Gyn Pelvis")
col1, col2 = st.columns(2)
with col1:
    """
    To recommend a MR Pelvis Gyn, please use the following body parts 
    in the PowerScribe Follow-up Recommendations tool:"""

with col2:
    """
    Modality | Body Part
    --- | ---
    MR | Fallopian Tube
    MR | Female Genital Tract
    MR | Uterus
    MR | Vagina
    """
