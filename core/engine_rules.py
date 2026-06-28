def get_geo_master_matrix():
    return {
        "Section 1: Crawl Access & AI Bot Permissions": [
            {
                "id": "1.1",
                "metric": "Explicit Allow rules in robots.txt for 15 AI agents",
                "status": "Fail",
                "tool": "VS Code Editor / Terminal Curl Engine",
                "impact": "Silent permission is not enough for conservative citation engines that interpret ambiguous missing rules as an implicit site block.",
                "steps": [
                    "Open your root directory robots.txt file inside your workspace code editor.",
                    "Append explicit User-agent declarations for the 15 leading AI agents: GPTBot, OAI-SearchBot, ChatGPT-User, anthropic-ai, ClaudeBot, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, Google-Extended, Gemini-User, YouBot, Meta-ExternalAgent, Meta-ExternalFetcher, and Applebot-Extended.",
                    "Add an explicit 'Allow: /' token immediately below each user-agent block configuration.",
                    "Save modifications and deploy the updated robots.txt file directly to your production site root."
                ],
                "verify": "Execute a terminal curl command: 'curl -A \"OAI-SearchBot\" https://www.koinx.com/robots.txt' and verify the routing paths return an explicit Allow token."
            },
            {
                "id": "1.2",
                "metric": "Secondary crawlers acknowledged explicitly (Bytespider, CCBot)",
                "status": "Pass",
                "tool": "Linux Grep Core / Robots Parser",
                "impact": "Decide explicitly whether to allow or deny secondary data blocks like Common Crawl (CCBot) and ByteDance (Bytespider) that feed downstream AI models.",
                "steps": [
                    "Audit server traffic logs to trace inbound requests from secondary data blocks.",
                    "Configure dedicated directives within your routing tables to regulate access without triggering resource fatigue."
                ],
                "verify": "Review the live robots.txt live web response directly to confirm your system explicitly declares permissions for 'User-agent: Bytespider' and 'User-agent: CCBot'."
            },
            {
                "id": "1.3",
                "metric": "No conflicting Edge-level Cloudflare AI Scraper Toggle",
                "status": "Fail",
                "tool": "Cloudflare Edge WAF Dashboard / API API",
                "impact": "The 'Block AI Scrapers and Crawlers' switch in Cloudflare completely overrides robots.txt rules, blocking bots before they can read site paths.",
                "steps": [
                    "Log into the administrative Cloudflare console for KoinX.",
                    "Navigate directly to Security -> Bots via the sidebar navigation index.",
                    "Locate the global toggle switch labeled 'Block AI Scrapers and Crawlers'.",
                    "Turn off this option to ensure edge-level rules defer access logic to your custom robots.txt file instead."
                ],
                "verify": "Review edge traffic distribution graphs to ensure valid automated crawler request streams are no longer returning 403 Forbidden codes."
            },
            {
                "id": "1.4",
                "metric": "No CAPTCHA or Bot Fight Mode challenges on content URLs",
                "status": "Pass",
                "tool": "Screaming Frog SEO Spider / Cloudflare Page Rules",
                "impact": "AI crawlers fail interactive challenges and quietly leave. Reserve protections for forms and administrative paths only.",
                "steps": [
                    "Isolate secure transactional pages from public informational pathways.",
                    "Configure Cloudflare Page Rules to completely bypass Bot Fight Mode across content directories."
                ],
                "verify": "Run an automated crawl over content paths using non-standard web client strings to ensure pages resolve directly with a clean HTTP status 200 without throwing an intermediate challenge wall."
            },
            {
                "id": "1.5",
                "metric": "Server access log verification confirms real AI crawler hits",
                "status": "Fail",
                "tool": "DataDog / Logstash Logs / AWS CloudWatch Console",
                "impact": "Grep access logs for user-agent strings over a 30-day window. Zero hits means your configured rules are purely theoretical.",
                "steps": [
                    "Access your production environment access logs via your central dashboard console.",
                    "Execute an explicit filter string targeting active search crawlers: 'grep -Ei \"(gptbot|perplexitybot|claude-searchbot)\" /var/log/nginx/access.log'.",
                    "Analyze request frequencies over a rolling 30-day monitoring window.",
                    "Set up automated tracking alerts to notify technical teams if verified crawler traffic falls to zero over any 72-hour period."
                ],
                "verify": "Query your central logging infrastructure data to confirm real-time user-agent hits from 'OAI-SearchBot' or 'PerplexityBot' are actively populating metrics dashboards."
            },
            {
                "id": "1.6",
                "metric": "No JavaScript-only rendering gates on canonical content paths",
                "status": "Pass",
                "tool": "Screaming Frog SEO Spider Rendering Engine",
                "impact": "Some AI crawlers do not execute JavaScript or execute it on a heavy delay. Core content must load instantly in the initial HTML response.",
                "steps": [
                    "Deactivate JavaScript execution within a local sandbox testing browser view.",
                    "Load key compliance documentation pages to check content rendering behavior."
                ],
                "verify": "Inspect the raw page source code string to confirm that high-value compliance explanations are fully readable within the server-delivered HTML payload."
            },
            {
                "id": "1.7",
                "metric": "XML Sitemap declared explicitly inside robots.txt and reachable",
                "status": "Pass",
                "tool": "Sitemap Engine Parser / W3C XML Validator",
                "impact": "A clean Sitemap directive is the secondary route AI crawlers use to discover canonical URLs. Validate that the XML returns 200 and lists every page that matters.",
                "steps": [
                    "Open your robots.txt file in the workspace editor interface.",
                    "Append a clean absolute link reference at the bottom: 'Sitemap: https://www.koinx.com/in/sitemap.xml'."
                ],
                "verify": "Run a curl validation pass against the sitemap endpoint to verify it delivers a valid, error-free xml structure containing your full index of canonical URLs."
            },
            {
                "id": "1.8",
                "metric": "No legacy or stale noindex directives on canonical pages",
                "status": "Pass",
                "tool": "Screaming Frog / Link Audit Engine",
                "impact": "Stale meta robots noindex tags on high-value landing paths will silently drop your pages from AI retrieval systems.",
                "steps": [
                    "Run a comprehensive crawl across all active target directories.",
                    "Filter the results to check for any active meta robots tags set to 'noindex' or 'nosnippet' states."
                ],
                "verify": "Review site crawls to ensure metadata headers display clean 'index, follow' directives across your high-intent entry nodes."
            }
        ],
        "Section 2: llms.txt & llms-full.txt Specifications": [
            {
                "id": "2.1",
                "metric": "llms.txt file exists precisely at the site root path",
                "status": "Fail",
                "tool": "Terminal Curl Engine / VS Code Editor",
                "impact": "The URL must be /llms.txt exactly. Subdirectories or alternate naming patterns will not be discovered by automated system parsers.",
                "steps": [
                    "Create a plain markdown file named exactly 'llms.txt' within your production root folder directory.",
                    "Add a clean Markdown layout starting with a single H1 site title, followed by a brief blockquote summary of the platform's core compliance features.",
                    "Save and deploy the asset so it resolves exactly at https://www.koinx.com/llms.txt."
                ],
                "verify": "Execute 'curl -I https://www.koinx.com/llms.txt' to verify that the file returns a clean, active status 200 response."
            },
            {
                "id": "2.2",
                "metric": "llms-full.txt companion file exists at the site root",
                "status": "Fail",
                "tool": "Markdown Compiler Engine / Webpack Build Pipeline",
                "impact": "Provides single-fetch crawlers with a consolidated document containing your entire structured content layer, completely stripping out header and footer noise.",
                "steps": [
                    "Create a file named 'llms-full.txt' at your project root directory path.",
                    "Set up automated build scripts to compile your text content into this single asset whenever updates are made to your production site.",
                    "Verify the file is served from your root folder without any redirect chains."
                ],
                "verify": "Confirm the server responds correctly to direct network queries targeting the /llms-full.txt endpoint."
            },
            {
                "id": "2.3",
                "metric": "Correct MIME type configurations served by target web server",
                "status": "Fail",
                "tool": "Network DevTools Console / Nginx Config",
                "impact": "Both files must be served explicitly as text/markdown or text/plain with UTF-8 encoding. Standard HTML page responses break the system contract.",
                "steps": [
                    "Open your server configuration files (e.g., Nginx, Apache, or edge server routing parameters).",
                    "Add custom rules to explicitly map text/markdown header extensions.",
                    "Verify the server response explicitly includes 'Content-Type: text/markdown; charset=utf-8'."
                ],
                "verify": "Inspect the network response headers inside your browser development console to confirm the content type maps correctly."
            },
            {
                "id": "2.4",
                "metric": "ASCII-clean content syntax layout inside text formats",
                "status": "Fail",
                "tool": "Python RegEx Parser Module / Linter Tools",
                "impact": "Curly quotes, em-dashes, and other smart-typography characters cause tokenization issues across multiple AI models. Stick to plain ASCII or simple UTF-8 strings.",
                "steps": [
                    "Scan your markdown documentation files using string sanitization routines.",
                    "Replace smart curly quotes with basic straight quotes and convert em-dashes into standard single hyphen formats."
                ],
                "verify": "Run an automated typography check to confirm your target markdown files consist exclusively of clean ASCII characters."
            },
            {
                "id": "2.5",
                "metric": "Structure precisely matches the official llms.txt schema spec",
                "status": "Fail",
                "tool": "VS Code Editor Markdown Linter",
                "impact": "Requires an H1 site name, one blockquote summary, then H2 sections of Markdown links with a one-sentence description after the colon on each line. Optional content goes under a ## Optional H2.",
                "steps": [
                    "Open your /llms.txt file inside your editor tool setup.",
                    "Refactor the document hierarchy to use exactly one H1 tag, a single blockquote block, followed by structured H2 sections.",
                    "Verify that link sub-elements use the required syntax format: '- [Link Title](URL): Brief descriptive definition string here.'"
                ],
                "verify": "Review the file structure to ensure it matches current markdown content formatting guidelines."
            },
            {
                "id": "2.6",
                "metric": "Freshness timestamp updated inside context text block",
                "status": "Fail",
                "tool": "Git Commit Webhooks / GitHub Actions Workflow",
                "impact": "A 'Last updated: YYYY-MM-DD' line at the top tells AI systems the document is maintained. Bump it whenever the site adds material content.",
                "steps": [
                    "Insert a clear 'Last Updated: YYYY-MM-DD' timestamp at the top of your markdown files.",
                    "Configure automated scripts within your build workflows to update this timestamp whenever changes are committed."
                ],
                "verify": "Check file outputs to ensure the header layer reflects live file modification timestamps."
            },
            {
                "id": "2.7",
                "metric": "robots.txt explicitly references both markdown asset paths",
                "status": "Fail",
                "tool": "Sitemap Engine Parser Core",
                "impact": "Adding 'Sitemap: /llms.txt' and 'Sitemap: /llms-full.txt' directives makes the files discoverable by crawlers that do not check the root path automatically.",
                "steps": [
                    "Open your robots.txt file inside your workspace editor.",
                    "Append explicit sitemap directives pointing directly to your markdown paths: 'Sitemap: https://www.koinx.com/llms.txt'.",
                    "Append a second sitemap directive line pointing directly to your /llms-full.txt endpoint."
                ],
                "verify": "Read the file directly to ensure your sitemap references match active production endpoints."
            }
        ],
        "Section 3: Content Extractability & Vector Alignment": [
            {
                "id": "3.1",
                "metric": "Direct-answer paragraph within the first 200 words",
                "status": "Pass",
                "tool": "Hemingway Editor Framework / Custom Text Parser",
                "impact": "Every page targeting a specific question must answer it explicitly within the first viewport. Inverted-pyramid structures mirror how AI systems extract text.",
                "steps": [
                    "Structure content using an inverted pyramid approach across all educational paths.",
                    "Place clear, direct regulatory answers right in the introductory paragraph before expanding into granular technical details."
                ],
                "verify": "Verify the opening paragraph of each high-intent page answers the primary topic question completely within a 200-word limit."
            },
            {
                "id": "3.2",
                "metric": "Single-fact assertions for high impact statements",
                "status": "Pass",
                "tool": "Internal Content Audit Team Core",
                "impact": "Concrete assertions like 'improves by 23%' are highly extractable. Vague phrasing like 'has become quite significant recently' will not be indexed as factual data.",
                "steps": [
                    "Audit marketing copy to remove ambiguous language.",
                    "Convert generic descriptions into data-driven statements containing verified tax figures and explicit legal codes."
                ],
                "verify": "Ensure core regulatory updates use precise definitions like 'Section 115BBH defines a flat 30% tax rate on virtual asset gains'."
            },
            {
                "id": "3.3",
                "metric": "Semantic HTML5 structural architecture deployed",
                "status": "Pass",
                "tool": "W3C Validation Engine / Google Lighthouse Studio",
                "impact": "Using semantic tags like article, section, aside, and nav gives AI parsers a clean navigation map to understand page context.",
                "steps": [
                    "Refactor theme templates to wrap main editorial content sections within semantic <article> tags.",
                    "Use structural <section> layout breaks and maintain a clean header hierarchy from H1 down through consecutive subheaders."
                ],
                "verify": "Run automated accessibility checks to confirm your layout components adhere to modern semantic standards."
            },
            {
                "id": "3.4",
                "metric": "FAQ blocks closely match raw user prompt syntax",
                "status": "Pass",
                "tool": "Google Search Console API / Prompt Analyser",
                "impact": "Write FAQ questions in the exact phrasing a user would type into ChatGPT. Answer in a single, complete paragraph below each question.",
                "steps": [
                    "Extract common question formats from user search analytics.",
                    "Format FAQ headers using natural, conversational language like 'How do I report crypto staking returns under Indian tax law?'."
                ],
                "verify": "Ensure question formats precisely replicate query patterns discovered across search consoles."
            },
            {
                "id": "3.5",
                "metric": "Numbered lists deployed for operational stepwise setups",
                "status": "Pass",
                "tool": "Structured Content Markup Parser",
                "impact": "AI systems process list-structured content into procedural summaries with significantly higher fidelity.",
                "steps": [
                    "Convert multi-step tutorial writeups into ordered HTML <ol> list containers.",
                    "Ensure each step begins with a clear, actionable statement describing the necessary action."
                ],
                "verify": "Check that complex procedural guides render inside clear, consecutive list formats."
            },
            {
                "id": "3.6",
                "metric": "HTML Tables utilized for data comparative elements",
                "status": "Pass",
                "tool": "Rich Snippets Dev Studio / HTML DOM Checker",
                "impact": "Tabular data is highly retrievable by AI engines and rarely appears on pages relying purely on prose. Image screenshots of tables cannot be read.",
                "steps": [
                    "Replace static image tables with clean, responsive HTML <table> elements.",
                    "Use appropriate header tags (`<th>`) and explicit cell containers (`<td>`) to map complex comparisons."
                ],
                "verify": "Confirm data layouts remain fully copy-pasteable as text strings directly from your live pages."
            },
            {
                "id": "3.7",
                "metric": "Speakable CSS selectors declared on page templates",
                "status": "Fail",
                "tool": "Schema Markup Core Lab / JSON-LD Compiler",
                "impact": "The speakable property inside Article schema points AI systems and voice surfaces directly at the specific snippets worth reading aloud.",
                "steps": [
                    "Open your primary JSON-LD site generation configuration template.",
                    "Inject an explicit 'speakable' property wrapper target block within your central Article schema metadata architecture.",
                    "Set the target cssSelector path parameters to map precisely to your high-value definitions blocks: 'cssSelector': ['article h2', 'article h2 + p']."
                ],
                "verify": "Run your live URL through a schema validation console to verify the speakable cssSelector paths point directly to your primary content containers."
            },
            {
                "id": "3.8",
                "metric": "No critical business or tax metrics locked inside images",
                "status": "Pass",
                "tool": "Accessibility Inspector Core Suite",
                "impact": "Pricing, definitions, and headline claims in image form are invisible to most AI parsers. Alt text helps but cannot substitute for extractable HTML.",
                "steps": [
                    "Audit promotional content to move metrics out of image assets and into native text overlays backed by detailed alternative text descriptions."
                ],
                "verify": "Temporarily toggle image visibility off within test profiles to ensure all relevant information remains readable."
            },
            {
                "id": "3.9",
                "metric": "No client-side-only rendered text frameworks active",
                "status": "Pass",
                "tool": "Accessibility Inspector Core Suite",
                "impact": "If a page returns an empty div in the initial HTML and populates it via JS, AI crawlers that skip JS see absolutely nothing.",
                "steps": [
                    "Deploy server-side rendering architecture for calculation landing paths to deliver complete content models on initial requests."
                ],
                "verify": "Verify initial page loads deliver full text components before running client-side hydration scripts."
            }
        ],
        "Section 4: Structured Data & Entity Graph Matrix": [
            {
                "id": "4.1",
                "metric": "Organization profile initialized with unique @id",
                "status": "Pass",
                "tool": "Google Rich Results Testing Matrix",
                "impact": "One Org entity, one canonical @id referenced sitewide. Fragmented Org IDs dilute your entity signal across the web.",
                "steps": [
                    "Define a unified identifier tag across your schema objects: 'https://www.koinx.com/in/#organization'.",
                    "Ensure all editorial paths reference this central identifier node."
                ],
                "verify": "Validate the JSON-LD payload to confirm your organization entry includes a sameAs array linking your Wikidata profile, Google Business CID, and social indices."
            },
            {
                "id": "4.2",
                "metric": "Article schema injected across editorial pages",
                "status": "Pass",
                "tool": "Schema Markup Validator Core",
                "impact": "Requires headline, description, publication/modification dates, author, and keywords. This data helps search models calculate content recency and authority.",
                "steps": [
                    "Configure automated functions to inject detailed Article metadata scripts across all informational paths, defining modification fields and proper author attribution links."
                ],
                "verify": "Confirm generated scripts pass validation checks with zero warning flags."
            },
            {
                "id": "4.3",
                "metric": "FAQPage schema active matching user visible values",
                "status": "Pass",
                "tool": "Rich Result Engine Testing Suite",
                "impact": "Map each visible FAQ item to a structured Question entity. Hidden schema text with no visible counterpart poses a severe manual action risk.",
                "steps": [
                    "Generate FAQPage schema scripts that map to your visible page questions.",
                    "Verify the script values precisely mirror user-facing page elements."
                ],
                "verify": "Confirm validation tests register active, fully formatted FAQ entities."
            },
            {
                "id": "4.4",
                "metric": "HowTo schema deployed on procedural guidelines",
                "status": "Fail",
                "tool": "JSON-LD Validator Engine Core",
                "impact": "Audit guides and step-by-step playbooks deserve structured HowTo entries pointing directly at clear heading anchors via distinct sub-URLs.",
                "steps": [
                    "Access your tutorial layout code files.",
                    "Build a dynamic JSON-LD parser that generates '@type': 'HowTo' for procedural content blocks.",
                    "Map out distinct 'step' elements inside the array, assigning unique sub-URL fragment hash targets (e.g., 'url': 'https://www.koinx.com/guide#step1') to each procedural block."
                ],
                "verify": "Validate code snippets to confirm that multi-step instructions register as structured procedural nodes."
            },
            {
                "id": "4.5",
                "metric": "BreadcrumbList elements deployed sitewide",
                "status": "Pass",
                "tool": "Schema Linter Stack Tools",
                "impact": "AI systems use breadcrumbs to reconstruct site taxonomy when navigation elements are heavily dependent on complex JavaScript layouts.",
                "steps": [
                    "Integrate structured BreadcrumbList tracking metadata models into your universal template design."
                ],
                "verify": "Confirm code outputs accurately reflect breadcrumb hierarchy data across all site locations."
            },
            {
                "id": "4.6",
                "metric": "Service plus Offer on commercial pages",
                "status": "Fail",
                "tool": "Enterprise Schema Studio Module",
                "impact": "Service schema with nested Offer details containing price range, currency, and availability signals concreteness that AI systems weight heavily.",
                "steps": [
                    "Open your commercial landing page files inside your editor workspace.",
                    "Inject a detailed '@type': 'Service' data structure into the page code template.",
                    "Nest an explicit 'offers' object within the service structure, defining explicit fields for 'priceRange', 'priceCurrency': 'INR', and 'availability': 'https://schema.org/InStock'."
                ],
                "verify": "Check structural script records to confirm product offering arrays display explicit price classification parameters."
            },
            {
                "id": "4.7",
                "metric": "Person schema linked to real author bio records",
                "status": "Pass",
                "tool": "Wikidata Engine Integration Portal",
                "impact": "Author bylines deserve a real Person entity with jobTitle, worksFor, and sameAs links pointing to verified external public profiles.",
                "steps": [
                    "Configure author attribution fields to pull from detailed biographical records, populating professional fields and external identity links."
                ],
                "verify": "Confirm author profile objects return clean validation connections without structural errors."
            },
            {
                "id": "4.8",
                "metric": "Validation checks confirm zero warning blocks",
                "status": "Pass",
                "tool": "Schema.org Official Tracker Portal",
                "impact": "Ensures structural data remains clean and fully legible to search engines over continuous deployment cycles.",
                "steps": [
                    "Integrate schema regression tests into build workflows to automatically flag syntax errors before changes reach production environments."
                ],
                "verify": "Confirm testing suites generate clear validation scores across all monitored schema templates."
            }
        ],
        "Section 5: Domain Authority & Citation Signals": [
            {
                "id": "5.1",
                "metric": "Bylined individual profiles with deep author bios",
                "status": "Pass",
                "tool": "Internal Content Database Console",
                "impact": "Every editorial post must be bylined by a specific person, linking to a populated profile page. Generic 'Team' or 'Admin' attributions measurably underperform.",
                "steps": [
                    "Link article bylines directly to detailed bio pages that outline the writer's professional certifications and experience."
                ],
                "verify": "Check that all informational paths reference dedicated, individual author profiles."
            },
            {
                "id": "5.2",
                "metric": "Wikidata entity configured with dual binding links",
                "status": "Fail",
                "tool": "Wikidata Query Interface Matrix",
                "impact": "A Wikidata entry is the strongest entity-disambiguation signal available. Declare your Wikidata link in Organization.sameAs, and link back to your site from Wikidata.",
                "steps": [
                    "Navigate to the official Wikidata entry created for your organization entity.",
                    "Add an explicit 'official website' statement pointing directly to your primary domain URL.",
                    "Open your local site code metadata and verify your 'sameAs' profile array contains the exact matching corporate Wikidata entity URI string."
                ],
                "verify": "Run query checks to confirm that entity profiles resolve semantic connections in both directions."
            },
            {
                "id": "5.3",
                "metric": "Google Business Profile configured for local relevance",
                "status": "Pass",
                "tool": "GBP Dashboard Console Interface",
                "impact": "Ensures local categorization parameters match sitewide references exactly to establish localized authority hooks.",
                "steps": [
                    "Keep corporate contact records, office addresses, and support availability hours completely consistent with details on your core landing pages."
                ],
                "verify": "Ensure core business metrics match identically across both third-party map records and your native contact footers."
            },
            {
                "id": "5.4",
                "metric": "Third-party platform data aligned (G2, Clutch, Trustpilot)",
                "status": "Pass",
                "tool": "Brand Reputation Indexer Matrix Hub",
                "impact": "AI systems resolve ambiguity by completely ignoring inconsistent sources. Ensure identical name, address, phone, and offering descriptions across external hubs.",
                "steps": [
                    "Audit company profile text across review hubs to remove inconsistent descriptions and eliminate mismatched profile metrics."
                ],
                "verify": "Confirm corporate operational details are completely uniform across all tracked external platforms."
            },
            {
                "id": "5.5",
                "metric": "Factual reference vectors linked directly inline",
                "status": "Pass",
                "tool": "Link Analysis System Engine Tools",
                "impact": "Numbers and benchmarks linked to authoritative sources via real anchor tags achieve 30% higher citation rates in independent GEO studies.",
                "steps": [
                    "Review informational articles to link statistical assertions and tax rules directly to official legislative portals using descriptive anchor text."
                ],
                "verify": "Verify external hyperlinks resolve cleanly to trusted regulatory sources with status 200 response codes."
            },
            {
                "id": "5.6",
                "metric": "Proprietary research or survey models published",
                "status": "Pass",
                "tool": "Data Analysis Platform Logs Base",
                "impact": "Original numbers and metrics are the single most citeable content category because they cannot be sourced anywhere else on the web.",
                "steps": [
                    "Anonymize, process, and publish transactional trends and compliance statistics to serve as primary citation targets for research engines."
                ],
                "verify": "Confirm these research assets map to distinct, indexable endpoints that search engines can easily crawl."
            }
        ],
        "Section 6: Freshness Vectors & Conversion Design": [
            {
                "id": "6.1",
                "metric": "article:modified_time OpenGraph meta tags active",
                "status": "Pass",
                "tool": "Facebook Sharing Debugger Core Engine",
                "impact": "Pages updated within the last sixty days earn roughly 28% more AI citations. Models read the article:modified_time property directly.",
                "steps": [
                    "Update CMS templates to dynamically output the exact date modification values into your open graph metadata tags."
                ],
                "verify": "Verify page headers explicitly return an '<meta property=\"article:modified_time\" content=\"YYYY-MM-DD...\" />' block matching current code updates."
            },
            {
                "id": "6.2",
                "metric": "Schema time vectors align with frontend design timestamps",
                "status": "Pass",
                "tool": "Screaming Frog Meta Scraper Interface",
                "impact": "Both schema dateModified and user-facing timestamps must reflect real edits, not build-pipeline auto-bumps. Date-faking is detected and discounted.",
                "steps": [
                    "Verify your automated layout templates update page-visible timestamps whenever data modification parameters change inside your core system records."
                ],
                "verify": "Audit target pages to confirm that user-visible update indicators and hidden metadata records align perfectly."
            },
            {
                "id": "6.3",
                "metric": "UTM traffic parameter mapping applied for AI referrers",
                "status": "Fail",
                "tool": "Google Analytics 4 / JavaScript Session Trackers",
                "impact": "Capture document.referrer on form submissions to tag lead attribution with chatgpt.com or perplexity.ai. Otherwise, CRMs lump AI traffic into generic 'Direct' pools.",
                "steps": [
                    "Open your main application form submission controller script file.",
                    "Inject a custom JavaScript tracker block to capture the inbound referral string: 'const refSource = document.referrer;'.",
                    "Add conditional logic checking if 'refSource' contains 'chatgpt.com', 'perplexity.ai', or 'claude.ai'.",
                    "Map these extracted values into a hidden UTM form field to accurately pass the channel origin data into your database tools."
                ],
                "verify": "Test form submission logic to ensure referral attributes map correctly into your analytics platform."
            },
            {
                "id": "6.4",
                "metric": "Conversion layouts positioned above fold regions prominently",
                "status": "Pass",
                "tool": "Hotjar User Session Heatmaps Portal",
                "impact": "AI-referred users typically arrive deeper in the consideration funnel. Placing calculators and CTAs above the fold captures this low-friction intent instantly.",
                "steps": [
                    "Position interactive tax input widgets clearly at the top of landing pathways, removing unnecessary conversion steps."
                ],
                "verify": "Review interface sessions to confirm call-to-action features load prominently in initial viewport displays."
            },
            {
                "id": "6.5",
                "metric": "Dynamic sitemap lastmod parameters accurate and updated",
                "status": "Pass",
                "tool": "Sitemap Engine Hydrator Tool Hub",
                "impact": "Accurate lastmod dates alert crawlers to fresh content updates, reinforcing your meta freshness signals.",
                "steps": [
                    "Configure sitemap generators to update date elements immediately whenever data fields change within database systems."
                ],
                "verify": "Examine sitemap files to confirm formatting elements display accurate update records."
            }
        ],
        "Section 7: Automated Monitoring & Metrics Tracking": [
            {
                "id": "7.1",
                "metric": "Google Search Console long-tail fan-out query parsing",
                "status": "Fail",
                "tool": "GSC Query Filter Console Dashboard View",
                "impact": "Filter GSC data for queries above 10 words containing exclusions like '-site:'. These indicate machine-generated queries, confirming your site is being retrieved.",
                "steps": [
                    "Log into your centralized Google Search Console interface dashboard.",
                    "Navigate directly to the Performance report metrics grid.",
                    "Apply a custom regex search filter to isolate long queries: '^([^ ]+ ){10,}[^ ]+$'.",
                    "Look for search chains containing boolean exclusions to uncover machine-generated fan-out query profiles."
                ],
                "verify": "Confirm detailed query strings isolate properly inside analytics tracking setups."
            },
            {
                "id": "7.2",
                "metric": "AI tracking services connected to platform logs active",
                "status": "Fail",
                "tool": "Peec AI / Otterly / Profound API Tracking Core",
                "impact": "Subscribing to programmatic tracking tools provides an accurate share-of-voice metric across specific prompt lists and models.",
                "steps": [
                    "Establish a corporate monitoring subscription with an AI visibility tracking service.",
                    "Input your core technical keyword and prompt matrices into the service configuration engine.",
                    "Link the tracking service's data webhooks to stream metrics back to your team's tracking boards."
                ],
                "verify": "Confirm visibility analytics metrics stream properly into marketing intelligence platforms."
            },
            {
                "id": "7.3",
                "metric": "GA4 reporting parameters handling custom intent vectors",
                "status": "Fail",
                "tool": "GA4 Custom Dimension Editor Portal Layout",
                "impact": "Capturing AI-referred variables within standard GA4 dashboards makes channel acquisition performance visible to business stake-holders.",
                "steps": [
                    "Open the Admin console settings pane within Google Analytics 4.",
                    "Navigate to Data Display -> Custom Definitions -> Custom Dimensions.",
                    "Create a custom dimension variable named exactly 'geo_referrer_source'.",
                    "Map this parameter tag to read incoming tracking data layer strings passed by your site's form scripts."
                ],
                "verify": "Check acquisition matrices to ensure conversational search platforms report as separate channels."
            },
            {
                "id": "7.4",
                "metric": "Monthly share of voice reporting pipelines compiled",
                "status": "Fail",
                "tool": "Enterprise Report Builder Core Engine Stack",
                "impact": "Tracks targeted prompt variations, model tracking shifts, and citation rate deltas over time to measure compounding growth.",
                "steps": [
                    "Build a reusable document reporting blueprint inside your data management system.",
                    "Configure automated collection jobs to pull citation rates from your tracking systems on the 1st of every month.",
                    "Compile comparative charts highlighting visibility changes alongside newly identified fan-out query blocks."
                ],
                "verify": "Ensure monthly reporting systems compile and deliver metrics consistently to technical stakeholders."
            }
        ]
    }