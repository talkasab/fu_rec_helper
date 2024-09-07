import streamlit as st

st.header("Recommendation Dashboard")

col1, col2 = st.columns([2, 1])
with col1:
    """
Radiologist recommendation history can now be viewed via a dashboard site.
  """

with col2:
    st.page_link(
        "https://csrraddash.partners.org/",
        label="Dashboard Site (MGB Network Only)",
        icon=":material/dashboard:",
    )

st.image("images/dashboard.png", use_column_width=True)

"""
- Use MGB username/password to log in
- Shows prior recommendations, both those which are well-formed and those which will require an addendum. 
- Periodically updates automatically
- New recommendations will appear in the dashboard between 2 and 5 minutes of being made

_(Unfortunately, unactionable recommendations don't update automatically once the addendum has been made yet—
this feature will be added in the future.)_
"""
