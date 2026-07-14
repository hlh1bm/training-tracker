import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# ============================================================
# PAGE SETUP
# ============================================================
st.set_page_config(
    page_title="Training Tracker",
    page_icon="📋",
    layout="wide"
)

# ============================================================
# LANGUAGE
# ============================================================
LANG = {
    "en": {
        "title": "📋 Training Tracker",
        "employees": "👥 Employees",
        "machines": "⚙️ Machines",
        "add_employee": "➕ Add Employee",
        "add_machine": "➕ Add Machine",
        "export": "📤 Export Data",
        "import": "📥 Import Data",
        "search": "🔎 Search...",
        "filter": "Filter",
        "all": "All",
        "all_employees": "All Employees",
        "all_machines": "All Machines",
        "in_training": "In Training",
        "trained": "Trained",
        "ready_for_test": "Ready for Test",
        "passed": "Passed",
        "overdue": "Overdue",
        "certified": "Certified",
        "progress": "Progress",
        "no_training": "No training assigned",
        "add_training": "➕ Add Training",
        "sessions": "sessions",
        "days": "days",
        "difficulty": "Difficulty",
        "high": "🔴 High",
        "medium": "🟡 Medium",
        "low": "🟢 Low",
        "save": "💾 Save",
        "cancel": "✖ Cancel",
        "close": "✖ Close",
        "delete": "🗑️ Delete",
        "ready": "Ready",
        "pass": "Pass",
        "showing": "Showing",
        "employees_count": "employees",
        "machines_count": "machines",
        "status_guide": "Status Guide:",
        "click_ready": "💡 Click 'Ready' then 'Pass'",
        "auto_saved": "💾 Auto-saved",
        "employee_number": "Employee Number",
        "employee_name": "Employee Name",
        "machine_name": "Machine Name",
        "required_sessions": "Required Sessions",
        "test_window": "Test Window (days)",
        "training_date": "Training Date",
        "sessions_completed": "Sessions",
        "new_name": "New Name",
        "confirm_delete": "Delete?",
    },
    "th": {
        "title": "📋 ระบบติดตามการฝึกอบรม",
        "employees": "👥 พนักงาน",
        "machines": "⚙️ เครื่องจักร",
        "add_employee": "➕ เพิ่มพนักงาน",
        "add_machine": "➕ เพิ่มเครื่องจักร",
        "export": "📤 ส่งออกข้อมูล",
        "import": "📥 นำเข้าข้อมูล",
        "search": "🔎 ค้นหา...",
        "filter": "ตัวกรอง",
        "all": "ทั้งหมด",
        "all_employees": "พนักงานทั้งหมด",
        "all_machines": "เครื่องจักรทั้งหมด",
        "in_training": "กำลังฝึกอบรม",
        "trained": "ฝึกอบรมเสร็จ",
        "ready_for_test": "พร้อมสอบ",
        "passed": "สอบผ่าน",
        "overdue": "เลยกำหนด",
        "certified": "ผ่านการรับรอง",
        "progress": "ความคืบหน้า",
        "no_training": "ไม่มีการฝึกอบรม",
        "add_training": "➕ เพิ่มการฝึกอบรม",
        "sessions": "ครั้ง",
        "days": "วัน",
        "difficulty": "ระดับความยาก",
        "high": "🔴 สูง",
        "medium": "🟡 ปานกลาง",
        "low": "🟢 ต่ำ",
        "save": "💾 บันทึก",
        "cancel": "✖ ยกเลิก",
        "close": "✖ ปิด",
        "delete": "🗑️ ลบ",
        "ready": "พร้อมสอบ",
        "pass": "สอบผ่าน",
        "showing": "กำลังแสดง",
        "employees_count": "พนักงาน",
        "machines_count": "เครื่องจักร",
        "status_guide": "คู่มือสถานะ:",
        "click_ready": "💡 คลิก 'พร้อมสอบ' แล้ว 'สอบผ่าน'",
        "auto_saved": "💾 บันทึกอัตโนมัติ",
        "employee_number": "รหัสพนักงาน",
        "employee_name": "ชื่อพนักงาน",
        "machine_name": "ชื่อเครื่องจักร",
        "required_sessions": "จำนวนครั้งที่ต้องฝึก",
        "test_window": "ระยะเวลาสอบ (วัน)",
        "training_date": "วันที่ฝึก",
        "sessions_completed": "จำนวนครั้ง",
        "new_name": "ชื่อใหม่",
        "confirm_delete": "ลบ?",
    },
    "zh": {
        "title": "📋 培训追踪系统",
        "employees": "👥 员工",
        "machines": "⚙️ 机器",
        "add_employee": "➕ 添加员工",
        "add_machine": "➕ 添加机器",
        "export": "📤 导出数据",
        "import": "📥 导入数据",
        "search": "🔎 搜索...",
        "filter": "筛选",
        "all": "全部",
        "all_employees": "所有员工",
        "all_machines": "所有机器",
        "in_training": "培训中",
        "trained": "培训完成",
        "ready_for_test": "准备考试",
        "passed": "已通过",
        "overdue": "已逾期",
        "certified": "已认证",
        "progress": "进度",
        "no_training": "未分配培训",
        "add_training": "➕ 添加培训",
        "sessions": "次",
        "days": "天",
        "difficulty": "难度",
        "high": "🔴 高",
        "medium": "🟡 中",
        "low": "🟢 低",
        "save": "💾 保存",
        "cancel": "✖ 取消",
        "close": "✖ 关闭",
        "delete": "🗑️ 删除",
        "ready": "准备考试",
        "pass": "通过",
        "showing": "显示",
        "employees_count": "员工",
        "machines_count": "机器",
        "status_guide": "状态指南:",
        "click_ready": "💡 点击'准备考试'然后'通过'",
        "auto_saved": "💾 自动保存",
        "employee_number": "员工编号",
        "employee_name": "员工姓名",
        "machine_name": "机器名称",
        "required_sessions": "所需培训次数",
        "test_window": "考试期限(天)",
        "training_date": "培训日期",
        "sessions_completed": "次数",
        "new_name": "新名称",
        "confirm_delete": "删除?",
    }
}

# ============================================================
# SESSION STATE
# ============================================================
if 'lang' not in st.session_state:
    st.session_state.lang = "en"
if 'theme' not in st.session_state:
    st.session_state.theme = "light"
if 'employees' not in st.session_state:
    st.session_state.employees = []
if 'machines' not in st.session_state:
    st.session_state.machines = {}

# ============================================================
# THEME CSS
# ============================================================
def get_theme_css():
    if st.session_state.theme == "light":
        return """
        <style>
            .stApp { background-color: #f5f7fa !important; }
            .employee-card { background: white !important; border: 1px solid #e8ecf1 !important; }
            .stat-box { background: white !important; border: 1px solid #e8ecf1 !important; }
            .legend-box { background: #f8f9fa !important; border: 1px solid #e8ecf1 !important; }
            .stButton > button { background: white !important; border: 1px solid #d0d7de !important; color: #1a2a6c !important; }
            h1, h2, h3 { color: #1a2a6c !important; }
            .emp-name { color: #1a2a6c !important; }
        </style>
        """
    else:
        return """
        <style>
            .stApp { background-color: #1a1a2e !important; }
            .employee-card { background: #16213e !important; border: 1px solid #2d3a5e !important; }
            .stat-box { background: #16213e !important; border: 1px solid #2d3a5e !important; }
            .stat-box .number { color: #e0e0e0 !important; }
            .stat-box .label { color: #aaa !important; }
            .legend-box { background: #16213e !important; border: 1px solid #2d3a5e !important; }
            .stButton > button { background: #16213e !important; border: 1px solid #2d3a5e !important; color: #e0e0e0 !important; }
            h1, h2, h3 { color: #e0e0e0 !important; }
            .emp-name { color: #e0e0e0 !important; }
            .stTextInput > div > input { background: #1a2744 !important; color: #e0e0e0 !important; border: 1px solid #2d3a5e !important; }
            .stNumberInput > div > input { background: #1a2744 !important; color: #e0e0e0 !important; border: 1px solid #2d3a5e !important; }
            .stSelectbox > div > div { background: #1a2744 !important; color: #e0e0e0 !important; }
        </style>
        """

# ============================================================
# DATA FILE
# ============================================================
DATA_FILE = "data/training_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            return data.get("machines", {}), data.get("employees", [])
        except:
            pass
    return {}, []

def save_data():
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump({"machines": st.session_state.machines, "employees": st.session_state.employees}, f, indent=2)

# ============================================================
# STATUS HELPERS
# ============================================================
def get_machine(name):
    return st.session_state.machines.get(name, None)

def get_status(training, machine):
    if not machine:
        return "gray", "No Config"
    if training.get("test_date"):
        return "yellow", LANG[st.session_state.lang]["passed"]
    if training.get("ready_date"):
        ready = datetime.strptime(training["ready_date"], "%Y-%m-%d")
        days = (datetime.now() - ready).days
        if days > machine.get("window_days", 7):
            return "red", LANG[st.session_state.lang]["overdue"]
        return "blue", LANG[st.session_state.lang]["ready_for_test"]
    if training.get("sessions", 0) < machine.get("required_sessions", 6):
        return "gray", LANG[st.session_state.lang]["in_training"]
    return "green", LANG[st.session_state.lang]["trained"]

def get_overall_status(emp):
    if not emp.get("training"):
        return "gray", LANG[st.session_state.lang]["no_training"], 0, 0
    
    total = len(emp["training"])
    passed = 0
    has_red = has_blue = has_green = has_gray = False
    
    for t in emp["training"]:
        m = get_machine(t["machine"])
        status, _ = get_status(t, m)
        if status == "yellow": passed += 1
        elif status == "red": has_red = True
        elif status == "blue": has_blue = True
        elif status == "green": has_green = True
        elif status == "gray": has_gray = True
    
    if has_red:
        return "red", LANG[st.session_state.lang]["overdue"], passed, total
    if has_blue:
        return "blue", LANG[st.session_state.lang]["ready_for_test"], passed, total
    if has_green:
        return "green", LANG[st.session_state.lang]["trained"], passed, total
    if has_gray:
        return "gray", LANG[st.session_state.lang]["in_training"], passed, total
    if passed == total and total > 0:
        return "certified", LANG[st.session_state.lang]["certified"], passed, total
    return "gray", "Unknown", passed, total

# ============================================================
# LOAD DATA
# ============================================================
if 'data_loaded' not in st.session_state:
    machines, employees = load_data()
    st.session_state.machines = machines
    st.session_state.employees = employees
    st.session_state.data_loaded = True

# ============================================================
# CSS
# ============================================================
st.markdown(get_theme_css(), unsafe_allow_html=True)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-1d391kg {display: none !important;}
    .css-1kyxreq {display: none !important;}
    
    .main > div { padding: 0.5rem 1rem !important; max-width: 1200px !important; margin: 0 auto !important; }
    h1 { font-size: 22px !important; font-weight: 700 !important; margin-bottom: 10px !important; }
    
    .employee-card {
        padding: 14px 18px !important;
        border-radius: 10px !important;
        margin-bottom: 10px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    }
    .emp-name { font-size: 16px !important; font-weight: 600 !important; }
    .emp-number { font-size: 13px !important; margin-left: 8px !important; color: #7f8c8d !important; }
    
    .status-badge {
        padding: 2px 14px !important;
        border-radius: 20px !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        display: inline-block !important;
        color: white !important;
    }
    .badge-gray { background: #6c757d !important; }
    .badge-green { background: #28a745 !important; }
    .badge-blue { background: #007bff !important; }
    .badge-yellow { background: #ffc107 !important; color: #212529 !important; }
    .badge-red { background: #dc3545 !important; }
    .badge-certified { background: #17a2b8 !important; }
    
    .training-row {
        background: #f8f9fa !important;
        padding: 6px 12px !important;
        border-radius: 6px !important;
        margin-bottom: 4px !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
        font-size: 13px !important;
        border: 1px solid #e9ecef !important;
    }
    .machine-name { font-weight: 600 !important; min-width: 100px !important; }
    
    .stat-box { padding: 8px 12px !important; border-radius: 8px !important; text-align: center !important; }
    .stat-box .number { font-size: 20px !important; font-weight: 700 !important; }
    .stat-box .label { font-size: 11px !important; }
    
    .legend-box {
        padding: 8px 14px !important;
        border-radius: 8px !important;
        margin-bottom: 12px !important;
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 12px !important;
        align-items: center !important;
        font-size: 12px !important;
    }
    .legend-item { display: flex !important; align-items: center !important; gap: 5px !important; }
    .legend-dot { width: 10px !important; height: 10px !important; border-radius: 50% !important; display: inline-block !important; }
    .dot-gray { background: #6c757d !important; }
    .dot-green { background: #28a745 !important; }
    .dot-blue { background: #007bff !important; }
    .dot-yellow { background: #ffc107 !important; }
    .dot-red { background: #dc3545 !important; }
    .dot-certified { background: #17a2b8 !important; }
    
    .stButton > button { border-radius: 6px !important; font-weight: 500 !important; font-size: 12px !important; padding: 4px 14px !important; }
    .stButton > button:hover { transform: translateY(-1px) !important; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 4px !important; padding: 4px !important; border-radius: 8px !important; }
    .stTabs [data-baseweb="tab"] { border-radius: 6px !important; padding: 6px 16px !important; font-weight: 500 !important; font-size: 13px !important; }
    
    @media (max-width: 768px) { .training-row { flex-direction: column !important; align-items: stretch !important; } }
</style>
""", unsafe_allow_html=True)

# ============================================================
# TOP BAR
# ============================================================
L = LANG[st.session_state.lang]

col1, col2, col3, col4 = st.columns([2, 0.8, 0.6, 0.6])
with col1:
    st.title(L["title"])
with col2:
    st.markdown(f'<span style="font-size:12px;color:#28a745;">💾 {L["auto_saved"]}</span>', unsafe_allow_html=True)
with col3:
    lang_options = {"🇬🇧 EN": "en", "🇹🇭 TH": "th", "🇨🇳 中文": "zh"}
    new_lang = st.selectbox("", list(lang_options.keys()), 
                           index=list(lang_options.values()).index(st.session_state.lang), 
                           label_visibility="collapsed")
    if new_lang and lang_options[new_lang] != st.session_state.lang:
        st.session_state.lang = lang_options[new_lang]
        st.rerun()
with col4:
    theme_options = ["☀️", "🌙"]
    current_theme = 0 if st.session_state.theme == "light" else 1
    new_theme = st.selectbox("", theme_options, index=current_theme, label_visibility="collapsed")
    if new_theme == "☀️" and st.session_state.theme != "light":
        st.session_state.theme = "light"
        st.rerun()
    elif new_theme == "🌙" and st.session_state.theme != "dark":
        st.session_state.theme = "dark"
        st.rerun()

# ============================================================
# STATS
# ============================================================
col1, col2, col3, col4, col5, col6 = st.columns(6)

gray = green = blue = yellow = red = certified = 0
for emp in st.session_state.employees:
    status, _, _, _ = get_overall_status(emp)
    if status == "gray": gray += 1
    elif status == "green": green += 1
    elif status == "blue": blue += 1
    elif status == "yellow": yellow += 1
    elif status == "red": red += 1
    elif status == "certified": certified += 1

col1.markdown(f'<div class="stat-box"><div class="number">{len(st.session_state.employees)}</div><div class="label">👥 {L["employees_count"]}</div></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="stat-box"><div class="number">{gray}</div><div class="label">⚪ {L["in_training"]}</div></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="stat-box"><div class="number">{green}</div><div class="label">🟢 {L["trained"]}</div></div>', unsafe_allow_html=True)
col4.markdown(f'<div class="stat-box"><div class="number">{blue}</div><div class="label">🔵 {L["ready_for_test"]}</div></div>', unsafe_allow_html=True)
col5.markdown(f'<div class="stat-box"><div class="number">{yellow}</div><div class="label">🟡 {L["passed"]}</div></div>', unsafe_allow_html=True)
col6.markdown(f'<div class="stat-box"><div class="number">{red}</div><div class="label">🔴 {L["overdue"]}</div></div>', unsafe_allow_html=True)

# ============================================================
# LEGEND
# ============================================================
st.markdown(f"""
<div class="legend-box">
    <span style="font-weight:600;">{L["status_guide"]}</span>
    <span class="legend-item"><span class="legend-dot dot-gray"></span> {L["in_training"]}</span>
    <span class="legend-item"><span class="legend-dot dot-green"></span> {L["trained"]}</span>
    <span class="legend-item"><span class="legend-dot dot-blue"></span> {L["ready_for_test"]}</span>
    <span class="legend-item"><span class="legend-dot dot-yellow"></span> {L["passed"]}</span>
    <span class="legend-item"><span class="legend-dot dot-red"></span> {L["overdue"]}</span>
    <span class="legend-item"><span class="legend-dot dot-certified"></span> {L["certified"]}</span>
    <span style="margin-left:auto;font-size:11px;">{L["click_ready"]}</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# TABS
# ============================================================
tab1, tab2 = st.tabs([L["employees"], L["machines"]])

# ============================================================
# TAB 1: EMPLOYEES
# ============================================================
with tab1:
    # --- BUTTONS ---
    col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
    with col1:
        if st.button(L["add_employee"], use_container_width=True):
            st.session_state.show_add_emp = True
    with col2:
        if st.button(L["export"], use_container_width=True):
            data = {"machines": st.session_state.machines, "employees": st.session_state.employees}
            json_str = json.dumps(data, indent=2)
            st.download_button(
                label="📥 Download",
                data=json_str,
                file_name=f"training_data_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    with col3:
        uploaded_file = st.file_uploader(L["import"], type=["json"], label_visibility="collapsed")
        if uploaded_file:
            try:
                data = json.load(uploaded_file)
                if "machines" in data and "employees" in data:
                    st.session_state.machines = data["machines"]
                    st.session_state.employees = data["employees"]
                    save_data()
                    st.success("✅ Imported!")
                    st.rerun()
                else:
                    st.error("❌ Invalid file!")
            except:
                st.error("❌ Error reading file!")
    
    # --- ADD EMPLOYEE ---
    if st.session_state.get("show_add_emp", False):
        with st.container():
            st.info("➕ " + L["add_employee"])
            col1, col2, col3 = st.columns(3)
            with col1:
                new_num = st.text_input(L["employee_number"], placeholder="e.g. EMP-001")
            with col2:
                new_name = st.text_input(L["employee_name"], placeholder="Full Name")
            with col3:
                if st.button(L["save"]):
                    if new_num and new_name:
                        if any(e["emp_number"] == new_num for e in st.session_state.employees):
                            st.error("❌ Number already exists!")
                        else:
                            st.session_state.employees.append({
                                "emp_number": new_num,
                                "emp_name": new_name,
                                "training": []
                            })
                            save_data()
                            st.success("✅ Employee added!")
                            st.session_state.show_add_emp = False
                            st.rerun()
                    else:
                        st.warning("⚠️ Fill all fields!")
            if st.button(L["close"]):
                st.session_state.show_add_emp = False
                st.rerun()
        st.divider()
    
    # --- FILTERS ---
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_status = st.selectbox(L["filter"], [L["all"]] + [L["in_training"], L["trained"], L["ready_for_test"], L["passed"], L["overdue"], L["certified"]])
    with col2:
        filter_machine = st.selectbox(L["machines"], [L["all_machines"]] + list(st.session_state.machines.keys()))
    with col3:
        search = st.text_input("🔎", placeholder=L["search"], label_visibility="collapsed")
    
    # --- FILTER ---
    employees_to_show = st.session_state.employees.copy()
    
    status_map = {L["in_training"]: "gray", L["trained"]: "green", L["ready_for_test"]: "blue", L["passed"]: "yellow", L["overdue"]: "red", L["certified"]: "certified"}
    if filter_status != L["all"]:
        employees_to_show = [e for e in employees_to_show if get_overall_status(e)[0] == status_map.get(filter_status, "")]
    if filter_machine != L["all_machines"]:
        employees_to_show = [e for e in employees_to_show if any(t["machine"] == filter_machine for t in e.get("training", []))]
    if search:
        employees_to_show = [e for e in employees_to_show if search.lower() in e["emp_name"].lower() or search in e["emp_number"]]
    
    st.caption(f"{L['showing']}: {len(employees_to_show)} {L['employees_count']}")
    
    # --- DISPLAY EMPLOYEES ---
    if not employees_to_show:
        st.info(f"No {L['employees_count']} found. Click 'Add Employee' to add one!")
    
    for emp in employees_to_show:
        status, label, passed, total = get_overall_status(emp)
        
        colors = {"gray": "#6c757d", "green": "#28a745", "blue": "#007bff", "yellow": "#ffc107", "red": "#dc3545", "certified": "#17a2b8"}
        border = colors.get(status, "#6c757d")
        
        badge_map = {"gray": "badge-gray", "green": "badge-green", "blue": "badge-blue", "yellow": "badge-yellow", "red": "badge-red", "certified": "badge-certified"}
        badge = badge_map.get(status, "badge-gray")
        
        st.markdown(f"""
        <div class="employee-card" style="border-left: 4px solid {border};">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px;">
                <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
                    <span class="emp-name">{emp['emp_name']}</span>
                    <span class="emp-number">({emp['emp_number']})</span>
                </div>
                <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
                    <span class="status-badge {badge}">{label}</span>
                    <span style="font-size:12px;">{L['progress']}: {passed}/{total}</span>
                    <button style="background:#dc3545;color:white;border:none;border-radius:4px;padding:2px 10px;font-size:12px;cursor:pointer;" onclick="alert('{L['confirm_delete']} {emp['emp_name']}?')">🗑️</button>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🗑️ Delete", key=f"del_emp_{emp['emp_number']}"):
            st.session_state.employees = [e for e in st.session_state.employees if e["emp_number"] != emp["emp_number"]]
            save_data()
            st.rerun()
        
        if emp.get("training"):
            for idx, t in enumerate(emp["training"]):
                m = get_machine(t["machine"])
                t_status, t_label = get_status(t, m)
                req = m.get("required_sessions", 6) if m else "?"
                
                t_colors = {"gray": "#6c757d", "green": "#28a745", "blue": "#007bff", "yellow": "#ffc107", "red": "#dc3545"}
                t_color = t_colors.get(t_status, "#6c757d")
                
                col1, col2, col3, col4, col5, col6, col7 = st.columns([1.8, 0.8, 0.8, 1.2, 0.5, 0.5, 0.5])
                with col1:
                    st.markdown(f'<span style="font-weight:600;">{t["machine"]}</span>', unsafe_allow_html=True)
                with col2:
                    current = t.get("sessions", 0)
                    new = st.number_input("", min_value=0, max_value=99, value=current, key=f"sess_{emp['emp_number']}_{idx}", label_visibility="collapsed")
                    if new != current:
                        t["sessions"] = new
                        if m and new < m.get("required_sessions", 6):
                            t["ready_date"] = None
                            t["test_date"] = None
                        save_data()
                        st.rerun()
                    st.markdown(f'<span style="font-size:12px;">/{req}</span>', unsafe_allow_html=True)
                with col3:
                    st.write(t.get("training_date", "-"))
                with col4:
                    st.markdown(f'<span style="background:{t_color};color:white;padding:1px 10px;border-radius:10px;font-size:11px;">{t_label}</span>', unsafe_allow_html=True)
                with col5:
                    if st.button("➕", key=f"add_{emp['emp_number']}_{idx}"):
                        t["sessions"] = t.get("sessions", 0) + 1
                        save_data()
                        st.rerun()
                with col6:
                    if t_status == "green" and not t.get("ready_date"):
                        if st.button(L["ready"], key=f"rdy_{emp['emp_number']}_{idx}"):
                            t["ready_date"] = datetime.now().strftime("%Y-%m-%d")
                            save_data()
                            st.rerun()
                with col7:
                    if t_status == "blue" and not t.get("test_date"):
                        if st.button(L["pass"], key=f"pass_{emp['emp_number']}_{idx}"):
                            t["test_date"] = datetime.now().strftime("%Y-%m-%d")
                            save_data()
                            st.rerun()
                    elif t_status != "yellow" and t_status != "blue":
                        if st.button("✖", key=f"del_tr_{emp['emp_number']}_{idx}"):
                            emp["training"].pop(idx)
                            save_data()
                            st.rerun()
        else:
            st.markdown(f'<span style="color:#7f8c8d;font-size:13px;">{L["no_training"]}</span>', unsafe_allow_html=True)
        
        if st.button(L["add_training"], key=f"add_tr_{emp['emp_number']}"):
            st.session_state.add_training_for = emp["emp_number"]
        
        if st.session_state.get("add_training_for") == emp["emp_number"]:
            existing = [t["machine"] for t in emp.get("training", [])]
            available = [m for m in st.session_state.machines.keys() if m not in existing]
            
            if available:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    machine = st.selectbox(L["machines"], available, key=f"mach_{emp['emp_number']}")
                with col2:
                    sessions = st.number_input(L["sessions_completed"], min_value=0, value=0, key=f"sess_new_{emp['emp_number']}")
                with col3:
                    date = st.date_input(L["training_date"], datetime.now(), key=f"date_{emp['emp_number']}")
                with col4:
                    if st.button(L["save"], key=f"save_tr_{emp['emp_number']}"):
                        emp["training"].append({
                            "machine": machine,
                            "sessions": sessions,
                            "training_date": date.strftime("%Y-%m-%d"),
                            "ready_date": None,
                            "test_date": None
                        })
                        save_data()
                        st.session_state.add_training_for = None
                        st.rerun()
            else:
                st.info("✅ Training on all machines!")
                if st.button(L["close"], key=f"close_{emp['emp_number']}"):
                    st.session_state.add_training_for = None
                    st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# TAB 2: MACHINES
# ============================================================
with tab2:
    st.subheader(L["machines"])
    
    with st.expander("➕ Add Machine", expanded=False):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            new_name = st.text_input(L["machine_name"])
        with col2:
            new_sessions = st.number_input(L["required_sessions"], min_value=1, value=5)
        with col3:
            new_window = st.number_input(L["test_window"], min_value=1, value=7)
        with col4:
            new_color = st.selectbox(L["difficulty"], ["amber", "red", "green"])
        
        if st.button(L["save"]):
            if new_name and new_name not in st.session_state.machines:
                st.session_state.machines[new_name] = {
                    "required_sessions": new_sessions,
                    "window_days": new_window,
                    "color": new_color
                }
                save_data()
                st.success(f"✅ Added: {new_name}")
                st.rerun()
            else:
                st.warning("⚠️ Name already exists or empty")
    
    if not st.session_state.machines:
        st.info(f"No {L['machines_count']} found. Click 'Add Machine' to add one!")
    
    for name, cfg in st.session_state.machines.items():
        color_map = {"red": "#e74c3c", "amber": "#f39c12", "green": "#2ecc71"}
        border = color_map.get(cfg.get("color", "amber"), "#f39c12")
        diff = {"red": L["high"], "amber": L["medium"], "green": L["low"]}
        
        st.markdown(f"""
        <div style="background:white;padding:12px 16px;border-radius:8px;margin-bottom:8px;border:1px solid #e8ecf1;border-left:4px solid {border};">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;">
                <div style="font-weight:600;font-size:15px;">{name}</div>
                <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
                    <span>📚 {cfg['required_sessions']} {L['sessions']}</span>
                    <span>⏰ {cfg['window_days']} {L['days']}</span>
                    <span>{diff.get(cfg.get('color', 'amber'), L['medium'])}</span>
                    <button style="background:#007bff;color:white;border:none;border-radius:4px;padding:2px 12px;font-size:12px;cursor:pointer;" onclick="document.getElementById('edit_{name}').style.display='block'">✏️ Edit</button>
                    <button style="background:#dc3545;color:white;border:none;border-radius:4px;padding:2px 12px;font-size:12px;cursor:pointer;" onclick="alert('Delete {name}?')">🗑️</button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"✏️ Edit {name}", expanded=False):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                new_sessions = st.number_input(L["required_sessions"], min_value=1, value=cfg["required_sessions"], key=f"sess_{name}")
            with col2:
                new_window = st.number_input(L["test_window"], min_value=1, value=cfg["window_days"], key=f"win_{name}")
            with col3:
                new_color = st.selectbox(L["difficulty"], ["red", "amber", "green"], 
                                        index=["red", "amber", "green"].index(cfg.get("color", "amber")), 
                                        key=f"color_{name}")
            with col4:
                new_name = st.text_input(L["new_name"], value=name, key=f"rename_{name}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(L["save"], key=f"save_mach_{name}"):
                    if new_name and new_name != name and new_name not in st.session_state.machines:
                        st.session_state.machines[new_name] = st.session_state.machines.pop(name)
                        for emp in st.session_state.employees:
                            for t in emp.get("training", []):
                                if t["machine"] == name:
                                    t["machine"] = new_name
                        name = new_name
                    
                    st.session_state.machines[name]["required_sessions"] = new_sessions
                    st.session_state.machines[name]["window_days"] = new_window
                    st.session_state.machines[name]["color"] = new_color
                    save_data()
                    st.success("✅ Machine updated!")
                    st.rerun()
            with col2:
                if st.button(L["cancel"], key=f"cancel_mach_{name}"):
                    st.rerun()
            with col3:
                if st.button("🗑️ Delete", key=f"del_mach_{name}"):
                    for emp in st.session_state.employees:
                        emp["training"] = [t for t in emp.get("training", []) if t["machine"] != name]
                    del st.session_state.machines[name]
                    save_data()
                    st.rerun()

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.caption(f"📊 {len(st.session_state.employees)} {L['employees_count']} · {len(st.session_state.machines)} {L['machines_count']} · {L['auto_saved']}")