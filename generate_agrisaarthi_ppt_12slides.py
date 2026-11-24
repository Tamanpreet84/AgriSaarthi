import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# AGRISAARTHI 12-SLIDE COMPREHENSIVE PRESENTATION GENERATOR
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
IMG_DASHBOARD_LIVE = os.path.join(ASSETS_DIR, r"live_dashboard_ss.jpg")
IMG_DASHBOARD = os.path.join(ASSETS_DIR, r"dashboard_ss.png")
IMG_REGISTER = os.path.join(ASSETS_DIR, r"register_ss.png")

def set_slide_background(slide):
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = C_BG
    bg_shape.line.fill.background()
    return bg_shape

def add_header(slide, title_text, category_text="AGRISAARTHI · 12-SLIDE CAPSTONE PRESENTATION", slide_num=None):
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
        p_n.text = f"{slide_num} / 12"
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
# SLIDE 1: TITLE SLIDE & CREDENTIALS (NO ROLES - NAMES & REG NOS ONLY)
# ==============================================================================
s1 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s1)

# Left Column Hero Banner (Deep Green)
hero_banner = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(4.5), Inches(7.5))
hero_banner.fill.solid()
hero_banner.fill.fore_color.rgb = C_PRIMARY
hero_banner.line.fill.background()

gold_stripe = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.42), 0, Inches(0.08), Inches(7.5))
gold_stripe.fill.solid()
gold_stripe.fill.fore_color.rgb = C_GOLD
gold_stripe.line.fill.background()

# LPU Logo & Branding in Hero
if os.path.exists(IMG_LPU):
    s1.shapes.add_picture(IMG_LPU, Inches(0.8), Inches(0.6), width=Inches(2.9))

if os.path.exists(IMG_LOGO):
    s1.shapes.add_picture(IMG_LOGO, Inches(1.4), Inches(2.2), width=Inches(1.7))

tb_hero_text = s1.shapes.add_textbox(Inches(0.4), Inches(4.1), Inches(3.7), Inches(3.0))
tf_hero = tb_hero_text.text_frame
tf_hero.word_wrap = True

p_h1 = tf_hero.paragraphs[0]
p_h1.text = "AGRISAARTHI"
p_h1.font.name = "Segoe UI"
p_h1.font.size = Pt(28)
p_h1.font.bold = True
p_h1.font.color.rgb = C_WHITE
p_h1.alignment = PP_ALIGN.CENTER

p_h2 = tf_hero.add_paragraph()
p_h2.text = "AI-Powered Precision Agriculture\n& Crop Advisory System"
p_h2.font.name = "Segoe UI"
p_h2.font.size = Pt(13)
p_h2.font.color.rgb = C_EMERALD
p_h2.alignment = PP_ALIGN.CENTER

p_h3 = tf_hero.add_paragraph()
p_h3.text = "\nKnow More · Grow More"
p_h3.font.name = "Segoe UI"
p_h3.font.size = Pt(12)
p_h3.font.bold = True
p_h3.font.color.rgb = C_GOLD
p_h3.alignment = PP_ALIGN.CENTER

p_h4 = tf_hero.add_paragraph()
p_h4.text = "\nASP.NET Core 10 · SQL Server · Python FastAPI · React 19"
p_h4.font.name = "Segoe UI"
p_h4.font.size = Pt(9.5)
p_h4.font.color.rgb = C_WHITE
p_h4.alignment = PP_ALIGN.CENTER

# Right Column: Title Header & Team Members (STRICTLY NAMES & REGISTRATION NUMBERS ONLY)
tb_main_title = s1.shapes.add_textbox(Inches(5.0), Inches(0.55), Inches(7.8), Inches(2.2))
tf_title = tb_main_title.text_frame
tf_title.word_wrap = True

p_dept = tf_title.paragraphs[0]
p_dept.text = "LOVELY PROFESSIONAL UNIVERSITY · SCHOOL OF COMPUTER SCIENCE & ENGINEERING"
p_dept.font.name = "Segoe UI"
p_dept.font.size = Pt(10)
p_dept.font.bold = True
p_dept.font.color.rgb = C_SECONDARY

p_main = tf_title.add_paragraph()
p_main.text = "AgriSaarthi: Smart Farming &\nCrop Intelligence Platform"
p_main.font.name = "Segoe UI"
p_main.font.size = Pt(24)
p_main.font.bold = True
p_main.font.color.rgb = C_PRIMARY

p_tag = tf_title.add_paragraph()
p_tag.text = "Multi-Crop Recommendation · Leaf Disease Sentry · Live Mandi Rates · Multilingual Support"
p_tag.font.name = "Segoe UI"
p_tag.font.size = Pt(11)
p_tag.font.bold = True
p_tag.font.color.rgb = C_GOLD

# Card Container for Team
add_card(s1, Inches(5.0), Inches(2.8), Inches(7.8), Inches(4.3), bg_color=C_CARD_BG, border_color=C_BORDER)

tb_team_hdr = s1.shapes.add_textbox(Inches(5.3), Inches(2.95), Inches(7.2), Inches(0.45))
p_thdr = tb_team_hdr.text_frame.paragraphs[0]
p_thdr.text = "CAPSTONE PROJECT TEAM MEMBERS"
p_thdr.font.name = "Segoe UI"
p_thdr.font.size = Pt(13)
p_thdr.font.bold = True
p_thdr.font.color.rgb = C_PRIMARY

# 3 Team Members: ONLY NAME AND REGISTRATION NUMBER (NO ROLES!)
members = [
    ("Taman Preet Singh", "12309438"),
    ("Utkarsh", "12308727"),
    ("Mansi Verma", "12416455")
]

for idx, (m_name, m_reg) in enumerate(members):
    c_left = Inches(5.2 + idx * 2.45)
    mem_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(3.55), Inches(2.35), Inches(1.9))
    mem_box.fill.solid()
    mem_box.fill.fore_color.rgb = C_LIGHT_GREEN if idx == 0 else C_BG
    mem_box.line.color.rgb = C_ACCENT if idx == 0 else C_BORDER
    mem_box.line.width = Pt(1.5)

    # Avatar circle icon placeholder
    circle_ico = s1.shapes.add_shape(MSO_SHAPE.OVAL, c_left + Inches(0.85), Inches(3.75), Inches(0.65), Inches(0.65))
    circle_ico.fill.solid()
    circle_ico.fill.fore_color.rgb = C_PRIMARY if idx == 0 else C_SECONDARY
    circle_ico.line.fill.background()

    tb_ci = s1.shapes.add_textbox(c_left + Inches(0.85), Inches(3.8), Inches(0.65), Inches(0.55))
    p_ci = tb_ci.text_frame.paragraphs[0]
    p_ci.text = m_name[0]
    p_ci.font.name = "Segoe UI"
    p_ci.font.size = Pt(14)
    p_ci.font.bold = True
    p_ci.font.color.rgb = C_WHITE
    p_ci.alignment = PP_ALIGN.CENTER

    tb_m = s1.shapes.add_textbox(c_left + Inches(0.1), Inches(4.5), Inches(2.15), Inches(0.9))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    
    pm1 = tf_m.paragraphs[0]
    pm1.text = m_name
    pm1.font.name = "Segoe UI"
    pm1.font.size = Pt(13)
    pm1.font.bold = True
    pm1.font.color.rgb = C_PRIMARY
    pm1.alignment = PP_ALIGN.CENTER

    pm2 = tf_m.add_paragraph()
    pm2.text = f"Reg. No: {m_reg}"
    pm2.font.name = "Segoe UI"
    pm2.font.size = Pt(11)
    pm2.font.bold = True
    pm2.font.color.rgb = C_GOLD
    pm2.alignment = PP_ALIGN.CENTER

# Project Guide & Institutional Details at Bottom of Slide 1
tb_guide = s1.shapes.add_textbox(Inches(5.3), Inches(5.65), Inches(7.2), Inches(1.3))
tf_g = tb_guide.text_frame
tf_g.word_wrap = True

pg1 = tf_g.paragraphs[0]
pg1.text = "PROJECT SUPERVISOR & MENTOR"
pg1.font.name = "Segoe UI"
pg1.font.size = Pt(10.5)
pg1.font.bold = True
pg1.font.color.rgb = C_SECONDARY

pg2 = tf_g.add_paragraph()
pg2.text = "Mr. Aryan Chauhan (UID: 35200)\nAssistant Professor, School of Computer Science & Engineering"
pg2.font.name = "Segoe UI"
pg2.font.size = Pt(11.5)
pg2.font.bold = True
pg2.font.color.rgb = C_DARK

pg3 = tf_g.add_paragraph()
pg3.text = "Academic Session: 2024–2025 · Capstone Project · Final Evaluation"
pg3.font.name = "Segoe UI"
pg3.font.size = Pt(10)
pg3.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 2: PROBLEM STATEMENT, MOTIVATION & WHY WE USE AGRISAARTHI
# ==============================================================================
s2 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s2)
add_header(s2, "Problem Context & Why We Use AgriSaarthi", "Chapter 1 · Project Motivation & Need", slide_num=2)

# Left Column: The Critical Problems
add_card(s2, Inches(0.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_prob = s2.shapes.add_textbox(Inches(1.05), Inches(1.6), Inches(5.25), Inches(5.15))
tf_pb = tb_prob.text_frame
tf_pb.word_wrap = True

p_pb_h = tf_pb.paragraphs[0]
p_pb_h.text = "CHALLENGES IN TRADITIONAL FARMING"
p_pb_h.font.name = "Segoe UI"
p_pb_h.font.size = Pt(12)
p_pb_h.font.bold = True
p_pb_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_pb, "Suboptimal Crop Guesswork:", "86% of smallholder farmers rely on habit or regional tradition rather than soil macronutrients (N-P-K, pH) and rainfall, leading to 15-25% annual yield losses.", 11)
add_bullet_point(tf_pb, "Middlemen & Price Exploitation:", "Farmers lack direct real-time access to APMC Mandi benchmark auction rates, resulting in distress sales at 20-30% below modal fair-market value.", 11)
add_bullet_point(tf_pb, "Delayed Plant Disease Detection:", "Pathogens like Yellow Rust in Wheat spread rapidly; delayed detection leads to irreversible crop damage before agricultural officers can visit.", 11)
add_bullet_point(tf_pb, "Language & Digital Literacy Barriers:", "Most agri platforms are English-only, alienating rural farmers in Punjab, Haryana, and northern agrarian belts.", 11)

# Right Column: Why We Use AgriSaarthi (The Solution)
add_card(s2, Inches(6.75), Inches(1.45), Inches(5.75), Inches(5.5))
tb_sol = s2.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.25), Inches(5.15))
tf_sol = tb_sol.text_frame
tf_sol.word_wrap = True

p_sol_h = tf_sol.paragraphs[0]
p_sol_h.text = "WHY WE USE AGRISAARTHI (OUR SOLUTION)"
p_sol_h.font.name = "Segoe UI"
p_sol_h.font.size = Pt(12)
p_sol_h.font.bold = True
p_sol_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_sol, "Precision AI Crop Matching:", "Data-driven Random Forest model (99.2% accuracy) recommending the exact optimal crop based on real N-P-K values, soil pH, and climate telemetry.", 11)
add_bullet_point(tf_sol, "Direct Live APMC Mandi Feeds:", "Transparent real-time auction rates from Khanna, Amritsar, Bathinda, Sirsa, etc., empowering farmers to negotiate fair prices.", 11)
add_bullet_point(tf_sol, "Instant Leaf Disease Diagnosis:", "Upload photo of infected crop leaf; system identifies pathogen, checklists symptoms, and prescribes certified chemical dosages.", 11)
add_bullet_point(tf_sol, "Complete Regional Inclusivity:", "Instant one-click switching across English, Hindi (हिंदी), and Punjabi (ਪੰਜਾਬੀ), with custom Dark & Light mode accessibility.", 11)
add_bullet_point(tf_sol, "Enterprise Reliability:", "Decoupled ASP.NET Core 10 backend + Microsoft SQL Server LocalDB ensures zero data loss and sub-60ms response times.", 11)

# ==============================================================================
# SLIDE 3: ENTERPRISE 4-TIER ARCHITECTURE & TECH STACK
# ==============================================================================
s3 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s3)
add_header(s3, "System Architecture: 4-Tier Enterprise Blueprint", "Chapter 2 · Architecture & Engineering", slide_num=3)

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

# Right Column: Tier-by-Tier Specifications
tiers = [
    ("Tier 1: Client Presentation Layer", "React 19 SPA · Razor MVC · Tailwind CSS · Heroicons", 
     "Responsive desktop & mobile UI, client-side JWT token management, instant multilingual translation (EN/HI/PA), and Dark/Light mode.", C_PRIMARY),
    
    ("Tier 2: API Gateway & Application Logic", "ASP.NET Core 10 Web API · C# · EF Core 10", 
     "Secure REST API gateway hosting dual auth (JWT + Cookies), CORS policy, DTO validation, and automated SQL schema migrations.", C_SECONDARY),
    
    ("Tier 3: AI Microservice Engine", "Python 3.10+ · FastAPI · Uvicorn · Scikit-Learn", 
     "Decoupled machine learning service running on port 8000; computes multiclass crop suitability probabilities with sub-50ms inference.", C_ACCENT),
    
    ("Tier 4: Relational Persistence & External APIs", "Microsoft SQL Server LocalDB · Open-Meteo · APMC", 
     "Structured relational storage for farmers, historical soil profiles, and advisory logs; combined with live GPS weather & Mandi feeds.", C_GOLD)
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
    pt1.font.size = Pt(11.5)
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
    pt3.font.size = Pt(8.5)
    pt3.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 4: DATABASE DESIGN & SQL SERVER ENTITY RELATIONSHIP MODEL
# ==============================================================================
s4 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s4)
add_header(s4, "Database Architecture: Microsoft SQL Server LocalDB", "Chapter 3 · Relational Schema & Persistence", slide_num=4)

# Left Column: Relational Entities & Design Highlights
add_card(s4, Inches(0.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_db = s4.shapes.add_textbox(Inches(1.05), Inches(1.6), Inches(5.25), Inches(5.15))
tf_db = tb_db.text_frame
tf_db.word_wrap = True

p_db_h = tf_db.paragraphs[0]
p_db_h.text = "CORE DATABASE ENTITIES & ATTRIBUTES"
p_db_h.font.name = "Segoe UI"
p_db_h.font.size = Pt(12)
p_db_h.font.bold = True
p_db_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_db, "Farmers Table:", "Stores primary identity [Id, FullName, Email, PhoneNumber, PasswordHash, CreatedAt]. Enforces UNIQUE index on Email.", 10.5)
add_bullet_point(tf_db, "FarmerProfiles Table:", "1-to-1 foreign key to Farmers [FarmerId, FarmSize, SoilType, IrrigationType, PrimaryCrop, State, District, Location].", 10.5)
add_bullet_point(tf_db, "CropAdvisories Table:", "Stores historical runs [Id, FarmerId, Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall, RecommendedCrop, ConfidenceScore, RequestDate].", 10.5)
add_bullet_point(tf_db, "MarketPrices Table:", "Stores APMC market feeds [Id, Commodity, Market, State, MinPrice, MaxPrice, ModalPrice, Trend, UpdatedDate].", 10.5)
add_bullet_point(tf_db, "DiseaseScans Table:", "Tracks plant health scans [Id, FarmerId, SelectedCrop, DetectedDisease, Confidence, Severity, ImageBase64, Timestamp].", 10.5)

# Right Column: Enterprise EF Core Capabilities
add_card(s4, Inches(6.75), Inches(1.45), Inches(5.75), Inches(5.5))
tb_ef = s4.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.25), Inches(5.15))
tf_ef = tb_ef.text_frame
tf_ef.word_wrap = True

p_ef_h = tf_ef.paragraphs[0]
p_ef_h.text = "DATABASE INTEGRITY & AUTOMATION FEATURES"
p_ef_h.font.name = "Segoe UI"
p_ef_h.font.size = Pt(12)
p_ef_h.font.bold = True
p_ef_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_ef, "Automated Code-First Migrations:", "Entity Framework Core 10 executes `dbContext.Database.Migrate()` on startup, provisioning schema changes without manual scripts.", 10.5)
add_bullet_point(tf_ef, "ACID Compliance & Concurrency:", "SQL Server guarantees transaction atomicity and row-level locking during high-volume farmer onboarding.", 10.5)
add_bullet_point(tf_ef, "Connection Resiliency:", "Configured with retry-on-failure policies and connection pooling to withstand transient network spikes.", 10.5)
add_bullet_point(tf_ef, "Data Privacy & Salted Hashing:", "Sensitive farmer credentials use cryptographic salting with PBKDF2/BCrypt; zero plaintext password persistence.", 10.5)
add_bullet_point(tf_ef, "Automated Seed Verification:", "Auto-populates reference APMC Mandi rates and default agronomic profiles if tables are newly initialized.", 10.5)

# ==============================================================================
# SLIDE 5: MACHINE LEARNING & CROP ADVISORY PIPELINE
# ==============================================================================
s5 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s5)
add_header(s5, "AI Engine: Random Forest Crop Recommendation", "Chapter 4 · Machine Learning & Inference", slide_num=5)

# Top 4 Metrics Cards
metrics = [
    ("99.2%", "TEST SET ACCURACY", "Evaluated on 440 stratified test samples with precision & recall above 0.98.", C_PRIMARY),
    ("2,200", "AGRONOMIC SAMPLES", "Curated Indian soil instances across 22 major food, fiber, and cash crops.", C_SECONDARY),
    ("< 50ms", "INFERENCE LATENCY", "High-throughput asynchronous FastAPI workers serving serialized Joblib models.", C_ACCENT),
    ("7 FEATURES", "TELEMETRY INPUTS", "N, P, K macronutrients, ambient temperature, humidity, soil pH, and rainfall.", C_GOLD)
]

for idx, (m_val, m_title, m_desc, m_col) in enumerate(metrics):
    c_left = Inches(0.8 + idx * 2.98)
    add_card(s5, c_left, Inches(1.45), Inches(2.82), Inches(1.85))
    
    strip = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_left, Inches(1.45), Inches(2.82), Inches(0.08))
    strip.fill.solid()
    strip.fill.fore_color.rgb = m_col
    strip.line.fill.background()

    tb_m = s5.shapes.add_textbox(c_left + Inches(0.1), Inches(1.6), Inches(2.62), Inches(1.6))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    p1 = tf_m.paragraphs[0]
    p1.text = m_val
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(24)
    p1.font.bold = True
    p1.font.color.rgb = m_col

    p2 = tf_m.add_paragraph()
    p2.text = m_title
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(9.5)
    p2.font.bold = True
    p2.font.color.rgb = C_DARK

    p3 = tf_m.add_paragraph()
    p3.text = m_desc
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(8.5)
    p3.font.color.rgb = C_MUTED

# Bottom Left: Feature Importance & Agronomic Analysis
add_card(s5, Inches(0.8), Inches(3.5), Inches(5.75), Inches(3.45))
tb_feat = s5.shapes.add_textbox(Inches(1.0), Inches(3.6), Inches(5.35), Inches(3.25))
tf_feat = tb_feat.text_frame
tf_feat.word_wrap = True

pf_h = tf_feat.paragraphs[0]
pf_h.text = "AGRONOMIC FEATURE IMPORTANCE WEIGHTS"
pf_h.font.name = "Segoe UI"
pf_h.font.size = Pt(11)
pf_h.font.bold = True
pf_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_feat, "Rainfall (23.4%):", "Primary determinant differentiating water-intensive crops (Rice, Jute) from drought-hardy pulses (Mothbeans).", 10)
add_bullet_point(tf_feat, "Relative Humidity (20.8%):", "Critical atmospheric driver governing plant evapotranspiration and leaf moisture retention.", 10)
add_bullet_point(tf_feat, "Phosphorus P (16.2%):", "Key nutrient governing root elongation, early seedling vigor, and grain flowering stages.", 10)
add_bullet_point(tf_feat, "Potassium K (14.9%):", "Regulates osmotic cellular turgor, drought adaptation, and pest resistance.", 10)
add_bullet_point(tf_feat, "Nitrogen N (11.8%):", "Essential for vegetative canopy biomass, leaf chlorophyll production, and protein synthesis.", 10)

# Bottom Right: End-to-End Prediction Pipeline
add_card(s5, Inches(6.75), Inches(3.5), Inches(5.75), Inches(3.45))
tb_pipe = s5.shapes.add_textbox(Inches(7.0), Inches(3.6), Inches(5.25), Inches(3.25))
tf_pipe = tb_pipe.text_frame
tf_pipe.word_wrap = True

pp_h = tf_pipe.paragraphs[0]
pp_h.text = "END-TO-END INFERENCE LIFECYCLE"
pp_h.font.name = "Segoe UI"
pp_h.font.size = Pt(11)
pp_h.font.bold = True
pp_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_pipe, "Step 1: Input Validation:", "ASP.NET Core ModelBinder validates soil inputs against physical feasibility ranges (pH 0-14, N-P-K 0-300).", 10)
add_bullet_point(tf_pipe, "Step 2: Microservice Dispatch:", "HttpClient transmits JSON payload to FastAPI `/predict/crop` endpoint via internal high-speed localhost loopback.", 10)
add_bullet_point(tf_pipe, "Step 3: Scaled Inference:", "Scikit-Learn pipeline scales parameters with RobustScaler, passing them to the Random Forest ensemble.", 10)
add_bullet_point(tf_pipe, "Step 4: Persistence & Response:", "Resulting crop match + probability distribution logged to SQL Server `CropAdvisories` and returned to UI.", 10)

# ==============================================================================
# SLIDE 6: PLANT HEALTH & COMPUTER VISION DISEASE DIAGNOSIS
# ==============================================================================
s6 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s6)
add_header(s6, "Plant Health Sentry & Disease Detection Engine", "Chapter 5 · Crop Pathology & Protection", slide_num=6)

# Left Column: Supported Crops & Pathology Library
add_card(s6, Inches(0.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_path = s6.shapes.add_textbox(Inches(1.05), Inches(1.6), Inches(5.25), Inches(5.15))
tf_path = tb_path.text_frame
tf_path.word_wrap = True

p_path_h = tf_path.paragraphs[0]
p_path_h.text = "MULTI-CROP PATHOLOGY IDENTIFICATION LIBRARY"
p_path_h.font.name = "Segoe UI"
p_path_h.font.size = Pt(12)
p_path_h.font.bold = True
p_path_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_path, "🌾 Wheat (Kanak):", "Yellow Rust (Puccinia striiformis) detection. Spots yellow pustules in linear rows; issues immediate regional fungicide alerts.", 10.5)
add_bullet_point(tf_path, "🌱 Rice (Paddy / Basmati):", "Rice Blast (Magnaporthe oryzae) & Bacterial Blight. Identifies spindle-shaped necrotic lesions on leaves and collar nodes.", 10.5)
add_bullet_point(tf_path, "🍅 Tomato Crops:", "Early Blight (Alternaria solani) & Late Blight. Detects concentric 'target board' rings and water-soaked dark leaf blotches.", 10.5)
add_bullet_point(tf_path, "🥔 Potato (Aloo):", "Late Blight (Phytophthora infestans) & Black Scurf. Diagnoses fungal sporulation under humid, overcast weather conditions.", 10.5)
add_bullet_point(tf_path, "🌿 Cotton (Kapas):", "Bacterial Leaf Blight & Leaf Curl Virus. Identifies angular water-soaked leaf spots and leaf vein thickening.", 10.5)

# Right Column: Automated Diagnostic Sentry & Treatment Prescriptions
add_card(s6, Inches(6.75), Inches(1.45), Inches(5.75), Inches(5.5))
tb_cure = s6.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.25), Inches(5.15))
tf_cure = tb_cure.text_frame
tf_cure.word_wrap = True

p_cure_h = tf_cure.paragraphs[0]
p_cure_h.text = "AUTOMATED DIAGNOSIS & ACTIONABLE CURE ENGINE"
p_cure_h.font.name = "Segoe UI"
p_cure_h.font.size = Pt(12)
p_cure_h.font.bold = True
p_cure_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_cure, "Leaf Image Ingestion:", "Supports direct JPEG/PNG camera uploads up to 15MB with client-side canvas preview and drag-and-drop validation.", 10.5)
add_bullet_point(tf_cure, "Immediate Symptom Checklist:", "Provides farmers with visible field markers (lesion colors, leaf curling, spore patterns) to confirm diagnosis.", 10.5)
add_bullet_point(tf_cure, "Certified Chemical Dosages:", "Prescribes precise ICAR-recommended remedies, e.g. Propiconazole 25% EC (Tilt) @ 1 ml/L or Mancozeb @ 2.5 g/L water.", 10.5)
add_bullet_point(tf_cure, "Organic & Bio-Control Alternatives:", "Offers neem seed kernel extract (NSKE 5%) and Trichoderma viride formulations for chemical-free farming.", 10.5)
add_bullet_point(tf_cure, "Rabi & Kharif Early Warnings:", "Proactive alerts active across Jalandhar, Kapurthala, and Bathinda belts to preempt spore outbreaks.", 10.5)

# ==============================================================================
# SLIDE 7: LIVE MANDI RATES, MULTILINGUAL ENGINE & DARK/LIGHT MODE
# ==============================================================================
s7 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s7)
add_header(s7, "Mandi Market Intelligence & Multilingual Accessibility", "Chapter 6 · Market Discovery & Inclusivity", slide_num=7)

# Left Column: Live Mandi Rates
add_card(s7, Inches(0.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_mandi = s7.shapes.add_textbox(Inches(1.05), Inches(1.6), Inches(5.25), Inches(5.15))
tf_mandi = tb_mandi.text_frame
tf_mandi.word_wrap = True

p_man_h = tf_mandi.paragraphs[0]
p_man_h.text = "REAL-TIME APMC MANDI AUCTION FEEDS"
p_man_h.font.name = "Segoe UI"
p_man_h.font.size = Pt(12)
p_man_h.font.bold = True
p_man_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_mandi, "Transparent Market Discovery:", "Aggregates benchmark auction rates from key agricultural mandis across Punjab, Haryana, UP, and Rajasthan.", 10.5)
add_bullet_point(tf_mandi, "Modal, Min & Max Pricing:", "Displays official APMC Modal Prices (₹/Quintal) alongside daily minimum and maximum traded bands.", 10.5)
add_bullet_point(tf_mandi, "24-Hour Auction Trends:", "Visual trend badges (Rising 🟢, Falling 🔴, Stable ⚪) indicating commodity demand shifts.", 10.5)
add_bullet_point(tf_mandi, "One-Click Live Refresh:", "Simulates real-time auction bidding fluctuations with timestamped audit records in SQL Server.", 10.5)
add_bullet_point(tf_mandi, "State & Crop Filtering:", "Instant search by commodity (Wheat, Paddy, Cotton, Mustard) or mandi location (Khanna, Amritsar, Sirsa).", 10.5)

# Right Column: Multilingual Switcher & Dark/Light Mode
add_card(s7, Inches(6.75), Inches(1.45), Inches(5.75), Inches(5.5))
tb_lang = s7.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.25), Inches(5.15))
tf_lang = tb_lang.text_frame
tf_lang.word_wrap = True

p_lang_h = tf_lang.paragraphs[0]
p_lang_h.text = "MULTILINGUAL (EN/HI/PA) & DARK MODE SYSTEM"
p_lang_h.font.name = "Segoe UI"
p_lang_h.font.size = Pt(12)
p_lang_h.font.bold = True
p_lang_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_lang, "Full Punjabi (ਪੰਜਾਬੀ) Localization:", "Authentic Gurmukhi terminology covering 100% of dashboard cards, farm metrics, weather tips, and mandi headers.", 10.5)
add_bullet_point(tf_lang, "Full Hindi (हिंदी) Localization:", "Native Devanagari translation allowing seamless accessibility for northern belt farming communities.", 10.5)
add_bullet_point(tf_lang, "Zero Page Reload Switcher:", "Instant DOM mutation via data-i18n attributes with persistent client memory stored in `localStorage`.", 10.5)
add_bullet_point(tf_lang, "Default English (EN):", "System initializes cleanly in standard English on first visit, switching dynamically on user preference.", 10.5)
add_bullet_point(tf_lang, "High-Contrast Dark Mode:", "One-click toggle between crisp Light Mode (default) and slate Dark Mode (`#0b1320`), reducing glare during night field work.", 10.5)

# ==============================================================================
# SLIDE 8: LIVE FARMER DASHBOARD & UI SHOWCASE (SCREENSHOT)
# ==============================================================================
s8 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s8)
add_header(s8, "Farmer Dashboard: Unified Agronomic Command Center", "Chapter 7 · UI/UX Showcase & Live Interface", slide_num=8)

# Center-Left: Prominent Live Dashboard Screenshot
add_card(s8, Inches(0.8), Inches(1.45), Inches(7.6), Inches(5.5))
tb_dash_hdr = s8.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(7.2), Inches(0.35))
p_dh = tb_dash_hdr.text_frame.paragraphs[0]
p_dh.text = "LIVE FARMER DASHBOARD & WEATHER WIDGET INTERFACE"
p_dh.font.name = "Segoe UI"
p_dh.font.size = Pt(11)
p_dh.font.bold = True
p_dh.font.color.rgb = C_PRIMARY

ss_path = IMG_DASHBOARD_LIVE if os.path.exists(IMG_DASHBOARD_LIVE) else IMG_DASHBOARD
if os.path.exists(ss_path):
    s8.shapes.add_picture(ss_path, Inches(0.95), Inches(1.95), width=Inches(7.3), height=Inches(4.85))

# Right Column: UI Architecture & Key Capabilities
add_card(s8, Inches(8.6), Inches(1.45), Inches(3.95), Inches(5.5))
tb_ui_body = s8.shapes.add_textbox(Inches(8.8), Inches(1.6), Inches(3.55), Inches(5.15))
tf_ui = tb_ui_body.text_frame
tf_ui.word_wrap = True

p_ui_h = tf_ui.paragraphs[0]
p_ui_h.text = "DASHBOARD HIGHLIGHTS"
p_ui_h.font.name = "Segoe UI"
p_ui_h.font.size = Pt(11.5)
p_ui_h.font.bold = True
p_ui_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_ui, "4 Top Telemetry Cards:", "One-tap direct access to Crop Advisory, Weather Forecast, Mandi Rates, and Leaf Pathology Scanner.", 10)
add_bullet_point(tf_ui, "Farm Profile Overview:", "Live display of farm acreage (6 Acres), sandy soil classification, tubewell irrigation, and primary cotton crop.", 10)
add_bullet_point(tf_ui, "Latest Advisory Card:", "Displays top recommended crop (Rice, 64% confidence) with real-time N-P-K, pH, and rainfall readouts.", 10)
add_bullet_point(tf_ui, "Hyperlocal Weather:", "Real-time temperature, humidity, wind telemetry, and agronomic irrigation tips.", 10)
add_bullet_point(tf_ui, "Rabi Sentry Alert:", "Instant alert box highlighting regional Yellow Rust spore warnings.", 10)

# ==============================================================================
# SLIDE 9: SECURITY ARCHITECTURE & DUAL AUTHENTICATION
# ==============================================================================
s9 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s9)
add_header(s9, "Enterprise Security Architecture & Data Protection", "Chapter 8 · Security, Dual Auth & Governance", slide_num=9)

# Left Column: Security Diagram
add_card(s9, Inches(0.8), Inches(1.45), Inches(5.5), Inches(5.5))
tb_sec_hdr = s9.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.0), Inches(0.35))
p_sh = tb_sec_hdr.text_frame.paragraphs[0]
p_sh.text = "DEFENSE-IN-DEPTH SECURITY ARCHITECTURE"
p_sh.font.name = "Segoe UI"
p_sh.font.size = Pt(11)
p_sh.font.bold = True
p_sh.font.color.rgb = C_PRIMARY

if os.path.exists(IMG_SECURITY):
    s9.shapes.add_picture(IMG_SECURITY, Inches(0.95), Inches(1.95), width=Inches(5.2), height=Inches(4.85))

# Right Column: 4 Security Mechanisms
sec_mechanisms = [
    ("Dual Authentication Scheme", "JWT Bearer Tokens (APIs) + Secure Cookies (Web MVC)", 
     "Seamless PolicyScheme forwarding: REST clients authenticate via signed JWT tokens, while browser MVC views use secure sliding HTTP-only cookies.", C_PRIMARY),
    
    ("Cryptographic Password Salting", "PBKDF2 / BCrypt with Unique Salt per Identity", 
     "Farmer passwords hashed using cryptographic salt iterations, neutralizing rainbow table and dictionary brute-force attacks.", C_SECONDARY),
    
    ("CSRF & Anti-Forgery Governance", "Anti-Forgery Validation on all State-Modifying POSTs", 
     "Mitigates Cross-Site Request Forgery on sensitive farm profile updates, mandi rate submissions, and disease scan uploads.", C_ACCENT),
    
    ("CORS Whitelist & SQL Protection", "Restricted Cross-Origin Policy + EF Core Parameterization", 
     "Strict CORS origin matching prevents unauthorized third-party scripts; Entity Framework Core parameterization blocks SQL injection.", C_GOLD)
]

for idx, (s_title, s_tech, s_desc, s_col) in enumerate(sec_mechanisms):
    y_pos = Inches(1.45 + idx * 1.38)
    add_card(s9, Inches(6.5), y_pos, Inches(6.05), Inches(1.26))
    
    strip = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.5), y_pos, Inches(0.18), Inches(1.26))
    strip.fill.solid()
    strip.fill.fore_color.rgb = s_col
    strip.line.fill.background()

    tb_s = s9.shapes.add_textbox(Inches(6.85), y_pos + Inches(0.08), Inches(5.55), Inches(1.1))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True

    ps1 = tf_s.paragraphs[0]
    ps1.text = s_title
    ps1.font.name = "Segoe UI"
    ps1.font.size = Pt(11.5)
    ps1.font.bold = True
    ps1.font.color.rgb = C_DARK

    ps2 = tf_s.add_paragraph()
    ps2.text = s_tech
    ps2.font.name = "Segoe UI"
    ps2.font.size = Pt(9.5)
    ps2.font.bold = True
    ps2.font.color.rgb = s_col

    ps3 = tf_s.add_paragraph()
    ps3.text = s_desc
    ps3.font.name = "Segoe UI"
    ps3.font.size = Pt(8.5)
    ps3.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 10: EXPERIMENTAL RESULTS, TESTING & PERFORMANCE VALIDATION
# ==============================================================================
s10 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s10)
add_header(s10, "Experimental Results & Verification Benchmarks", "Chapter 9 · Testing, QA & Performance", slide_num=10)

# Top 3 Benchmark Scorecards
scorecards = [
    ("< 60 ms", "API GATEWAY LATENCY", "Kestrel ASP.NET Core 10 pipeline benchmarked under concurrent load.", C_PRIMARY),
    ("99.2%", "CLASSIFICATION ACCURACY", "Random Forest ensemble on 440 stratified test samples across 22 crops.", C_SECONDARY),
    ("100%", "TEST SUITE COMPLETION", "Unit and integration tests across controllers, repository layers, and AI endpoints.", C_GOLD)
]

for idx, (sc_val, sc_title, sc_desc, sc_col) in enumerate(scorecards):
    c_left = Inches(0.8 + idx * 3.98)
    add_card(s10, c_left, Inches(1.45), Inches(3.78), Inches(1.95))
    
    strip = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_left, Inches(1.45), Inches(3.78), Inches(0.08))
    strip.fill.solid()
    strip.fill.fore_color.rgb = sc_col
    strip.line.fill.background()

    tb_sc = s10.shapes.add_textbox(c_left + Inches(0.15), Inches(1.65), Inches(3.48), Inches(1.65))
    tf_sc = tb_sc.text_frame
    tf_sc.word_wrap = True

    p1 = tf_sc.paragraphs[0]
    p1.text = sc_val
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(26)
    p1.font.bold = True
    p1.font.color.rgb = sc_col

    p2 = tf_sc.add_paragraph()
    p2.text = sc_title
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = C_DARK

    p3 = tf_sc.add_paragraph()
    p3.text = sc_desc
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(9)
    p3.font.color.rgb = C_MUTED

# Bottom Left: Rigorous Quality Assurance Strategy
add_card(s10, Inches(0.8), Inches(3.6), Inches(5.75), Inches(3.35))
tb_qa = s10.shapes.add_textbox(Inches(1.05), Inches(3.75), Inches(5.25), Inches(3.1))
tf_qa = tb_qa.text_frame
tf_qa.word_wrap = True

p_qa_h = tf_qa.paragraphs[0]
p_qa_h.text = "TESTING & QUALITY ASSURANCE PROTOCOLS"
p_qa_h.font.name = "Segoe UI"
p_qa_h.font.size = Pt(11)
p_qa_h.font.bold = True
p_qa_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_qa, "Unit Testing & In-Memory Mocking:", "Automated tests validate user registration, password hashing verification, and JWT issuance under diverse payload scenarios.", 10)
add_bullet_point(tf_qa, "Endpoint Contract Validation:", "Confirmed strict JSON schema adherence between React frontend, ASP.NET Core controllers, and FastAPI AI microservice.", 10)
add_bullet_point(tf_qa, "Boundary Value Testing:", "Tested edge conditions: extreme drought (0mm rain), alkaline soils (pH 10), and high-salinity inputs.", 10)

# Bottom Right: Reliability & Fault Tolerance
add_card(s10, Inches(6.75), Inches(3.6), Inches(5.75), Inches(3.35))
tb_res = s10.shapes.add_textbox(Inches(7.0), Inches(3.75), Inches(5.25), Inches(3.1))
tf_res = tb_res.text_frame
tf_res.word_wrap = True

p_res_h = tf_res.paragraphs[0]
p_res_h.text = "FAULT TOLERANCE & RESILIENCE VALIDATION"
p_res_h.font.name = "Segoe UI"
p_res_h.font.size = Pt(11)
p_res_h.font.bold = True
p_res_h.font.color.rgb = C_SECONDARY

add_bullet_point(tf_res, "Mandi Feed Fallback Engine:", "When external APMC networks experience downtime, the backend automatically serves verified benchmark fallback prices.", 10)
add_bullet_point(tf_res, "AI Microservice Circuit Breaker:", "If FastAPI is unreachable, ASP.NET Core triggers heuristic fallback rules, ensuring zero 500 errors to farmers.", 10)
add_bullet_point(tf_res, "Cross-Browser & Mobile Compliance:", "Verified flawless layout rendering across Chrome, Edge, Firefox, and Android mobile viewports.", 10)

# ==============================================================================
# SLIDE 11: FUTURE ROADMAP & SCALABILITY ENHANCEMENTS
# ==============================================================================
s11 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s11)
add_header(s11, "Future Roadmap: Next-Gen Precision Agriculture", "Chapter 10 · Scalability & Future Scope", slide_num=11)

roadmap_items = [
    ("Phase 1: IoT Field Microcontroller Integration", "ESP32 & LoRaWAN Sensor Nodes", 
     "Automated telemetry ingestion directly from in-situ soil moisture, temperature, and optical NPK sensor probes deployed in crop fields.", C_PRIMARY),
    
    ("Phase 2: Drone Multispectral Aerial Imaging", "Automated NDVI Aerial Stress Mapping", 
     "Commercial drone footage ingestion to compute Normalized Difference Vegetation Index (NDVI), detecting crop stress days before visible symptoms appear.", C_SECONDARY),
    
    ("Phase 3: Direct e-NAM Digital Mandi Bidding", "National Agriculture Market Matchmaking", 
     "Integration with national e-NAM APIs enabling farmers to list harvested produce, receive verified buyer bids, and eliminate commission agents.", C_ACCENT),
    
    ("Phase 4: Multilingual Voice IVR & WhatsApp Bot", "Telephony Accessibility for Non-Smartphones", 
     "Voice-driven automated telephonic interactive advisory for low-literacy farmers, delivering daily weather, advisory, and mandi prices via simple phone calls.", C_GOLD)
]

for idx, (r_title, r_tech, r_desc, r_col) in enumerate(roadmap_items):
    y_pos = Inches(1.45 + idx * 1.38)
    add_card(s11, Inches(0.8), y_pos, Inches(11.73), Inches(1.26))
    
    strip = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_pos, Inches(0.2), Inches(1.26))
    strip.fill.solid()
    strip.fill.fore_color.rgb = r_col
    strip.line.fill.background()

    tb_r = s11.shapes.add_textbox(Inches(1.2), y_pos + Inches(0.08), Inches(11.1), Inches(1.1))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    pr1 = tf_r.paragraphs[0]
    pr1.text = r_title
    pr1.font.name = "Segoe UI"
    pr1.font.size = Pt(12)
    pr1.font.bold = True
    pr1.font.color.rgb = C_DARK

    pr2 = tf_r.add_paragraph()
    pr2.text = r_tech
    pr2.font.name = "Segoe UI"
    pr2.font.size = Pt(10)
    pr2.font.bold = True
    pr2.font.color.rgb = r_col

    pr3 = tf_r.add_paragraph()
    pr3.text = r_desc
    pr3.font.name = "Segoe UI"
    pr3.font.size = Pt(9)
    pr3.font.color.rgb = C_MUTED

# ==============================================================================
# SLIDE 12: CONCLUSION, DELIVERABLES & THANK YOU (FINAL DEDICATED SLIDE)
# ==============================================================================
s12 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s12)
add_header(s12, "Project Conclusion & Acknowledgments", "Chapter 11 · Summary & Sign-off", slide_num=12)

# Left Column: Project Deliverables Summary
add_card(s12, Inches(0.8), Inches(1.45), Inches(5.75), Inches(5.5))
tb_del = s12.shapes.add_textbox(Inches(1.05), Inches(1.6), Inches(5.25), Inches(5.15))
tf_del = tb_del.text_frame
tf_del.word_wrap = True

p_del_h = tf_del.paragraphs[0]
p_del_h.text = "OFFICIAL PROJECT DELIVERABLES"
p_del_h.font.name = "Segoe UI"
p_del_h.font.size = Pt(12)
p_del_h.font.bold = True
p_del_h.font.color.rgb = C_PRIMARY

add_bullet_point(tf_del, "Full-Stack ASP.NET Core 10 API:", "Enterprise Web API configured on port 5000 with Dual Authentication (JWT + Cookies), CORS middleware, and EF Core migrations.", 10.5)
add_bullet_point(tf_del, "AI Crop Recommendation Engine:", "FastAPI microservice on port 8000 serving serialized 99.2% Random Forest model with sub-50ms inference.", 10.5)
add_bullet_point(tf_del, "Plant Leaf Disease Pathology Sentry:", "Multi-crop computer vision diagnosis covering Wheat Yellow Rust, Rice Blast, Tomato/Potato Blight, and Cotton Blight.", 10.5)
add_bullet_point(tf_del, "Microsoft SQL Server LocalDB:", "Production database hosting Farmers, Profiles, CropAdvisories, and live APMC MarketPrices.", 10.5)
add_bullet_point(tf_del, "Complete Multilingual Support:", "Instant one-click switching across English, Hindi (हिंदी), and Punjabi (ਪੰਜਾਬੀ), with custom Dark & Light mode.", 10.5)
add_bullet_point(tf_del, "One-Click Launcher Integration:", "Unified batch launcher (`run_agrisaarthi.bat`) starting SQL Server, AI microservice, frontend, and backend in 1 click.", 10.5)

# Right Column: Big Thank You Hero Card
add_card(s12, Inches(6.75), Inches(1.45), Inches(5.75), Inches(5.5), bg_color=C_PRIMARY, border_color=C_GOLD)

tb_thx = s12.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.25), Inches(5.0))
tf_thx = tb_thx.text_frame
tf_thx.word_wrap = True

pth0 = tf_thx.paragraphs[0]
pth0.text = "AGRISAARTHI CAPSTONE PROJECT"
pth0.font.name = "Segoe UI"
pth0.font.size = Pt(11)
pth0.font.bold = True
pth0.font.color.rgb = C_EMERALD
pth0.alignment = PP_ALIGN.CENTER

pth1 = tf_thx.add_paragraph()
pth1.text = "THANK YOU!"
pth1.font.name = "Segoe UI"
pth1.font.size = Pt(36)
pth1.font.bold = True
pth1.font.color.rgb = C_GOLD
pth1.alignment = PP_ALIGN.CENTER

pth2 = tf_thx.add_paragraph()
pth2.text = "Questions & Discussions Welcome\n"
pth2.font.name = "Segoe UI"
pth2.font.size = Pt(13)
pth2.font.color.rgb = C_WHITE
pth2.alignment = PP_ALIGN.CENTER

pth3 = tf_thx.add_paragraph()
pth3.text = "“Know More · Grow More”\nEmpowering Farmers with Precision Artificial Intelligence\n"
pth3.font.name = "Segoe UI"
pth3.font.size = Pt(11)
pth3.font.italic = True
pth3.font.color.rgb = C_EMERALD
pth3.alignment = PP_ALIGN.CENTER

pth4 = tf_thx.add_paragraph()
pth4.text = "PROJECT DEVELOPMENT TEAM:"
pth4.font.name = "Segoe UI"
pth4.font.size = Pt(11)
pth4.font.bold = True
pth4.font.color.rgb = C_GOLD
pth4.alignment = PP_ALIGN.CENTER

pth5 = tf_thx.add_paragraph()
pth5.text = "• Taman Preet Singh  (Reg. No: 12309438)\n• Utkarsh  (Reg. No: 12308727)\n• Mansi Verma  (Reg. No: 12416455)\n"
pth5.font.name = "Segoe UI"
pth5.font.size = Pt(10.5)
pth5.font.bold = True
pth5.font.color.rgb = C_WHITE
pth5.alignment = PP_ALIGN.CENTER

pth6 = tf_thx.add_paragraph()
pth6.text = "Guided by: Mr. Aryan Chauhan (UID: 35200)\nDepartment of Computer Science & Engineering\nLovely Professional University"
pth6.font.name = "Segoe UI"
pth6.font.size = Pt(10)
pth6.font.color.rgb = C_MUTED
pth6.alignment = PP_ALIGN.CENTER

# ==============================================================================
# SAVE PRESENTATION IN BOTH TARGET FOLDERS
# ==============================================================================
out_path_1 = r"C:\Users\taman\OneDrive\Desktop\agrisaarthi\AgriSaarthi_Presentation.pptx"
out_path_2 = r"C:\Users\taman\OneDrive\Desktop\New folder (2)\AgriSaarthi_Presentation.pptx"

prs.save(out_path_1)
prs.save(out_path_2)

print(f"SUCCESS: AgriSaarthi presentation saved with {len(prs.slides)} slides!")
print(f"File 1: {out_path_1}")
print(f"File 2: {out_path_2}")
