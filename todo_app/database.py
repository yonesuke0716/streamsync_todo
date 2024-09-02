import sqlite3
import pandas as pd


class Database:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name

    def read_sql2df(self) -> pd.DataFrame:
        """
        sqlite3のテーブルをDataFrameに変換する

        Args:
            path (str): sqlite3のパス
            table_name (str): sqlite3のテーブル名

        Returns:
            DataFrame: sqlite3のテーブルをpandas.DataFrameに変換したDataFrame
        """
        sqlite_path = f"static/{self.db_name}"
        conn = sqlite3.connect(sqlite_path)
        query = f"SELECT * FROM {self.table_name}"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    def write_df2sql(self, df) -> None:
        """
        DataFrameをsqlite3のテーブルに書き込む

        Args:
            df (DataFrame): 書き込むDataFrame
            path (str): sqlite3のパス
            table_name (str): sqlite3のテーブル名
        """
        sqlite_path = f"static/{self.db_name}"
        conn = sqlite3.connect(sqlite_path)
        df.to_sql(self.table_name, conn, if_exists="replace", index=False)
        conn.close()


# テスト用
if __name__ == "__main__":
    # 初期化
    df = pd.DataFrame(
        {
            "日付": ["2024-9-1", "2024-9-1", "2024-9-2"],
            "タスク": ["買い物", "掃除", "勉強"],
        },
    )
    # 太郎テーブルクラスのsqliteを設定
    taro_table = Database("todo.db", "taro")
    # sqlite→Datagrameで読み込む
    df = taro_table.read_sql2df()
    # DataFrameに追加
    df = pd.concat([df, pd.DataFrame({"日付": ["2024-9-3"], "タスク": ["運動"]})])
    # reset index
    df = df.reset_index(drop=True)
    # DataFrame→sqliteで書き込む
    taro_table.write_df2sql(df)
    print(df)
