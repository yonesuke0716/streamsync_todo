import writer as wf
import pandas as pd

initial_state = wf.init_state(
    {
        "my_app": {"title": "MY APP"},
        "df": pd.DataFrame(
            {
                "日付": ["2024-9-1", "2024-9-1", "2024-9-2"],
                "タスク": ["買い物", "掃除", "勉強"],
            },
        ),
    }
)
