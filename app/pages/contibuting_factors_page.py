import streamlit as st
import plotly.express as px


st.title("Contributing Factors to Happiness Score")
st.write(
    "Explore the factors that contribute to happiness scores across different countries and regions."
)


def trend_chart(df, column, trend):
    if trend == "General":
        fig = px.scatter(
            df.loc[
                (df["Region"].isin(st.session_state.region_select))
                & (df["Year"].isin(st.session_state.year_select))
            ],
            x=column,
            y="Happiness Score",
            hover_name="Country",
            trendline="ols",
            # title=f"Happiness Score vs. {column}",
        )
    else:
        fig = px.scatter(
            df.loc[
                (df["Region"].isin(st.session_state.region_select))
                & (df["Year"].isin(st.session_state.year_select))
            ],
            x=column,
            y="Happiness Score",
            color=trend,
            hover_name="Country",
            trendline="ols",
            # title=f"Happiness Score vs. {column}",
        )
    return fig


with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.multiselect(
            "Select Region:",
            options=sorted(st.session_state.df["Region"].unique()),
            default=sorted(st.session_state.df["Region"].unique()),
            key="region_select",
        )
    with col2:
        st.multiselect(
            "Select Year/s:",
            options=sorted(st.session_state.df["Year"].unique()),
            default=sorted(st.session_state.df["Year"].unique()),
            key="year_select",
        )
    st.segmented_control(
        "Select a trend:",
        options=[
            "General",
            "Region",
            "Year",
        ],
        default="General",
        key="trend_select",
    )

with st.container(border=True):
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Happiness Score vs. Economy (GDP per Capita)")
        fig = trend_chart(
            st.session_state.df,
            "Economy (GDP per Capita)",
            st.session_state.trend_select,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Happiness Score vs. Health (Life Expectancy)")
        fig = trend_chart(
            st.session_state.df,
            "Health (Life Expectancy)",
            st.session_state.trend_select,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Happiness Score vs. Trust (Government Corruption)")
        fig = trend_chart(
            st.session_state.df,
            "Trust (Government Corruption)",
            st.session_state.trend_select,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.subheader("Happiness Score vs. Family")
        fig = trend_chart(
            st.session_state.df,
            "Family",
            st.session_state.trend_select,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Happiness Score vs. Freedom")
        fig = trend_chart(
            st.session_state.df,
            "Freedom",
            st.session_state.trend_select,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Happiness Score vs. Generosity")
        fig = trend_chart(
            st.session_state.df,
            "Generosity",
            st.session_state.trend_select,
        )
        st.plotly_chart(fig, use_container_width=True)


# st.subheader("Factor influence on Happiness Score")
# fig = px.density_heatmap(
#     st.session_state.df,
#     x=st.session_state.factor_select,
#     y="Happiness Score",
#     # color="Happiness Rank",
#     title=f"Happiness Score vs. {st.session_state.factor_select}",
# )
# st.plotly_chart(fig, use_container_width=True)
