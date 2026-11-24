import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Initialize Presentation with 16:9 Widescreen
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_slide_layout = prs.slide_layouts[6]

# Color Palette Definitions
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

def add_header(slide, title_text, category_text="AGRISAARTHI PLATFORM"):
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
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = C_WHITE

    if os.path.exists(IMG_LOGO):
        try:
            slide.shapes.add_picture(IMG_LOGO, Inches(11.8), Inches(0.12), width=Inches(1.0))
        except:
            pass

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

def add_bullet_point(text_frame, bold_prefix, text_content, font_size=13, is_first=False):
    p = text_frame.paragraphs[0] if is_first else text_frame.add_paragraph()
    p.space_after = Pt(8)
    p.space_before = Pt(3)
    
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
# SLIDE 1: TITLE SLIDE
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
    s1.shapes.add_picture(IMG_LPU, Inches(0.8), Inches(0.8), width=Inches(2.9))

tb_left = s1.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(3.2), Inches(4.5))
tf_left = tb_left.text_frame
tf_left.word_wrap = True

p_dept = tf_left.paragraphs[0]
p_dept.text = "LOVELY PROFESSIONAL UNIVERSITY\nPHAGWARA, PUNJAB"
p_dept.font.name = "Segoe UI"
p_dept.font.size = Pt(13)
p_dept.font.bold = True
p_dept.font.color.rgb = C_EMERALD

p_deg = tf_left.add_paragraph()
p_deg.text = "\nB.Tech. in Computer Science & Engineering\nCapstone Project Report Presentation\nNovember 2026"
p_deg.font.name = "Segoe UI"
p_deg.font.size = Pt(11)
p_deg.font.color.rgb = RGBColor(220, 240, 230)

p_sup = tf_left.add_paragraph()
p_sup.text = "\nUnder the Supervision of:\nMr. Aryan Chauhan (UID: 35200)\nDepartment of CSE, LPU"
p_sup.font.name = "Segoe UI"
p_sup.font.size = Pt(11)
p_sup.font.bold = True
p_sup.font.color.rgb = C_WHITE

if os.path.exists(IMG_LOGO):
    s1.shapes.add_picture(IMG_LOGO, Inches(5.2), Inches(0.8), width=Inches(1.8))

tb_right = s1.shapes.add_textbox(Inches(7.2), Inches(0.7), Inches(5.6), Inches(2.2))
tf_right = tb_right.text_frame
tf_right.word_wrap = True

p_main = tf_right.paragraphs[0]
p_main.text = "AgriSaarthi"
p_main.font.name = "Segoe UI"
p_main.font.size = Pt(40)
p_main.font.bold = True
p_main.font.color.rgb = C_PRIMARY

p_sub = tf_right.add_paragraph()
p_sub.text = "AI-Powered Crop Advisory & Farmer Companion Platform"
p_sub.font.name = "Segoe UI"
p_sub.font.size = Pt(16)
p_sub.font.bold = True
p_sub.font.color.rgb = C_SECONDARY

p_tag = tf_right.add_paragraph()
p_tag.text = "“KNOW MORE GROW MORE”"
p_tag.font.name = "Segoe UI"
p_tag.font.size = Pt(13)
p_tag.font.bold = True
p_tag.font.color.rgb = C_GOLD

add_card(s1, Inches(5.2), Inches(3.2), Inches(7.5), Inches(3.6), bg_color=C_CARD_BG, border_color=C_BORDER)

tb_team_hdr = s1.shapes.add_textbox(Inches(5.5), Inches(3.35), Inches(6.8), Inches(0.5))
p_thdr = tb_team_hdr.text_frame.paragraphs[0]
p_thdr.text = "PROJECT DEVELOPMENT TEAM"
p_thdr.font.name = "Segoe UI"
p_thdr.font.size = Pt(13)
p_thdr.font.bold = True
p_thdr.font.color.rgb = C_PRIMARY

members = [
    ("Taman Preet Singh", "12309438", "Backend API Gateway,\nSecurity & Database"),
    ("Utkarsh", "12308727", "Frontend Development,\nUI/UX & Dashboards"),
    ("Mansi Verma", "12416455", "AI/ML Microservices &\nAgri-Knowledge Data")
]

for idx, (m_name, m_reg, m_role) in enumerate(members):
    c_left = Inches(5.4 + idx * 2.35)
    mem_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(3.9), Inches(2.2), Inches(2.6))
    mem_box.fill.solid()
    mem_box.fill.fore_color.rgb = C_LIGHT_GREEN if idx == 0 else C_BG
    mem_box.line.color.rgb = C_ACCENT if idx == 0 else C_BORDER
    mem_box.line.width = Pt(1)

    tb_m = s1.shapes.add_textbox(c_left + Inches(0.1), Inches(4.0), Inches(2.0), Inches(2.4))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    
    pm1 = tf_m.paragraphs[0]
    pm1.text = m_name
    pm1.font.name = "Segoe UI"
    pm1.font.size = Pt(13)
    pm1.font.bold = True
    pm1.font.color.rgb = C_PRIMARY

    pm2 = tf_m.add_paragraph()
    pm2.text = f"Reg: {m_reg}"
    pm2.font.name = "Segoe UI"
    pm2.font.size = Pt(11)
    pm2.font.bold = True
    pm2.font.color.rgb = C_GOLD

    pm3 = tf_m.add_paragraph()
    pm3.text = f"\n{m_role}"
    pm3.font.name = "Segoe UI"
    pm3.font.size = Pt(10)
    pm3.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 2: EXECUTIVE SUMMARY & MOTIVATION
# ==============================================================================
s2 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s2)
add_header(s2, "Executive Summary & Core Motivation", "Chapter 1 · Background")

add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
tb_s2_left = s2.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.8))
tf_s2_l = tb_s2_left.text_frame
tf_s2_l.word_wrap = True

add_bullet_point(tf_s2_l, "Agricultural Backbone:", "Agriculture forms the economic foundation for millions of households. However, smallholder farmers often make critical decisions without timely scientific or quantitative inputs.", 13, True)
add_bullet_point(tf_s2_l, "The Academic-to-Field Bridge:", "AgriSaarthi bridges academic Computer Science engineering principles with ground-level precision agriculture, building a fully production-ready full-stack system from scratch.", 13)
add_bullet_point(tf_s2_l, "Guiding Vision:", "“KNOW MORE GROW MORE” — Empowering agricultural producers with timely, localized, actionable intelligence covering crops, pathology, weather, and market context.", 13)
add_bullet_point(tf_s2_l, "Enterprise Architecture:", "Unlike fragmented mobile apps, AgriSaarthi unifies modern Web API design, relational data integrity, and machine learning behind a singular, responsive dashboard.", 13)

pillars = [
    ("Machine Learning Advisory", "Random Forest crop suitability + MobileNetV2 leaf disease pathology.", C_PRIMARY),
    ("Real-Time Weather Intelligence", "Deterministic agronomic rule engine driven by live Open-Meteo 7-day forecasts.", C_SECONDARY),
    ("Curated Agronomic Knowledge", "Structured offline JSON repositories for crops, diseases, pests, and best practices.", C_ACCENT),
    ("Modern Multi-Tier Stack", "Decoupled React 19 SPA, ASP.NET Core API gateway, and Python FastAPI microservice.", C_GOLD)
]

for i, (p_title, p_desc, p_col) in enumerate(pillars):
    top_pos = Inches(1.5 + i * 1.35)
    c = add_card(s2, Inches(6.8), top_pos, Inches(5.7), Inches(1.2))
    
    strip = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), top_pos, Inches(0.18), Inches(1.2))
    strip.fill.solid()
    strip.fill.fore_color.rgb = p_col
    strip.line.fill.background()

    tb_p = s2.shapes.add_textbox(Inches(7.15), top_pos + Inches(0.12), Inches(5.2), Inches(0.95))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True
    
    pp1 = tf_p.paragraphs[0]
    pp1.text = p_title
    pp1.font.name = "Segoe UI"
    pp1.font.size = Pt(13)
    pp1.font.bold = True
    pp1.font.color.rgb = C_DARK

    pp2 = tf_p.add_paragraph()
    pp2.text = p_desc
    pp2.font.name = "Segoe UI"
    pp2.font.size = Pt(11)
    pp2.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 3: PROBLEM STATEMENT
# ==============================================================================
s3 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s3)
add_header(s3, "Problem Statement: 4 Critical Agricultural Barriers", "Chapter 1.2 · The Challenge")

problems = [
    ("1. Suboptimal Crop-to-Soil Matching", 
     "Farmers frequently select crops based on regional habit or tradition rather than quantitative evaluation of soil macronutrients (Nitrogen, Phosphorus, Potassium), soil pH, and seasonal precipitation.",
     "Risk: Reduced yield, soil degradation, and poor fertilizer ROI."),
    
    ("2. Delayed Plant Leaf Disease Recognition",
     "Fungal, bacterial, and viral infections spread exponentially across crop fields. Delayed visual diagnosis leads to incorrect chemical pesticide spraying and severe, preventable yield losses.",
     "Risk: Crop failure, excessive pesticide costs, and ecological harm."),
    
    ("3. Uncontextualized Weather Forecasts",
     "Standard weather apps display raw numbers (e.g., 28°C, 15mm rain) without translating them into deterministic farming guidance like halting irrigation before heavy rains or preventing heat stress.",
     "Risk: Water wastage, root rotting, and foliar wash-off."),
    
    ("4. Fragmented Agronomic Knowledge",
     "Crucial agronomic guidance—crop cultivation timetables, integrated pest management, and reference market prices—is scattered across disconnected booklets, PDF reports, and siloed portals.",
     "Risk: Information asymmetry and delayed farmer decision-making.")
]

for idx, (p_title, p_desc, p_impact) in enumerate(problems):
    col = idx % 2
    row = idx // 2
    x = Inches(0.8 + col * 5.95)
    y = Inches(1.5 + row * 2.75)
    
    add_card(s3, x, y, Inches(5.75), Inches(2.55))
    
    top_bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(5.75), Inches(0.42))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = C_PRIMARY if idx % 2 == 0 else C_SECONDARY
    top_bar.line.fill.background()

    tb_t = s3.shapes.add_textbox(x + Inches(0.2), y + Inches(0.06), Inches(5.35), Inches(0.35))
    pt = tb_t.text_frame.paragraphs[0]
    pt.text = p_title
    pt.font.name = "Segoe UI"
    pt.font.size = Pt(13)
    pt.font.bold = True
    pt.font.color.rgb = C_WHITE

    tb_b = s3.shapes.add_textbox(x + Inches(0.25), y + Inches(0.52), Inches(5.25), Inches(1.9))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    
    pb1 = tf_b.paragraphs[0]
    pb1.text = p_desc
    pb1.font.name = "Segoe UI"
    pb1.font.size = Pt(11)
    pb1.font.color.rgb = C_DARK

    pb2 = tf_b.add_paragraph()
    pb2.text = f"\n▪ {p_impact}"
    pb2.font.name = "Segoe UI"
    pb2.font.size = Pt(10.5)
    pb2.font.bold = True
    pb2.font.color.rgb = RGBColor(185, 28, 28)

# ==============================================================================
# SLIDE 4: OBJECTIVES & SCOPE OF WORK
# ==============================================================================
s4 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s4)
add_header(s4, "Project Objectives & Scope of Work", "Chapter 1.3 & 1.4 · Goals")

add_card(s4, Inches(0.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s4_l = s4.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.25), Inches(4.9))
tf_s4_l = tb_s4_l.text_frame
tf_s4_l.word_wrap = True

add_bullet_point(tf_s4_l, "Decoupled Architecture:", "Architect a 4-tier system separating presentation, API routing, database persistence, and AI inference for maintainability and scalability.", 12.5, True)
add_bullet_point(tf_s4_l, "Secure Identity & Profiles:", "Implement JWT authentication with BCrypt hashing and persistent 1-to-1 farmer profile specifications (land size, soil category, coordinates).", 12.5)
add_bullet_point(tf_s4_l, "Crop Recommendation Engine:", "Train and serve a Scikit-learn Random Forest model predicting optimal crops across 7 soil-climate parameters.", 12.5)
add_bullet_point(tf_s4_l, "Leaf Pathology Screening:", "Deploy PyTorch MobileNetV2 CNN for plant leaf disease recognition with transparent AI prediction disclaimers.", 12.5)
add_bullet_point(tf_s4_l, "Automated Weather Alerts:", "Integrate Open-Meteo API live forecasts and apply deterministic agricultural rules (rain delays, heat alerts, fungal risks).", 12.5)

add_card(s4, Inches(6.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s4_r = s4.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.25), Inches(4.9))
tf_s4_r = tb_s4_r.text_frame
tf_s4_r.word_wrap = True

p_rhdr = tf_s4_r.paragraphs[0]
p_rhdr.text = "SCOPE: 10 IMPLEMENTED CORE MODULES"
p_rhdr.font.name = "Segoe UI"
p_rhdr.font.size = Pt(13)
p_rhdr.font.bold = True
p_rhdr.font.color.rgb = C_PRIMARY

features_list = [
    "1. Farmer Registration & Login (JWT Bearer)",
    "2. Farmer Profile & Specification Management",
    "3. AI Crop Recommendation (Random Forest)",
    "4. Automated Weather Advisory (Open-Meteo)",
    "5. AI Leaf Disease Detection (MobileNetV2)",
    "6. Pest & Disease Management Knowledge Base",
    "7. Reference Commodity Market Prices",
    "8. Categorized Sustainable Farming Tips",
    "9. Centralized Agricultural Knowledge Hub",
    "10. Unified Mobile-Responsive Dashboard"
]

for f in features_list:
    pf = tf_s4_r.add_paragraph()
    pf.text = f"✔ {f}"
    pf.font.name = "Segoe UI"
    pf.font.size = Pt(11)
    pf.font.bold = True
    pf.font.color.rgb = C_SECONDARY
    pf.space_before = Pt(4)

# ==============================================================================
# SLIDE 5: SYSTEM ARCHITECTURE (FIGURE 2.1)
# ==============================================================================
s5 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s5)
add_header(s5, "Multi-Tier System Architecture & Gateway Isolation", "Chapter 2.3 · System Design")

add_card(s5, Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.4))
if os.path.exists(IMG_ARCH):
    s5.shapes.add_picture(IMG_ARCH, Inches(1.0), Inches(1.7), width=Inches(7.1))

add_card(s5, Inches(8.5), Inches(1.5), Inches(4.0), Inches(5.4))
tb_s5_r = s5.shapes.add_textbox(Inches(8.75), Inches(1.8), Inches(3.5), Inches(4.8))
tf_s5_r = tb_s5_r.text_frame
tf_s5_r.word_wrap = True

add_bullet_point(tf_s5_r, "Four Decoupled Tiers:", "Clean separation between React SPA, ASP.NET Core API Gateway, Python FastAPI AI microservice, and SQL Server persistence.", 12, True)
add_bullet_point(tf_s5_r, "Strict Security Boundary:", "The frontend browser never communicates directly with FastAPI or SQL Server. All requests flow strictly through the ASP.NET Core API.", 12)
add_bullet_point(tf_s5_r, "Centralized Governance:", "Enforces JWT bearer authentication, input range validation, CORS origin policies, and error handling at the gateway.", 12)
add_bullet_point(tf_s5_r, "High Availability:", "Microservices can be scaled independently (e.g. AI inference instances can scale without redeploying the core API).", 12)

# ==============================================================================
# SLIDE 6: TECHNOLOGY STACK & TOOLS HANDLED
# ==============================================================================
s6 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s6)
add_header(s6, "Technology Stack & Development Tools", "Chapter 2.2 · Technologies")

tech_cards = [
    ("Frontend Layer", "React 19 + TypeScript + Vite + Tailwind CSS", 
     "Single Page Application (SPA), typed components, Lucide icons, responsive dashboard, client-side validation.", C_PRIMARY),
    
    ("Backend API Gateway", "ASP.NET Core Web API (.NET 10 / 8) + C#",
     "RESTful controllers, JWT bearer authentication, dependency injection, HttpClient proxying, EF Core.", C_SECONDARY),
    
    ("AI / ML Services", "Python 3.10 + FastAPI + Uvicorn",
     "Asynchronous microservice on port 8000, serialized model hosting, tensor transformations, fast inference.", C_ACCENT),
    
    ("Machine Learning", "Scikit-learn, PyTorch, MobileNetV2, Joblib",
     "Random Forest crop classifier (`crop_rf_model.joblib`), MobileNetV2 leaf classifier (`disease_model.pth`).", C_GOLD),
    
    ("Database & ORM", "SQL Server 2025 / LocalDB + EF Core",
     "Relational persistence, code-first migrations (`dotnet ef database update`), BCrypt password hashing.", C_PRIMARY),
    
    ("Tooling & QA", "Microsoft Visual Studio, Git, npm, Vite",
     "Visual Studio Solution (`AgriSaarthi.sln`), static type checking (`tsc`), production bundle optimization.", C_DARK)
]

for idx, (t_layer, t_tech, t_detail, t_color) in enumerate(tech_cards):
    c_idx = idx % 3
    r_idx = idx // 3
    x = Inches(0.8 + c_idx * 3.95)
    y = Inches(1.5 + r_idx * 2.75)
    
    add_card(s6, x, y, Inches(3.75), Inches(2.55))
    
    top_strip = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(3.75), Inches(0.38))
    top_strip.fill.solid()
    top_strip.fill.fore_color.rgb = t_color
    top_strip.line.fill.background()

    tb_th = s6.shapes.add_textbox(x + Inches(0.15), y + Inches(0.05), Inches(3.45), Inches(0.3))
    pth = tb_th.text_frame.paragraphs[0]
    pth.text = t_layer
    pth.font.name = "Segoe UI"
    pth.font.size = Pt(12)
    pth.font.bold = True
    pth.font.color.rgb = C_WHITE

    tb_tc = s6.shapes.add_textbox(x + Inches(0.2), y + Inches(0.48), Inches(3.35), Inches(1.95))
    tf_tc = tb_tc.text_frame
    tf_tc.word_wrap = True

    pt1 = tf_tc.paragraphs[0]
    pt1.text = t_tech
    pt1.font.name = "Segoe UI"
    pt1.font.size = Pt(11.5)
    pt1.font.bold = True
    pt1.font.color.rgb = C_SECONDARY

    pt2 = tf_tc.add_paragraph()
    pt2.text = f"\n{t_detail}"
    pt2.font.name = "Segoe UI"
    pt2.font.size = Pt(10)
    pt2.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 7: TEAM ROLES & CONTRIBUTIONS
# ==============================================================================
s7 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s7)
add_header(s7, "Team Roles, Ownership & Contributions", "Chapter 2.1 & 4.3 · Team Attribution")

team_details = [
    ("Taman Preet Singh", "Registration No: 12309438", "Backend API Gateway, Security & Database", [
        "Architected and implemented ASP.NET Core Web API (`AgriSaarthi.Api`).",
        "Configured JWT bearer authentication (`AuthController`) and authorization filters.",
        "Engineered SQL Server relational schemas and EF Core database auto-migrations.",
        "Integrated Open-Meteo weather API and built deterministic alert rule evaluation."
    ], C_PRIMARY),
    
    ("Utkarsh", "Registration No: 12308727", "Frontend Development, UI/UX & Dashboards", [
        "Architected the single-page application using React 19, TypeScript, and Vite.",
        "Designed and styled responsive farmer dashboard with Tailwind CSS and Lucide icons.",
        "Implemented interactive advisory forms, validation, and profile management.",
        "Built leaf image upload preview pipeline and structured Knowledge Hub views."
    ], C_SECONDARY),
    
    ("Mansi Verma", "Registration No: 12416455", "AI/ML Microservice & Agri-Knowledge Data", [
        "Developed Python FastAPI inference microservice (`ai-service/main.py`) on port 8000.",
        "Trained and serialized Scikit-learn Random Forest model (`crop_rf_model.joblib`).",
        "Fine-tuned PyTorch MobileNetV2 CNN on PlantVillage dataset (`disease_model.pth`).",
        "Curated agronomic reference datasets for crops, pests, diseases, and market prices."
    ], C_ACCENT)
]

for idx, (m_name, m_reg, m_domain, m_tasks, m_col) in enumerate(team_details):
    x = Inches(0.8 + idx * 3.95)
    y = Inches(1.5)
    add_card(s7, x, y, Inches(3.75), Inches(5.4))
    
    t_banner = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(3.75), Inches(0.95))
    t_banner.fill.solid()
    t_banner.fill.fore_color.rgb = m_col
    t_banner.line.fill.background()

    tb_th = s7.shapes.add_textbox(x + Inches(0.2), y + Inches(0.12), Inches(3.35), Inches(0.75))
    tf_th = tb_th.text_frame
    tf_th.word_wrap = True
    
    p1 = tf_th.paragraphs[0]
    p1.text = m_name
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(14)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE

    p2 = tf_th.add_paragraph()
    p2.text = m_reg
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_EMERALD

    tb_dom = s7.shapes.add_textbox(x + Inches(0.2), y + Inches(1.05), Inches(3.35), Inches(0.6))
    p_dom = tb_dom.text_frame.paragraphs[0]
    p_dom.text = m_domain
    p_dom.font.name = "Segoe UI"
    p_dom.font.size = Pt(11)
    p_dom.font.bold = True
    p_dom.font.color.rgb = C_DARK

    tb_tsk = s7.shapes.add_textbox(x + Inches(0.2), y + Inches(1.75), Inches(3.35), Inches(3.5))
    tf_tsk = tb_tsk.text_frame
    tf_tsk.word_wrap = True
    
    for t_idx, task in enumerate(m_tasks):
        add_bullet_point(tf_tsk, f"Task {t_idx+1}:", task, 10.5, t_idx == 0)

# ==============================================================================
# SLIDE 8: ML ENGINE 1 - CROP RECOMMENDATION
# ==============================================================================
s8 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s8)
add_header(s8, "Machine Learning Engine 1: Crop Suitability Recommendation", "Chapter 2.5 & 3.3 · Random Forest")

add_card(s8, Inches(0.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s8_l = s8.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(5.25), Inches(4.8))
tf_s8_l = tb_s8_l.text_frame
tf_s8_l.word_wrap = True

add_bullet_point(tf_s8_l, "Algorithmic Foundation:", "Trained using an ensemble Random Forest Classifier, evaluating multi-dimensional non-linear interactions across soil chemistry and regional atmospheric variables.", 12.5, True)
add_bullet_point(tf_s8_l, "Input Parameter Vector:", "Accepts 7 numerical features:\n• Soil Nitrogen (N), Phosphorus (P), Potassium (K)\n• Ambient Temperature (°C) & Relative Humidity (%)\n• Soil pH (0–14) & Seasonal Rainfall (mm)", 12)
add_bullet_point(tf_s8_l, "Output Inference & Scoring:", "Generates optimal crop category alongside class probabilistic confidence scores (e.g., Rice @ 90% confidence).", 12)
add_bullet_point(tf_s8_l, "Model Serialization:", "Exported as `crop_rf_model.joblib` (~3.5 MB) located in `ml/crop-recommendation/model/`.", 12)

add_card(s8, Inches(6.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s8_r = s8.shapes.add_textbox(Inches(7.05), Inches(1.8), Inches(5.25), Inches(4.8))
tf_s8_r = tb_s8_r.text_frame
tf_s8_r.word_wrap = True

p_spec = tf_s8_r.paragraphs[0]
p_spec.text = "TECHNICAL SPECIFICATION & ENDPOINTS"
p_spec.font.name = "Segoe UI"
p_spec.font.size = Pt(13)
p_spec.font.bold = True
p_spec.font.color.rgb = C_PRIMARY

specs = [
    ("FastAPI Endpoint", "POST http://localhost:8000/predict/crop"),
    ("Backend API Gateway", "POST /api/crop-advisory/recommend"),
    ("Dataset Utilized", "Crop Recommendation Dataset (2,200 samples)"),
    ("Evaluation Metrics", "High precision across major Kharif/Rabi crops"),
    ("Validation Boundary", "ASP.NET Core enforces range checks prior to FastAPI invocation.")
]

for s_name, s_val in specs:
    add_bullet_point(tf_s8_r, s_name + ":", s_val, 11)

json_card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(4.6), Inches(5.15), Inches(2.0))
json_card.fill.solid()
json_card.fill.fore_color.rgb = RGBColor(15, 23, 42)
json_card.line.fill.background()

tb_json = s8.shapes.add_textbox(Inches(7.25), Inches(4.7), Inches(4.85), Inches(1.8))
tf_json = tb_json.text_frame
tf_json.word_wrap = True
p_code = tf_json.paragraphs[0]
p_code.text = '// Sample Request & Response Payload\n{\n  "recommendedCrop": "rice",\n  "confidence": 0.9000,\n  "soilInputs": {"N": 90, "P": 42, "K": 43, "pH": 6.5}\n}'
p_code.font.name = "Consolas"
p_code.font.size = Pt(9.5)
p_code.font.color.rgb = RGBColor(52, 211, 153)

# ==============================================================================
# SLIDE 9: ML ENGINE 2 - LEAF DISEASE DETECTION
# ==============================================================================
s9 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s9)
add_header(s9, "Machine Learning Engine 2: Plant Leaf Disease Pathology", "Chapter 2.5 & 3.3 · MobileNetV2")

add_card(s9, Inches(0.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s9_l = s9.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(5.25), Inches(4.8))
tf_s9_l = tb_s9_l.text_frame
tf_s9_l.word_wrap = True

add_bullet_point(tf_s9_l, "Deep Neural Architecture:", "Fine-tuned MobileNetV2 Convolutional Neural Network utilizing inverted residual blocks and depthwise separable convolutions for lightweight CPU inference.", 12, True)
add_bullet_point(tf_s9_l, "Training Corpus:", "Trained on PlantVillage dataset spanning healthy and infected foliage images across tomato, potato, apple, corn, and grape crops.", 12)
add_bullet_point(tf_s9_l, "Preprocessing Pipeline:", "Uploaded RGB images are dynamically resized to 224×224 pixels, converted to PyTorch tensors, and normalized with ImageNet mean/standard deviation.", 12)
add_bullet_point(tf_s9_l, "Transparent AI Disclaimer:", "The platform explicitly displays warnings that AI disease detection provides probabilistic screening estimates and should be verified before chemical application.", 12)

add_card(s9, Inches(6.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s9_r = s9.shapes.add_textbox(Inches(7.05), Inches(1.8), Inches(5.25), Inches(4.8))
tf_s9_r = tb_s9_r.text_frame
tf_s9_r.word_wrap = True

p_s9_hdr = tf_s9_r.paragraphs[0]
p_s9_hdr.text = "DISEASE DETECTION PIPELINE SPECIFICATIONS"
p_s9_hdr.font.name = "Segoe UI"
p_s9_hdr.font.size = Pt(13)
p_s9_hdr.font.bold = True
p_s9_hdr.font.color.rgb = C_PRIMARY

d_specs = [
    ("FastAPI Endpoint", "POST http://localhost:8000/predict/disease"),
    ("Backend API Gateway", "POST /api/disease-detection/predict"),
    ("Upload Handling", "Accepts multipart image stream (up to 10 MB JPG/PNG)"),
    ("Model Artifacts", "`disease_model.pth` and `classes.json`"),
    ("Knowledge Base Link", "Matches predicted disease name to management protocols in `AgriKnowledgeController`.")
]

for d_name, d_val in d_specs:
    add_bullet_point(tf_s9_r, d_name + ":", d_val, 11)

note_box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(4.8), Inches(5.15), Inches(1.8))
note_box.fill.solid()
note_box.fill.fore_color.rgb = C_LIGHT_BLUE
note_box.line.color.rgb = RGBColor(147, 197, 253)

tb_note = s9.shapes.add_textbox(Inches(7.25), Inches(4.9), Inches(4.85), Inches(1.6))
tf_note = tb_note.text_frame
tf_note.word_wrap = True
pn = tf_note.paragraphs[0]
pn.text = "💡 Architectural Resilience Feature:\nAI microservice employs dynamic PyTorch lazy-loading. If PyTorch weights are pending download, service boots smoothly and continues serving crop recommendations while returning friendly HTTP 503 status for image calls."
pn.font.name = "Segoe UI"
pn.font.size = Pt(10)
pn.font.color.rgb = RGBColor(30, 58, 138)

# ==============================================================================
# SLIDE 10: END-TO-END INFERENCE WORKFLOW (FIGURE 2.2)
# ==============================================================================
s10 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s10)
add_header(s10, "End-to-End Request Validation & ML Inference Pipeline", "Chapter 2.5 · Pipeline Workflow")

add_card(s10, Inches(0.8), Inches(1.5), Inches(11.75), Inches(3.2))
if os.path.exists(IMG_ML_FLOW):
    s10.shapes.add_picture(IMG_ML_FLOW, Inches(1.2), Inches(1.7), width=Inches(10.95))

steps = [
    ("Stage 1: Client Capture", "Farmer inputs soil values or uploads leaf image in React single-page dashboard."),
    ("Stage 2: Gateway Validation", "ASP.NET Core verifies JWT token, validates input ranges, and streams payload."),
    ("Stage 3: FastAPI Inference", "FastAPI passes tensors to Random Forest or MobileNetV2 models for CPU scoring."),
    ("Stage 4: Enriched Response", "Predictions mapped to curated treatment tips & displayed with confidence rating.")
]

for idx, (st_title, st_desc) in enumerate(steps):
    x = Inches(0.8 + idx * 2.98)
    y = Inches(4.95)
    add_card(s10, x, y, Inches(2.8), Inches(1.95), bg_color=C_CARD_BG)
    
    tb_st = s10.shapes.add_textbox(x + Inches(0.15), y + Inches(0.15), Inches(2.5), Inches(1.65))
    tf_st = tb_st.text_frame
    tf_st.word_wrap = True
    
    ps1 = tf_st.paragraphs[0]
    ps1.text = st_title
    ps1.font.name = "Segoe UI"
    ps1.font.size = Pt(11.5)
    ps1.font.bold = True
    ps1.font.color.rgb = C_PRIMARY

    ps2 = tf_st.add_paragraph()
    ps2.text = f"\n{st_desc}"
    ps2.font.name = "Segoe UI"
    ps2.font.size = Pt(10)
    ps2.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 11: DATABASE DESIGN & EF CORE
# ==============================================================================
s11 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s11)
add_header(s11, "Database Schema & Entity Framework Core", "Chapter 2.4 · Data Persistence")

entities = [
    ("Users Entity", "Stores core authentication credentials", [
        "Id (Primary Key, GUID/Int)",
        "FullName (Farmer display name)",
        "Email (Unique index, login identifier)",
        "PasswordHash (BCrypt salted hash)",
        "CreatedAt (Timestamp of registration)"
    ]),
    ("Farmers Entity", "Links identity to agricultural metadata", [
        "Id (Primary Key)",
        "UserId (Foreign Key to Users)",
        "FullName & PhoneNumber (Unique index)",
        "Location (Village / District / State)"
    ]),
    ("FarmerProfiles Entity", "1-to-1 persistent farm specification", [
        "Id (Primary Key), FarmerId (Foreign Key)",
        "FarmSize (Acres), SoilType (Loamy, Clay, etc.)",
        "PrimaryCrops & IrrigationType",
        "Latitude & Longitude coordinates"
    ])
]

for idx, (e_name, e_desc, e_attrs) in enumerate(entities):
    y = Inches(1.5 + idx * 1.8)
    add_card(s11, Inches(0.8), y, Inches(6.5), Inches(1.65))
    
    tb_e = s11.shapes.add_textbox(Inches(1.0), y + Inches(0.1), Inches(6.1), Inches(1.45))
    tf_e = tb_e.text_frame
    tf_e.word_wrap = True
    
    pe1 = tf_e.paragraphs[0]
    pe1.text = f"{e_name} — {e_desc}"
    pe1.font.name = "Segoe UI"
    pe1.font.size = Pt(12)
    pe1.font.bold = True
    pe1.font.color.rgb = C_PRIMARY

    pe2 = tf_e.add_paragraph()
    pe2.text = " • " + " • ".join(e_attrs)
    pe2.font.name = "Segoe UI"
    pe2.font.size = Pt(10)
    pe2.font.color.rgb = C_DARK

add_card(s11, Inches(7.6), Inches(1.5), Inches(4.95), Inches(5.4))
tb_s11_r = s11.shapes.add_textbox(Inches(7.85), Inches(1.8), Inches(4.45), Inches(4.8))
tf_s11_r = tb_s11_r.text_frame
tf_s11_r.word_wrap = True

p_orm_hdr = tf_s11_r.paragraphs[0]
p_orm_hdr.text = "ORM ARCHITECTURE & FEATURES"
p_orm_hdr.font.name = "Segoe UI"
p_orm_hdr.font.size = Pt(13)
p_orm_hdr.font.bold = True
p_orm_hdr.font.color.rgb = C_PRIMARY

add_bullet_point(tf_s11_r, "Microsoft SQL Server:", "Backed by SQL Server 2025 LocalDB (`mssqllocaldb`) for robust relational transactions and indexing.", 11.5)
add_bullet_point(tf_s11_r, "Code-First Migrations:", "Entity Framework Core migrations maintain versioned schema snapshots (`20260918072755_InitialCreate.cs`).", 11.5)
add_bullet_point(tf_s11_r, "Automated On-Boot Migration:", "Application automatically executes `dbContext.Database.Migrate()` on API startup, eliminating manual setup hurdles.", 11.5)
add_bullet_point(tf_s11_r, "Data Integrity & Cascades:", "Configured cascading deletes on Farmer-to-Profile relationships and unique indexes preventing duplicate accounts.", 11.5)

# ==============================================================================
# SLIDE 12: WEATHER ADVISORY & RULES ENGINE
# ==============================================================================
s12 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s12)
add_header(s12, "Weather Advisory & Agricultural Rule Engine", "Chapter 3.4 · Meteorological Rules")

add_card(s12, Inches(0.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s12_l = s12.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(5.25), Inches(4.8))
tf_s12_l = tb_s12_l.text_frame
tf_s12_l.word_wrap = True

add_bullet_point(tf_s12_l, "Open-Meteo Integration:", "Integrated with Open-Meteo API to query real-time meteorological conditions and 7-day weather forecasts without requiring commercial API keys.", 12, True)
add_bullet_point(tf_s12_l, "Automated Rule Evaluation:", "Raw temperature, humidity, wind, and precipitation data are parsed by `WeatherController` into farmer-oriented advisories.", 12)
add_bullet_point(tf_s12_l, "Field Safety Metrics:", "Calculates agricultural safety windows for outdoor field work, foliar spraying, sowing, and fertilizer application.", 12)
add_bullet_point(tf_s12_l, "Coordinates Geocoding:", "Queries weather forecasts based on latitude & longitude stored directly in the farmer's profile.", 12)

rules = [
    ("Rain-Delay Irrigation Alert", 
     "Condition: Rainfall probability > 60% or forecast precipitation > 5mm in next 24-48 hours.\nAdvisory: Suspend electric tube well/canal irrigation immediately to avoid waterlogging and nutrient runoff.", 
     C_PRIMARY),
    
    ("Heat Stress Advisory", 
     "Condition: Ambient temperature > 38°C with low humidity.\nAdvisory: Schedule irrigation in early morning or late evening; apply mulch to conserve root moisture and prevent crop wilting.", 
     C_GOLD),
    
    ("Fungal Pathology Warning", 
     "Condition: Relative humidity > 80% with temperatures between 20°C–28°C.\nAdvisory: High risk of foliar blights, mildew, or rust. Inspect leaf undersides and avoid overhead sprinkler watering.", 
     RGBColor(185, 28, 28))
]

for idx, (r_name, r_body, r_col) in enumerate(rules):
    y = Inches(1.5 + idx * 1.8)
    add_card(s12, Inches(6.8), y, Inches(5.75), Inches(1.65))
    
    rst = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), y, Inches(0.18), Inches(1.65))
    rst.fill.solid()
    rst.fill.fore_color.rgb = r_col
    rst.line.fill.background()

    tb_r = s12.shapes.add_textbox(Inches(7.15), y + Inches(0.1), Inches(5.25), Inches(1.45))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    
    pr1 = tf_r.paragraphs[0]
    pr1.text = r_name
    pr1.font.name = "Segoe UI"
    pr1.font.size = Pt(12)
    pr1.font.bold = True
    pr1.font.color.rgb = C_DARK

    pr2 = tf_r.add_paragraph()
    pr2.text = r_body
    pr2.font.name = "Segoe UI"
    pr2.font.size = Pt(9.5)
    pr2.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 13: KNOWLEDGE HUB & MARKET PRICES
# ==============================================================================
s13 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s13)
add_header(s13, "Centralized Agronomic Knowledge Hub & Market Data", "Chapter 2.4 & 3.4 · Reference Hub")

kh_modules = [
    ("Crops Reference Data", "`ml/agri-knowledge/crops.json`", 
     "Detailed cultivation profiles across cereals, pulses, oilseeds, and vegetables detailing ideal sowing windows, soil compatibility, water requirements, and harvesting best practices."),
    
    ("Pest & Disease Catalog", "`ml/agri-knowledge/diseases.json & pests.json`",
     "Comprehensive index of foliar diseases and insect pests categorized by crop. Includes visual symptom checklists, biological controls, and chemical intervention thresholds."),
    
    ("Sustainable Farming Tips", "`ml/agri-knowledge/farming-tips.json`",
     "Actionable agronomic advice covering drip irrigation efficiency, crop rotation benefits, organic compost preparation, and soil conservation techniques."),
    
    ("Reference Market Prices", "`ml/agri-knowledge/market-prices.json`",
     "Sample commodity rate snapshots (Wheat, Paddy, Mustard, Maize, Gram) clearly accompanied by disclaimers that rates serve educational reference purposes rather than live mandi tickers.")
]

for idx, (kh_title, kh_file, kh_desc) in enumerate(kh_modules):
    col = idx % 2
    row = idx // 2
    x = Inches(0.8 + col * 5.95)
    y = Inches(1.5 + row * 2.75)
    
    add_card(s13, x, y, Inches(5.75), Inches(2.55))
    
    tb_k = s13.shapes.add_textbox(x + Inches(0.25), y + Inches(0.2), Inches(5.25), Inches(2.15))
    tf_k = tb_k.text_frame
    tf_k.word_wrap = True
    
    pk1 = tf_k.paragraphs[0]
    pk1.text = kh_title
    pk1.font.name = "Segoe UI"
    pk1.font.size = Pt(13)
    pk1.font.bold = True
    pk1.font.color.rgb = C_PRIMARY

    pk2 = tf_k.add_paragraph()
    pk2.text = f"File: {kh_file}\n"
    pk2.font.name = "Consolas"
    pk2.font.size = Pt(9.5)
    pk2.font.color.rgb = C_SECONDARY

    pk3 = tf_k.add_paragraph()
    pk3.text = kh_desc
    pk3.font.name = "Segoe UI"
    pk3.font.size = Pt(11)
    pk3.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 14: REST API INVENTORY & SECURITY BOUNDARY (FIGURE 3.1)
# ==============================================================================
s14 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s14)
add_header(s14, "REST API Inventory & Network Security Boundary", "Chapter 3.5 & 3.7 · API Gateway")

add_card(s14, Inches(0.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s14_l = s14.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.25), Inches(4.9))
tf_s14_l = tb_s14_l.text_frame
tf_s14_l.word_wrap = True

p_api_h = tf_s14_l.paragraphs[0]
p_api_h.text = "18 RESTFUL ENDPOINTS ACROSS 9 CONTROLLERS"
p_api_h.font.name = "Segoe UI"
p_api_h.font.size = Pt(12)
p_api_h.font.bold = True
p_api_h.font.color.rgb = C_PRIMARY

api_routes = [
    ("AuthController", "POST /api/auth/register, POST /api/auth/login"),
    ("FarmersController", "POST, GET, PUT /api/farmers/{id}/profile"),
    ("CropAdvisoryController", "POST /api/crop-advisory/recommend"),
    ("DiseaseDetectionController", "POST /api/disease-detection/predict"),
    ("WeatherController", "GET /api/weather (Current & 7-Day Forecast)"),
    ("AgriKnowledgeController", "GET /api/agri-knowledge/{crops|diseases|pests}"),
    ("MarketPricesController", "GET /api/market-prices"),
    ("FarmingTipsController", "GET /api/farming-tips"),
    ("HealthController", "GET /api/health (Service Heartbeat)")
]

for c_name, c_routes in api_routes:
    add_bullet_point(tf_s14_l, c_name + ":", c_routes, 10.5)

add_card(s14, Inches(6.8), Inches(1.5), Inches(5.75), Inches(5.4))
if os.path.exists(IMG_SECURITY):
    s14.shapes.add_picture(IMG_SECURITY, Inches(7.0), Inches(1.75), width=Inches(5.35))

# ==============================================================================
# SLIDE 15: INTERFACE SHOWCASE - FARMER DASHBOARD (FIGURE 4.1)
# ==============================================================================
s15 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s15)
add_header(s15, "Application Showcase: Unified Farmer Dashboard", "Chapter 4.2 · User Interface")

add_card(s15, Inches(0.8), Inches(1.5), Inches(7.6), Inches(5.4))
if os.path.exists(IMG_DASHBOARD):
    s15.shapes.add_picture(IMG_DASHBOARD, Inches(0.95), Inches(1.65), width=Inches(7.3))

add_card(s15, Inches(8.6), Inches(1.5), Inches(3.95), Inches(5.4))
tb_s15_r = s15.shapes.add_textbox(Inches(8.85), Inches(1.8), Inches(3.45), Inches(4.8))
tf_s15_r = tb_s15_r.text_frame
tf_s15_r.word_wrap = True

add_bullet_point(tf_s15_r, "Personalized Banner:", "Greets the farmer by name (e.g. Gurpreet Singh) and highlights active farm coordinates, soil health, and temperature.", 11.5, True)
add_bullet_point(tf_s15_r, "Seasonal Advisory Cards:", "Displays real-time crop recommendations categorized by Kharif, Rabi, and Zaid cultivation cycles.", 11.5)
add_bullet_point(tf_s15_r, "Weather Advisory Widget:", "Live forecast with automated 24-hour field guidance (e.g., 'Good conditions for field work today').", 11.5)
add_bullet_point(tf_s15_r, "Leaf Disease Drag-and-Drop:", "One-click leaf image upload box for instant AI pathology diagnosis.", 11.5)
add_bullet_point(tf_s15_r, "Reference Market Ticker:", "Snapshot of regional commodity market rates and farming community discussion feed.", 11.5)

# ==============================================================================
# SLIDE 16: INTERFACE SHOWCASE - ONBOARDING & PROFILE (FIGURE 4.2)
# ==============================================================================
s16 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s16)
add_header(s16, "Application Showcase: Farmer Onboarding & Profile", "Chapter 4.2 · Authentication & Profile")

add_card(s16, Inches(0.8), Inches(1.5), Inches(7.6), Inches(5.4))
if os.path.exists(IMG_REGISTER):
    s16.shapes.add_picture(IMG_REGISTER, Inches(0.95), Inches(1.65), width=Inches(7.3))

add_card(s16, Inches(8.6), Inches(1.5), Inches(3.95), Inches(5.4))
tb_s16_r = s16.shapes.add_textbox(Inches(8.85), Inches(1.8), Inches(3.45), Inches(4.8))
tf_s16_r = tb_s16_r.text_frame
tf_s16_r.word_wrap = True

add_bullet_point(tf_s16_r, "Frictionless Onboarding:", "Designed specifically for farmers with high-contrast inputs, clear labels, and intuitive validation.", 11.5, True)
add_bullet_point(tf_s16_r, "Identity Verification:", "Validates full name, email address, mobile phone number, and encrypted password confirmation.", 11.5)
add_bullet_point(tf_s16_r, "Farm Specifications:", "Subsequent profile view captures farm acreage, primary soil classification (Loamy/Clay), and irrigation infrastructure.", 11.5)
add_bullet_point(tf_s16_r, "JWT Token Generation:", "On successful login, ASP.NET Core issues a signed cryptographic JWT bearer token stored safely for subsequent requests.", 11.5)

# ==============================================================================
# SLIDE 17: TECHNICAL CHALLENGES & SOLUTIONS
# ==============================================================================
s17 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s17)
add_header(s17, "Technical Challenges Overcome & Solutions", "Chapter 2.6 · Engineering Problem Solving")

challenges = [
    ("Challenge 1: Strict Gateway Isolation",
     "Problem: Ensuring client browsers cannot bypass authentication or query the FastAPI AI microservice and SQL Server database directly.\n\n"
     "Solution: Routed all client traffic strictly through ASP.NET Core typed HttpClient services and restricted FastAPI `ALLOWED_ORIGINS` to the backend gateway.",
     C_PRIMARY),
    
    ("Challenge 2: Multi-Hop Image Streaming",
     "Problem: Uploading multipart leaf photographs from React through ASP.NET Core to FastAPI caused potential memory bottlenecks and stream corruption.\n\n"
     "Solution: Implemented asynchronous `IFormFile` stream reading in ASP.NET Core and relayed payload as `MultipartFormDataContent` to FastAPI without disk caching.",
     C_SECONDARY),
    
    ("Challenge 3: ML Artifact Governance",
     "Problem: Large model weight binaries (PyTorch weights, Scikit-learn joblib) risk bloating Git version control and slowing repository cloning.\n\n"
     "Solution: Excluded raw heavy datasets via `.gitignore`, documented explicit runtime requirements, and implemented startup loading with graceful fallback.",
     C_ACCENT)
]

for idx, (c_title, c_text, c_col) in enumerate(challenges):
    x = Inches(0.8 + idx * 3.95)
    y = Inches(1.5)
    add_card(s17, x, y, Inches(3.75), Inches(5.4))
    
    t_bar = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(3.75), Inches(0.45))
    t_bar.fill.solid()
    t_bar.fill.fore_color.rgb = c_col
    t_bar.line.fill.background()

    tb_ch = s17.shapes.add_textbox(x + Inches(0.15), y + Inches(0.08), Inches(3.45), Inches(0.35))
    pch = tb_ch.text_frame.paragraphs[0]
    pch.text = c_title
    pch.font.name = "Segoe UI"
    pch.font.size = Pt(12)
    pch.font.bold = True
    pch.font.color.rgb = C_WHITE

    tb_cb = s17.shapes.add_textbox(x + Inches(0.2), y + Inches(0.6), Inches(3.35), Inches(4.6))
    tf_cb = tb_cb.text_frame
    tf_cb.word_wrap = True
    
    pcb = tf_cb.paragraphs[0]
    pcb.text = c_text
    pcb.font.name = "Segoe UI"
    pcb.font.size = Pt(11)
    pcb.font.color.rgb = C_DARK

# ==============================================================================
# SLIDE 18: BUILD VERIFICATION & QUALITY ASSURANCE
# ==============================================================================
s18 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s18)
add_header(s18, "Build Verification, Testing & Quality Assurance", "Chapter 3.6 & 3.7 · QA")

add_card(s18, Inches(0.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s18_l = s18.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(5.25), Inches(4.8))
tf_s18_l = tb_s18_l.text_frame
tf_s18_l.word_wrap = True

p_qa = tf_s18_l.paragraphs[0]
p_qa.text = "RIGOROUS MULTI-TIER BUILD CHECKS"
p_qa.font.name = "Segoe UI"
p_qa.font.size = Pt(13)
p_qa.font.bold = True
p_qa.font.color.rgb = C_PRIMARY

add_bullet_point(tf_s18_l, "Frontend TypeScript Check:", "`npx tsc --noEmit` executed with 0 type errors, ensuring strict static typing across all components.", 11.5)
add_bullet_point(tf_s18_l, "Production Bundle Build:", "`npm run build` compiled client bundle (367 kB JS, 50 kB CSS) in 3.7s with zero missing dependencies.", 11.5)
add_bullet_point(tf_s18_l, "Backend .NET Build:", "`dotnet build` compiled with 0 errors on .NET 10 targeting ASP.NET Core Web API.", 11.5)
add_bullet_point(tf_s18_l, "Live Endpoint Probing:", "Automated HTTP probes confirmed healthy 200 OK responses on `/health` and valid model inference on `/predict/crop`.", 11.5)

add_card(s18, Inches(6.8), Inches(1.5), Inches(5.75), Inches(5.4))
tb_s18_r = s18.shapes.add_textbox(Inches(7.05), Inches(1.8), Inches(5.25), Inches(4.8))
tf_s18_r = tb_s18_r.text_frame
tf_s18_r.word_wrap = True

p_env = tf_s18_r.paragraphs[0]
p_env.text = "ENVIRONMENT VARIABLES CONFIGURATION"
p_env.font.name = "Segoe UI"
p_env.font.size = Pt(13)
p_env.font.bold = True
p_env.font.color.rgb = C_PRIMARY

env_items = [
    ("ConnectionStrings:DefaultConnection", "SQL Server LocalDB connection string"),
    ("Jwt:Key & Jwt:Issuer", "Cryptographic key and issuer for signing tokens"),
    ("AiService:BaseUrl", "Internal HTTP URL pointing to FastAPI (http://localhost:8000)"),
    ("ALLOWED_ORIGINS", "CORS whitelist restricting FastAPI access to backend"),
    ("VITE_API_URL", "Frontend environment setting pointing to ASP.NET Core API")
]

for ev_name, ev_desc in env_items:
    add_bullet_point(tf_s18_r, ev_name + ":", ev_desc, 11)

# ==============================================================================
# SLIDE 19: FUTURE SCOPE & ENHANCEMENTS
# ==============================================================================
s19 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s19)
add_header(s19, "Future Perspective & Architectural Roadmap", "Chapter 4.3 · Roadmap")

roadmap = [
    ("1. Regional Language & Voice UI", 
     "Adding multilingual Indian language localization (Punjabi, Hindi, Marathi, etc.) alongside speech-to-text voice input to empower semi-literate farmers with conversational advisory queries.",
     C_PRIMARY),
    
    ("2. Live Government Mandi Feeds",
     "Connecting to official national agricultural portals (e-NAM and Agmarknet) to supplement reference rates with real-time district-level mandi prices and market arrivals.",
     C_SECONDARY),
    
    ("3. IoT Soil Sensor Telemetry",
     "Deploying low-cost IoT field soil probes reporting real-time Nitrogen, Phosphorus, Potassium, moisture, and soil temperature via MQTT/REST webhooks for automated advisory.",
     C_ACCENT),
    
    ("4. Offline PWA & SMS Weather Alerts",
     "Packaging the frontend as an offline-first Progressive Web App (PWA) with automated SMS broadcast alerts for severe weather events like unseasonal frost, hailstorms, and torrential downpours.",
     C_GOLD)
]

for idx, (r_title, r_body, r_col) in enumerate(roadmap):
    col = idx % 2
    row = idx // 2
    x = Inches(0.8 + col * 5.95)
    y = Inches(1.5 + row * 2.75)
    
    add_card(s19, x, y, Inches(5.75), Inches(2.55))
    
    l_strip = s19.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(0.2), Inches(2.55))
    l_strip.fill.solid()
    l_strip.fill.fore_color.rgb = r_col
    l_strip.line.fill.background()

    tb_rm = s19.shapes.add_textbox(x + Inches(0.35), y + Inches(0.2), Inches(5.15), Inches(2.15))
    tf_rm = tb_rm.text_frame
    tf_rm.word_wrap = True
    
    prm1 = tf_rm.paragraphs[0]
    prm1.text = r_title
    prm1.font.name = "Segoe UI"
    prm1.font.size = Pt(13)
    prm1.font.bold = True
    prm1.font.color.rgb = C_DARK

    prm2 = tf_rm.add_paragraph()
    prm2.text = f"\n{r_body}"
    prm2.font.name = "Segoe UI"
    prm2.font.size = Pt(11)
    prm2.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 20: CONCLUSION & ATTRIBUTION
# ==============================================================================
s20 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s20)

end_banner = s20.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(2.2))
end_banner.fill.solid()
end_banner.fill.fore_color.rgb = C_PRIMARY
end_banner.line.fill.background()

e_accent = s20.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(2.2), Inches(13.333), Inches(0.08))
e_accent.fill.solid()
e_accent.fill.fore_color.rgb = C_GOLD
e_accent.line.fill.background()

tb_e_hdr = s20.shapes.add_textbox(Inches(1.0), Inches(0.4), Inches(11.333), Inches(1.4))
tf_e_hdr = tb_e_hdr.text_frame
tf_e_hdr.word_wrap = True

pe_t = tf_e_hdr.paragraphs[0]
pe_t.text = "AgriSaarthi: Conclusion & Acknowledgments"
pe_t.font.name = "Segoe UI"
pe_t.font.size = Pt(28)
pe_t.font.bold = True
pe_t.font.color.rgb = C_WHITE

pe_sub = tf_e_hdr.add_paragraph()
pe_sub.text = "“KNOW MORE GROW MORE” · AI-Powered Crop Advisory and Farmer Companion Platform"
pe_sub.font.name = "Segoe UI"
pe_sub.font.size = Pt(14)
pe_sub.font.bold = True
pe_sub.font.color.rgb = C_EMERALD

add_card(s20, Inches(0.8), Inches(2.55), Inches(5.75), Inches(4.35))
tb_c_l = s20.shapes.add_textbox(Inches(1.05), Inches(2.75), Inches(5.25), Inches(3.95))
tf_c_l = tb_c_l.text_frame
tf_c_l.word_wrap = True

p_cl_h = tf_c_l.paragraphs[0]
p_cl_h.text = "PROJECT SUMMARY & ACHIEVEMENTS"
p_cl_h.font.name = "Segoe UI"
p_cl_h.font.size = Pt(13)
p_cl_h.font.bold = True
p_cl_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_c_l, "Complete Full-Stack Delivery:", "Successfully built and validated an integrated platform combining React 19, ASP.NET Core API Gateway, SQL Server, and Python FastAPI.", 11.5)
add_bullet_point(tf_c_l, "Applied AI in Precision Farming:", "Demonstrated real-world machine learning application through quantitative Random Forest crop advice and MobileNetV2 leaf disease detection.", 11.5)
add_bullet_point(tf_c_l, "Production Engineering Standard:", "Adhered to industry principles: strict security boundaries, code-first migrations, automated build checks, and decoupled microservices.", 11.5)

add_card(s20, Inches(6.8), Inches(2.55), Inches(5.75), Inches(4.35))
tb_c_r = s20.shapes.add_textbox(Inches(7.05), Inches(2.75), Inches(5.25), Inches(3.95))
tf_c_r = tb_c_r.text_frame
tf_c_r.word_wrap = True

p_cr_h = tf_c_r.paragraphs[0]
p_cr_h.text = "TEAM MEMBERS & SUPERVISOR"
p_cr_h.font.name = "Segoe UI"
p_cr_h.font.size = Pt(13)
p_cr_h.font.bold = True
p_cr_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_c_r, "Taman Preet Singh:", "Registration Number: 12309438 (Backend, Security & DB)", 11.5)
add_bullet_point(tf_c_r, "Utkarsh:", "Registration Number: 12308727 (Frontend, UI/UX & Dashboards)", 11.5)
add_bullet_point(tf_c_r, "Mansi Verma:", "Registration Number: 12416455 (AI/ML Microservices & Data)", 11.5)
add_bullet_point(tf_c_r, "Under Supervision of:", "Mr. Aryan Chauhan (UID: 35200), Dept of CSE, LPU", 11.5)

p_git = tf_c_r.add_paragraph()
p_git.text = "\n🔗 GitHub Repository: https://github.com/Tamanpreet84/AgriSaarthi\n\nThank You! Open for Questions & Evaluation."
p_git.font.name = "Segoe UI"
p_git.font.size = Pt(12)
p_git.font.bold = True
p_git.font.color.rgb = C_SECONDARY

# Save Presentation directly in agrisaarthi directory
out_pptx = r"C:\Users\taman\OneDrive\Desktop\agrisaarthi\AgriSaarthi_Presentation.pptx"
prs.save(out_pptx)
print(f"SUCCESS: AgriSaarthi presentation saved to {out_pptx} with {len(prs.slides)} slides!")
