import os
import re

# CONFIGURATION
BASE_DIR = './docs'  # Aapka main folder
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')

# --- YE HAI AAPKA COMMON NAVBAR (Jo har tool mein jayega) ---
# {rel} ki jagah script automatically ../../ daal degi
NAV_TEMPLATE = """
<!-- Universal Glass Header -->
<nav class="sticky top-0 z-50 w-full border-b border-white/10 bg-white/10 backdrop-blur-xl saturate-150 no-print">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
            <!-- Left: Logo -->
            <div class="flex items-center gap-3">
                <a href="{rel}index.html" class="flex items-center gap-3 group">
                    <div class="bg-indigo-600 text-white p-2 rounded-xl shadow-lg group-hover:scale-110 transition-transform">
                        <i class="fa-solid fa-screwdriver-wrench"></i>
                    </div>
                    <span class="font-bold text-xl tracking-tight text-inherit dark:text-white">DailyTools</span>
                </a>
            </div>

            <!-- Right: Navigation -->
            <div class="flex items-center gap-6 text-sm font-semibold">
                <a href="{rel}index.html" class="text-inherit opacity-70 hover:opacity-100 hover:text-indigo-500 transition-all dark:text-white">Home</a>
                <a href="{rel}pages/contact.html" class="text-inherit opacity-70 hover:opacity-100 hover:text-indigo-500 transition-all dark:text-white">Contact</a>
                
                <!-- Github Icon with subtle border -->
                <div class="h-6 w-[1px] bg-gray-300/20 mx-2"></div>
                <a href="https://github.com/nkd2000" class="text-inherit opacity-70 hover:opacity-100 transition-all dark:text-white text-lg">
                    <i class="fa-brands fa-github"></i>
                </a>
            </div>
        </div>
    </div>
</nav>
"""

# --- YE HAI AAPKA COMMON FOOTER ---
FOOTER_TEMPLATE = """
<footer class="relative bg-[#0f172a] text-gray-300 pt-20 pb-10 overflow-hidden no-print">
    <!-- Background Decoration: Subtle Dot Grid & Glow -->
    <div class="absolute inset-0 z-0">
        <div class="absolute inset-0 opacity-[0.03]" style="background-image: radial-gradient(circle at 2px 2px, #4f46e5 1px, transparent 0); background-size: 40px 40px;"></div>
        <div class="absolute -top-24 -left-24 w-96 h-96 bg-indigo-600/10 rounded-full blur-[100px]"></div>
        <div class="absolute -bottom-24 -right-24 w-96 h-96 bg-purple-600/10 rounded-full blur-[100px]"></div>
    </div>

    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-12 mb-16">
            
            <!-- Column 1: Brand & Bio -->
            <div class="md:col-span-5">
                <div class="flex items-center gap-3 mb-6">
                    <div class="w-11 h-11 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-xl shadow-indigo-500/20">
                        <i class="fa-solid fa-screwdriver-wrench text-white text-xl"></i>
                    </div>
                    <span class="font-extrabold text-2xl text-white tracking-tight">DailyTools<span class="text-indigo-500">.</span></span>
                </div>
                <p class="text-gray-400 text-base leading-relaxed max-w-md">
                    The ultimate destination for free, privacy-first web utilities. Helping you simplify complex digital tasks since 2023.
                </p>
                <!-- Social Buttons -->
                <div class="flex gap-4 mt-8">
                    <a href="https://github.com/nkd2000" class="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center hover:bg-indigo-600 hover:border-indigo-600 transition-all duration-300 group">
                        <i class="fa-brands fa-github text-white group-hover:scale-110 transition-transform"></i>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center hover:bg-blue-400 hover:border-blue-400 transition-all duration-300 group">
                        <i class="fa-brands fa-x-twitter text-white group-hover:scale-110 transition-transform"></i>
                    </a>
                </div>
            </div>

            <!-- Column 2: Navigation -->
            <div class="md:col-span-2 md:col-start-7">
                <h4 class="text-white font-bold mb-6 text-sm uppercase tracking-widest">Platform</h4>
                <ul class="space-y-4 text-sm">
                    <li><a href="{rel}index.html" class="text-gray-400 hover:text-indigo-400 transition-colors flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> All Tools</a></li>
                    <li><a href="{rel}pages/contact.html" class="text-gray-400 hover:text-indigo-400 transition-colors flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Contact Us</a></li>
                    <li><a href="{rel}pages/privacy.html" class="text-gray-400 hover:text-indigo-400 transition-colors flex items-center gap-2"><i class="fa-solid fa-chevron-right text-[10px]"></i> Privacy</a></li>
                </ul>
            </div>

            <!-- Column 3: Suggest Tool CTA -->
            <div class="md:col-span-4">
                <h4 class="text-white font-bold mb-6 text-sm uppercase tracking-widest">Contribute</h4>
                <div class="p-6 rounded-2xl bg-gradient-to-br from-white/5 to-transparent border border-white/10 backdrop-blur-md">
                    <p class="text-gray-400 text-sm mb-5">Have an idea for a new tool? Submit your request on GitHub.</p>
                    <a href="https://github.com/nkd2000/Daily_tools/issues" class="flex items-center justify-center gap-2 w-full py-3 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm transition-all shadow-lg shadow-indigo-600/30">
                        <i class="fa-brands fa-github-alt"></i> Request Feature
                    </a>
                </div>
            </div>
        </div>

        <!-- Bottom Bar -->
        <div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="flex flex-col md:flex-row items-center gap-4 md:gap-8">
                <p class="text-gray-500 text-sm">&copy; 2025 <span class="text-white font-semibold">DailyTools Pro</span>.</p>
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
<style>
/* Header text adaptive color logic */
nav .text-inherit {
    color: currentColor; /* Ye apne parent ka color lega */
}

/* Agar tool dark hai toh text white ho jayega automatically */
.dark-theme nav { color: white; border-bottom-color: rgba(255,255,255,0.1); }
.light-theme nav { color: #1e293b; border-bottom-color: rgba(0,0,0,0.05); }

/* Strong blur effect */
.backdrop-blur-xl {
    -webkit-backdrop-filter: blur(24px) saturate(150%);
    backdrop-filter: blur(24px) saturate(150%);
}
</style>
"""

def update_tool_file(file_path, rel_prefix):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Purana <nav> dhundo aur naye se badlo
    new_nav = NAV_TEMPLATE.replace("{rel}", rel_prefix)
    # Ye regex kisi bhi tarah ke <nav> tag ko replace kar dega
    content = re.sub(r'<nav.*?>.*?</nav>', new_nav, content, flags=re.DOTALL)

    # 2. Purana <footer> dhundo aur naye se badlo
    new_footer = FOOTER_TEMPLATE.replace("{rel}", rel_prefix)
    content = re.sub(r'<footer.*?>.*?</footer>', new_footer, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def start_automation():
    print("🚀 Automation Shuru Ho Rahi Hai...")
    
    # Category folders scan karein (image, pdf, dev, etc.)
    for root, dirs, files in os.walk(TOOLS_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                # Check path depth to set correct ../../
                # docs/tools/pdf/passphoto.html -> depth 2 (../../)
                depth = file_path.replace(BASE_DIR, "").count(os.sep) - 1
                rel_prefix = "../" * depth
                
                print(f"Updating: {file} | Depth: {depth}")
                update_tool_file(file_path, rel_prefix)

    print("✅ Sabhi 30+ tools update ho gaye hain!")

if __name__ == "__main__":
    start_automation()