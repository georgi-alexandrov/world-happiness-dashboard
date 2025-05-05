import streamlit as st
import plotly.express as px


st.title("The Countries with Highest and Lowest Happiness ")
st.write(
    "Explore the happiest and least happy countries based on the average happiness score from 2015 to 2019."
)

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("📈 The 10 countries with highest happiness score")
            st.write("Based on the average happiness score from 2015 to 2019.")
            top_10_total = (
                st.session_state.df.groupby("Country")["Happiness Score"]
                .mean()
                .nlargest(10)
                .reset_index()
            )
            st.write("")
            fig = px.bar(
                top_10_total,
                x="Happiness Score",
                y="Country",
                color="Country",
                color_discrete_map=st.session_state.color_map,  # Apply consistent color mapping
                template="plotly_dark",
                orientation="h",  # Make the bars horizontal
                range_x=[
                    top_10_total["Happiness Score"].min() - 0.05,
                    top_10_total["Happiness Score"].max() + 0.05,
                ],
            )
            fig.update_layout(
                xaxis_title="Happiness Score",  # Label for the scores
                yaxis=dict(tickmode="linear"),  # Ensure all countries are displayed
                showlegend=False,  # Hide legend
            )
            st.plotly_chart(fig, use_container_width=True)
            st.write("")
            st.write("")

    with col2:
        with st.container(border=True):
            st.subheader("The 10 happiest countries per year")
            st.selectbox(
                "Select a year:",
                options=st.session_state.df["Year"].unique(),
                index=0,
                key="top_10_year_select",
            )
            top_10_year = (
                st.session_state.df[
                    st.session_state.df["Year"] == st.session_state.top_10_year_select
                ]
                .groupby("Country")["Happiness Score"]
                .mean()
                .nlargest(10)
                .reset_index()
            )
            fig = px.bar(
                top_10_year,
                x="Happiness Score",
                y="Country",
                color="Country",
                color_discrete_map=st.session_state.color_map,  # Apply consistent color mapping
                template="plotly_dark",
                orientation="h",  # Make the bars horizontal
                range_x=[
                    top_10_year["Happiness Score"].min() - 0.05,
                    top_10_year["Happiness Score"].max() + 0.05,
                ],
            )
            fig.update_layout(
                xaxis_title="Happiness Score",  # Label for the scores
                yaxis=dict(tickmode="linear"),  # Ensure all countries are displayed
                showlegend=False,  # Hide legend
            )
            st.plotly_chart(fig, use_container_width=True)


with st.container(border=True):
    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            st.subheader("📉 The 10 countries with lowest happiness score")
            st.write("Based on the average happiness score from 2015 to 2019.")
            bottom_10_total = (
                st.session_state.df.groupby("Country")["Happiness Score"]
                .mean()
                .nsmallest(10)
                .reset_index()
            )
            st.write("")
            fig = px.bar(
                bottom_10_total,
                x="Happiness Score",
                y="Country",
                color="Country",
                color_discrete_map=st.session_state.color_map,  # Apply consistent color mapping
                template="plotly_dark",
                orientation="h",  # Make the bars horizontal
                range_x=[
                    bottom_10_total["Happiness Score"].min() - 0.05,
                    bottom_10_total["Happiness Score"].max() + 0.05,
                ],
            )
            fig.update_layout(
                xaxis_title="Happiness Score",  # Label for the scores
                yaxis=dict(tickmode="linear"),  # Ensure all countries are displayed
                showlegend=False,  # Hide legend
            )
            st.plotly_chart(fig, use_container_width=True)
            st.write("")
            st.write("")

    with col4:
        with st.container(border=True):
            st.subheader("The 10 least happy countries per year")
            st.selectbox(
                "Select a year:",
                options=st.session_state.df["Year"].unique(),
                index=0,
                key="bottom_10_year_select",
            )
            bottom_10_year = (
                st.session_state.df[
                    st.session_state.df["Year"]
                    == st.session_state.bottom_10_year_select
                ]
                .groupby("Country")["Happiness Score"]
                .mean()
                .nsmallest(10)
                .reset_index()
            )
            fig = px.bar(
                bottom_10_year,
                x="Happiness Score",
                y="Country",
                color="Country",
                color_discrete_map=st.session_state.color_map,  # Apply consistent color mapping
                template="plotly_dark",
                orientation="h",  # Make the bars horizontal
                range_x=[
                    bottom_10_year["Happiness Score"].min() - 0.05,
                    bottom_10_year["Happiness Score"].max() + 0.05,
                ],
            )
            fig.update_layout(
                xaxis_title="Happiness Score",  # Label for the scores
                yaxis=dict(tickmode="linear"),  # Ensure all countries are displayed
                showlegend=False,  # Hide legend
            )
            st.plotly_chart(fig, use_container_width=True)


# fig = px.scatter_geo(
#     st.session_state.df,
#     locations="Country",
#     locationmode="country names",
#     color="Region",
#     hover_name="Country",
#     size="Happiness Score",
#     animation_frame="Year",
#     projection="natural earth",
#     title="World Happiness Report (2015-2019)",
#     template="plotly_dark",
#     color_discrete_map=st.session_state.color_map,  # Apply consistent color mapping
#     height=600,
#     size_max=40,
# )
# st.plotly_chart(fig, use_container_width=True)
