from ap_sci.course import Course

C = Course(
    family="ap_physics_1", slug="ap-physics-1", name="AP Physics 1: Algebra-Based", short="AP Physics 1", prefix="ap-phys1-",
    nums=list(range(1, 9)), heading="Physics 1: Algebra-Based", before_id="ap-physics-c-mechanics",
    blurb=("Algebra-based mechanics for the current course (CED effective fall 2024; the exam is 42 multiple-choice questions in "
           "85 minutes and four free-response questions in 95 minutes). Each of the eight units has a study guide (notes, worked "
           "examples and section checks) and a question set: exam-style multiple choice, some built on a shared graph or data table, "
           "and one full free-response question with a scoring guide. The four free-response types (Mathematical Routines, "
           "Translation Between Representations, Experimental Design and Analysis, Qualitative/Quantitative Translation) each appear twice."),
    pace=2.0, tools="Use the AP equation sheet and a calculator; take $g = 9.8\\ \\mathrm{m/s^2}$.",
    setup="Allow about 2 minutes per question, the exam&rsquo;s pace. Keep the AP equation sheet and a calculator at hand; take g = 9.8 m/s&sup2;.",
    exam_mc="42 multiple-choice questions in 85 minutes")
