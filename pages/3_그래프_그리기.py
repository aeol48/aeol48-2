import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="그래프 그리기 예제", layout="wide")
st.title("📊 그래프 그리기 예제")
st.write("matplotlib, seaborn, plotly를 활용한 그래프 예시입니다.")


def get_korean_font_name():
    font_path = "fonts/NotoSansKR-Medium.ttf"
    try:
        font_prop = fm.FontProperties(fname=font_path)
        return font_prop.get_name()
    except Exception:
        korean_fonts = ["NanumGothic", "Malgun Gothic", "AppleGothic"]
        for system_path in fm.findSystemFonts(fontpaths=None, fontext="ttf"):
            if any(name in system_path for name in korean_fonts):
                return fm.FontProperties(fname=system_path).get_name()
        return "DejaVu Sans"

plt.rc("font", family=get_korean_font_name())
plt.rc("axes", unicode_minus=False)

# matplotlib 예시
st.header("1. matplotlib 막대 그래프")
mat_data = {
    "과일": ["사과", "바나나", "귤", "포도", "수박"],
    "판매량": [120, 95, 70, 45, 30],
}
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(mat_data["과일"], mat_data["판매량"], color=["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854"])
ax.set_title("과일별 판매량")
ax.set_xlabel("과일")
ax.set_ylabel("판매량 (개)")
ax.grid(axis="y", linestyle="--", alpha=0.5)
for i, value in enumerate(mat_data["판매량"]):
    ax.text(i, value + 2, str(value), ha="center")
st.pyplot(fig)

# seaborn 예시
st.header("2. seaborn 선 그래프")
seaborn_df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "매출": [350, 420, 390, 480, 520, 580],
})
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.lineplot(data=seaborn_df, x="월", y="매출", marker="o", ax=ax2)
ax2.set_title("월별 매출 추이")
ax2.set_xlabel("월")
ax2.set_ylabel("매출 (만원)")
ax2.grid(True, linestyle="--", alpha=0.5)
st.pyplot(fig2)

# plotly 예시
st.header("3. plotly 파이 차트")
plotly_df = pd.DataFrame({
    "카테고리": ["전자제품", "음식", "의류", "도서", "생활용품"],
    "비율": [28, 22, 18, 15, 17],
})
plotly_fig = px.pie(
    plotly_df,
    names="카테고리",
    values="비율",
    title="카테고리별 판매 비중",
    hole=0.4,
)
plotly_fig.update_traces(textposition="inside", textinfo="percent+label")
plotly_fig.update_layout(title_font_size=20, legend_title_text="카테고리")
st.plotly_chart(plotly_fig, use_container_width=True)

st.write("---")
st.write("### 사용 방법")
st.write("- matplotlib로 막대 그래프를 만들고, seaborn으로 선 그래프를 그립니다.")
st.write("- plotly로 인터랙티브한 파이 차트를 확인하세요.")
