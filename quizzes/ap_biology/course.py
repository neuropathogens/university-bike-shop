from ap_sci.course import Course

C = Course(
    family="ap_biology", slug="ap-biology", name="AP Biology", short="AP Biology", prefix="ap-bio-",
    nums=list(range(1, 9)), heading="Biology", before_id="ap-calculus-bc",
    blurb=("Biology for the current course (CED effective fall 2025; the exam is 60 multiple-choice questions in 90 minutes "
           "and six free-response questions in 90 minutes). Each of the eight units has a study guide (notes, worked examples "
           "and section checks) and a question set: exam-style multiple choice, many built on a shared experiment, data table "
           "or graph, and one free-response question in one of the exam&rsquo;s six formats, scored point by point as the CED "
           "describes. The graphing question includes a model graph."),
    pace=1.5, tools="A calculator and the AP Biology equations and formulas sheet are allowed.",
    setup="Allow about 90 seconds per question, the exam&rsquo;s pace. Keep a calculator and the AP Biology equations and formulas sheet at hand.",
    exam_mc="60 multiple-choice questions in 90 minutes")
