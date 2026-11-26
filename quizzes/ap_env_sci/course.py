from ap_sci.course import Course

C = Course(
    family="ap_env_sci", slug="ap-environmental-science", name="AP Environmental Science", short="AP Environmental Science",
    prefix="ap-envsci-", nums=list(range(1, 10)), heading="Environmental Science", before_id="ap-french",
    blurb=("Environmental science for the new course (CED effective fall 2026; the exam is 80 multiple-choice questions in "
           "90 minutes and three free-response questions in 70 minutes). Each of the nine units has a study guide (notes, worked "
           "examples and section checks) and a question set: exam-style multiple choice, many built on a shared data table, graph "
           "or described study, and one 10-point free-response question. The three free-response types (design an investigation; "
           "analyze and interpret quantitative data; analyze an environmental problem doing calculations) each appear three times."),
    pace=1.1, tools="A calculator is allowed; show your setup in calculations.",
    setup="Allow a little over a minute per question, the exam&rsquo;s pace. A calculator is allowed.",
    exam_mc="80 multiple-choice questions in 90 minutes")
