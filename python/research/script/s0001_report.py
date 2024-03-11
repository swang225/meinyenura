from dash import Dash, dcc, html, Input, Output, callback, State
import dash
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd


def get_test_opt_results():
    grid = [
        (50, 10, 0.2, 0.5, 0.6),
        (50, 30, -0.1, 0.3, -0.3),
        (50, 50, 1.1, 0.7, 0.54),
        (100, 10, 1.2, 1.1, 1.3),
        (100, 30, 0.6, 0.8, 0.5),
        (100, 50, 0.1, 0.2, 0.12),
        (300, 10, 0.5, 0.33, 0.5),
        (300, 50, -0.5, 0.4, -0.2)
    ]

    df = pd.DataFrame(data={
        "lookback": [g[0] for g in grid],
        "refit": [g[1] for g in grid],
        "long_sharpe": [g[2] for g in grid],
        "short_sharpe": [g[3] for g in grid],
        "blend_sharpe": [g[4] for g in grid],
    })

    return df


def get_test_opt_grid_results():
    test_data = {
        "long_sharpe": [0.5],
        "short_sharpe": [1.1],
        "blend_sharpe": [1.2]
    }

    sharpe_res = pd.DataFrame(data=test_data)

    test_data = {
        "start_date": [
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),

            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),
        ],
        "date": [
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-02"),
            pd.Timestamp("2021-01-03"),
            pd.Timestamp("2021-01-04"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-02"),
            pd.Timestamp("2021-01-03"),
            pd.Timestamp("2021-01-04"),

            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-02"),
            pd.Timestamp("2021-01-03"),
            pd.Timestamp("2021-01-04"),
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-02"),
            pd.Timestamp("2021-01-03"),
            pd.Timestamp("2021-01-04"),

            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-02"),
            pd.Timestamp("2021-02-03"),
            pd.Timestamp("2021-02-04"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-02"),
            pd.Timestamp("2021-02-03"),
            pd.Timestamp("2021-02-04"),

            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-02"),
            pd.Timestamp("2021-02-03"),
            pd.Timestamp("2021-02-04"),
            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-02"),
            pd.Timestamp("2021-02-03"),
            pd.Timestamp("2021-02-04"),
        ],
        "side": [
            "L", "L", "L", "L", "L", "L", "L", "L",
            "S", "S", "S", "S", "S", "S", "S", "S",

            "L", "L", "L", "L", "L", "L", "L", "L",
            "S", "S", "S", "S", "S", "S", "S", "S"
        ],
        "alpha_name": [
            "alpha1", "alpha1", "alpha1", "alpha1", "alpha2", "alpha2", "alpha2", "alpha2",
            "alpha3", "alpha3", "alpha3", "alpha3", "alpha2", "alpha2", "alpha2", "alpha2",

            "alpha1", "alpha1", "alpha1", "alpha1", "alpha4", "alpha4", "alpha4", "alpha4",
            "alpha3", "alpha3", "alpha3", "alpha3", "alpha5", "alpha5", "alpha5", "alpha5"
        ],
        "pnl": [
            10, -10, 12, -2, -5, 5, 6, 3,
            8, -7, -2, 3, -4, 4, 2, 1,

            20, -9, 11, -3, 5, -5, 16, 23,
            18, 7, 2, 23, 4, 12, 5, 3
        ]
    }

    pnl_each = pd.DataFrame(data=test_data).set_index(["start_date", "date", "side", "alpha_name"]).sort_index()

    test_data = {
        "date": [
            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),

            pd.Timestamp("2021-01-01"),
            pd.Timestamp("2021-01-01"),

            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),

            pd.Timestamp("2021-02-01"),
            pd.Timestamp("2021-02-01"),

        ],
        "side": [
            "L", "L",
            "S", "S",

            "L", "L",
            "S", "S",
        ],
        "alpha_name": [
            "alpha1", "alpha2",
            "alpha3", "alpha2",

            "alpha1", "alpha4",
            "alpha3", "alpha5"
        ],
        "weight": [
            1.2, 0.7,
            0.2, 0.5,

            0.9, 0.8,
            1.1, 0.5,
        ]
    }

    weights = pd.DataFrame(data=test_data).set_index(["date", "side", "alpha_name"]).sort_index()
    cvx_weights = pd.DataFrame(data=test_data).set_index(["date", "side", "alpha_name"]).sort_index()

    return sharpe_res, pnl_each, weights, cvx_weights


def get_heatmap(res, name):
    fig = go.Figure(data=go.Heatmap(
        z=res[name],
        x=res["refit"],
        y=res["lookback"],
        colorscale='Viridis',
        text=res[name],
        texttemplate="%{text}",
        textfont={"size": 15}
    ))

    fig.update_layout(
        autosize=True,
        # width=800,
        height=500,
        margin=dict(
            l=5,
            r=5,
            b=5,
            t=25,
            pad=0
        ),
        # paper_bgcolor="LightSteelBlue",
        xaxis_title="refit", yaxis_title="lookback"
    )

    return fig


def get_opt_heat_map(name="long_sharpe"):
    res = get_test_opt_results()
    fig = get_heatmap(res, name)

    return fig


def get_opt_heat_map_long():
    return get_opt_heat_map("long_sharpe")


def get_opt_heat_map_short():
    return get_opt_heat_map("short_sharpe")


def get_opt_heat_map_blend():
    return get_opt_heat_map("blend_sharpe")


def get_test_data():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    return df


def side_name(name):
    res = "Blend"
    if name == "L":
        res = "Long"
    elif name == "S":
        res = "Short"

    return res


class OptimizationReport:
    def __init__(
            self,
            port=8114,
            debug=False
    ):
        self.app = Dash(__name__)
        self.app.title = "Optimization Report"
        self.port = port
        self.debug = debug

        self.curr_res = None
        self.side = None

    def click(self, clickData):
        if not clickData:
            raise dash.exceptions.PreventUpdate

        print(clickData)
        self.curr_res = get_test_opt_grid_results()
        sharpe_res, pnl_each, weights, cvx_weights = self.curr_res

        dates = weights.index.levels[0]

        res_min = dates.min().value
        res_max = dates.max().value
        res_value = res_max
        res_marks = {d.value: d.strftime("%Y-%m-%d") for d in dates}

        return res_min, res_max, res_value, res_marks

    def click_long(self, clickData):
        self.side = "L"
        return self.click(clickData)

    def click_short(self, clickData):
        self.side = "S"
        return self.click(clickData)

    def click_blend(self, clickData):
        self.side = None
        return self.click(clickData)

    def show_graph(self, value, marks):

        date_str = marks[str(value)]
        date = pd.Timestamp(date_str)
        print(date)

        side = self.side
        sharpe_res, pnl_each, weights, cvx_weights = self.curr_res
        if side is not None:
            pnl_each = pnl_each.loc[date].swaplevel(0,1).loc[side].reset_index()
            weights = weights.loc[date].loc[side].reset_index()
            cvx_weights = cvx_weights.loc[date].loc[side].reset_index()
        else:
            pnl_each = pnl_each.loc[date].swaplevel(0, 1).droplevel(0).reset_index()
            weights = weights.loc[date].droplevel(0).reset_index()
            cvx_weights = cvx_weights.loc[date].droplevel(0).reset_index()

        fig = px.bar(pnl_each, x="date", y="pnl", color="alpha_name", title=f"{date_str} Daily PnL {side_name(side)}")
        fig_weight = px.bar(weights, x="alpha_name", y="weight", title=f"{date_str} Alpha Weights {side_name(side)}")
        fig_cvx_weight = px.bar(cvx_weights, x="alpha_name", y="weight", title=f"{date_str} CVX Alpha Weights {side_name(side)}")

        g_style = {'width': '33%', 'align': 'center', 'display': 'inline-block'}
        return fig, fig_weight, fig_cvx_weight, g_style, g_style, g_style


    def create_callbacks(self):
        self.app.callback(
            Output("date-slider", "min", allow_duplicate=True),
            Output("date-slider", "max", allow_duplicate=True),
            Output("date-slider", "value", allow_duplicate=True),
            Output("date-slider", "marks", allow_duplicate=True),
            Input("g1_long", "clickData"),
            prevent_initial_call=True
        )(self.click_long)

        self.app.callback(
            Output("date-slider", "min", allow_duplicate=True),
            Output("date-slider", "max", allow_duplicate=True),
            Output("date-slider", "value", allow_duplicate=True),
            Output("date-slider", "marks", allow_duplicate=True),
            Input("g1_short", "clickData"),
            prevent_initial_call=True
        )(self.click_short)

        self.app.callback(
            Output("date-slider", "min", allow_duplicate=True),
            Output("date-slider", "max", allow_duplicate=True),
            Output("date-slider", "value", allow_duplicate=True),
            Output("date-slider", "marks", allow_duplicate=True),
            Input("g1_blend", "clickData"),
            prevent_initial_call=True
        )(self.click_blend)

        self.app.callback(
            Output("g2_pnl", "figure"),
            Output("g3_weight", "figure"),
            Output("g4_cvx_weight", "figure"),
            Output("g2_div", "style"),
            Output("g3_div", "style"),
            Output("g4_div", "style"),
            Input("date-slider", "value"),
            State("date-slider", "marks"),
            prevent_initial_call=True
        )(self.show_graph)

    def create_layout(self):

        self.app.layout = html.Div([
            html.Div([
                html.Div([dcc.Graph(id='g1_long', figure=get_opt_heat_map_long())],
                         style={'width': '33%', 'align': 'center', 'display': 'inline-block'}),
                html.Div([dcc.Graph(id='g1_short', figure=get_opt_heat_map_short())],
                         style={'width': '33%', 'align': 'center', 'display': 'inline-block'}),
                html.Div([dcc.Graph(id='g1_blend', figure=get_opt_heat_map_blend())],
                         style={'width': '33%', 'align': 'center', 'display': 'inline-block'}),
            ]),
            dcc.Slider(
                min=None,
                max=None,
                step=None,
                value=None,
                marks=None,
                id='date-slider'
            ),
            html.Div([
                html.Div([dcc.Graph(id='g2_pnl')],
                         style={'width': '33%', 'align': 'center', 'display': 'none'}, id="g2_div"),
                html.Div([dcc.Graph(id='g3_weight')],
                         style={'width': '33%', 'align': 'center', 'display': 'none'}, id="g3_div"),
                html.Div([dcc.Graph(id='g4_cvx_weight')],
                         style={'width': '33%', 'align': 'center', 'display': 'none'}, id="g4_div"),
            ])
        ])

    def run(self):
        self.create_layout()
        self.create_callbacks()
        self.app.run(
            debug=self.debug,
            port=self.port
        )


if __name__ == '__main__':
    rep = OptimizationReport(debug=False)
    rep.run()
