import re

with open("Introduction to Indigenous Data Sovereignty.qmd", "r") as f:
    content = f.read()

# Split by the slide headers
parts = re.split(r"(^##\s+.*$)", content, flags=re.MULTILINE)

# parts[0] is frontmatter
# parts[1] is header 1, parts[2] is content 1, etc.
slides = {}
frontmatter = parts[0]

for i in range(1, len(parts), 2):
    header = parts[i]
    body = parts[i+1]
    # normalize header string
    title = header.strip()
    slides[title] = body

# Combine the identity slides directly if possible, or just rename them
slide_24_title = "## From Webinar Practice: Colonial Definitions and Enrollment"
slide_27_title = "## Tribal Enrollment Data: The Unresolved Governance Gap"

if slide_24_title in slides:
    merged_bullets = slides[slide_24_title].split("::: {.notes}")[0].strip() + "\n" + slides[slide_27_title].split("::: {.notes}")[0].strip()
    merged_notes = "::: {.notes}\n" + slides[slide_24_title].split("::: {.notes}")[1].split(":::")[0].strip() + "\n\n" + slides[slide_27_title].split("::: {.notes}")[1].split(":::")[0].strip() + "\n:::\n\n"
    merged_slide_body = "\n" + merged_bullets + "\n\n" + merged_notes
    slides["## Domain: Identity and Enrollment Sovereignty"] = merged_slide_body

order = [
    "## Historical Context and Colonial Extraction",
    "## Lessons from Exploitation: The Havasupai Case",
    "## Weapons of Extraction: Pacific Salmon Case Study",
    "## Defining Indigenous Data Sovereignty",
    "## The Indigenous Data Relationship Pyramid",
    "## Human Rights and International Frameworks",
    "## The First Nations Principles of OCAP®",
    "## The CARE Principles for Data Governance",
    "## Technical Synergy: Aligning FAIR and CARE",
    "## IEEE 2890-2025: A Global Technical Standard",
    "## Local Contexts: TK and Biocultural Labels",
    "## Tribal Institutional Review Boards and Data Use Agreements",
    "## Domain: Environmental and Geospatial Sovereignty",
    "## Domain: Genomic and Biocultural Data",
    "## Domain: Health and Social Data Sovereignty",
    "## Public Health Governance Case: Arizona vs New Mexico (COVID-19)",
    "## Domain: Education and Economic Sovereignty",
    "## Domain: Identity and Enrollment Sovereignty",
    "## Sovereign Digital Infrastructure",
    "## Artificial Intelligence and Digital Colonialism",
    "## Responding to the AI Threat: Proactive Governance",
    "## Operationalizing Sovereignty: Cherokee Nation Model",
    "## Cherokee Values as Policy Pillars",
    "## Legal Infrastructure: Yurok and Karuk Models",
    "## The Māori Data Sovereignty Model",
    "## Global Networks and Actionable Steps",
    "## References {.smaller}"
]

new_content = frontmatter
for header in order:
    if header in slides:
        new_content += header + slides[header]
    else:
        print(f"MISSING SLIDE: {header}")

with open("Introduction to Indigenous Data Sovereignty.qmd", "w") as f:
    f.write(new_content)

print("Reordering complete.")
