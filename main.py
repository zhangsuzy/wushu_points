import streamlit as st

# ===================== 基础数据库 =====================
# 1. 十二正经数据库
MERIDIANS = {
    # 阴经（木火土金水）
    "肝": {"阴阳": "阴经", "五行": "木", "五输穴": {
        "井": {"名称": "大敦", "编号": "LR1", "五行": "木"},
        "荥": {"名称": "行间", "编号": "LR2", "五行": "火"},
        "输": {"名称": "太冲", "编号": "LR3", "五行": "土"},
        "经": {"名称": "中封", "编号": "LR4", "五行": "金"},
        "合": {"名称": "曲泉", "编号": "LR8", "五行": "水"}
    }},
    "心": {"阴阳": "阴经", "五行": "火", "五输穴": {
        "井": {"名称": "少冲", "编号": "HT9", "五行": "木"},
        "荥": {"名称": "少府", "编号": "HT8", "五行": "火"},
        "输": {"名称": "神门", "编号": "HT7", "五行": "土"},
        "经": {"名称": "灵道", "编号": "HT4", "五行": "金"},
        "合": {"名称": "少海", "编号": "HT3", "五行": "水"}
    }},
    "脾": {"阴阳": "阴经", "五行": "土", "五输穴": {
        "井": {"名称": "隐白", "编号": "SP1", "五行": "木"},
        "荥": {"名称": "大都", "编号": "SP2", "五行": "火"},
        "输": {"名称": "太白", "编号": "SP3", "五行": "土"},
        "经": {"名称": "商丘", "编号": "SP5", "五行": "金"},
        "合": {"名称": "阴陵泉", "编号": "SP9", "五行": "水"}
    }},
    "肺": {"阴阳": "阴经", "五行": "金", "五输穴": {
        "井": {"名称": "少商", "编号": "LU11", "五行": "木"},
        "荥": {"名称": "鱼际", "编号": "LU10", "五行": "火"},
        "输": {"名称": "太渊", "编号": "LU9", "五行": "土"},
        "经": {"名称": "经渠", "编号": "LU8", "五行": "金"},
        "合": {"名称": "尺泽", "编号": "LU5", "五行": "水"}
    }},
    "肾": {"阴阳": "阴经", "五行": "水", "五输穴": {
        "井": {"名称": "涌泉", "编号": "KI1", "五行": "木"},
        "荥": {"名称": "然谷", "编号": "KI2", "五行": "火"},
        "输": {"名称": "太溪", "编号": "KI3", "五行": "土"},
        "经": {"名称": "复溜", "编号": "KI7", "五行": "金"},
        "合": {"名称": "阴谷", "编号": "KI10", "五行": "水"}
    }},
    "心包": {"阴阳": "阴经", "五行": "火", "五输穴": {
        "井": {"名称": "中冲", "编号": "PC9", "五行": "木"},
        "荥": {"名称": "劳宫", "编号": "PC8", "五行": "火"},
        "输": {"名称": "大陵", "编号": "PC7", "五行": "土"},
        "经": {"名称": "间使", "编号": "PC5", "五行": "金"},
        "合": {"名称": "曲泽", "编号": "PC3", "五行": "水"}
    }},
    # 阳经（金水木火土）
    "胆": {"阴阳": "阳经", "五行": "木", "五输穴": {
        "井": {"名称": "足窍阴", "编号": "GB44", "五行": "金"},
        "荥": {"名称": "侠溪", "编号": "GB43", "五行": "水"},
        "输": {"名称": "足临泣", "编号": "GB41", "五行": "木"},
        "经": {"名称": "阳辅", "编号": "GB38", "五行": "火"},
        "合": {"名称": "阳陵泉", "编号": "GB34", "五行": "土"}
    }},
    "膀胱": {"阴阳": "阳经", "五行": "水", "五输穴": {
        "井": {"名称": "至阴", "编号": "BL67", "五行": "金"},
        "荥": {"名称": "足通谷", "编号": "BL66", "五行": "水"},
        "输": {"名称": "束骨", "编号": "BL65", "五行": "木"},
        "经": {"名称": "昆仑", "编号": "BL60", "五行": "火"},
        "合": {"名称": "委中", "编号": "BL40", "五行": "土"}
    }},
    "小肠": {"阴阳": "阳经", "五行": "火", "五输穴": {
        "井": {"名称": "少泽", "编号": "SI1", "五行": "金"},
        "荥": {"名称": "前谷", "编号": "SI2", "五行": "水"},
        "输": {"名称": "后溪", "编号": "SI3", "五行": "木"},
        "经": {"名称": "阳谷", "编号": "SI5", "五行": "火"},
        "合": {"名称": "小海", "编号": "SI8", "五行": "土"}
    }},
    "胃": {"阴阳": "阳经", "五行": "土", "五输穴": {
        "井": {"名称": "厉兑", "编号": "ST45", "五行": "金"},
        "荥": {"名称": "内庭", "编号": "ST44", "五行": "水"},
        "输": {"名称": "陷谷", "编号": "ST43", "五行": "木"},
        "经": {"名称": "解溪", "编号": "ST41", "五行": "火"},
        "合": {"名称": "足三里", "编号": "ST36", "五行": "土"}
    }},
    "大肠": {"阴阳": "阳经", "五行": "金", "五输穴": {
        "井": {"名称": "商阳", "编号": "LI1", "五行": "金"},
        "荥": {"名称": "二间", "编号": "LI2", "五行": "水"},
        "输": {"名称": "三间", "编号": "LI3", "五行": "木"},
        "经": {"名称": "阳溪", "编号": "LI5", "五行": "火"},
        "合": {"名称": "曲池", "编号": "LI11", "五行": "土"}
    }},
    "三焦": {"阴阳": "阳经", "五行": "火", "五输穴": {
        "井": {"名称": "关冲", "编号": "TE1", "五行": "金"},
        "荥": {"名称": "液门", "编号": "TE2", "五行": "水"},
        "输": {"名称": "中渚", "编号": "TE3", "五行": "木"},
        "经": {"名称": "支沟", "编号": "TE6", "五行": "火"},
        "合": {"名称": "天井", "编号": "TE10", "五行": "土"}
    }}
}

# 2. 五行关系表
WUXING_RELATIONS = {
    "木": {"生": "火", "克": "土", "所胜": "土", "所不胜": "金"},
    "火": {"生": "土", "克": "金", "所胜": "金", "所不胜": "水"},
    "土": {"生": "金", "克": "水", "所胜": "水", "所不胜": "木"},
    "金": {"生": "水", "克": "木", "所胜": "木", "所不胜": "火"},
    "水": {"生": "木", "克": "火", "所胜": "火", "所不胜": "土"}
}

# ===================== 核心逻辑 =====================
class AcupunctureSystem:
    def __init__(self, meridian):
        self.meridian = MERIDIANS[meridian]
        self.name = meridian
        self.wuxing = self.meridian["五行"]
        self.yinyang = self.meridian["阴阳"]

    def find_point(self, element):
        """根据五行属性查找穴位"""
        for role, point in self.meridian["五输穴"].items():
            if point["五行"] == element:
                return f"{point['名称']}({point['编号']})[{element}]"
        return None

    def find_related_meridian(self, relation_type):
        """查找相关经络"""
        target_wuxing = WUXING_RELATIONS[self.wuxing][relation_type]
        for m, data in MERIDIANS.items():
            if data["五行"] == target_wuxing and data["阴阳"] == self.yinyang:
                return m
        return None

# ===================== 用户界面 =====================
st.title("精准配穴系统")

# 输入选择
col1, col2, col3 = st.columns(3)
with col1:
    meridian = st.selectbox("选择经络", list(MERIDIANS.keys()))
with col2:
    condition = st.selectbox("选择证型", ["虚证", "实证"])
with col3:
    method = st.selectbox("选择针法", ["二针法", "四针法"])

# 初始化系统
asys = AcupunctureSystem(meridian)

# 显示配穴方案
st.subheader("配穴方案")
result = []

# 二针法逻辑
if method == "二针法":
    if condition == "虚证":
        # 补母穴
        mother_element = WUXING_RELATIONS[asys.wuxing]["生"]
        point1 = asys.find_point(mother_element)
        # 母经母穴
        mother_meridian = asys.find_related_meridian("生")
        if mother_meridian:
            m_asys = AcupunctureSystem(mother_meridian)
            point2 = m_asys.find_point(WUXING_RELATIONS[m_asys.wuxing]["生"])
            result.append(f"**补法方案（二针法）**")
            result.append(f"1. 本经母穴：{point1}")
            result.append(f"2. 母经母穴：{point2}（{mother_meridian}经）")
    else:
        # 泻子穴
        child_element = WUXING_RELATIONS[asys.wuxing]["克"]
        point1 = asys.find_point(child_element)
        # 子经子穴
        child_meridian = asys.find_related_meridian("克")
        if child_meridian:
            c_asys = AcupunctureSystem(child_meridian)
            point2 = c_asys.find_point(WUXING_RELATIONS[c_asys.wuxing]["克"])
            result.append(f"**泻法方案（二针法）**")
            result.append(f"1. 本经子穴：{point1}")
            result.append(f"2. 子经子穴：{point2}（{child_meridian}经）")

# 四针法逻辑
else:
    if condition == "虚证":
        # 补母穴
        mother_element = WUXING_RELATIONS[asys.wuxing]["生"]
        point1 = asys.find_point(mother_element)
        # 母经母穴
        mother_meridian = asys.find_related_meridian("生")
        if mother_meridian:
            m_asys = AcupunctureSystem(mother_meridian)
            point2 = m_asys.find_point(WUXING_RELATIONS[m_asys.wuxing]["生"])

        # 泻所不胜穴
        restrain_element = WUXING_RELATIONS[asys.wuxing]["所不胜"]
        point3 = asys.find_point(restrain_element)
        # 所不胜经穴
        restrain_meridian = asys.find_related_meridian("所不胜")
        if restrain_meridian:
            r_asys = AcupunctureSystem(restrain_meridian)
            point4 = r_asys.find_point(WUXING_RELATIONS[r_asys.wuxing]["所不胜"])

            result.append(f"**补泻方案（四针法）**")
            result.append("### 补法部分")
            result.append(f"1. 本经母穴：{point1}")
            result.append(f"2. 母经母穴：{point2}（{mother_meridian}经）")
            result.append("### 泻法部分")
            result.append(f"3. 本经所不胜穴：{point3}")
            result.append(f"4. 所不胜经穴：{point4}（{restrain_meridian}经）")
    else:
        # 泻子穴
        child_element = WUXING_RELATIONS[asys.wuxing]["克"]
        point1 = asys.find_point(child_element)
        # 子经子穴
        child_meridian = asys.find_related_meridian("克")
        if child_meridian:
            c_asys = AcupunctureSystem(child_meridian)
            point2 = c_asys.find_point(WUXING_RELATIONS[c_asys.wuxing]["克"])

        # 补所不胜穴
        restrain_element = WUXING_RELATIONS[asys.wuxing]["所不胜"]
        point3 = asys.find_point(restrain_element)
        # 所不胜经穴
        restrain_meridian = asys.find_related_meridian("所不胜")
        if restrain_meridian:
            r_asys = AcupunctureSystem(restrain_meridian)
            point4 = r_asys.find_point(WUXING_RELATIONS[r_asys.wuxing]["所不胜"])

            result.append(f"**补泻方案（四针法）**")
            result.append("### 泻法部分")
            result.append(f"1. 本经子穴：{point1}")
            result.append(f"2. 子经子穴：{point2}（{child_meridian}经）")
            result.append("### 补法部分")
            result.append(f"3. 本经所不胜穴：{point3}")
            result.append(f"4. 所不胜经穴：{point4}（{restrain_meridian}经）")

# 显示结果
for line in result:
    if "**" in line:
        st.markdown(line)
    elif "###" in line:
        st.markdown(line)
    else:
        st.markdown(f"""
        <div style="padding:10px; margin:5px; border-left:4px solid #4CAF50; background:#f8f9fa">
            {line}
        </div>
        """, unsafe_allow_html=True)
