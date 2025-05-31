import streamlit as st
import json

# 从 JSON 文件加载 regulation_data
with open("regulation_data.json", "r", encoding="utf-8") as f:
    regulation_data = json.load(f)


# 设置页面布局为宽屏 + 限宽
st.set_page_config(page_title="化学品合规工具箱", layout="wide")

# 页面样式：限制宽度为 75%
st.markdown("""
    <style>
    .main {
        max-width: 75vw;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# ===== 侧边栏导航 =====
st.sidebar.title("🧰 工具导航")
page = st.sidebar.radio("请选择要使用的工具", [
    "国家/地区名录整理小工具",
    "（预留）1",
    "（预留）2",
])

# ===== 页面路由逻辑 =====
if page == "国家/地区名录整理小工具":
    # 当前已开发好的工具页面
    st.title("国家/地区名录整理小工具")

    # 四列布局
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        country_options = ['请选择'] + list(regulation_data.keys())
        selected_country = st.selectbox("##### 选择国家", country_options)

    selected_regulation = '请选择'
    selected_catalog = '请选择'

    if selected_country != '请选择':
        with col2:
            regulation_options = ['请选择'] + list(regulation_data[selected_country].keys())
            selected_regulation = st.radio("##### 选择法规", regulation_options)

    if selected_regulation != '请选择':
        with col3:
            catalog_options = ['请选择'] + list(regulation_data[selected_country][selected_regulation].keys())
            selected_catalog = st.radio("##### 选择名录", catalog_options)

    if selected_catalog != '请选择':
        with col4:
            sub_catalogs = regulation_data[selected_country][selected_regulation][selected_catalog]['sub_catalogs']
            st.markdown("##### 子名录一览")
            if sub_catalogs:
                for sub in sub_catalogs:
                    with st.expander(f"📘 {sub['name']}"):
                        st.markdown(sub['intro'])
            else:
                st.info("该名录暂无子名录信息。")

    st.markdown("---")

    if selected_catalog != '请选择':
        catalog_intro = regulation_data[selected_country][selected_regulation][selected_catalog]['intro']
        st.success(f"你选择的是：{selected_country} - {selected_regulation} - {selected_catalog}")
        st.markdown(f"**名录简介：** {catalog_intro}")
    else:
        st.info("请依次选择国家、法规和名录")

else:
    st.title("该工具页面尚未开发，敬请期待 🛠️")
