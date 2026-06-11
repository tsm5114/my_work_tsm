#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
陶诗曼 - 简历PDF生成器（支持中文）
使用方法：python generate_pdf_chinese.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white, Color
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from datetime import datetime

# 注册中文字体
def register_chinese_font():
    """注册系统中文字体"""
    font_paths = [
        # Windows字体路径
        r"C:\Windows\Fonts\simhei.ttf",      # 黑体
        r"C:\Windows\Fonts\msyh.ttc",        # 微软雅黑
        r"C:\Windows\Fonts\simsun.ttc",      # 宋体
        r"C:\Windows\Fonts\simkai.ttf",      # 楷体
    ]
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                if font_path.endswith('.ttc'):
                    # TTC字体需要指定子字体索引
                    pdfmetrics.registerFont(TTFont('ChineseFont', font_path, subfontIndex=0))
                else:
                    pdfmetrics.registerFont(TTFont('ChineseFont', font_path))
                print(f"[OK] 已加载中文字体: {font_path}")
                return True
            except Exception as e:
                print(f"[WARN] 字体加载失败: {font_path}, {e}")
                continue
    
    print("[WARN] 未找到中文字体，将使用默认字体")
    return False

# 颜色配置
PRIMARY_COLOR = HexColor('#2C3E50')      # 深炭灰色
SECONDARY_COLOR = HexColor('#7F8C8D')    # 柔和灰色  
ACCENT_COLOR = HexColor('#E67E22')       # 温暖橙色
LIGHT_BG = HexColor('#F8F9FA')           # 浅灰背景
BORDER_COLOR = HexColor('#E0E0E0')       # 边框灰色
WHITE = white
BLACK = black

def create_resume_pdf():
    """生成陶诗曼的简历PDF"""
    
    # 注册中文字体
    register_chinese_font()
    
    # 文件名
    filename = f"陶诗曼_简历_{datetime.now().strftime('%Y-%m-%d')}.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), filename)
    
    # 创建PDF
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    
    # 页边距
    margin_left = 15 * mm
    margin_right = 15 * mm
    margin_top = 15 * mm
    margin_bottom = 15 * mm
    content_width = width - margin_left - margin_right
    
    # ===== 第一页 =====
    y = height - margin_top
    
    # 页眉背景条
    c.setFillColor(ACCENT_COLOR)
    c.rect(0, height - 30*mm, width, 30*mm, fill=1, stroke=0)
    
    # 姓名（白色）
    c.setFillColor(WHITE)
    c.setFont("ChineseFont", 22)
    c.drawString(margin_left, height - 15*mm, "陶诗曼")
    
    # 副标题
    c.setFont("ChineseFont", 10)
    c.drawString(margin_left, height - 23*mm, "武汉大学 2028届 | 财务管理专业")
    
    # 联系方式（右侧，白色）
    c.setFont("ChineseFont", 8)
    contact = "Email: 1807492456@qq.com | Tel: 159-7147-0623 | GitHub: github.com/tsm5114"
    c.drawRightString(width - margin_right, height - 23*mm, contact)
    
    y = height - 40*mm
    
    # 简介区块（浅灰背景）
    c.setFillColor(LIGHT_BG)
    c.roundRect(margin_left, y - 25*mm, content_width, 25*mm, 3*mm, fill=1, stroke=0)
    
    # 简介文字
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 12)
    c.drawCentredString(width/2, y - 8*mm, "你好，我是陶诗曼")
    
    c.setFont("ChineseFont", 9)
    c.setFillColor(SECONDARY_COLOR)
    c.drawCentredString(width/2, y - 15*mm, "武汉大学财务管理专业，拥抱数字化转型，渴望用数据驱动商业决策")
    
    y -= 32*mm
    
    # 章节标题绘制函数
    def draw_title(title, y_pos):
        # 左侧橙色竖线
        c.setStrokeColor(ACCENT_COLOR)
        c.setLineWidth(2)
        c.line(margin_left, y_pos, margin_left, y_pos - 6*mm)
        # 标题文字
        c.setFillColor(ACCENT_COLOR)
        c.setFont("ChineseFont", 12)
        c.drawString(margin_left + 4*mm, y_pos - 2*mm, title)
        return y_pos - 10*mm
    
    # ===== 教育背景 =====
    y = draw_title("教育背景", y)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 10)
    c.drawString(margin_left, y, "武汉大学 - 财务管理专业")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left + 90*mm, y, "本科 | 2024.09 - 2028.06")
    
    y -= 5*mm
    c.drawString(margin_left, y, "GPA: 3.62/4.0 | 专业排名前20%")
    y -= 4*mm
    c.drawString(margin_left, y, "相关课程: 财务报表分析、公司金融、战略管理、数据分析")
    
    y -= 8*mm
    
    # ===== 核心项目 =====
    y = draw_title("核心项目", y)
    
    # 项目1: 潮汕手钩花
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 10)
    c.drawString(margin_left, y, "潮汕手钩花跨境电商出海方案")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawRightString(width - margin_right, y, "2025.03 - 2025.05")
    
    y -= 4*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left, y, "国家级大学生创新创业训练项目 | 项目负责人")
    
    y -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left, y, "针对潮汕手钩花非物质文化遗产，探索'非遗+'跨境电商新模式")
    
    y -= 4*mm
    points1 = [
        "用户研究: 完成3省8市调研，访谈非遗传承人24位，深度访谈用户300+",
        "数据分析: 收集1200+份数据，构建用户画像，洞察海外华人核心需求",
        "方案设计: 制定'独立站+第三方平台'双轨运营策略",
        "推广策略: TikTok短视频+Instagram种草，预测年GMV超200万元",
        "项目成果: 省级重点立项，优秀结项"
    ]
    for p in points1:
        c.drawString(margin_left + 2*mm, y, "- " + p)
        y -= 4*mm
    
    # 项目图片
    img1 = os.path.join(os.path.dirname(__file__), "images", "图片1.jpg")
    img2 = os.path.join(os.path.dirname(__file__), "images", "图片2.jpg")
    
    if os.path.exists(img1):
        c.drawImage(img1, margin_left, y - 22*mm, width=60*mm, height=22*mm)
        c.setFont("ChineseFont", 6)
        c.setFillColor(SECONDARY_COLOR)
        c.drawCentredString(margin_left + 30*mm, y - 25*mm, "用户调研报告")
    
    if os.path.exists(img2):
        c.drawImage(img2, margin_left + 65*mm, y - 22*mm, width=60*mm, height=22*mm)
        c.setFont("ChineseFont", 6)
        c.drawCentredString(margin_left + 95*mm, y - 25*mm, "独立站设计方案")
    
    y -= 30*mm
    
    # 项目2: AB Test
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 10)
    c.drawString(margin_left, y, "电商平台AB Test实验分析")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawRightString(width - margin_right, y, "2025.01 - 2025.02")
    
    y -= 4*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left, y, "课程项目 | 数据分析")
    
    y -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left, y, "为电商平台设计A/B Test实验，评估UI版本对转化率的影响")
    
    y -= 4*mm
    points2 = [
        "实验设计: 样本量4032/组，统计功效>=80%",
        "数据处理: Python清洗10000+条用户行为日志",
        "统计建模: 双样本T检验+贝叶斯分析",
        "实验结论: 转化率提升2.34%，预测年增GMV 500万"
    ]
    for p in points2:
        c.drawString(margin_left + 2*mm, y, "- " + p)
        y -= 4*mm
    
    y -= 5*mm
    
    # 项目3: 千域供应链
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 10)
    c.drawString(margin_left, y, "千域供应链商业计划书")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawRightString(width - margin_right, y, "2024.10 - 2024.11")
    
    y -= 4*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left, y, "课程项目 | 商业分析")
    
    y -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left, y, "撰写完整商业计划书，涵盖市场分析、商业模式、运营策略")
    
    y -= 4*mm
    points3 = [
        "行业研究: 宏观环境和行业竞争态势分析",
        "商业模式: SaaS+供应链金融双驱动模式",
        "财务预测: 5年财务预测，IRR达35%",
        "项目成果: '电商三创赛'校级一等奖"
    ]
    for p in points3:
        c.drawString(margin_left + 2*mm, y, "- " + p)
        y -= 4*mm
    
    # ===== 第二页 =====
    c.showPage()
    y = height - margin_top
    
    # 页眉
    c.setFillColor(ACCENT_COLOR)
    c.rect(0, height - 20*mm, width, 20*mm, fill=1, stroke=0)
    
    c.setFillColor(WHITE)
    c.setFont("ChineseFont", 14)
    c.drawString(margin_left, height - 12*mm, "陶诗曼 - 个人简历")
    
    c.setFont("ChineseFont", 8)
    c.drawRightString(width - margin_right, height - 12*mm, "第2页")
    
    y = height - 28*mm
    
    # ===== 实习经历 =====
    y = draw_title("实习经历", y)
    
    # 实习卡片背景
    c.setFillColor(WHITE)
    c.setStrokeColor(BORDER_COLOR)
    c.roundRect(margin_left, y - 50*mm, content_width, 50*mm, 2*mm, fill=1, stroke=1)
    
    y -= 6*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 10)
    c.drawString(margin_left + 2*mm, y, "战略运营实习生")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawRightString(width - margin_right - 2*mm, y, "2025.05 - 2025.07")
    
    y -= 4*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("ChineseFont", 9)
    c.drawString(margin_left + 2*mm, y, "万物云空间数字科技有限公司")
    
    y -= 5*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left + 2*mm, y, "日常工作:")
    
    y -= 4*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    work_points = [
        "追踪多模态大模型(GPT-4o、Gemini、文心一言、豆包)最新动态",
        "监控竞品动态，输出日度/周度信息监控报告",
        "整理内部分享会议纪要"
    ]
    for p in work_points:
        c.drawString(margin_left + 4*mm, y, "- " + p)
        y -= 4*mm
    
    y -= 2*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left + 2*mm, y, "核心成果:")
    
    y -= 4*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left + 4*mm, y, "- 独立完成《多模态大模型竞品分析报告》")
    y -= 4*mm
    c.drawString(margin_left + 4*mm, y, "- 报告发布在公司公众号，累计阅读量2000+")
    
    # 实习图片
    exp_img1 = r"C:\Users\tsmti\Pictures\Screenshots\屏幕截图 2026-06-11 151117.png"
    exp_img2 = r"C:\Users\tsmti\Pictures\Screenshots\屏幕截图 2026-06-11 151050.png"
    
    if os.path.exists(exp_img1):
        c.drawImage(exp_img1, margin_left + 2*mm, y - 20*mm, width=75*mm, height=20*mm)
        c.setFont("ChineseFont", 6)
        c.setFillColor(SECONDARY_COLOR)
        c.drawCentredString(margin_left + 39*mm, y - 23*mm, "竞品分析报告")
    
    if os.path.exists(exp_img2):
        c.drawImage(exp_img2, margin_left + 80*mm, y - 20*mm, width=75*mm, height=20*mm)
        c.setFont("ChineseFont", 6)
        c.drawCentredString(margin_left + 117*mm, y - 23*mm, "行业信息监控")
    
    y -= 28*mm
    
    # ===== 校园经历 =====
    y = draw_title("校园经历", y)
    
    c.setFillColor(WHITE)
    c.setStrokeColor(BORDER_COLOR)
    c.roundRect(margin_left, y - 18*mm, content_width, 18*mm, 2*mm, fill=1, stroke=1)
    
    y -= 5*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 9)
    c.drawString(margin_left + 2*mm, y, "武汉大学KAB创业俱乐部 - 创业实践部负责人")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 7)
    c.drawRightString(width - margin_right - 2*mm, y, "2024.09 - 2025.06")
    
    y -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left + 2*mm, y, "- 策划创业沙龙活动5场，覆盖学生300+")
    y -= 4*mm
    c.drawString(margin_left + 2*mm, y, "- 协助举办'创客马拉松'，吸引20+团队参与")
    
    y -= 10*mm
    
    # ===== 技能特长 =====
    y = draw_title("技能特长", y)
    
    # 左列: 数据分析
    c.setFillColor(WHITE)
    c.setStrokeColor(BORDER_COLOR)
    c.roundRect(margin_left, y - 30*mm, content_width/2 - 2*mm, 30*mm, 2*mm, fill=1, stroke=1)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 9)
    c.drawString(margin_left + 2*mm, y - 4*mm, "数据分析")
    
    skills = [("SQL", 90), ("Python", 90), ("Excel", 95), ("R语言", 90)]
    skill_y = y - 10*mm
    for skill, pct in skills:
        c.setFillColor(SECONDARY_COLOR)
        c.setFont("ChineseFont", 8)
        c.drawString(margin_left + 2*mm, skill_y, skill)
        
        # 进度条
        bar_x = margin_left + 20*mm
        bar_w = 30*mm
        c.setFillColor(BORDER_COLOR)
        c.rect(bar_x, skill_y - 1*mm, bar_w, 3*mm, fill=1, stroke=0)
        c.setFillColor(ACCENT_COLOR)
        c.rect(bar_x, skill_y - 1*mm, bar_w * pct / 100, 3*mm, fill=1, stroke=0)
        
        c.setFillColor(SECONDARY_COLOR)
        c.drawRightString(bar_x + bar_w + 5*mm, skill_y, f"{pct}%")
        skill_y -= 6*mm
    
    # 右列: 工具能力
    c.setFillColor(WHITE)
    c.setStrokeColor(BORDER_COLOR)
    c.roundRect(margin_left + content_width/2 + 2*mm, y - 30*mm, content_width/2 - 2*mm, 30*mm, 2*mm, fill=1, stroke=1)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 9)
    c.drawString(margin_left + content_width/2 + 4*mm, y - 4*mm, "工具能力")
    
    tools = ["Claude Code", "VS Code", "ChatGPT", "GitHub"]
    tool_y = y - 12*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    for tool in tools:
        c.drawString(margin_left + content_width/2 + 4*mm, tool_y, "- " + tool)
        tool_y -= 5*mm
    
    y -= 38*mm
    
    # ===== 语言能力 =====
    y = draw_title("语言能力", y)
    
    c.setFillColor(WHITE)
    c.setStrokeColor(BORDER_COLOR)
    c.roundRect(margin_left, y - 12*mm, content_width, 12*mm, 2*mm, fill=1, stroke=1)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("ChineseFont", 9)
    c.drawString(margin_left + 2*mm, y - 5*mm, "英语 CET-4 (639分)")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 8)
    c.drawString(margin_left + 2*mm, y - 9*mm, "具备良好的商务英语读写能力")
    
    # 页脚
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("ChineseFont", 7)
    c.drawCentredString(width/2, 8*mm, "2026 陶诗曼 | 武汉大学 财务管理 | 求职意向: 产品经理 / 运营 / 商业分析")
    
    # 保存
    c.save()
    print(f"[OK] PDF已生成: {filename}")
    return filename

if __name__ == "__main__":
    print("正在生成简历PDF...")
    try:
        filename = create_resume_pdf()
        print(f"\n生成成功!")
        print(f"文件位置: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"生成失败: {e}")
        import traceback
        traceback.print_exc()