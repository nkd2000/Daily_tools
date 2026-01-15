#!/usr/bin/env node
/**
 * BUILD SCRIPT: Generate tools-data.js from index.html
 * 
 * Usage: node build-tools-data.js
 * 
 * This script:
 * 1. Reads docs/index.html
 * 2. Extracts toolsData array
 * 3. Transforms it to TOOLS_DATABASE format
 * 4. Writes to docs/tools-data.js
 * 
 * Run this after adding new tools to index.html
 */

const fs = require('fs');
const path = require('path');

// Colors for console output
const colors = {
    reset: '\x1b[0m',
    green: '\x1b[32m',
    blue: '\x1b[34m',
    yellow: '\x1b[33m',
    red: '\x1b[31m',
};

function log(color, ...args) {
    console.log(`${color}${args.join(' ')}${colors.reset}`);
}

// Paths
const indexPath = path.join(__dirname, 'docs', 'index.html');
const outputPath = path.join(__dirname, 'docs', 'tools-data.js');

try {
    log(colors.blue, '🔨 Building tools-data.js from index.html...\n');

    // Read index.html
    log(colors.blue, '📖 Reading docs/index.html...');
    const indexContent = fs.readFileSync(indexPath, 'utf8');

    // Extract toolsData array using regex
    const toolsMatch = indexContent.match(/const toolsData = \[([\s\S]*?)\];/);
    if (!toolsMatch) {
        throw new Error('Could not find toolsData array in index.html');
    }

    log(colors.green, '✓ Found toolsData array');

    // Parse the tools
    const toolsText = toolsMatch[1];
    
    // Simple parser for tool objects
    const toolObjects = [];
    const toolRegex = /\{([^}]*)\}/g;
    let match;

    while ((match = toolRegex.exec(toolsText)) !== null) {
        const toolObj = match[1];
        
        // Extract fields
        const catMatch = toolObj.match(/cat:\s*'([^']*)'/) || toolObj.match(/cat:\s*"([^"]*)"/);
        const urlMatch = toolObj.match(/url:\s*'([^']*)'/) || toolObj.match(/url:\s*"([^"]*)"/);
        const iconMatch = toolObj.match(/icon:\s*'([^']*)'/) || toolObj.match(/icon:\s*"([^"]*)"/);
        const titleMatch = toolObj.match(/title:\s*'([^']*)'/) || toolObj.match(/title:\s*"([^"]*)"/);
        const descMatch = toolObj.match(/desc:\s*'([^']*)'/) || toolObj.match(/desc:\s*"([^"]*)"/);

        if (catMatch && urlMatch && titleMatch) {
            // Extract icon without 'fa-solid fa-' prefix
            let icon = iconMatch ? iconMatch[1] : '';
            icon = icon.replace('fa-solid ', '').replace('fa-regular ', '').replace('fa-brands ', '');

            toolObjects.push({
                name: titleMatch[1],
                url: urlMatch[1],
                cat: catMatch[1],
                icon: icon,
                title: titleMatch[1],
                desc: descMatch ? descMatch[1] : ''
            });
        }
    }

    log(colors.green, `✓ Extracted ${toolObjects.length} tools`);

    // Create the output file content
    const headerComment = `/**
 * TOOLS DATABASE - Single Source of Truth
 * AUTO-GENERATED from index.html toolsData
 * 
 * Generated: ${new Date().toISOString()}
 * Total tools: ${toolObjects.length}
 * 
 * ⚠️  DO NOT EDIT MANUALLY - Run: node build-tools-data.js
 * 
 * Instead of editing this file:
 * 1. Update toolsData[] in docs/index.html
 * 2. Run: node build-tools-data.js
 * 3. This file will auto-update
 */

`;

    const toolsCode = 'const TOOLS_DATABASE = [\n';
    const toolsArray = toolObjects.map(tool => {
        return `    {
        name: '${tool.name}',
        url: '${tool.url}',
        cat: '${tool.cat}',
        icon: '${tool.icon}',
        title: '${tool.title}',
        desc: '${tool.desc.replace(/'/g, "\\'")}'
    }`;
    }).join(',\n');

    const closingBracket = '\n];\n\n';

    // Utility functions (same as before)
    const utilityFunctions = `/**
 * Utility Functions for Search & Suggestions
 */

// Simple Fuzzy Match (tolerates typos)
function fuzzyMatch(searchTerm, text) {
    let searchIdx = 0;
    for (let i = 0; i < text.length; i++) {
        if (searchTerm[searchIdx]?.toLowerCase() === text[i].toLowerCase()) {
            searchIdx++;
            if (searchIdx === searchTerm.length) return true;
        }
    }
    return false;
}

// Levenshtein Distance for typo detection
function levenshteinDistance(str1, str2) {
    const len1 = str1.length;
    const len2 = str2.length;
    const matrix = Array(len2 + 1).fill(null).map(() => Array(len1 + 1).fill(0));
    
    for (let i = 0; i <= len1; i++) matrix[0][i] = i;
    for (let j = 0; j <= len2; j++) matrix[j][0] = j;
    
    for (let j = 1; j <= len2; j++) {
        for (let i = 1; i <= len1; i++) {
            const indicator = str1[i - 1] === str2[j - 1] ? 0 : 1;
            matrix[j][i] = Math.min(
                matrix[j][i - 1] + 1,
                matrix[j - 1][i] + 1,
                matrix[j - 1][i - 1] + indicator
            );
        }
    }
    return matrix[len2][len1];
}

// Search with fuzzy matching
function searchTools(query) {
    if (!query || query.length === 0) return [];
    
    const q = query.toLowerCase();
    
    // Exact & partial matches (higher priority)
    const exactMatches = TOOLS_DATABASE.filter(tool => 
        tool.name.toLowerCase().includes(q) ||
        tool.desc.toLowerCase().includes(q) ||
        tool.cat.toLowerCase().includes(q)
    );
    
    // Fuzzy matches (if few exact matches)
    if (exactMatches.length < 3) {
        const fuzzyMatches = TOOLS_DATABASE.filter(tool =>
            !exactMatches.includes(tool) && fuzzyMatch(q, tool.name)
        );
        return [...exactMatches, ...fuzzyMatches];
    }
    
    return exactMatches;
}

// Get tool suggestions based on category
function getToolsByCategory(category) {
    return TOOLS_DATABASE.filter(tool => tool.cat.toLowerCase() === category.toLowerCase());
}

// Get similar tools (by category or name similarity)
function getSimilarTools(toolName, limit = 3) {
    const tool = TOOLS_DATABASE.find(t => t.name.toLowerCase() === toolName.toLowerCase());
    if (!tool) return [];
    
    const similar = TOOLS_DATABASE.filter(t => 
        t.cat === tool.cat && t.name !== tool.name
    );
    return similar.slice(0, limit);
}

// Get all categories
function getAllCategories() {
    const categories = [...new Set(TOOLS_DATABASE.map(t => t.cat))];
    return categories.sort();
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { TOOLS_DATABASE, searchTools, getToolsByCategory, getSimilarTools, getAllCategories };
}
`;

    const fullContent = headerComment + toolsCode + toolsArray + closingBracket + utilityFunctions;

    // Write to file
    fs.writeFileSync(outputPath, fullContent, 'utf8');
    log(colors.green, `✓ Generated tools-data.js (${toolObjects.length} tools)\n`);

    // Statistics
    log(colors.yellow, '📊 STATISTICS:');
    const categories = {};
    toolObjects.forEach(tool => {
        categories[tool.cat] = (categories[tool.cat] || 0) + 1;
    });

    Object.entries(categories).sort().forEach(([cat, count]) => {
        log(colors.yellow, `   ${cat}: ${count} tools`);
    });

    log(colors.green, `\n✅ SUCCESS! Generated ${outputPath}`);
    log(colors.green, `\n📝 Next steps:`);
    log(colors.blue, `   1. Review the generated file`);
    log(colors.blue, `   2. Commit to git`);
    log(colors.blue, `   3. Test the 404 page`);
    log(colors.blue, `\n⚠️  Remember: Always run this script after adding new tools to index.html\n`);

} catch (error) {
    log(colors.red, `\n❌ ERROR: ${error.message}\n`);
    process.exit(1);
}
