subj = ['Математика', 'Русский', 'Белорусский', 'Физика', 'Биология', 'Химия']
for subjects in subj:
    print(subjects)
x=input("Введите какой предмет вам не нравится: ")
if x=='Математика':
    subj.pop(0)
if x=='Русский':
    subj.pop(1)
if x=='Белорусский':
    subj.pop(2)
if x=='Информатика':
    subj.pop(3)
if x=='Биология':
    subj.pop(4)
if x=='Английский':
    subj.pop(5)
for subjects in subj:
    print(subjects)