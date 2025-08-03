import streamlit as st

DATA_TYPES = [
    "INT", "VARCHAR(255)", "TEXT", "DATE", "TIMESTAMP", "BOOLEAN", "DECIMAL(10,2)"
]

st.title("DDL自動生成ツール")

if 'tables' not in st.session_state:
    st.session_state.tables = []

table_name = st.text_input("テーブル名")
columns = []

col_count = st.number_input("カラム数", min_value=1, max_value=50, value=5)
for i in range(int(col_count)):
    cols = st.columns(8)
    name = cols[0].text_input(f"カラム名 {i+1}", key=f'name{i}')
    dtype = cols[1].selectbox(f"型 {i+1}", DATA_TYPES, key=f'dtype{i}')
    # ★ デフォルト候補
    default_suggest = ""
    if dtype == "TIMESTAMP":
        default_suggest = "CURRENT_TIMESTAMP"
    elif dtype == "BOOLEAN":
        default_suggest = "TRUE"
    default = cols[2].text_input(f"デフォルト値 {i+1}", value=default_suggest, key=f'default{i}')
    pk = cols[3].checkbox(f"主キー {i+1}", key=f'pk{i}')
    fk = cols[4].checkbox(f"外部キー {i+1}", key=f'fk{i}')
    fk_ref = cols[5].text_input(f"外部参照 {i+1}", key=f'fkref{i}')
    notnull = cols[6].checkbox(f"NOT NULL {i+1}", key=f'notnull{i}')
    comment = cols[7].text_input(f"コメント {i+1}", key=f'comment{i}', placeholder='例：ユーザID')
    if name and dtype:
        columns.append([name, dtype, default, pk, fk, fk_ref, notnull, comment])

if st.button("次のテーブルを生成"):
    if table_name and columns:
        st.session_state.tables.append((table_name, columns))
        st.success(f"テーブル「{table_name}」を追加しました。続けて入力できます。")
    else:
        st.error("テーブル名とカラム情報を入力してください。")

if st.button("出力"):
    temp_list = st.session_state.tables.copy()
    if table_name and columns:
        temp_list.append((table_name, columns))
    if not temp_list:
        st.error("テーブル情報がありません。")
    else:
        def generate_ddl(table_name, columns):
            ddl = f"CREATE TABLE {table_name} (\n"
            col_lines = []
            pk_cols = []
            fk_lines = []
            for col in columns:
                name, dtype, default, is_pk, is_fk, fk_ref, notnull, comment = col
                line = f"  {name} {dtype}"
                if notnull:
                    line += " NOT NULL"
                if default:
                    line += f" DEFAULT {default}"
                if is_pk:
                    pk_cols.append(name)
                if is_fk and fk_ref:
                    fk_lines.append(f"  FOREIGN KEY ({name}) REFERENCES {fk_ref}")
                col_lines.append(line)
            if pk_cols:
                col_lines.append(f"  PRIMARY KEY ({', '.join(pk_cols)})")
            col_lines += fk_lines
            ddl += ",\n".join(col_lines)
            ddl += "\n);"
            return ddl

        ddl = '\n\n'.join([generate_ddl(name, cols) for name, cols in temp_list])
        st.text_area("DDL.sql", ddl, height=200)
        st.download_button("DDL.sqlをダウンロード", ddl, file_name="DDL.sql")

if st.button("クリア"):
    st.session_state.tables.clear()
    st.experimental_rerun()
