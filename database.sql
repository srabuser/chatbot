CREATE TABLE courses (
    course_code VARCHAR(50),
    course_name VARCHAR(255),
    units INT,
    prerequisites VARCHAR(255),
    semester INT
);

CREATE TABLE elective_courses (
    course_code VARCHAR(50),
    course_name VARCHAR(255),
    units INT,
    prerequisites VARCHAR(255),
    category VARCHAR(255),
    semester INT
);
-- Semester 1 Courses (15 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('عال 114', 'تراكيب محددة 1', 3, 'لا يوجد', 1),
('عال 150', 'مقدمة في برمجة الحاسبات', 4, 'لا يوجد', 1),
('نجل 140', 'اللغة الإنجليزية 1', 3, 'لا يوجد', 1),
('ريض 113', 'حساب التفاضل والتكامل التطبيقي 1', 4, 'لا يوجد', 1),
('قرا 101', 'القرآن الكريم 1', 1, 'لا يوجد', 1);

-- Semester 2 Courses (15 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('عال 125', 'تصميم المنطق الرقمي', 4, 'عال 114', 2),
('عال 151', 'البرمجة الشيئية', 4, 'عال 150', 2),
('نال 201', 'أسس نظم المعلومات', 3, 'عال 114', 2),
('قرا 151', 'القرآن الكريم 2', 1, 'لا يوجد', 2),
('فيز 103', 'الفيزياء العامة', 3, 'لا يوجد', 2);

-- Semester 3 Courses (14 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('عال 252', 'تراكيب البيانات', 4, 'عال 114, عال 151', 3),
('دار 100', 'مقدمة في إدارة المعلومات', 3, 'لا يوجد', 3),
('نجل 141', 'اللغة الإنجليزية 2', 3, 'نجل 140', 3),
('قصد 105', 'الاقتصاد الجزئي', 3, 'لا يوجد', 3),
('قرا 201', 'القرآن الكريم 3', 1, 'لا يوجد', 3);

-- Semester 4 Courses (17 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('فيز 104', 'فيزياء تطبيقية', 3, 'فيز 103', 4),
('نجل 210', 'الكتابة التقنية', 3, 'نجل 141', 4),
('نال 230', 'تحليل متطلبات الأعمال', 3, 'نال 201', 4),
('احص 111', 'مقدمة في الاحتمالات والإحصاء', 3, 'عال 114', 4),
('نحو 105', 'النحو', 2, 'لا يوجد', 4),
('حسب 100', 'مبادئ المحاسبة 1', 3, 'لا يوجد', 4);

-- Semester 5 Courses (15 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('نال 220', 'مقدمة في قواعد البيانات', 3, 'نال 230', 5),
('عال 222', 'أنظمة التشغيل', 4, 'عال 252', 5),
('قرا 201', 'القرآن الكريم 4', 1, 'لا يوجد', 5),
('تسق 301', 'مبادئ التسويق', 2, 'قصد 105', 5),
('عقد 133', 'التوحيد', 2, 'لا يوجد', 5),
('نال 350', 'نظم دعم اتخاذ القرار', 3, 'احص 111', 5);

-- Semester 6 Courses (18 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('عال 330', 'شبكات الحاسب', 4, 'عال 222', 6),
('نال 321', 'نظم إدارة قواعد البيانات', 3, 'نال 220', 6),
('نال 335', 'تحليل وتصميم النظم', 3, 'نال 220', 6),
('نال 352', 'نظم المعلومات الجغرافية', 3, 'نال 220', 6),
('مال 300', 'مبادئ المالية', 3, 'حسب 100', 6),
('ترخ 102', 'تاريخ المملكة العربية السعودية', 2, 'لا يوجد', 6);

-- Semester 7 Courses (14 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('نال 336', 'إدارة مشاريع نظم المعلومات', 3, 'نال 335', 7),
('نال 380', 'الأمن السيبراني', 3, 'عال 330', 7),
('نال 337', 'تطوير التطبيقات', 3, 'نال 321', 7),
('دعا 129', 'الدعوة الإصلاحية', 2, 'لا يوجد', 7);

-- Semester 8 Courses (13 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('نال 401', 'علاقات الأعمال', 1, 'تسق 301', 8),
('نال 460', 'الأعمال الإلكترونية', 3, 'نال 337', 8),
('نال 492', 'أمن المعلومات', 3, 'نال 380', 8),
('نال 495', 'مشروع تخرج 1', 3, 'نال 337, نال 336', 8);

-- Semester 9 Courses (11 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('نال 410', 'بنية المؤسسات', 3, 'نال 336', 9),
('نال 482', 'استراتيجيات وسياسة نظم المعلومات', 3, 'نال 460', 9),
('نال 496', 'مشروع تخرج 2', 3, 'نال 495', 9),
('فقه 200', 'الفقه', 2, 'لا يوجد', 9);

-- Semester 10 Courses (9 units)
INSERT INTO courses (course_code, course_name, units, prerequisites, semester) VALUES
('نال 398', 'التدريب العملي', 9, 'نال 350', 10);

-- Semester 6 - Group: Ansys Computing Systems
INSERT INTO elective_courses (course_code, course_name, units, prerequisites, category, semester) VALUES
('نال 352', 'نظم المعلومات الجغرافية', 3, 'نال 220', 'مجموعة أنظمة الحوسبة', 6),
('نال 370', 'تفاعل الإنسان مع الحاسب', 3, 'نال 220', 'مجموعة أنظمة الحوسبة', 6),
('نال 372', 'تجربة المستخدم', 3, 'نال 220', 'مجموعة أنظمة الحوسبة', 6),
('نال 323', 'نظم إدارة المعرفة', 3, 'نال 220, نال 350', 'مجموعة أنظمة الحوسبة', 6),
('نال 354', 'نظم المعلومات الصحية', 3, 'نال 220', 'مجموعة أنظمة الحوسبة', 6),
('نال 384', 'مواضيع مختارة في نظم المعلومات 1', 3, 'نال 220', 'مجموعة أنظمة الحوسبة', 6);

-- Semester 7 - Group: Data Management
INSERT INTO elective_courses (course_code, course_name, units, prerequisites, category, semester) VALUES
('نال 424', 'إدارة قواعد البيانات', 3, 'نال 321, نال 335', 'مجموعة إدارة البيانات', 7),
('نال 440', 'تعدين البيانات', 3, 'نال 335', 'مجموعة إدارة البيانات', 7),
('نال 442', 'ذكاء الأعمال', 3, 'نال 335', 'مجموعة إدارة البيانات', 7),
('نال 435', 'جودة تجربة البرمجيات', 3, 'نال 335', 'مجموعة إدارة البيانات', 7),
('نال 385', 'مواضيع مختارة في نظم المعلومات 2', 3, 'نال 335', 'مجموعة إدارة البيانات', 7);

-- Semester 8 - Group: Business Management
INSERT INTO elective_courses (course_code, course_name, units, prerequisites, category, semester) VALUES
('نال 463', 'إدارة التغيير', 3, 'نال 336', 'مجموعة إدارة الأعمال', 8),
('نال 451', 'نظم تخطيط موارد المؤسسات', 3, 'حسب 100, نال 335', 'مجموعة إدارة الأعمال', 8),
('نال 461', 'إدارة عمليات الأعمال', 3, 'نال 336, نال 335', 'مجموعة إدارة الأعمال', 8),
('نال 487', 'أمن التجارة الإلكترونية', 3, 'نال 336', 'مجموعة إدارة الأعمال', 8),
('نال 490', 'مواضيع مختارة في نظم المعلومات 3', 3, 'نال 336', 'مجموعة إدارة الأعمال', 8);
