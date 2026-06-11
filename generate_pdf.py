#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
陶诗曼 - 简历PDF生成器
使用方法：python generate_pdf.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from PIL import Image
import os
from datetime import datetime

# 颜色配置
PRIMARY_COLOR = HexColor('#2C3E50')      # 深炭灰色
SECONDARY_COLOR = HexColor('#7F8C8D')    # 柔和灰色
ACCENT_COLOR = HexColor('#E67E22')       # 温暖橙色
LIGHT_BG = HexColor('#F8F9FA')          # 浅灰背景
BORDER_COLOR = HexColor('#E0E0E0')      # 边框灰色

def create_resume_pdf():
    """生成陶诗曼的简历PDF"""
    
    # 文件名
    filename = f"陶诗曼_简历_{datetime.now().strftime('%Y-%m-%d')}.pdf"
    pdf_path = os.path.join(os.path.dirname(__file__), filename)
    
    # 创建PDF
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    
    # 页边距
    margin_left = 20 * mm
    margin_right = 20 * mm
    margin_top = 20 * mm
    content_width = width - margin_left - margin_right
    
    # ===== 第一页 =====
    y_position = height - margin_top
    
    # 页眉背景
    c.setFillColor(ACCENT_COLOR)
    c.rect(0, height - 35*mm, width, 35*mm, fill=1, stroke=0)
    
    # 姓名
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(margin_left, height - 18*mm, "陶诗曼")
    
    # 副标题
    c.setFont("Helvetica", 11)
    c.drawString(margin_left, height - 26*mm, "武汉大学 2028届 财务管理专业")
    
    # 联系方式（右侧）
    c.setFont("Helvetica", 9)
    contact_info = "1807492456@qq.com  |  159-7147-0623  |  github.com/tsm5114"
    c.drawRightString(width - margin_right, height - 26*mm, contact_info)
    
    y_position = height - 45*mm
    
    # 简介区块
    c.setFillColor(LIGHT_BG)
    c.roundRect(margin_left, y_position - 30*mm, content_width, 30*mm, 5*mm, fill=1, stroke=0)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, y_position - 10*mm, "你好，我是陶诗曼")
    
    c.setFont("Helvetica", 10)
    c.setFillColor(SECONDARY_COLOR)
    c.drawCentredString(width/2, y_position - 18*mm, "武汉大学财务管理专业，拥抱数字化转型，渴望用数据驱动商业决策")
    
    y_position -= 40*mm
    
    # 辅助函数：绘制标题
    def draw_section_title(title, y):
        c.setStrokeColor(ACCENT_COLOR)
        c.setLineWidth(3)
        c.line(margin_left, y, margin_left + 5*mm, y)
        c.setFillColor(ACCENT_COLOR)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(margin_left + 8*mm, y - 2*mm, title)
        return y - 10*mm
    
    # 教育背景
    y_position = draw_section_title("教育背景", y_position)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin_left, y_position, "武汉大学 - 财务管理专业")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(SECONDARY_COLOR)
    c.drawString(margin_left + 100*mm, y_position, "本科 | 2024.09 - 2028.06（预计）")
    
    y_position -= 6*mm
    c.drawString(margin_left, y_position, "GPA: 3.62/4.0 | 专业排名前20%")
    y_position -= 5*mm
    c.drawString(margin_left, y_position, "相关课程：财务报表分析、公司金融、战略管理、数据分析")
    
    y_position -= 12*mm
    
    # 核心项目
    y_position = draw_section_title("核心项目", y_position)
    
    # 项目1：潮汕手钩花
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin_left, y_position, "潮汕手钩花跨境电商出海方案")
    c.setFont("Helvetica", 9)
    c.setFillColor(SECONDARY_COLOR)
    c.drawRightString(width - margin_right, y_position, "2025.03 - 2025.05")
    
    y_position -= 5*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left, y_position, "国家级大学生创新创业训练项目 | 项目负责人")
    
    y_position -= 6*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left, y_position, "项目背景：针对潮汕手钩花这一非物质文化遗产，探索'非遗+'跨境电商新模式，助力非遗文化出海。")
    
    y_position -= 5*mm
    # 项目要点
    points = [
        "用户研究：完成3省8市非遗手钩花产业发展调研，访谈非遗传承人24位，深度访谈用户300+",
        "数据分析：通过SEM和问卷收集1200+份数据，构建用户画像，洞察海外华人及对中国文化感兴趣群体的核心需求",
        "方案设计：制定'独立站+第三方平台'双轨运营策略，设计选品矩阵和差异化定价方案",
        "推广策略：制定TikTok短视频和Instagram种草内容策略，预测年GMV超200万元",
        "项目成果：获省级重点立项，优秀结项，经验收获评'优秀'等级"
    ]
    
    for point in points:
        c.drawString(margin_left + 3*mm, y_position, "• " + point)
        y_position -= 5*mm
    
    # 项目图片
    img1_path = os.path.join(os.path.dirname(__file__), "images", "图片1.jpg")
    img2_path = os.path.join(os.path.dirname(__file__), "images", "图片2.jpg")
    
    if os.path.exists(img1_path):
        c.drawImage(img1_path, margin_left, y_position - 30*mm, width=65*mm, height=30*mm)
        c.setFont("Helvetica", 7)
        c.setFillColor(SECONDARY_COLOR)
        c.drawCentredString(margin_left + 32.5*mm, y_position - 33*mm, "用户调研报告")
    
    if os.path.exists(img2_path):
        c.drawImage(img2_path, margin_left + 70*mm, y_position - 30*mm, width=65*mm, height=30*mm)
        c.setFont("Helvetica", 7)
        c.setFillColor(SECONDARY_COLOR)
        c.drawCentredString(margin_left + 102.5*mm, y_position - 33*mm, "独立站设计方案")
    
    y_position -= 40*mm
    
    # 项目2：AB Test
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin_left, y_position, "电商平台AB Test实验分析")
    c.setFont("Helvetica", 9)
    c.setFillColor(SECONDARY_COLOR)
    c.drawRightString(width - margin_right, y_position, "2025.01 - 2025.02")
    
    y_position -= 5*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left, y_position, "课程项目 | 数据分析")
    
    y_position -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left, y_position, "为某电商平台设计并实施A/B Test实验，评估新旧UI版本对用户转化率的影响。")
    
    y_position -= 5*mm
    points2 = [
        "实验设计：确定实验假设、样本量（4,032/组）和分流策略，确保实验统计功效≥80%",
        "数据处理：使用Python进行数据清洗，处理10,000+条用户行为日志，识别异常流量",
        "统计建模：运用Python实现双样本T检验和贝叶斯分析，计算转化率提升及置信区间",
        "实验结论：新版本转化率提升2.34%，95%置信区间[1.85%, 2.83%]，预测年增GMV 500万"
    ]
    
    for point in points2:
        c.drawString(margin_left + 3*mm, y_position, "• " + point)
        y_position -= 5*mm
    
    y_position -= 5*mm
    
    # 项目3：千域供应链
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin_left, y_position, "千域供应链商业计划书")
    c.setFont("Helvetica", 9)
    c.setFillColor(SECONDARY_COLOR)
    c.drawRightString(width - margin_right, y_position, "2024.10 - 2024.11")
    
    y_position -= 5*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left, y_position, "课程项目 | 商业分析")
    
    y_position -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left, y_position, "为千域供应链撰写完整商业计划书，涵盖市场分析、商业模式、运营策略和财务预测。")
    
    y_position -= 5*mm
    points3 = [
        "行业研究：通过公开数据、行业报告等完成宏观环境和行业竞争态势分析",
        "商业模式设计：设计SaaS+供应链金融双驱动模式，明确价值主张和收入结构",
        "财务预测：基于合理假设，完成5年财务预测，预测IRR达35%",
        "项目成果：获'电商三创赛'校级一等奖"
    ]
    
    for point in points3:
        c.drawString(margin_left + 3*mm, y_position, "• " + point)
        y_position -= 5*mm
    
    # ===== 第二页 =====
    c.showPage()
    y_position = height - margin_top
    
    # 页眉（简化版）
    c.setFillColor(ACCENT_COLOR)
    c.rect(0, height - 25*mm, width, 25*mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin_left, height - 15*mm, "陶诗曼 - 个人简历")
    c.setFont("Helvetica", 10)
    c.drawRightString(width - margin_right, height - 15*mm, "第2页 / 共2页")
    
    y_position = height - 35*mm
    
    # 实习经历
    y_position = draw_section_title("实习经历", y_position)
    
    # 实习卡片
    c.setStrokeColor(BORDER_COLOR)
    c.setFillColor(white)
    c.roundRect(margin_left, y_position - 60*mm, content_width, 60*mm, 3*mm, fill=1, stroke=1)
    
    y_position -= 8*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin_left + 3*mm, y_position, "战略运营实习生")
    c.setFont("Helvetica", 9)
    c.setFillColor(SECONDARY_COLOR)
    c.drawRightString(width - margin_right - 3*mm, y_position, "2025.05 - 2025.07")
    
    y_position -= 6*mm
    c.setFillColor(ACCENT_COLOR)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_left + 3*mm, y_position, "万物云空间数字科技有限公司")
    
    y_position -= 6*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(margin_left + 3*mm, y_position, "日常工作：")
    
    y_position -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 9)
    exp_points = [
        "追踪多模态大模型（GPT-4o、Gemini 1.5 Pro、文心一言V3.5、豆包）最新动态",
        "监控竞品动态，输出日度/周度信息监控报告",
        "整理内部分享会议纪要，提炼关键信息"
    ]
    for point in exp_points:
        c.drawString(margin_left + 6*mm, y_position, "• " + point)
        y_position -= 5*mm
    
    y_position -= 2*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(margin_left + 3*mm, y_position, "核心成果：")
    
    y_position -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left + 6*mm, y_position, "• 独立完成《多模态大模型竞品分析报告》，获部门负责人高度认可")
    y_position -= 5*mm
    c.drawString(margin_left + 6*mm, y_position, "• 报告已发布在公司公众号，累计阅读量2000+")
    
    # 实习图片
    exp_img1 = r"C:\Users\tsmti\Pictures\Screenshots\屏幕截图 2026-06-11 151117.png"
    exp_img2 = r"C:\Users\tsmti\Pictures\Screenshots\屏幕截图 2026-06-11 151050.png"
    
    if os.path.exists(exp_img1):
        c.drawImage(exp_img1, margin_left + 3*mm, y_position - 25*mm, width=80*mm, height=25*mm)
        c.setFont("Helvetica", 7)
        c.setFillColor(SECONDARY_COLOR)
        c.drawCentredString(margin_left + 43*mm, y_position - 28*mm, "多模态大模型竞品分析报告")
    
    if os.path.exists(exp_img2):
        c.drawImage(exp_img2, margin_left + 88*mm, y_position - 25*mm, width=80*mm, height=25*mm)
        c.setFont("Helvetica", 7)
        c.setFillColor(SECONDARY_COLOR)
        c.drawCentredString(margin_left + 128*mm, y_position - 28*mm, "行业信息监控与分析")
    
    y_position -= 35*mm
    
    # 校园经历
    y_position = draw_section_title("校园经历", y_position)
    
    # 校园经历卡片
    c.setStrokeColor(BORDER_COLOR)
    c.setFillColor(white)
    c.roundRect(margin_left, y_position - 20*mm, content_width, 20*mm, 3*mm, fill=1, stroke=1)
    
    y_position -= 8*mm
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_left + 3*mm, y_position, "武汉大学KAB创业俱乐部 - 创业实践部负责人")
    c.setFont("Helvetica", 8)
    c.setFillColor(SECONDARY_COLOR)
    c.drawRightString(width - margin_right - 3*mm, y_position, "2024.09 - 2025.06")
    
    y_position -= 5*mm
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left + 3*mm, y_position, "• 策划并执行创业沙龙活动5场，覆盖学生300+")
    y_position -= 4*mm
    c.drawString(margin_left + 3*mm, y_position, "• 协助举办'创客马拉松'，吸引20+团队参与")
    y_position -= 4*mm
    c.drawString(margin_left + 3*mm, y_position, "• 负责活动宣传物料设计与社群运营")
    
    y_position -= 12*mm
    
    # 技能特长
    y_position = draw_section_title("技能特长", y_position)
    
    # 左列：数据分析
    c.setStrokeColor(BORDER_COLOR)
    c.setFillColor(white)
    c.roundRect(margin_left, y_position - 35*mm, content_width/2 - 3*mm, 35*mm, 3*mm, fill=1, stroke=1)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_left + 3*mm, y_position - 5*mm, "数据分析")
    
    skills = [
        ("SQL", 0.9),
        ("Python", 0.9),
        ("Excel", 0.95),
        ("R语言", 0.9)
    ]
    
    skill_y = y_position - 12*mm
    for skill, level in skills:
        c.setFillColor(SECONDARY_COLOR)
        c.setFont("Helvetica", 9)
        c.drawString(margin_left + 3*mm, skill_y, skill)
        
        # 技能条
        bar_x = margin_left + 25*mm
        bar_width = 35*mm
        bar_height = 3*mm
        
        c.setFillColor(BORDER_COLOR)
        c.roundRect(bar_x, skill_y - 1*mm, bar_width, bar_height, 1*mm, fill=1, stroke=0)
        
        c.setFillColor(ACCENT_COLOR)
        c.roundRect(bar_x, skill_y - 1*mm, bar_width * level, bar_height, 1*mm, fill=1, stroke=0)
        
        c.setFillColor(SECONDARY_COLOR)
        c.drawRightString(bar_x + bar_width - 1*mm, skill_y - 0.5*mm, f"{int(level*100)}%")
        
        skill_y -= 7*mm
    
    # 右列：工具能力
    c.setStrokeColor(BORDER_COLOR)
    c.setFillColor(white)
    c.roundRect(margin_left + content_width/2 + 3*mm, y_position - 35*mm, content_width/2 - 3*mm, 35*mm, 3*mm, fill=1, stroke=1)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_left + content_width/2 + 6*mm, y_position - 5*mm, "工具能力")
    
    tools = ["Claude Code", "VS Code", "ChatGPT", "GitHub"]
    tool_y = y_position - 14*mm
    for tool in tools:
        c.setFillColor(SECONDARY_COLOR)
        c.setFont("Helvetica", 9)
        c.drawString(margin_left + content_width/2 + 6*mm, tool_y, "✓ " + tool)
        tool_y -= 6*mm
    
    y_position -= 45*mm
    
    # 语言能力
    y_position = draw_section_title("语言能力", y_position)
    
    c.setStrokeColor(BORDER_COLOR)
    c.setFillColor(white)
    c.roundRect(margin_left, y_position - 15*mm, content_width, 15*mm, 3*mm, fill=1, stroke=1)
    
    c.setFillColor(PRIMARY_COLOR)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_left + 3*mm, y_position - 7*mm, "英语 CET-4 (639分)")
    
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 9)
    c.drawString(margin_left + 3*mm, y_position - 12*mm, "具备良好的商务英语读写能力")
    
    # 页脚
    c.setFillColor(SECONDARY_COLOR)
    c.setFont("Helvetica", 8)
    c.drawCentredString(width/2, 10*mm, "© 2026 陶诗曼 | 武汉大学 财务管理 | 求职意向：产品经理 / 运营 / 商业分析")
    
    # 保存
    c.save()
    print(f"[OK] 简历PDF已生成：{filename}")
    return filename

if __name__ == "__main__":
    print("正在生成简历PDF...")
    try:
        filename = create_resume_pdf()
        print("\n生成成功！")
        print(f"PDF文件位置：{os.path.abspath(filename)}")
    except Exception as e:
        print(f"生成失败：{e}")
        import traceback
        traceback.print_exc()