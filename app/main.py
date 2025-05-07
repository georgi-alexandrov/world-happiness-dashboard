import os
import streamlit as st
import plotly.express as px
from data_management import get_data


def main():
    st.set_page_config(
        layout="wide",
        page_title="World Happiness Dashboard",
        page_icon="🌍",
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://github.com/georgi-alexandrov/world-happiness-dashboard",
            "Report a bug": "https://github.com/georgi-alexandrov/world-happiness-dashboard/issues",
            "About": "This is a dashboard to explore the world happiness data from 2015 to 2019.",
        },
    )
    st.session_state.df = get_data()
    st.session_state.color_map = {
        country: color
        for country, color in zip(
            st.session_state.df["Country"].unique(),
            px.colors.qualitative.Plotly,  # Use Plotly's qualitative color palette
        )
    }

    st.sidebar.image(os.path.join(os.path.dirname(__file__), "assets/logo.png"), width=200, use_container_width=True)
    st.sidebar.markdown(
        """
        <div style="text-align: center;">
            <h2>World Happiness Dashboard</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar.expander("ℹ️ Data Overview", expanded=True):
        st.write(
            "Explore the world happiness data! "
            f"This dashboard provides insights into the world happiness data from {st.session_state.df['Year'].min()} to {st.session_state.df['Year'].max()}. "
            f"Happiness Scores and 6 explanatory factors from {len(st.session_state.df['Country'].unique())} countries across {len(st.session_state.df['Region'].unique())} regions. "
            "You can explore the data by different countries, regions, and years."
        )
    st.sidebar.write()

    main_page = st.Page("pages/top_ten_page.py", title="Top 10", icon="🌐")  # "🌍"
    second_page = st.Page("pages/trend_page.py", title="Trends", icon="📊")  # "💹"
    third_page = st.Page(
        "pages/contibuting_factors_page.py",
        title="Contributing factors",
        icon="✨",  # 💡🌟💭
    )
    pg = st.navigation([main_page, second_page, third_page])

    pg.run()


if __name__ == "__main__":
    main()
