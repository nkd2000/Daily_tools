import os
import shutil
import re
import datetime

# --- CONFIGURATION: Categories Mapping ---
categories = {
    "image": [
        "imageCompressor.html", "image_reducer.html", "yt_thumbnail.html", 
        "smart_image_processor.html", "svg_converter.html", "meme_generator.html",
        "color_picker.html", "signature_compressor.html"
    ],
    "pdf": [
        "image_to_pdf.html", "mergePDF.html", "pdf_compressor.html", 
        "passport_maker.html"
    ],
    "utility": [
        "ageCalculator.html", "bmi_calculator.html", "stopwatch.html", 
        "qr_code_generator.html", "password_generator.html", "resume_builder.html",
        "typing_speed_test.html", "screen_recorder.html", "unitConverter.html",
        "word_counter.html", "text_to_speech.html", "speed_test.html"
    ],
    "developer": [
        "code_minifier.html", "json_formatter.html"
    ],
    "finance": [
        "discount_calculator.html", "emi_calculator.html", "invoice_generator.html",
        "sip_calculator.html"
    ],
    "converter": [
        "vfc_to_excel_converter.html"
    ]
}

page_files = ["contact.html", "privacy.html", "about.html", "terms.html", "disclaimer.html"]

# Log File Name
LOG_FILE = "organization_log.txt"

# Helper: Logger
def log(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] [{level}] {message}"
    print(formatted_message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_message + "\n")

# Helper: Convert filename to kebab-case
def to_kebab_case(name):
    base_name, ext = os.path.splitext(name)
    s1 = base_name.replace('_', '-')
    s2 = re.sub(r'(.)([A-Z][a-z]+)', r'\1-\2', s1)
    s3 = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s2)
    return s3.lower() + ext

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log(f"Created directory: {path}")

def update_html_content(content, depth_level=1):
    prefix = "../" * depth_level
    
    # Update Nav Links
    content = re.sub(r'href=["\'](\.\/|\.\.\/)*index\.html["\']', f'href="{prefix}index.html"', content)
    content = re.sub(r'href=["\'](\.\/|\.\.\/)*(pages\/)?contact\.html["\']', f'href="{prefix}pages/contact.html"', content)
    content = re.sub(r'href=["\'](\.\/|\.\.\/)*(pages\/)?privacy\.html["\']', f'href="{prefix}pages/privacy.html"', content)
    content = re.sub(r'href=["\'](\.\/|\.\.\/)*(pages\/)?about\.html["\']', f'href="{prefix}pages/about.html"', content)
    content = re.sub(r'href=["\'](\.\/|\.\.\/)*(pages\/)?terms\.html["\']', f'href="{prefix}pages/terms.html"', content)
    content = re.sub(r'href=["\'](\.\/|\.\.\/)*(pages\/)?disclaimer\.html["\']', f'href="{prefix}pages/disclaimer.html"', content)
    content = re.sub(r'href=["\'](\.\/|\.\.\/)*404\.html["\']', f'href="{prefix}404.html"', content)
    
    return content

def organize_project():
    if os.path.exists(LOG_FILE): os.remove(LOG_FILE)
    log("🚀 Starting Index Fix & Cleanup Process...")
    
    ensure_dir("tools")
    ensure_dir("pages")

    # Read Index Content
    index_content = ""
    if os.path.exists("index.html"):
        with open("index.html", 'r', encoding='utf-8') as f:
            index_content = f.read()

    # -----------------------------
    # 1. PROCESS TOOLS
    # -----------------------------
    log("--- Processing Tools ---")
    
    for category, files in categories.items():
        cat_dir = os.path.join("tools", category)
        ensure_dir(cat_dir)
        
        for old_name in files:
            new_filename = to_kebab_case(old_name)
            dest_path = os.path.join(cat_dir, new_filename)
            
            # Step 1: Move file if needed
            if os.path.exists(dest_path):
                # File is already in the right place
                pass
            else:
                # Find source
                src_path = old_name
                found = False
                if os.path.exists(src_path):
                    found = True
                elif os.path.exists(os.path.join("tools", old_name)):
                    src_path = os.path.join("tools", old_name)
                    found = True
                
                if found:
                    try:
                        # Update content inside the tool
                        with open(src_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        new_content = update_html_content(content, depth_level=2)
                        
                        with open(src_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                            
                        # Move
                        shutil.move(src_path, dest_path)
                        log(f"Moved: {old_name} -> {dest_path}")
                    except Exception as e:
                        log(f"Error processing file {old_name}: {e}", "ERROR")
                        continue
                else:
                    log(f"File not found anywhere: {old_name}", "WARNING")
                    # Even if file is missing, we proceed to update index links if they exist
            
            # Step 2: Update Index Links (ALWAYS RUN THIS)
            target_link = f"tools/{category}/{new_filename}"
            
            # Pattern A: HTML href="oldName.html"
            pattern_html = r'href=["\'](tools\/)?' + re.escape(old_name) + r'["\']'
            if re.search(pattern_html, index_content):
                index_content = re.sub(pattern_html, f'href="{target_link}"', index_content)
                log(f"Updated HTML link for {old_name}")
            
            # Pattern B: JS Object url: 'oldName.html' (Crucial for your dashboard)
            pattern_js = r"url:\s*['\"](tools\/)?(" + re.escape(old_name) + r")['\"]"
            if re.search(pattern_js, index_content):
                index_content = re.sub(pattern_js, f"url: '{target_link}'", index_content)
                log(f"Updated JS data link for {old_name}")

    # -----------------------------
    # 2. PROCESS PAGES
    # -----------------------------
    log("--- Processing Pages ---")
    for page in page_files:
        src_path = page
        if not os.path.exists(src_path):
             if os.path.exists(os.path.join("pages", page)):
                 src_path = os.path.join("pages", page)
             else:
                 log(f"Page not found: {page}", "WARNING")
                 continue

        dest_path = os.path.join("pages", page)
        
        try:
            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = update_html_content(content, depth_level=1)
            
            with open(src_path, 'w', encoding='utf-8') as f:
                f.write(content)

            if os.path.abspath(src_path) != os.path.abspath(dest_path):
                shutil.move(src_path, dest_path)
                log(f"Moved Page: {page} -> pages/{page}")
                
            # Update Index Links
            index_content = re.sub(r'href=["\'](\.\/)?' + re.escape(page) + r'["\']', f'href="pages/{page}"', index_content)
            
        except Exception as e:
            log(f"Error processing page {page}: {e}", "ERROR")

    # -----------------------------
    # 3. SAVE INDEX
    # -----------------------------
    try:
        if os.path.exists("index.html"):
            with open("index.html", 'w', encoding='utf-8') as f:
                f.write(index_content)
            log("Index.html updated successfully.")
    except Exception as e:
        log(f"Failed to save index.html: {e}", "ERROR")

    print(f"\n✅ Fix Complete! Links Updated. Log: {LOG_FILE}")

if __name__ == "__main__":
    organize_project()