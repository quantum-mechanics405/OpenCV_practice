from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "Solved English Precis & Composition Past Paper 2024", ln=True, align='C')
pdf.ln(10)


pdf.set_font("Arial", size=12)

# MCQs Section (Solutions)
mcqs_solutions = [
    ("1. UBIQUITOUS:", "B) Present everywhere"),
    ("2. PERNICIOUS:", "B) Harmful"),
    ("3. MELLIFLUOUS:", "B) Smooth and sweet-sounding"),
    ("4. EPHEMERAL:", "C) Short-lived"),
    ("5. ASTUTE:", "D) Insightful"),
    ("6. ENTHRALL:", "B) Captivate"),
    ("7. SYCOPHANT:", "D) Flatterer"),
    ("8. ASSUAGE:", "C) Soothe"),
    ("9. RETICENT:", "D) Reserved"),
    ("10. INCESSANT:", "C) Persistent"),
    ("11. ESOTERIC:", "A) Obvious"),
    ("12. SQUALID:", "D) Clean"),
    ("13. TACITURN:", "A) Loquacious"),
    ("14. CONSTRICT:", "C) Expand"),
    ("15. LOQUACIOUS:", "B) Silent"),
    ("16. INDOLENT:", "B) Active"),
    ("17. COALESCE:", "D) Separate"),
    ("18. RANCOR:", "D) Amicability"),
    ("19. ACQUIESCE:", "B) Resist"),
    ("20. DEBILITATE:", "A) Fortify")
]

pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "PART-I (MCQs) SOLUTIONS:", ln=True)
pdf.ln(5)
pdf.set_font("Arial", size=12)

for question, answer in mcqs_solutions:
    pdf.multi_cell(0, 7, f"{question} {answer}")

pdf.ln(10)

# Precis Writing
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "PART-II (Descriptive Section)", ln=True)
pdf.ln(5)
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Q.2: Precis Writing", ln=True)
pdf.ln(5)

precis_title = "The Importance of Urban Green Spaces"
precis_text = ("Urban green spaces, such as parks and gardens, offer crucial benefits in modern cities. "
               "Beyond their aesthetic appeal, these areas provide a sanctuary for both people and wildlife, "
               "enhancing environmental balance. They contribute to cleaner air, reduce the urban heat effect, "
               "and improve mental well-being. These spaces also foster community engagement through social gatherings, "
               "sports, and cultural events. However, rapid urbanization threatens their existence, necessitating "
               "sustainable urban planning to integrate nature into city life. Balancing development with green "
               "preservation ensures healthier, more livable urban environments.")

pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, f"Title: {precis_title}", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 7, precis_text)
pdf.ln(10)

# Answers to Passage Questions
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Q.3: Answers to Passage Questions", ln=True)
pdf.ln(5)

passage_answers = [
    ("1. Main Theme:", "The passage explores the evolving relationship between humanity and technology, emphasizing "
                       "how digital advancements shape education, communication, and ethics."),
    ("2. Education Adaptation:", "Education is transitioning to digital platforms, offering global accessibility. "
                                 "However, challenges like the digital divide and ethical considerations remain."),
    ("3. Digital Divide:", "The passage highlights the gap between those with and without technological access. "
                           "Inclusivity is crucial to ensure equal opportunities for education and development."),
    ("4. Ethics in AI:", "The passage underscores the need for ethical guidelines in AI as its influence grows. "
                         "Transparency and responsibility are key considerations."),
    ("5. Social Responsibility:", "It calls for collective wisdom in balancing technological advancements with "
                                  "equity and ethical awareness, ensuring progress benefits all."),
]

for question, answer in passage_answers:
    pdf.set_font("Arial", style='B', size=12)
    pdf.multi_cell(0, 7, question)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 7, answer)
    pdf.ln(5)

pdf.ln(10)

# Grammar and Sentence Correction
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Q.4: Sentence Corrections", ln=True)
pdf.ln(5)

corrections = [
    ("1. Chewing slowly, he found the pepperoni pizza delicious."),
    ("2. Kicking and screaming, the toddler was dragged out of the grocery store by his exasperated father."),
    ("3. A young girl in the corner was holding a red balloon."),
    ("4. Whom do you admire the most?"),
    ("5. He ordered a high-protein meal from the restaurant."),
]

for sentence in corrections:
    pdf.multi_cell(0, 7, sentence)

pdf.ln(10)

# Punctuation Correction
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Q.5: Corrected Punctuation", ln=True)
pdf.ln(5)

punctuation_fixes = [
    ("1. The cordless vacuum, one of the least interesting household appliances, got its start as a moon drill."),
    ("2. Dr. Seuss books are famous for their delightful rhymes and nonsense words. 'If I Ran a Zoo,' however, "
     "likely gave us the real word 'nerd'."),
    ("3. There are many theories about Edgar Allan Poe's mysterious death, including rabies, alcoholism, "
     "and a truly strange possibility—he may have been a victim of a voter fraud scheme."),
    ("4. The film critic said, 'One of the most misquoted lines in movie history is Play it again, Sam.'"),
]

for fix in punctuation_fixes:
    pdf.multi_cell(0, 7, fix)

pdf.ln(10)

# Prepositions
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 10, "Q.5(b): Prepositions", ln=True)
pdf.ln(5)

preposition_fixes = [
    ("1. His research is characterized by a deep understanding of genetic mutations."),
    ("2. The solution is contingent upon various factors."),
    ("3. The experiment is predicated on the assumption of uniform conditions."),
    ("4. The project is commensurate with the skills of the research team."),
    ("5. The discussion oscillated between two main points."),
]

for fix in preposition_fixes:
    pdf.multi_cell(0, 7, fix)

# Save PDF
pdf_path = "/mnt/data/Solved_English_Paper_2024.pdf"
pdf.output(pdf_path)

# Provide user with the PDF
pdf_path
