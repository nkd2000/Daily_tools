import os
import re

# CONFIGURATION
BASE_DIR = './docs' 
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')

# --- 1. HEAD (Favicon Link) ---
HEAD_TEMPLATE = '<link rel="icon" type="image/svg+xml" href="{rel}assets/img/favicon.svg">'

# --- 2. NAVBAR (Linking the same SVG file) ---
NAV_TEMPLATE = """
<nav class="sticky top-0 z-50 w-full border-b border-white/10 bg-white/70 backdrop-blur-xl saturate-150 no-print transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
            <!-- Left: Logo & Branding -->
            <div class="flex items-center gap-3">
                <a href="{rel}index.html" class="flex items-center gap-3 group">
                    <!-- Ab yahan aapka favicon.svg render hoga -->
                    <div class="relative flex items-center justify-center w-10 h-10 bg-gradient-to-br from-indigo-600 to-violet-600 rounded-xl shadow-lg shadow-indigo-500/30 group-hover:scale-110 group-hover:rotate-3 transition-all duration-300 overflow-hidden p-1.5">
                        <img src="{rel}assets/img/favicon.svg" class="w-full h-full object-contain" alt="Logo">
                    </div>
                    <div class="flex flex-col">
                        <span class="font-black text-xl tracking-tight text-slate-900 leading-none">DailyTools<span class="text-indigo-600">.</span></span>
                        <span class="text-[8px] font-bold text-slate-400 uppercase tracking-[0.2em] mt-1">Smart Utilities</span>
                    </div>
                    <span class="font-bold text-xl tracking-tight text-inherit dark:text-white">Gen Tools</span>
                </a>
            </div>
            <!-- Right: Navigation -->
            <div class="flex items-center gap-6 text-sm font-bold">
                <a href="{rel}index.html" class="text-slate-500 hover:text-indigo-600 transition-all">Home</a>
                <a href="{rel}pages/contact.html" class="text-slate-500 hover:text-indigo-600 transition-all">Contact</a>
                <div class="h-6 w-[1px] bg-slate-200 mx-1"></div>
                <a href="https://github.com/nkd2000" target="_blank" class="w-9 h-9 rounded-xl bg-slate-50 flex items-center justify-center text-slate-400 hover:bg-slate-900 hover:text-white transition-all shadow-sm border border-slate-100">
                    <i class="fa-brands fa-github text-lg"></i>
                </a>
            </div>
        </div>
    </div>
</nav>
"""

# --- 3. FOOTER (Linking the same SVG file) ---
FOOTER_TEMPLATE = """
<footer class="relative bg-[#0f172a] text-gray-300 pt-20 pb-10 overflow-hidden no-print">
    <div class="absolute inset-0 z-0 opacity-[0.03]" style="background-image: radial-gradient(circle at 2px 2px, #4f46e5 1px, transparent 0); background-size: 40px 40px;"></div>
    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-12 mb-16">
            <div class="md:col-span-5">
                <div class="flex items-center gap-3 mb-6">
                    <!-- Footer Logo using favicon.svg -->
                    <div class="w-11 h-11 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-xl shadow-indigo-500/20 p-0">
                        <img src="{rel}assets/img/favicon.svg" class="w-full h-full object-contain" alt="Logo">
                    </div>
                    <span class="font-extrabold text-2xl text-white tracking-tight">Gen Tools<span class="text-indigo-500">.</span></span>
                </div>
                <p class="text-gray-400 text-sm leading-relaxed max-w-md">Helping you simplify complex digital tasks since 2023. Fast, Secure, and 100% Client-Side.</p>
                <div class="flex gap-4 mt-8">
                    <a href="https://github.com/nkd2000" class="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center hover:bg-indigo-600 transition-all"><i class="fa-brands fa-github"></i></a>
                    <a href="#" class="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center hover:bg-blue-400 transition-all"><i class="fa-brands fa-x-twitter"></i></a>
                </div>
            </div>
            <div class="md:col-span-2 md:col-start-7">
                <h4 class="text-white font-bold mb-6 text-sm uppercase tracking-widest">Platform</h4>
                <ul class="space-y-4 text-sm text-gray-400">
                    <li><a href="{rel}index.html" class="hover:text-indigo-400 transition-colors">All Tools</a></li>
                    <li><a href="{rel}pages/privacy.html" class="hover:text-indigo-400 transition-colors">Privacy Policy</a></li>
                    <li><a href="{rel}pages/contact.html" class="hover:text-indigo-400 transition-colors">Contact</a></li>
                </ul>
            </div>
            <div class="md:col-span-4">
                <h4 class="text-white font-bold mb-6 text-sm uppercase tracking-widest">Contribute</h4>
                <div class="p-6 rounded-3xl bg-white/5 border border-white/10 backdrop-blur-md">
                    <p class="text-gray-400 text-xs mb-4 uppercase tracking-tighter">Found a bug or need a feature?</p>
                    <a href="https://github.com/nkd2000/Daily_tools/issues" class="w-full inline-flex items-center justify-center py-3 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm transition-all">Submit Issue</a>
                </div>
            </div>
        </div>
        <div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="flex flex-col md:flex-row items-center gap-4 md:gap-8">
                <p class="text-gray-500 text-sm">&copy; 2025 <span class="text-white font-semibold">Gen Tools Pro</span>.</p>
                <div class="flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/5 border border-emerald-500/20">
                    <span class="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse"></span>
                    <span class="text-[10px] font-bold text-emerald-500 uppercase tracking-tighter">Systems Operational</span>
                </div>
            </div>
            
            <div class="text-gray-500 text-sm font-medium">
                Made with <i class="fa-solid fa-heart text-indigo-500 mx-1"></i> by <span class="text-gray-200">Nkd2000</span>
            </div>
        </div>
    </div>
</footer>
"""

def update_tool_file(file_path, rel_prefix):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.strip(): return

    # .replace() is used to avoid issues with CSS curly braces in Templates
    final_head = HEAD_TEMPLATE.replace("{rel}", rel_prefix)
    final_nav = NAV_TEMPLATE.replace("{rel}", rel_prefix)
    final_footer = FOOTER_TEMPLATE.replace("{rel}", rel_prefix)

    # 1. Update Favicon Link in <head>
    if '<link rel="icon"' in content:
        content = re.sub(r'<link rel="icon".*?>', final_head, content)
    else:
        content = re.sub(r'(</title>)', r'\1\n    ' + final_head, content)

    # 2. Update Navbar
    if '<nav' in content:
        content = re.sub(r'<nav.*?>.*?</nav>', final_nav, content, flags=re.DOTALL)
    else:
        content = re.sub(r'(<body.*?>)', r'\1\n' + final_nav, content)

    # 3. Update Footer
    if '<footer' in content:
        content = re.sub(r'<footer.*?>.*?</footer>', final_footer, content, flags=re.DOTALL)
    else:
        content = re.sub(r'(</body>)', final_footer + r'\n</body>', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def start_automation():
    print("🚀 Syncing Layouts with favicon.svg...")
    count = 0
    for root, dirs, files in os.walk(TOOLS_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                depth = file_path.replace(BASE_DIR, "").count(os.sep) - 1
                rel_prefix = "../" * depth
                try:
                    update_tool_file(file_path, rel_prefix)
                    print(f"✅ Synced: {file}")
                    count += 1
                except Exception as e:
                    print(f"❌ Error in {file}: {e}")
    print(f"\n✨ Done! {count} pages are now using assets/img/favicon.svg")

if __name__ == "__main__":
    start_automation()