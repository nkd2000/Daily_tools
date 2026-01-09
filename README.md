# Daily Tools

A collection of free online tools to make your daily tasks easier. This repository contains various web-based utilities organized into categories for quick access.

## 🚀 Live Demo

Visit the live site at: [https://nkd2000.github.io/Daily_tools/](https://nkd2000.github.io/Daily_tools/)

## 📁 Project Structure

The site is hosted using GitHub Pages from the `docs/` directory. All tools are static HTML pages with no server-side dependencies.

## 🛠️ Available Tools

### Converter Tools
- **VFC to Excel Converter** - Convert VFC files to Excel format

### Developer Tools
- **Code Minifier** - Minify your code for production
- **JSON Formatter** - Format and validate JSON data
- **Text Diff Checker** - Compare text differences

### Finance Tools
- **Discount Calculator** - Calculate discounts and savings
- **EMI Calculator** - Calculate Equated Monthly Installments
- **Invoice Generator** - Generate professional invoices
- **SIP Calculator** - Systematic Investment Plan calculator

### Image Tools
- **Color Picker** - Pick colors from images or palettes
- **Image Compressor** - Compress images to reduce file size
- **Image Converter** - Convert between different image formats
- **Image Reducer** - Reduce image dimensions
- **Meme Generator** - Create custom memes
- **Signature Compressor** - Compress signature images
- **Smart Image Processor** - Advanced image processing
- **SVG Converter** - Convert images to SVG format
- **YouTube Thumbnail** - Generate YouTube thumbnails

### PDF Tools
- **Image to PDF** - Convert images to PDF documents
- **Merge PDF** - Combine multiple PDF files
- **Passport Maker** - Create passport-sized photos
- **PDF Compressor** - Compress PDF file sizes

### Utility Tools
- **Age Calculator** - Calculate age from birth date
- **BMI Calculator** - Calculate Body Mass Index
- **Password Generator** - Generate secure passwords
- **QR Code Generator** - Create QR codes
- **Resume Builder** - Build professional resumes
- **Screen Recorder** - Record your screen
- **Speed Test** - Test internet connection speed
- **Stopwatch** - Digital stopwatch
- **Text to Speech** - Convert text to audio
- **Typing Speed Test** - Test your typing speed
- **Unit Converter** - Convert between different units
- **Voice Recorder** - Record audio
- **Word Counter** - Count words in text

## 🏗️ Setup & Deployment

This project is configured for GitHub Pages deployment:

1. All site files are in the `docs/` directory
2. GitHub Pages serves from the `main` branch → `docs` folder
3. Static HTML only (no PHP or server-side processing)

### Local Development

To run locally:
1. Clone the repository
2. Open any HTML file in your browser directly (no server required)

### Deployment

The site is automatically deployed via GitHub Pages. Any changes pushed to the `main` branch will be reflected on the live site.

## 📝 Notes

- All tools are client-side only, ensuring privacy and speed
- No data is stored or transmitted - everything runs in your browser
- Tools are designed to be lightweight and fast
- Compatible with modern web browsers

## 🤝 Contributing

Feel free to contribute new tools or improve existing ones. All tools should be:
- Static HTML/CSS/JavaScript
- Responsive design
- User-friendly interface
- No external dependencies (CDNs are acceptable)

### Adding New Tools

To maintain design consistency across the project, follow these guidelines when creating new tools:

#### 📁 File Structure
- Place new tool files in the appropriate category folder under `docs/tools/`
- Use kebab-case for filenames: `tool-name.html`
- Example: `docs/tools/utility/new-calculator.html`

#### 🎨 Design Guidelines
- **Framework**: Use Tailwind CSS (already included via CDN)
- **Fonts**: Use Inter font family (Google Fonts, already included)
- **Icons**: Use Font Awesome icons (already included)
- **Color Scheme**: 
  - Primary: Teal (`bg-teal-600`, `text-teal-600`)
  - Background: Light gray (`bg-gray-50`)
  - Text: Dark slate (`text-slate-800`)
  - Cards: White with subtle shadows (`bg-white shadow-sm`)

#### 🧭 Navigation Structure
Include this navigation bar at the top of every tool page:

```html
<nav class="bg-white border-b border-gray-200 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
            <div class="flex items-center gap-3">
                <div class="bg-teal-600 text-white p-2 rounded-lg">
                    <i class="fa-solid fa-tool-icon"></i> <!-- Use appropriate Font Awesome icon -->
                </div>
                <span class="font-bold text-xl tracking-tight text-gray-900">ToolName</span>
            </div>
            <div class="flex items-center gap-6 text-sm font-medium text-gray-500">
                <a href="../../index.html" class="hover:text-teal-600 transition">Home</a>
                <a href="https://jansuchnaforall.blogspot.com" target="_blank" class="hover:text-teal-600 transition">Blog</a>
                <a href="../../pages/contact.html" class="hover:text-teal-600 transition">Contact</a>
            </div>
        </div>
    </div>
</nav>
```

#### 📄 Page Structure
Follow this standard page layout:

1. **Header Section**:
   - Centered title (h1) with description
   - Use responsive text sizing: `text-3xl sm:text-4xl`

2. **Main Content**:
   - Use `max-w-6xl mx-auto px-4 py-8 sm:px-6` for container
   - Grid layout: `grid grid-cols-1 lg:grid-cols-12 gap-8`

3. **Input/Control Panels**:
   - White background cards: `bg-white rounded-lg shadow-sm border border-gray-200`
   - Proper padding: `p-6`
   - Form labels: `text-gray-800 font-semibold mb-4`

4. **Buttons**:
   - Primary: `bg-teal-600 hover:bg-teal-700 text-white font-medium py-2 px-4 rounded-lg`
   - Secondary: `bg-gray-100 hover:bg-gray-200 text-gray-700`

5. **Footer**:
   Include this footer at the bottom:

```html
<footer class="bg-white border-t border-gray-200 mt-auto">
    <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <p class="text-center text-sm text-gray-500">
            &copy; 2023 Free Online Tools. <a href="../../pages/privacy.html" class="text-teal-600 hover:text-teal-500">Privacy Policy</a>
        </p>
    </div>
</footer>
```

#### 🔍 SEO & Meta Tags
Include comprehensive meta tags for better SEO:

```html
<!-- Basic meta tags -->
<meta name="description" content="Brief description of your tool for SEO">
<meta name="keywords" content="relevant, keywords, for, search">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://nkd2000.github.io/Daily_tools/tools/category/tool-name.html">

<!-- Open Graph meta tags -->
<meta property="og:type" content="website">
<meta property="og:title" content="Tool Name | Free Online Tools">
<meta property="og:description" content="Brief description">
<meta property="og:url" content="https://nkd2000.github.io/Daily_tools/tools/category/tool-name.html">
<meta property="og:image" content="https://nkd2000.github.io/Daily_tools/assets/og-default.svg">

<!-- Twitter meta tags -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Tool Name | Free Online Tools">
<meta name="twitter:description" content="Brief description">
```

#### ⚡ Performance & Best Practices
- **Client-side only**: No server-side processing
- **Responsive design**: Test on mobile and desktop
- **Accessibility**: Use proper ARIA labels and semantic HTML
- **Error handling**: Provide user-friendly error messages
- **Loading states**: Show feedback for long-running operations
- **Copy functionality**: Include copy-to-clipboard features where appropriate

#### 📝 JavaScript Guidelines
- Use modern ES6+ syntax
- Wrap code in IIFE: `(function() { ... })();`
- Use `const` and `let` instead of `var`
- Add event listeners properly with `addEventListener`
- Include error handling for user inputs
- Test calculations thoroughly

#### 🔄 Animation & UX
- Use fade-in animations: `fade-in delay-100 delay-200`
- Include hover states for interactive elements
- Provide visual feedback for user actions
- Use smooth transitions: `transition`

#### 📋 Checklist Before Submitting
- [ ] Tool works on mobile and desktop
- [ ] No console errors
- [ ] SEO meta tags are complete
- [ ] Navigation and footer are consistent
- [ ] Color scheme matches project theme
- [ ] Font Awesome icons are used appropriately
- [ ] Code is well-commented
- [ ] Tool description is added to README.md
- [ ] File is placed in correct category folder

#### 📂 Categories
Choose the appropriate category for your tool:
- **converter/**: File format conversions
- **developer/**: Code-related tools
- **finance/**: Financial calculators
- **image/**: Image processing tools
- **pdf/**: PDF manipulation tools
- **utility/**: General utility tools

After creating your tool, update the "Available Tools" section in this README.md with your new tool's information.

## 📄 License

This project is open source. Feel free to use and modify as needed.
