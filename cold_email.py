from flask import Flask, render_template_string, request, session, redirect, url_for
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

CSV_PATH = os.path.join(os.path.dirname(__file__), 'Email Project with Data for Alumni Database - Job & Internship Acceptances.csv')

# Read CSV and cache data
people = []
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        people.append(row)

# HTML templates (inline for simplicity)
USER_FORM = '''
<!doctype html>
<title>Cold Email Prompt Generator - User Info</title>
<h2>Enter Your Info (only once per session)</h2>
<form method="post">
  <label>Your Full Name: <input name="yourName" required></label><br><br>
  <label>Your Year: <input name="yourYear" required></label><br><br>
  <label>Your College in UNC (optional): <input name="yourCollegeinUNC"></label><br><br>
  <button type="submit">Continue</button>
</form>
'''

SELECT_PERSON = '''
<!doctype html>
<title>Cold Email Prompt Generator</title>
<h2>Generate ChatGPT Prompt for Cold Email</h2>
<p><b>User:</b> {{ user['yourName'] }}, {{ user['yourYear'] }}, {{ user['yourCollegeinUNC'] or 'UNC Chapel Hill' }}</p>
<form method="post">
  <label>Select Person:
    <select name="person_name" required>
      {% for p in people %}
        <option value="{{ p['Full Name'] }}">{{ p['Full Name'] }} - {{ p['Job Title'] }} at {{ p['Employer'] }}</option>
      {% endfor %}
    </select>
  </label><br><br>
  <label>Notes from Google Search (optional):<br>
    <textarea name="google_notes" rows="4" cols="50" placeholder="Enter any notes you found from researching this person online..."></textarea>
  </label><br><br>
  <button type="submit">Generate Prompt</button>
</form>
{% if prompt %}
  <h3>Generated ChatGPT Prompt</h3>
  <textarea rows="20" cols="100">{{ prompt }}</textarea>
{% endif %}
''' 

def make_prompt(user, person, google_notes=""):
    # College logic
    if user['yourCollegeinUNC']:
        college_str = f"UNC Chapel Hill's {user['yourCollegeinUNC']}"
    else:
        college_str = "UNC Chapel Hill"
    
    # Build notes section
    notes_section = ""
    if google_notes.strip():
        notes_section = f"\nHere are the notes from the google search query about {person['Full Name']}:\n\n{google_notes}\n"
    
    # Prompt
    prompt = f"""
Please help me generate a personalized cold email for {person['Full Name']} based on the following information:

{notes_section}

Using this information and any additional context you can provide, generate a personalized cold email using the following template (fill in the brackets with the appropriate information):

My name is {user['yourName']}, and I'm a {user['yourYear']} at {college_str}, reaching out on behalf of a passionate team of 20+ students working to launch UNC's first student-run federal credit union. Inspired by successful models like Georgetown University's student credit union, our initiative aims to empower students through practical financial literacy, affordable banking services, and meaningful hands-on experience.

To turn our vision into reality, we're currently raising an initial $100,000 to cover regulatory and setup costs. We're seeking donations from alumni or others who share our commitment to financial empowerment, education, and community impact. Your support would help us provide:

- No-fee student checking and savings accounts
- Unique credit-building products to improve student financial health
- On-campus financial literacy education
- Leadership and professional growth opportunities for UNC students

We believe your support could provide substantial mutual benefits, including prominent brand visibility and recognition as a foundational supporter of UNC student success.

Thank you for considering this opportunity to shape the future of student finance at UNC. I look forward to hearing from you soon!

Warm regards,
{user['yourName']}
Carolina Credit Union Initiative
"""
    return prompt

@app.route('/', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        session['user'] = {
            'yourName': request.form['yourName'],
            'yourYear': request.form['yourYear'].lower(),
            'yourCollegeinUNC': request.form.get('yourCollegeinUNC', '').strip()
        }
        return redirect(url_for('select_person'))
    return render_template_string(USER_FORM)

@app.route('/select', methods=['GET', 'POST'])
def select_person():
    user = session.get('user')
    if not user:
        return redirect(url_for('user_form'))
    prompt = None
    if request.method == 'POST':
        name = request.form['person_name']
        google_notes = request.form.get('google_notes', '').strip()
        person = next((p for p in people if p['Full Name'] == name), None)
        if person:
            prompt = make_prompt(user, person, google_notes)
    return render_template_string(SELECT_PERSON, user=user, people=people, prompt=prompt)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
