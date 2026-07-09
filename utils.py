import plotly.graph_objects as go

def apply_theme(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0D1117",
        plot_bgcolor="#0D1117",
        font=dict(color="#F0F6FC"),
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor="#30363D",
            tickfont=dict(color="#C9D1D9")
        ),
        yaxis=dict(
            gridcolor="#30363D",
            zeroline=False,
            tickfont=dict(color="#C9D1D9")
        ),
        legend=dict(bgcolor="rgba(0,0,0,0)")
    )
    return fig