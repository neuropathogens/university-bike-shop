from ap_sci.course import Course

C = Course(
    family="ap_physics_2", slug="ap-physics-2", name="AP Physics 2: Algebra-Based", short="AP Physics 2", prefix="ap-phys2-",
    nums=list(range(9, 16)), heading="Physics 2: Algebra-Based", before_id="ap-physics-c-mechanics",
    blurb=("Algebra-based thermodynamics, electricity and magnetism, optics, waves and modern physics for the current course "
           "(CED effective fall 2024; the exam is 42 multiple-choice questions in 85 minutes and four free-response questions in "
           "95 minutes). The units are numbered 9&ndash;15, continuing from Physics 1, as in the CED. Each has a study guide "
           "(notes, worked examples and section checks) and a question set: exam-style multiple choice, some built on a shared "
           "graph, circuit or data table, and one full free-response question with a scoring guide covering each of the four "
           "free-response types."),
    pace=2.0, tools="Use the AP equation sheet (with its table of constants) and a calculator.",
    setup="Allow about 2 minutes per question, the exam&rsquo;s pace. Keep the AP equation sheet, with its table of constants, and a calculator at hand.",
    exam_mc="42 multiple-choice questions in 85 minutes")
