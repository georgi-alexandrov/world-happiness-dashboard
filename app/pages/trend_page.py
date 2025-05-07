import streamlit as st
import plotly.express as px

st.title("Happiness and contributing factors - trends and comparison")
st.write(
    "Explore the trends and comparisons of happiness and contributing factors across different countries and regions."
)


def evolution_chart(df, column):
    """
    Create a line chart showing the evolution of a specified column over the years for selected countries and regions.
    """

    fig = px.line(
        df.loc[
            (df["Country"].isin(st.session_state.country_select))
            & (df["Region"].isin(st.session_state.region_select))
        ].sort_values(by="Year"),
        x="Year",
        y=column,
        color="Country",
        color_discrete_map=st.session_state.color_map,  # Apply consistent color mapping
        line_group="Country",
        hover_name="Country",
    )
    fig.update_layout(
        xaxis=dict(
            tickmode="linear",  # Use linear ticks
            dtick=1,  # Set tick interval to 1 year
            title="Year",  # Label for the x-axis
        )
    )
    if column == "Happiness Rank":
        fig.update_yaxes(
            title=column,
            autorange="reversed",  # Reverse the y-axis for rank
        )
    else:
        fig.update_yaxes(title=column)
    fig.update_traces(
        mode="lines+markers",
        marker=dict(size=8, opacity=0.8),
        line=dict(width=2, dash="solid"),
    )

    return fig


with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.multiselect(
            "Select Region:",
            options=sorted(st.session_state.df["Region"].unique()),
            default=sorted(st.session_state.df["Region"].unique())[0],
            key="region_select",
        )
    with col2:
        st.multiselect(
            "Select Countries:",
            options=sorted(
                st.session_state.df.loc[
                    st.session_state.df["Region"].isin(st.session_state.region_select),
                    "Country",
                ].unique()
            ),
            default=sorted(
                st.session_state.df.loc[
                    st.session_state.df["Region"].isin(st.session_state.region_select),
                    "Country",
                ].unique()
            )[0:7],
            key="country_select",
        )
    st.multiselect(
        "Select Scores:",
        options=st.session_state.df.columns[3:],
        default="Happiness Score",
        key="score_select",
    )

for score in st.session_state.score_select:
    with st.container(border=True):
        st.subheader(f"{score} per year")
        fig = evolution_chart(st.session_state.df, score)
        st.plotly_chart(fig, use_container_width=True)


# with st.container(border=True):
#     st.subheader("Evolution of Happiness Rank")
#     fig = evolution_chart(st.session_state.df, "Happiness Rank")
#     st.plotly_chart(fig, use_container_width=True)
