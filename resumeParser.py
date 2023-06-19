from resume_parser import ResumeParser

resume_path=r"C:\Users\PRIYANKA\OneDrive\Documents\PriyankaNihalchandani resume.pdf"

data=ResumeParser(resume_path).get_extracted_data()

name=data.get('name')
email=data.get('email')
phone=data.get('phone')
education=data.get('education')
work_experience=data.get('work_experience')
skills=data.get('skills')

print('Name:', name)
print('Email:', email)
print('Phone:', phone)
print('Education:', education)
print('Work Experience:', work_experience)
print('Skills:', skills)