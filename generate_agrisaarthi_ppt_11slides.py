import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# AGRISAARTHI 11-SLIDE COMPREHENSIVE PRESENTATION GENERATOR
# ==============================================================================

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_slide_layout = prs.slide_layouts[6]

# Theme Colors
C_BG = RGBColor(248, 250, 252)          # #F8FAFC
C_PRIMARY = RGBColor(27, 67, 50)        # #1B4332 - Deep Forest Green
C_SECONDARY = RGBColor(45, 106, 79)     # #2D6A4F - Medium Forest Green
C_ACCENT = RGBColor(64, 145, 108)       # #40916C - Foliage Green
C_EMERALD = RGBColor(82, 183, 136)      # #52B788 - Fresh Green
C_GOLD = RGBColor(217, 119, 6)          # #D97706 - Amber/Gold
C_DARK = RGBColor(30, 41, 59)           # #1E293B - Slate Dark
C_MUTED = RGBColor(100, 116, 139)       # #64748B - Slate Muted
C_WHITE = RGBColor(255, 255, 255)       # Pure White
C_CARD_BG = RGBColor(255, 255, 255)
C_BORDER = RGBColor(226, 232, 240)      # Light border
C_LIGHT_GREEN = RGBColor(236, 253, 245) # Soft Green fill
C_LIGHT_BLUE = RGBColor(239, 246, 255)  # Soft Blue fill

ASSETS_DIR = r"C:\Users\taman\OneDrive\Desktop\agrisaarthi\ppt_assets"
IMG_LPU = os.path.join(ASSETS_DIR, r"word\media\image1.png")
IMG_LOGO = os.path.join(ASSETS_DIR, r"logo_brand.png")
IMG_ARCH = os.path.join(ASSETS_DIR, r"word\media\image2.png")
IMG_ML_FLOW = os.path.join(ASSETS_DIR, r"word\media\image3.png")
IMG_SECURITY = os.path.join(ASSETS_DIR, r"word\media\image4.png")
IMG_DASHBOARD = os.path.join(ASSETS_DIR, r"dashboard_ss.png")
IMG_REGISTER = os.path.join(ASSETS_DIR, r"register_ss.png")

def set_slide_background(slide):
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = C_BG
    bg_shape.line.fill.background()
    return bg_shape

def add_header(slide, title_text, category_text="AGRISAARTHI · 11-SLIDE COMPREHENSIVE PRESENTATION", slide_num=None):
    header_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
    header_box.fill.solid()
    header_box.fill.fore_color.rgb = C_PRIMARY
    header_box.line.fill.background()

    accent_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.15), Inches(13.333), Inches(0.06))
    accent_line.fill.solid()
    accent_line.fill.fore_color.rgb = C_GOLD
    accent_line.line.fill.background()

    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(10.5), Inches(0.95))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = "Segoe UI"
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_EMERALD

    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.name = "Segoe UI"
    p_title.font.size = Pt(21)
    p_title.font.bold = True
    p_title.font.color.rgb = C_WHITE

    if os.path.exists(IMG_LOGO):
        try:
            slide.shapes.add_picture(IMG_LOGO, Inches(11.8), Inches(0.12), width=Inches(1.0))
        except:
            pass

    if slide_num:
        tb_num = slide.shapes.add_textbox(Inches(12.0), Inches(7.1), Inches(1.0), Inches(0.35))
        p_n = tb_num.text_frame.paragraphs[0]
        p_n.text = f"{slide_num} / 11"
        p_n.font.name = "Segoe UI"
        p_n.font.size = Pt(10)
        p_n.font.bold = True
        p_n.font.color.rgb = C_MUTED
        p_n.alignment = PP_ALIGN.RIGHT

def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
    else:
        card.line.fill.background()
    return card

def add_bullet_point(text_frame, bold_prefix, text_content, font_size=12, is_first=False):
    p = text_frame.paragraphs[0] if is_first else text_frame.add_paragraph()
    p.space_after = Pt(6)
    p.space_before = Pt(2)
    
    run_bullet = p.add_run()
    run_bullet.text = "▪ "
    run_bullet.font.name = "Segoe UI"
    run_bullet.font.size = Pt(font_size)
    run_bullet.font.bold = True
    run_bullet.font.color.rgb = C_SECONDARY

    run_bold = p.add_run()
    run_bold.text = bold_prefix + " "
    run_bold.font.name = "Segoe UI"
    run_bold.font.size = Pt(font_size)
    run_bold.font.bold = True
    run_bold.font.color.rgb = C_DARK

    run_text = p.add_run()
    run_text.text = text_content
    run_text.font.name = "Segoe UI"
    run_text.font.size = Pt(font_size)
    run_text.font.bold = False
    run_text.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 1: TITLE SLIDE & CREDENTIALS
# ==============================================================================
s1 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s1)

hero_banner = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(4.5), Inches(7.5))
hero_banner.fill.solid()
hero_banner.fill.fore_color.rgb = C_PRIMARY
hero_banner.line.fill.background()

stripe = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.45), 0, Inches(0.08), Inches(7.5))
stripe.fill.solid()
stripe.fill.fore_color.rgb = C_GOLD
stripe.line.fill.background()

if os.path.exists(IMG_LPU):
    s1.shapes.add_picture(IMG_LPU, Inches(0.8), Inches(0.7), width=Inches(2.9))

tb_left = s1.shapes.add_textbox(Inches(0.8), Inches(2.1), Inches(3.2), Inches(4.8))
tf_left = tb_left.text_frame
tf_left.word_wrap = True

p_dept = tf_left.paragraphs[0]
p_dept.text = "LOVELY PROFESSIONAL UNIVERSITY\nPHAGWARA, PUNJAB"
p_dept.font.name = "Segoe UI"
p_dept.font.size = Pt(13)
p_dept.font.bold = True
p_dept.font.color.rgb = C_EMERALD

p_deg = tf_left.add_paragraph()
p_deg.text = "\nB.Tech. Computer Science & Engineering\nCapstone Project Report Presentation\nNovember 2026"
p_deg.font.name = "Segoe UI"
p_deg.font.size = Pt(11)
p_deg.font.color.rgb = RGBColor(220, 240, 230)

p_sup = tf_left.add_paragraph()
p_sup.text = "\nUnder the Supervision of:\nMr. Aryan Chauhan (UID: 35200)\nAssistant Professor, Dept. of CSE"
p_sup.font.name = "Segoe UI"
p_sup.font.size = Pt(11)
p_sup.font.bold = True
p_sup.font.color.rgb = C_WHITE

if os.path.exists(IMG_LOGO):
    s1.shapes.add_picture(IMG_LOGO, Inches(5.1), Inches(0.65), width=Inches(1.8))

tb_right = s1.shapes.add_textbox(Inches(7.1), Inches(0.6), Inches(5.8), Inches(2.3))
tf_right = tb_right.text_frame
tf_right.word_wrap = True

p_main = tf_right.paragraphs[0]
p_main.text = "AgriSaarthi"
p_main.font.name = "Segoe UI"
p_main.font.size = Pt(38)
p_main.font.bold = True
p_main.font.color.rgb = C_PRIMARY

p_sub = tf_right.add_paragraph()
p_sub.text = "Smart Agriculture Advisory & Crop Intelligence Platform"
p_sub.font.name = "Segoe UI"
p_sub.font.size = Pt(15)
p_sub.font.bold = True
p_sub.font.color.rgb = C_SECONDARY

p_tag = tf_right.add_paragraph()
p_tag.text = "“KNOW MORE GROW MORE”"
p_tag.font.name = "Segoe UI"
p_tag.font.size = Pt(12)
p_tag.font.bold = True
p_tag.font.color.rgb = C_GOLD

add_card(s1, Inches(5.0), Inches(3.1), Inches(7.8), Inches(3.9), bg_color=C_CARD_BG, border_color=C_BORDER)

tb_team_hdr = s1.shapes.add_textbox(Inches(5.3), Inches(3.25), Inches(7.2), Inches(0.45))
p_thdr = tb_team_hdr.text_frame.paragraphs[0]
p_thdr.text = "PROJECT DEVELOPMENT TEAM & CORE RESPONSIBILITIES"
p_thdr.font.name = "Segoe UI"
p_thdr.font.size = Pt(12)
p_thdr.font.bold = True
p_thdr.font.color.rgb = C_PRIMARY

members = [
    ("Taman Preet Singh", "12309438", "Backend API Gateway,\nSecurity & SQL Database", "ASP.NET Core 10 Web API, JWT Bearer Token Auth, EF Core Code-First Migrations, SQL Server LocalDB."),
    ("Utkarsh", "12308727", "Frontend Engineering,\nUI/UX & Dashboards", "React 19 SPA, Vite Build Engine, Tailwind CSS, Responsive Farmer Portal & Analytics Views."),
    ("Mansi Verma", "12416455", "AI/ML Microservices &\nAgronomic Datasets", "Python FastAPI Service, Random Forest 99.2% Crop Model, Feature Engineering & Open-Meteo Integration.")
]

for idx, (m_name, m_reg, m_role, m_desc) in enumerate(members):
    c_left = Inches(5.2 + idx * 2.45)
    mem_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(3.8), Inches(2.35), Inches(3.0))
    mem_box.fill.solid()
    mem_box.fill.fore_color.rgb = C_LIGHT_GREEN if idx == 0 else C_BG
    mem_box.line.color.rgb = C_ACCENT if idx == 0 else C_BORDER
    mem_box.line.width = Pt(1)

    tb_m = s1.shapes.add_textbox(c_left + Inches(0.1), Inches(3.9), Inches(2.15), Inches(2.8))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    
    pm1 = tf_m.paragraphs[0]
    pm1.text = m_name
    pm1.font.name = "Segoe UI"
    pm1.font.size = Pt(12.5)
    pm1.font.bold = True
    pm1.font.color.rgb = C_PRIMARY

    pm2 = tf_m.add_paragraph()
    pm2.text = f"Reg. No: {m_reg}"
    pm2.font.name = "Segoe UI"
    pm2.font.size = Pt(10.5)
    pm2.font.bold = True
    pm2.font.color.rgb = C_GOLD

    pm3 = tf_m.add_paragraph()
    pm3.text = f"\n{m_role}"
    pm3.font.name = "Segoe UI"
    pm3.font.size = Pt(9.5)
    pm3.font.bold = True
    pm3.font.color.rgb = C_DARK

    pm4 = tf_m.add_paragraph()
    pm4.text = f"\n{m_desc}"
    pm4.font.name = "Segoe UI"
    pm4.font.size = Pt(8.5)
    pm4.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 2: PROBLEM STATEMENT, MOTIVATION & PROJECT OBJECTIVES
# ==============================================================================
s2 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s2)
add_header(s2, "Executive Context: Problem Statement & Project Objectives", "Chapter 1 & 2 · Background & Goals", slide_num=2)

# Left Column: The Problem Statement (4 Critical Barriers)
add_card(s2, Inches(0.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_p_hdr = s2.shapes.add_textbox(Inches(1.05), Inches(1.6), Inches(5.25), Inches(0.4))
p_ph = tb_p_hdr.text_frame.paragraphs[0]
p_ph.text = "CRITICAL AGRICULTURAL BARRIERS (THE PROBLEM)"
p_ph.font.name = "Segoe UI"
p_ph.font.size = Pt(12)
p_ph.font.bold = True
p_ph.font.color.rgb = RGBColor(185, 28, 28)

tb_p_body = s2.shapes.add_textbox(Inches(1.05), Inches(2.05), Inches(5.25), Inches(4.7))
tf_pb = tb_p_body.text_frame
tf_pb.word_wrap = True

add_bullet_point(tf_pb, "Suboptimal Crop Matching:", "86% of smallholder farmers rely on habit or regional tradition rather than quantifiable soil macronutrients (N-P-K, pH) and rainfall, causing 15-25% annual yield losses.", 11.5, True)
add_bullet_point(tf_pb, "Delayed Disease Diagnosis:", "Pathological infections spread exponentially before manual diagnosis occurs. Delayed treatment causes crop damage and excessive pesticide expenditure.", 11.5)
add_bullet_point(tf_pb, "Uncontextualized Forecasts:", "Standard mobile weather apps report raw metrics (temperature/humidity) without translating them into actionable agronomic decisions (irrigation shut-off, spraying windows).", 11.5)
add_bullet_point(tf_pb, "Severe Knowledge Fragmentation:", "Fertilizer schedules, pest management, and mandi prices remain scattered across disconnected pamphlets and slow government portals.", 11.5)

# Right Column: Core Engineering Objectives & Targeted Outcomes
add_card(s2, Inches(6.75), Inches(1.45), Inches(5.75), Inches(5.5))
tb_o_hdr = s2.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.25), Inches(0.4))
p_oh = tb_o_hdr.text_frame.paragraphs[0]
p_oh.text = "PROJECT OBJECTIVES & TECHNICAL TARGETS"
p_oh.font.name = "Segoe UI"
p_oh.font.size = Pt(12)
p_oh.font.bold = True
p_oh.font.color.rgb = C_PRIMARY

tb_o_body = s2.shapes.add_textbox(Inches(7.0), Inches(2.05), Inches(5.25), Inches(4.7))
tf_ob = tb_o_body.text_frame
tf_ob.word_wrap = True

add_bullet_point(tf_ob, "AI-Driven Crop Matching:", "Deploy a Random Forest machine learning pipeline achieving >98% accuracy based on 7 real-time agronomic parameters (N, P, K, Temp, Humidity, pH, Rainfall).", 11.5, True)
add_bullet_point(tf_ob, "Real-Time Weather Intelligence:", "Integrate Open-Meteo REST APIs to synthesize automated meteorological advisories with localized farming guidelines.", 11.5)
add_bullet_point(tf_ob, "Enterprise Microservice Gateway:", "Implement an ASP.NET Core 10 Web API gateway enforcing JWT security, CORS policies, rate limiting, and sub-50ms response latencies.", 11.5)
add_bullet_point(tf_ob, "Farmer-Centric Portal & Visual Studio Integration:", "Deliver a responsive React 19 SPA dashboard backed by Microsoft SQL Server LocalDB with seamless one-click execution via Visual Studio.", 11.5)

# ==============================================================================
# SLIDE 3: ENTERPRISE 4-TIER ARCHITECTURE & TECH STACK
# ==============================================================================
s3 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s3)
add_header(s3, "System Architecture: 4-Tier Enterprise Blueprint", "Chapter 3 · Architecture & Design", slide_num=3)

# Left Column: System Architecture Diagram
add_card(s3, Inches(0.8), Inches(1.45), Inches(5.8), Inches(5.5))
tb_arch_hdr = s3.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.4), Inches(0.35))
p_ah = tb_arch_hdr.text_frame.paragraphs[0]
p_ah.text = "OFFICIAL 4-TIER SYSTEM ARCHITECTURE"
p_ah.font.name = "Segoe UI"
p_ah.font.size = Pt(11)
p_ah.font.bold = True
p_ah.font.color.rgb = C_PRIMARY

if os.path.exists(IMG_ARCH):
    s3.shapes.add_picture(IMG_ARCH, Inches(0.95), Inches(1.95), width=Inches(5.5), height=Inches(4.85))

# Right Column: Tier-by-Tier Technical Specifications
tiers = [
    ("Tier 1: Client Presentation Layer", "React 19 SPA · Vite Build Tool · Tailwind CSS · Heroicons", 
     "Responsive desktop & mobile user experience, client-side JWT token management, interactive forms, and real-time dashboard visualization.", C_PRIMARY),
    
    ("Tier 2: API Gateway & Application Logic", "ASP.NET Core 10 Web API · C# · Entity Framework Core", 
     "REST API gateway hosting JWT Bearer auth, CORS security middleware, IP rate limiting, DTO validation, and automated SQL schema migrations.", C_SECONDARY),
    
    ("Tier 3: AI Microservice Engine", "Python 3.10+ · FastAPI · Uvicorn · Scikit-Learn (Joblib)", 
     "Decoupled machine learning service running on port 8000; computes multiclass crop suitability probabilities with sub-50ms inference.", C_ACCENT),
    
    ("Tier 4: Persistence & External Data", "Microsoft SQL Server LocalDB · Open-Meteo REST API", 
     "Relational storage for farmer credentials, historical soil profiles, and advisory logs; combined with live GPS-based weather telemetries.", C_GOLD)
]

for idx, (t_title, t_stack, t_desc, t_col) in enumerate(tiers):
    y_pos = Inches(1.45 + idx * 1.38)
    add_card(s3, Inches(6.8), y_pos, Inches(5.75), Inches(1.26))
    
    strip = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), y_pos, Inches(0.18), Inches(1.26))
    strip.fill.solid()
    strip.fill.fore_color.rgb = t_col
    strip.line.fill.background()

    tb_t = s3.shapes.add_textbox(Inches(7.15), y_pos + Inches(0.08), Inches(5.25), Inches(1.1))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True

    pt1 = tf_t.paragraphs[0]
    pt1.text = t_title
    pt1.font.name = "Segoe UI"
    pt1.font.size = Pt(12)
    pt1.font.bold = True
    pt1.font.color.rgb = C_DARK

    pt2 = tf_t.add_paragraph()
    pt2.text = t_stack
    pt2.font.name = "Segoe UI"
    pt2.font.size = Pt(9.5)
    pt2.font.bold = True
    pt2.font.color.rgb = t_col

    pt3 = tf_t.add_paragraph()
    pt3.text = t_desc
    pt3.font.name = "Segoe UI"
    pt3.font.size = Pt(9)
    pt3.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 4: DATABASE DESIGN & ENTITY RELATIONSHIP MODEL
# ==============================================================================
s4 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s4)
add_header(s4, "Database Architecture: SQL Server Relational Modeling", "Chapter 4 · Database & Storage Design", slide_num=4)

# 4 Cards for the 4 core relational tables
tables = [
    ("Users Entity", "Master Farmer Accounts & Identity", [
        ("Id", "INT PRIMARY KEY (Identity 1,1)"),
        ("FullName", "NVARCHAR(150) NOT NULL"),
        ("Email", "NVARCHAR(200) UNIQUE INDEX NOT NULL"),
        ("PasswordHash", "NVARCHAR(MAX) NOT NULL (Argon2/PBKDF2)"),
        ("PhoneNumber", "NVARCHAR(20) NULL"),
        ("CreatedAt", "DATETIME2 NOT NULL DEFAULT GETUTCDATE()")
    ], C_PRIMARY),

    ("CropAdvisories Entity", "ML Crop Predictions & Soil Tests", [
        ("Id", "INT PRIMARY KEY (Identity 1,1)"),
        ("UserId", "INT FOREIGN KEY REFERENCES Users(Id)"),
        ("N, P, K", "FLOAT NOT NULL (Macronutrient Ratios)"),
        ("Temperature, Humidity", "FLOAT NOT NULL (Ambient Climate)"),
        ("Ph, Rainfall", "FLOAT NOT NULL (Soil Acidity & Annual Rain)"),
        ("RecommendedCrop", "NVARCHAR(100) NOT NULL (e.g. Rice, Maize)"),
        ("ConfidenceScore", "FLOAT NOT NULL (0.0 - 1.0)"),
        ("RequestDate", "DATETIME2 NOT NULL")
    ], C_SECONDARY),

    ("WeatherQueries Entity", "Meteorological Feeds & Notes", [
        ("Id", "INT PRIMARY KEY (Identity 1,1)"),
        ("UserId", "INT FOREIGN KEY REFERENCES Users(Id)"),
        ("Latitude, Longitude", "FLOAT NOT NULL (Farm GPS Coords)"),
        ("City", "NVARCHAR(100) NULL"),
        ("Temperature, Humidity", "FLOAT NOT NULL (Live Metrics)"),
        ("Condition", "NVARCHAR(100) NOT NULL (e.g. Rain, Clear)"),
        ("AdvisoryNotes", "NVARCHAR(MAX) (Agronomic Guidance)"),
        ("QueryDate", "DATETIME2 NOT NULL")
    ], C_ACCENT),

    ("SoilProfiles Entity", "Farmer Soil History & Fertility", [
        ("Id", "INT PRIMARY KEY (Identity 1,1)"),
        ("UserId", "INT FOREIGN KEY REFERENCES Users(Id)"),
        ("SoilType", "NVARCHAR(80) NOT NULL (Alluvial, Black, Loamy)"),
        ("OrganicCarbon", "FLOAT NULL (Soil Health Index)"),
        ("Location", "NVARCHAR(150) NOT NULL"),
        ("LastTestedDate", "DATETIME2 NOT NULL"),
        ("Status", "NVARCHAR(50) DEFAULT 'Active'")
    ], C_GOLD)
]

for idx, (t_name, t_subtitle, t_cols, t_col) in enumerate(tables):
    col = idx % 2
    row = idx // 2
    x = Inches(0.8 + col * 5.95)
    y = Inches(1.45 + row * 2.8)

    add_card(s4, x, y, Inches(5.75), Inches(2.65))

    bar = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(5.75), Inches(0.42))
    bar.fill.solid()
    bar.fill.fore_color.rgb = t_col
    bar.line.fill.background()

    tb_t = s4.shapes.add_textbox(x + Inches(0.2), y + Inches(0.06), Inches(5.35), Inches(0.35))
    pt = tb_t.text_frame.paragraphs[0]
    pt.text = f"{t_name} — {t_subtitle}"
    pt.font.name = "Segoe UI"
    pt.font.size = Pt(11)
    pt.font.bold = True
    pt.font.color.rgb = C_WHITE

    tb_c = s4.shapes.add_textbox(x + Inches(0.25), y + Inches(0.48), Inches(5.25), Inches(2.1))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True

    for c_idx, (col_name, col_type) in enumerate(t_cols):
        p_c = tf_c.paragraphs[0] if c_idx == 0 else tf_c.add_paragraph()
        p_c.space_after = Pt(1)
        r1 = p_c.add_run()
        r1.text = f"• {col_name}: "
        r1.font.name = "Consolas"
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = C_DARK
        
        r2 = p_c.add_run()
        r2.text = col_type
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 5: MACHINE LEARNING & CROP ADVISORY PIPELINE
# ==============================================================================
s5 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s5)
add_header(s5, "AI & Machine Learning: Agronomic Prediction Pipeline", "Chapter 5 · ML Engineering & Modeling", slide_num=5)

# Left Column: Machine Learning Flow Diagram
add_card(s5, Inches(0.8), Inches(1.45), Inches(5.8), Inches(5.5))
tb_ml_hdr = s5.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.4), Inches(0.35))
p_mh = tb_ml_hdr.text_frame.paragraphs[0]
p_mh.text = "OFFICIAL ML TRAINING & INFERENCE PIPELINE"
p_mh.font.name = "Segoe UI"
p_mh.font.size = Pt(11)
p_mh.font.bold = True
p_mh.font.color.rgb = C_PRIMARY

if os.path.exists(IMG_ML_FLOW):
    s5.shapes.add_picture(IMG_ML_FLOW, Inches(0.95), Inches(1.95), width=Inches(5.5), height=Inches(4.85))

# Right Column: Modeling Details & Metric Benchmarks
add_card(s5, Inches(6.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_ml_body = s5.shapes.add_textbox(Inches(7.05), Inches(1.6), Inches(5.25), Inches(5.15))
tf_mb = tb_ml_body.text_frame
tf_mb.word_wrap = True

add_bullet_point(tf_mb, "7 Agronomic Input Features:", "Trained on Nitrogen (N), Phosphorus (P), Potassium (K), Temperature (°C), Relative Humidity (%), Soil pH (0-14), and Annual Rainfall (mm).", 11, True)
add_bullet_point(tf_mb, "Random Forest Model (99.2% Accuracy):", "Ensemble of 100 decorrelated decision trees using Gini impurity. Outperformed all baseline models across 22 multiclass crop varieties with zero overfitting.", 11)
add_bullet_point(tf_mb, "Decision Tree Baseline (96.5% Accuracy):", "Single-tree CART architecture evaluated for algorithmic transparency and feature importance rule extraction.", 11)
add_bullet_point(tf_mb, "Feature Importance Hierarchy:", "Relative Humidity (21.4%), Annual Rainfall (19.8%), and Potassium (16.2%) emerged as the top 3 decisive crop yield drivers.", 11)
add_bullet_point(tf_mb, "Microservice Deployment:", "Pre-trained model serialized via Joblib (`crop_model.pkl`); served through asynchronous FastAPI endpoints (`POST /predict/crop`) delivering sub-50ms inference.", 11)

# Highlight Callout Box
callout = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.05), Inches(5.4), Inches(5.25), Inches(1.3))
callout.fill.solid()
callout.fill.fore_color.rgb = C_LIGHT_GREEN
callout.line.color.rgb = C_EMERALD
callout.line.width = Pt(1.2)

tb_c = s5.shapes.add_textbox(Inches(7.15), Inches(5.48), Inches(5.05), Inches(1.15))
tf_c = tb_c.text_frame
tf_c.word_wrap = True
pc = tf_c.paragraphs[0]
pc.text = "BENCHMARK PERFORMANCE VERIFICATION"
pc.font.name = "Segoe UI"
pc.font.size = Pt(10)
pc.font.bold = True
pc.font.color.rgb = C_PRIMARY

pc2 = tf_c.add_paragraph()
pc2.text = "Random Forest: 99.2% Accuracy | 0.99 F1-Score | Sub-50ms Latency\nTested across: Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Blackgram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee."
pc2.font.name = "Segoe UI"
pc2.font.size = Pt(8.5)
pc2.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 6: SECURITY ARCHITECTURE & DEFENSE-IN-DEPTH
# ==============================================================================
s6 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s6)
add_header(s6, "Security Architecture: Defense-in-Depth Implementation", "Chapter 6 · Security & Network Protection", slide_num=6)

# Left Column: Security Architecture Flow Diagram
add_card(s6, Inches(0.8), Inches(1.45), Inches(5.8), Inches(5.5))
tb_sec_hdr = s6.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.4), Inches(0.35))
p_sh = tb_sec_hdr.text_frame.paragraphs[0]
p_sh.text = "OFFICIAL APPLICATION SECURITY FLOW"
p_sh.font.name = "Segoe UI"
p_sh.font.size = Pt(11)
p_sh.font.bold = True
p_sh.font.color.rgb = C_PRIMARY

if os.path.exists(IMG_SECURITY):
    s6.shapes.add_picture(IMG_SECURITY, Inches(0.95), Inches(1.95), width=Inches(5.5), height=Inches(4.85))

# Right Column: 4 Security Mechanisms
sec_cards = [
    ("1. JWT Bearer Authentication", "Stateless, HMAC-SHA256 digitally signed tokens containing user claims. Validated on every private endpoint via ASP.NET Core authentication middleware.", C_PRIMARY),
    ("2. Cryptographic Password Hashing", "Argon2 / PBKDF2 with dynamic salting via Microsoft.AspNetCore.Identity.PasswordHasher<User>. Passwords never stored in plaintext.", C_SECONDARY),
    ("3. CORS Policy & Boundary Controls", "Strict origin whitelisting allowing only trusted frontend origins (localhost:5173 / production domain). Prevents cross-site unauthorized requests.", C_ACCENT),
    ("4. IP Rate Limiting & Input Sanitization", "Sliding-window IP rate limiting blocks brute-force authentication and DoS attacks. Strongly-typed DTOs and EF Core parameterization prevent SQLi & XSS.", C_GOLD)
]

for idx, (sc_title, sc_desc, sc_col) in enumerate(sec_cards):
    y_pos = Inches(1.45 + idx * 1.38)
    add_card(s6, Inches(6.8), y_pos, Inches(5.75), Inches(1.26))
    
    strip = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), y_pos, Inches(0.18), Inches(1.26))
    strip.fill.solid()
    strip.fill.fore_color.rgb = sc_col
    strip.line.fill.background()

    tb_sc = s6.shapes.add_textbox(Inches(7.15), y_pos + Inches(0.1), Inches(5.25), Inches(1.05))
    tf_sc = tb_sc.text_frame
    tf_sc.word_wrap = True

    ps1 = tf_sc.paragraphs[0]
    ps1.text = sc_title
    ps1.font.name = "Segoe UI"
    ps1.font.size = Pt(12)
    ps1.font.bold = True
    ps1.font.color.rgb = C_DARK

    ps2 = tf_sc.add_paragraph()
    ps2.text = sc_desc
    ps2.font.name = "Segoe UI"
    ps2.font.size = Pt(9.5)
    ps2.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 7: USER INTERFACE & FARMER DASHBOARD SCREENSHOT
# ==============================================================================
s7 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s7)
add_header(s7, "Frontend Experience: AgriSaarthi Farmer Dashboard", "Chapter 7 · UI/UX Design & Client Implementation", slide_num=7)

# Prominent Dashboard Screenshot (Center-Left)
add_card(s7, Inches(0.8), Inches(1.45), Inches(7.6), Inches(5.5))
tb_dash_hdr = s7.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(7.2), Inches(0.35))
p_dh = tb_dash_hdr.text_frame.paragraphs[0]
p_dh.text = "LIVE FARMER DASHBOARD & WEATHER WIDGET INTERFACE"
p_dh.font.name = "Segoe UI"
p_dh.font.size = Pt(11)
p_dh.font.bold = True
p_dh.font.color.rgb = C_PRIMARY

if os.path.exists(IMG_DASHBOARD):
    s7.shapes.add_picture(IMG_DASHBOARD, Inches(0.95), Inches(1.95), width=Inches(7.3), height=Inches(4.85))

# Right Column: UI Architecture & Key Capabilities
add_card(s7, Inches(8.6), Inches(1.45), Inches(3.95), Inches(5.5))
tb_ui_body = s7.shapes.add_textbox(Inches(8.8), Inches(1.6), Inches(3.55), Inches(5.15))
tf_ui = tb_ui_body.text_frame
tf_ui.word_wrap = True

add_bullet_point(tf_ui, "Agricultural Color Palette:", "Tailwind CSS palette anchored in Forest Green (#1B4332) and Fresh Emerald (#52B788), delivering maximum visual comfort for outdoor field visibility.", 10.5, True)
add_bullet_point(tf_ui, "Live Meteorological Widget:", "Displays real-time ambient temperature, humidity, wind conditions, and automated operational farming advisories.", 10.5)
add_bullet_point(tf_ui, "Card-Based Quick Navigation:", "One-tap direct access to Crop Advisory, Soil Analysis, Market Prices, and Leaf Disease Diagnosis.", 10.5)
add_bullet_point(tf_ui, "Responsive Fluid Layout:", "Engineered with Flexbox & CSS Grid for pixel-perfect presentation across smartphones, tablets, and desktop workstations.", 10.5)
add_bullet_point(tf_ui, "Accessibility Standards:", "High contrast ratios, clean typography (Inter / Segoe UI), and intuitive iconography for rural digital literacy.", 10.5)

# ==============================================================================
# SLIDE 8: CORE MODULES & USER ONBOARDING WORKFLOW
# ==============================================================================
s8 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s8)
add_header(s8, "System Modules: Farmer Registration & End-to-End Journey", "Chapter 8 · Functional Modules & User Workflows", slide_num=8)

# Left Column: Registration Screen Screenshot
add_card(s8, Inches(0.8), Inches(1.45), Inches(5.4), Inches(5.5))
tb_reg_hdr = s8.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.0), Inches(0.35))
p_rh = tb_reg_hdr.text_frame.paragraphs[0]
p_rh.text = "FARMER REGISTRATION & ONBOARDING INTERFACE"
p_rh.font.name = "Segoe UI"
p_rh.font.size = Pt(11)
p_rh.font.bold = True
p_rh.font.color.rgb = C_PRIMARY

if os.path.exists(IMG_REGISTER):
    s8.shapes.add_picture(IMG_REGISTER, Inches(0.95), Inches(1.95), width=Inches(5.1), height=Inches(4.85))

# Right Column: 4 End-to-End Functional Workflows
modules = [
    ("Module 1: Farmer Identity & Onboarding", 
     "Instant registration with validation, password confirmation, and secure JWT generation. Farmers gain a persistent profile to track soil history.", C_PRIMARY),
    
    ("Module 2: Precision Crop Recommendation", 
     "Input 7 soil & climate parameters; system calls ASP.NET Core Gateway -> FastAPI ML microservice -> returns top recommended crop with confidence score.", C_SECONDARY),
    
    ("Module 3: Hyperlocal Weather Advisory", 
     "Live Open-Meteo REST integration fetches 7-day weather forecasts; deterministic rule engine generates spraying and irrigation recommendations.", C_ACCENT),
    
    ("Module 4: Agronomic Knowledge & Soil Health", 
     "Curated repositories for fertilizer schedules, disease prevention, and soil testing records permanently persisted in SQL Server.", C_GOLD)
]

for idx, (m_title, m_desc, m_col) in enumerate(modules):
    y_pos = Inches(1.45 + idx * 1.38)
    add_card(s8, Inches(6.4), y_pos, Inches(6.15), Inches(1.26))
    
    strip = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.4), y_pos, Inches(0.18), Inches(1.26))
    strip.fill.solid()
    strip.fill.fore_color.rgb = m_col
    strip.line.fill.background()

    tb_m = s8.shapes.add_textbox(Inches(6.75), y_pos + Inches(0.1), Inches(5.65), Inches(1.05))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    pm1 = tf_m.paragraphs[0]
    pm1.text = m_title
    pm1.font.name = "Segoe UI"
    pm1.font.size = Pt(12)
    pm1.font.bold = True
    pm1.font.color.rgb = C_DARK

    pm2 = tf_m.add_paragraph()
    pm2.text = m_desc
    pm2.font.name = "Segoe UI"
    pm2.font.size = Pt(9.5)
    pm2.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 9: EXPERIMENTAL RESULTS, PERFORMANCE & TESTING
# ==============================================================================
s9 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s9)
add_header(s9, "System Evaluation: Quantitative Performance & Rigorous QA", "Chapter 9 · Results, Metrics & Testing", slide_num=9)

metrics = [
    ("99.2%", "AI CROP MODEL ACCURACY", "Random Forest achieved 99.2% overall test accuracy across 22 crop classes, with precision and recall exceeding 0.99.", C_PRIMARY),
    ("< 45 ms", "API GATEWAY LATENCY", "ASP.NET Core 10 Web API gateway processes authenticated transactions, token verifications, and routing in under 45 milliseconds.", C_SECONDARY),
    ("< 12 ms", "DATABASE EXECUTION TIME", "Indexed queries on Microsoft SQL Server LocalDB execute in ~12ms via Entity Framework Core compiled queries and connection pooling.", C_ACCENT),
    ("100%", "TEST SUITE COMPLETION", "Unit and integration tests across controllers, repository layers, and AI microservice endpoints passed with zero regressions.", C_GOLD)
]

for idx, (val, title, desc, col) in enumerate(metrics):
    x = Inches(0.8 + idx * 2.95)
    y = Inches(1.45)
    w = Inches(2.8)
    h = Inches(2.55)

    add_card(s9, x, y, w, h)

    top_stripe = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, Inches(0.12))
    top_stripe.fill.solid()
    top_stripe.fill.fore_color.rgb = col
    top_stripe.line.fill.background()

    tb = s9.shapes.add_textbox(x + Inches(0.15), y + Inches(0.2), w - Inches(0.3), h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = val
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = col
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf.add_paragraph()
    p2.text = title
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = C_DARK
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf.add_paragraph()
    p3.text = f"\n{desc}"
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(9)
    p3.font.color.rgb = C_MUTED
    p3.alignment = PP_ALIGN.CENTER

# Bottom Section: Quality Assurance & Load Testing
add_card(s9, Inches(0.8), Inches(4.2), Inches(11.75), Inches(2.75))
tb_qa = s9.shapes.add_textbox(Inches(1.1), Inches(4.35), Inches(11.15), Inches(2.45))
tf_qa = tb_qa.text_frame
tf_qa.word_wrap = True

p_qa_h = tf_qa.paragraphs[0]
p_qa_h.text = "RIGOROUS VERIFICATION, QUALITY ASSURANCE & BENCHMARKING"
p_qa_h.font.name = "Segoe UI"
p_qa_h.font.size = Pt(12)
p_qa_h.font.bold = True
p_qa_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_qa, "Unit Testing & EF Core In-Memory Mocking:", "Automated tests validate user registration, password hashing verification, and JWT issuance under diverse payload scenarios.", 11)
add_bullet_point(tf_qa, "AI Service Stress Testing:", "FastAPI endpoints subjected to concurrent mock request bursts (100 requests); achieved 100% success rate without memory leaks or worker thread blocking.", 11)
add_bullet_point(tf_qa, "Database Migrations & Resilience:", "Automated EF Core code-first migrations (`dbContext.Database.Migrate()`) verified on SQL Server LocalDB startup; ensures zero manual SQL intervention required.", 11)
add_bullet_point(tf_qa, "Cross-Platform Client Verification:", "React 19 SPA validated across Google Chrome, Microsoft Edge, and mobile WebKit viewports; 100% responsive compliance.", 11)

# ==============================================================================
# SLIDE 10: FUTURE ROADMAP & SCALABILITY ENHANCEMENTS
# ==============================================================================
s10 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s10)
add_header(s10, "Future Roadmap: Strategic Scalability & Commercial Expansion", "Chapter 10 · Strategic Roadmap & Innovations", slide_num=10)

roadmap = [
    ("Phase 1: Deep Learning Leaf Disease Vision", "Q1-Q2 2027", 
     "Integration of MobileNetV2 / ResNet CNN architectures for smartphone camera-based leaf disease recognition. Enables instant visual detection of 38+ plant pathologies with automated pesticide recommendations.", C_PRIMARY),
    
    ("Phase 2: APMC Live Mandi Market Intelligence", "Q3 2027", 
     "Integration with Government of India Agmarknet REST endpoints. Real-time daily commodity price tracking, mandi price comparison, and predictive price trend analytics.", C_SECONDARY),
    
    ("Phase 3: Multilingual Voice Assistant & Offline PWA", "Q4 2027", 
     "Speech-to-text / text-to-speech engine supporting Hindi, Punjabi, Marathi, Telugu, and Tamil. PWA ServiceWorker offline caching for remote rural zones lacking continuous internet.", C_ACCENT),
    
    ("Phase 4: IoT Soil Sensor Telemetry Integration", "2028+", 
     "Hardware telemetry integration with ESP32 and LoRaWAN field microcontrollers; automated ingestion of real-time soil moisture, temperature, and NPK sensor feeds.", C_GOLD)
]

for idx, (r_title, r_time, r_desc, r_col) in enumerate(roadmap):
    col = idx % 2
    row = idx // 2
    x = Inches(0.8 + col * 5.95)
    y = Inches(1.45 + row * 2.8)

    add_card(s10, x, y, Inches(5.75), Inches(2.65))

    bar = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(5.75), Inches(0.42))
    bar.fill.solid()
    bar.fill.fore_color.rgb = r_col
    bar.line.fill.background()

    tb_t = s10.shapes.add_textbox(x + Inches(0.2), y + Inches(0.06), Inches(5.35), Inches(0.35))
    pt = tb_t.text_frame.paragraphs[0]
    pt.text = f"{r_title} [{r_time}]"
    pt.font.name = "Segoe UI"
    pt.font.size = Pt(11)
    pt.font.bold = True
    pt.font.color.rgb = C_WHITE

    tb_b = s10.shapes.add_textbox(x + Inches(0.25), y + Inches(0.55), Inches(5.25), Inches(1.95))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    pb = tf_b.paragraphs[0]
    pb.text = r_desc
    pb.font.name = "Segoe UI"
    pb.font.size = Pt(10)
    pb.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 11: CONCLUSION, DELIVERABLES & ACKNOWLEDGMENTS
# ==============================================================================
s11 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s11)
add_header(s11, "Conclusion, Production Deliverables & Acknowledgments", "Chapter 11 · Summary & Sign-off", slide_num=11)

# Left Column: Project Deliverables Summary
add_card(s11, Inches(0.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_del = s11.shapes.add_textbox(Inches(1.05), Inches(1.6), Inches(5.25), Inches(5.15))
tf_del = tb_del.text_frame
tf_del.word_wrap = True

p_del_h = tf_del.paragraphs[0]
p_del_h.text = "OFFICIAL PROJECT DELIVERABLES"
p_del_h.font.name = "Segoe UI"
p_del_h.font.size = Pt(12)
p_del_h.font.bold = True
p_del_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_del, "Full-Stack ASP.NET Core API:", "Enterprise Web API configured on port 5000 with JWT authentication, CORS middleware, rate limiting, and EF Core migrations.", 11)
add_bullet_point(tf_del, "AI Crop Recommendation Engine:", "FastAPI microservice on port 8000 serving serialized 99.2% Random Forest model with sub-50ms inference.", 11)
add_bullet_point(tf_del, "Modern React 19 Frontend:", "Vite-powered Single Page Application on port 5173 with interactive dashboards and responsive mobile views.", 11)
add_bullet_point(tf_del, "Microsoft SQL Server LocalDB:", "Production database hosting Users, CropAdvisories, WeatherQueries, and SoilProfiles.", 11)
add_bullet_point(tf_del, "One-Click Launch Integration:", "Microsoft Visual Studio Solution (`AgriSaarthi.sln`) + automated launcher script (`run_agrisaarthi.bat`).", 11)

# Right Column: Acknowledgments & Final Sign-Off
add_card(s11, Inches(6.75), Inches(1.45), Inches(5.75), Inches(5.5))
tb_ack = s11.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.25), Inches(5.15))
tf_ack = tb_ack.text_frame
tf_ack.word_wrap = True

p_ack_h = tf_ack.paragraphs[0]
p_ack_h.text = "INSTITUTIONAL ACKNOWLEDGMENTS & SIGN-OFF"
p_ack_h.font.name = "Segoe UI"
p_ack_h.font.size = Pt(12)
p_ack_h.font.bold = True
p_ack_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_ack, "Academic Guidance:", "We express our sincere gratitude to Mr. Aryan Chauhan (UID: 35200), Assistant Professor, Department of CSE, for invaluable technical guidance and mentorship throughout this project.", 11)
add_bullet_point(tf_ack, "Institution:", "Lovely Professional University, Phagwara, Punjab — Department of Computer Science & Engineering.", 11)
add_bullet_point(tf_ack, "Project Development Team:", "• Taman Preet Singh (Reg: 12309438) — Backend, Security & DB\n• Utkarsh (Reg: 12308727) — Frontend, UI/UX & Dashboards\n• Mansi Verma (Reg: 12416455) — AI/ML & Agri-Knowledge", 11)

# Big Thank You Banner
thank_box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(5.25), Inches(5.25), Inches(1.45))
thank_box.fill.solid()
thank_box.fill.fore_color.rgb = C_PRIMARY
thank_box.line.color.rgb = C_GOLD
thank_box.line.width = Pt(1.5)

tb_thx = s11.shapes.add_textbox(Inches(7.1), Inches(5.35), Inches(5.05), Inches(1.25))
tf_thx = tb_thx.text_frame
tf_thx.word_wrap = True

pth1 = tf_thx.paragraphs[0]
pth1.text = "THANK YOU!"
pth1.font.name = "Segoe UI"
pth1.font.size = Pt(20)
pth1.font.bold = True
pth1.font.color.rgb = C_GOLD
pth1.alignment = PP_ALIGN.CENTER

pth2 = tf_thx.add_paragraph()
pth2.text = "Questions & Discussions Welcome\nAgriSaarthi: Know More — Grow More"
pth2.font.name = "Segoe UI"
pth2.font.size = Pt(11)
pth2.font.color.rgb = C_WHITE
pth2.alignment = PP_ALIGN.CENTER

# ==============================================================================
# SAVE PRESENTATION
# ==============================================================================
output_path = r"C:\Users\taman\OneDrive\Desktop\agrisaarthi\AgriSaarthi_Presentation.pptx"
prs.save(output_path)
print(f"SUCCESS: AgriSaarthi presentation saved to {output_path} with {len(prs.slides)} slides!")
