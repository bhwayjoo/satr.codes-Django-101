# satr.codes-Django-101

مشروع واجهة مدرسة School
باستخدام ما تعلمته خلال هذهِ الدورة قم بتطبيق الآتي:


إنشاء مشروع مدرسة School.
إنشاء تطبيق Courses.
إنشاء View باسم (Welcome_View) تعرض رسالة ترحيبية للطالب (Welcome to Courses App).
إنشاء View خاصة بعرض المواد الدراسية باسم (Courses_Info).
تطبيق URL Mapping على صفحة Welcome_View وتسميتها (Welcome.html).
إنشاء مجلد Template بداخله صفحة base.html.
تعديل الموجود في صفحة base.html وإضافة متغير name يتم طباعته بالشكل التالي: (Hi {{name}}, Welcome to Courses App).
تعديل صفحة View وإضافة متغير name باسمك.
عرض محتويات ملف base.html بدلًا من الرسالة الترحيبية (Welcome to Courses App) داخل صفحة View.
إنشاء Model يحتوي نوعين من Fields.
اسم المقرر Course Name من نوع CharField وحدد max_length بحيث لايتجاوز 50.
رمز المقرر Course Number من نوع IntegerField وإضافة help_text (Course Number represents the Course ID).
إنشاء حساب Admin ومن خلاله قم بالآتي:
إضافة بيانات جديدة (اسم المقرر مع رمزه).
تعديل على البيانات المدخلة.
حذف أحد المقرارات الموجودة.
تطبيق (Migrations) على التعديلات الجديدة.
