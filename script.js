document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('mobile-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            navMenu.classList.toggle('hidden');
        });

        document.querySelectorAll('#mobile-menu a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                navMenu.classList.add('hidden');
            });
        });
    }

    const tabs = document.querySelectorAll('.tab');
    const cards = document.querySelectorAll('.portfolio-card');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            const category = tab.getAttribute('data-category');

            cards.forEach(card => {
                if (card.getAttribute('data-category') === category || category === 'all') {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });

    const portfolioCards = document.querySelectorAll('.portfolio-card');
    portfolioCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        
        setTimeout(() => {
            const observer2 = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, observerOptions);
            observer2.observe(card);
        }, index * 100);
    });

    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 60;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.05)';
        }
    });

    /* --- 作品集动态渲染 & 交互 --- */
    async function loadProjects(){
        try{
            const res = await fetch('projects.json');
            const data = await res.json();
            renderProjects(data);
            initCharts();
        }catch(e){
            console.error('加载项目数据失败', e);
        }
    }

    function renderProjects(list){
        const container = document.getElementById('projects-list');
        container.innerHTML = '';
        list.forEach(p => {
            const el = document.createElement('article');
            el.className = 'project-card card fade-in';
            el.setAttribute('data-tags', p.tags.join(','));
            el.innerHTML = `
                <h3>${p.title}</h3>
                <p class="muted">${p.time} · ${p.role}</p>
                <p>${p.summary}</p>
                <div class="tags">${p.tags.map(t=>`<span class="tag">${t}</span>`).join('')}</div>
                <div style="margin-top:10px;display:flex;gap:8px;justify-content:flex-end"><button class="btn small" data-id="${p.id}">查看详情</button></div>
            `;
            container.appendChild(el);
        });

        // 绑定详情按钮
        container.querySelectorAll('button[data-id]').forEach(btn=>{
            btn.addEventListener('click', (e)=>{
                const id = e.currentTarget.getAttribute('data-id');
                const project = list.find(x=>x.id===id);
                openModal(project);
            });
        });
    }

    function openModal(project){
        const modal = document.getElementById('modal');
        const body = document.getElementById('modal-body');
        body.innerHTML = `
            <h2>${project.title}</h2>
            <p class="muted">${project.time} · ${project.role} · ${project.tags.join(' / ')}</p>
            <div style="margin-top:12px">${project.content}</div>
        `;
        modal.setAttribute('aria-hidden','false');
    }

    document.getElementById('modal-close').addEventListener('click', ()=>{
        document.getElementById('modal').setAttribute('aria-hidden','true');
    });

    // 过滤
    document.getElementById('filter-all')?.addEventListener('click', ()=>filterBy('all'));
    document.getElementById('filter-product')?.addEventListener('click', ()=>filterBy('产品'));
    document.getElementById('filter-data')?.addEventListener('click', ()=>filterBy('数据'));
    document.getElementById('filter-op')?.addEventListener('click', ()=>filterBy('运营'));

    function filterBy(tag){
        document.querySelectorAll('.nav-btn').forEach(b=>b.classList.remove('active'));
        document.querySelectorAll('.nav-btn').forEach(b=>{ if(b.textContent.trim()===tag || tag==='all'){} });
        document.querySelectorAll('.project-card').forEach(card=>{
            const tags = card.getAttribute('data-tags');
            if(tag==='all' || tags.includes(tag)){
                card.style.display = '';
            }else{
                card.style.display = 'none';
            }
        });
    }

    // 主题切换
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle && themeToggle.addEventListener('click', ()=>{
        const root = document.documentElement;
        if(root.getAttribute('data-theme')==='dark') root.removeAttribute('data-theme'); else root.setAttribute('data-theme','dark');
    });

    // 图表
    function initCharts(){
        const ctx = document.getElementById('abChart');
        if(ctx){
            new Chart(ctx, {
                type:'line',
                data:{labels:['Week1','Week2','Week3','Week4'],datasets:[{label:'A 组',data:[2.1,2.3,2.6,3.0],borderColor:getComputedStyle(document.documentElement).getPropertyValue('--primary')||'#165DFF',fill:false},{label:'B 组',data:[1.8,2.0,2.5,2.9],borderColor:'#FF9A66',fill:false}]},
                options:{responsive:true,plugins:{legend:{display:true}}}
            });
        }
        const pie = document.getElementById('pieChart');
        if(pie){
            new Chart(pie,{type:'pie',data:{labels:['自然','付费','社媒','推荐'],datasets:[{data:[45,25,15,15],backgroundColor:['#0B5FFF','#66A3FF','#FFB86B','#A6C8FF']}]},options:{responsive:true}});
        }

        document.getElementById('export-chart')?.addEventListener('click', ()=>{
            const a = document.createElement('a');
            a.href = document.getElementById('abChart').toDataURL('image/png');
            a.download = 'ab-test.png';
            a.click();
        });
    }

    // PDF导出功能
    async function exportToPDF() {
        const downloadBtn = document.getElementById('download-resume');
        const originalText = downloadBtn.textContent;
        
        try {
            // 显示加载状态
            downloadBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>正在生成...';
            downloadBtn.disabled = true;

            // 获取页面中需要导出的内容区域
            const resumeContent = document.getElementById('resume-content');
            
            if (!resumeContent) {
                throw new Error('未找到简历内容区域');
            }

            // 使用html2canvas捕获内容
            const canvas = await html2canvas(resumeContent, {
                scale: 2, // 提高导出分辨率
                useCORS: true,
                allowTaint: true,
                backgroundColor: '#FFFFFF',
                logging: false
            });

            // 创建PDF文档
            const imgData = canvas.toDataURL('image/png');
            const pdf = new jspdf.jsPDF({
                orientation: 'portrait',
                unit: 'mm',
                format: 'a4'
            });

            // 计算图片尺寸以适应A4纸张
            const pdfWidth = pdf.internal.pageSize.getWidth();
            const pdfHeight = pdf.internal.pageSize.getHeight();
            const imgWidth = canvas.width;
            const imgHeight = canvas.height;
            const ratio = Math.min(pdfWidth / imgWidth, pdfHeight / imgHeight);
            const imgX = (pdfWidth - imgWidth * ratio) / 2;
            const imgY = 10;

            // 添加图片到PDF
            pdf.addImage(imgData, 'PNG', imgX, imgY, imgWidth * ratio, imgHeight * ratio);

            // 添加页脚
            pdf.setFontSize(10);
            pdf.setTextColor(100, 100, 100);
            pdf.text('简历导出 - 陶诗曼 | 武汉大学 2028届', 10, pdfHeight - 10);

            // 保存PDF
            const fileName = `陶诗曼_简历_${new Date().toISOString().split('T')[0]}.pdf`;
            pdf.save(fileName);

            console.log('PDF导出成功:', fileName);
            
        } catch (error) {
            console.error('PDF导出失败:', error);
            alert(`导出失败: ${error.message}\n\n请尝试刷新页面后重试，或检查浏览器控制台获取详细信息。`);
            
        } finally {
            // 恢复按钮状态
            downloadBtn.innerHTML = originalText;
            downloadBtn.disabled = false;
        }
    }

    // 绑定导出按钮事件
    document.getElementById('download-resume')?.addEventListener('click', exportToPDF);

    // 测试用例：验证导出功能
    function testPDFExport() {
        console.log('=== PDF导出功能测试 ===');
        
        // 测试1: 检查按钮是否存在
        const btn = document.getElementById('download-resume');
        if (btn) {
            console.log('[OK] 导出按钮存在');
        } else {
            console.log('[FAIL] 导出按钮不存在');
            return false;
        }

        // 测试2: 检查html2canvas是否加载
        if (typeof html2canvas !== 'undefined') {
            console.log('[OK] html2canvas 已加载');
        } else {
            console.log('[FAIL] html2canvas 未加载');
            return false;
        }

        // 测试3: 检查jsPDF是否加载
        if (typeof jspdf !== 'undefined') {
            console.log('[OK] jsPDF 已加载');
        } else {
            console.log('[FAIL] jsPDF 未加载');
            return false;
        }

        // 测试4: 检查简历内容区域是否存在
        const content = document.getElementById('resume-content');
        if (content) {
            console.log('[OK] 简历内容区域存在');
        } else {
            console.log('[FAIL] 简历内容区域不存在');
            return false;
        }

        console.log('=== 所有测试通过 ===');
        return true;
    }

    // 启动加载
    loadProjects();

    // 页面加载完成后运行测试
    testPDFExport();

});