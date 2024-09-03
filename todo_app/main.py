import writer as wf
import pandas as pd


def get_date(state, payload):
    state["get_date"] = payload


def get_task(state, payload):
    state["get_task"] = payload


def add_df_loc(state):
    if state["get_date"] == "" or state["get_task"] == "":
        state.add_notification(
            "warning",
            "追加情報に記入漏れがあります.",
            "日付とタスクを入力してください.",
        )
        return
    state["df"] = pd.concat(
        [
            state["df"],
            pd.DataFrame({"日付": [state["get_date"]], "タスク": [state["get_task"]]}),
        ]
    )


def delete_df_loc(state):
    state["df"] = state["df"].iloc[:-1]


initial_state = wf.init_state(
    {
        "my_app": {"title": "MY APP"},
        "df": pd.DataFrame(
            {
                "日付": ["2024-9-1", "2024-9-2", "2024-9-3"],
                "タスク": ["買い物", "掃除", "勉強"],
            },
        ),
        "get_date": "",
        "get_task": "",
    }
)
