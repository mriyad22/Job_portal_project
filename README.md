# Job Portal

A role-based job portal built with **Django** where recruiters can create job postings and review applicants, while job seekers can browse jobs, manage their profiles, and apply with a resume.

> **Project status:** This is a learning/development project. The current codebase is suitable for demonstrating Django fundamentals, but additional hardening and feature work is recommended before production deployment.

---

## 1. Project Overview

The **Job Portal** is a web application developed with Django to connect two primary user types:

- **Recruiter** — creates and manages job postings and views candidates who apply.
- **Seeker** — browses available jobs, maintains a profile, uploads a resume, and applies for jobs.

The project demonstrates practical Django concepts including:

- Custom user models
- Role-based behavior
- Django authentication
- Model relationships
- ModelForms
- Function-Based Views (FBVs)
- URL routing
- File uploads
- Django messages
- Templates and template inheritance
- SQLite database
- Django ORM filtering
- Password change functionality
- Category-based job filtering

### Main user flow

```text
User Registration
       |
       v
 Select User Type
   /           \
Recruiter      Seeker
   |              |
Profile          Profile
   |              |
Post Jobs      Browse Jobs
   |              |
View Candidates  Apply with Resume
```

---

## 2. Features

### Authentication

- User registration
- User login
- User logout
- Custom Django user model
- Recruiter/Seeker role selection
- Password change
- Django session-based authentication

### Recruiter Features

- Recruiter profile
- Company name, logo, address and phone
- Create job postings
- View recruiter-owned job postings
- View candidates for a specific job
- Access applicant resume links

### Seeker Features

- Seeker profile
- Profile image, address and phone
- Browse available jobs
- Filter jobs by category
- Apply to jobs
- Upload resume
- View applied jobs

### Job Features

- Job title
- Job category
- Job description
- Required skills
- Employment shift
- Number of openings
- Salary
- Application deadline
- Recruiter/company information
- Job application records

### UI Features

- Bootstrap-based layout
- Reusable base template
- Reusable navigation bar
- Django messages
- Responsive job cards
- Hover animations
- Gradient buttons
- Profile cards

---

## 3. Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django 6.0.4 | Web framework |
| SQLite3 | Development database |
| HTML5 | Page structure |
| CSS3 | Styling and animations |
| Bootstrap 5.3.8 | Responsive UI |
| Django Templates | Server-side rendering |
| Django ORM | Database interaction |
| Django Authentication | Login/session management |
| Git/GitHub | Version control and hosting |

### External frontend dependency

The base template loads Bootstrap 5.3.8 from jsDelivr.

For production, the project should also consider whether external CDN dependencies should be replaced or supplemented with locally managed static assets.

---

## 4. Django Architecture

The project follows Django's standard **MVT (Model-View-Template)** architecture.

```text
                    Browser
                       |
                       v
                    URLconf
                       |
                       v
                     View
                  /         \
                 v           v
              Model       Template
                 |           |
                 v           v
              Database <--- HTML
```

### Model

Models define the application's database structure.

Main models:

- `UserModel`
- `RecruiterProfileModel`
- `SeekerProfileModel`
- `CategoryModel`
- `JobPostModel`
- `JobApplyModel`

### View

Views contain request/response logic.

Examples:

- `user_register`
- `user_login`
- `profile`
- `profile_update`
- `jb_post`
- `jb_list`
- `apply_job`
- `my_applied`
- `candidete`
- `passwd_change`

The project currently uses **Function-Based Views (FBVs)**.

### Template

Templates are responsible for presenting data to users.

The project uses:

- Template inheritance
- `{% include %}`
- `{% url %}`
- `{% if %}`
- `{% for %}`
- Form rendering
- Django messages

---

## 5. App Structure

The main Django application is named `portal`.

```text
Riyad_NSDA_0001_portal/
│
├── manage.py
├── db.sqlite3
│
├── Riyad_NSDA_0001_portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── portal/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    │
    ├── migrations/
    │   ├── 0001_initial.py
    │   ├── 0002_jobpostmodel_shift.py
    │   └── __init__.py
    │
    └── templates/
        ├── master/
        │   ├── base.html
        │   └── nav.html
        │
        ├── auth/
        │   ├── login.html
        │   └── register.html
        │
        ├── jobs/
        │   ├── jb-list.html
        │   ├── jb-post.html
        │   ├── jb-details.html
        │   └── jb-edit.html
        │
        ├── home.html
        ├── profile.html
        ├── profile-update.html
        ├── jb-apply.html
        ├── my-applied.html
        ├── candidate.html
        └── message.html
```

### Important files

**`models.py`**

Contains the database models and relationships.

**`forms.py`**

Contains Django `ModelForm`, `UserCreationForm`, and `AuthenticationForm` based forms.

**`views.py`**

Contains application business logic.

**`urls.py`**

Maps URLs to views.

**`templates/`**

Contains HTML presentation files.

**`settings.py`**

Contains Django project configuration, installed apps, database configuration, custom user model configuration, etc.

---

## 6. Database / Model Relationships

The application uses a custom user model based on Django's `AbstractUser`.

### Relationship overview

```text
                    UserModel
                   /         \
              OneToOne       OneToOne
                /               \
               v                 v
   RecruiterProfileModel   SeekerProfileModel
               |                 |
               |                 |
          ForeignKey          ForeignKey
               |                 |
               v                 v
        JobPostModel <------ JobApplyModel
               ^
               |
          ForeignKey
               |
       CategoryModel
```

### `UserModel`

Extends Django's `AbstractUser`.

Important fields:

- `display_name`
- `username`
- `email`
- `user_type`
- Django password/authentication fields

User types:

```text
Recruiter
Seeker
```

---

### `RecruiterProfileModel`

Stores recruiter/company information.

Fields include:

- `company_name`
- `logo`
- `address`
- `phone`
- `recruiter`

Relationship:

```text
UserModel 1 ---- 1 RecruiterProfileModel
```

The relationship uses `OneToOneField`.

---

### `SeekerProfileModel`

Stores job seeker information.

Fields include:

- `image`
- `phone`
- `address`
- `seeker`

Relationship:

```text
UserModel 1 ---- 1 SeekerProfileModel
```

---

### `CategoryModel`

Stores job categories.

Example:

```text
Web Development
Cyber Security
Graphic Design
Marketing
Software Development
```

---

### `JobPostModel`

Stores job information.

Important fields:

- `jb_title`
- `category`
- `jb_description`
- `jb_skills`
- `shift`
- `opening`
- `created_at`
- `salary`
- `deadline`
- `posted_by`

Relationships:

```text
CategoryModel 1 ---- * JobPostModel

RecruiterProfileModel 1 ---- * JobPostModel
```

---

### `JobApplyModel`

Stores applications submitted by seekers.

Important fields:

- `resume`
- `apply_at`
- `jb_applyer`
- `applied_by`

Relationships:

```text
SeekerProfileModel 1 ---- * JobApplyModel

JobPostModel 1 ---- * JobApplyModel
```

This creates the core relationship:

```text
Seeker
  |
  | applies
  v
JobApply
  |
  | applied to
  v
JobPost
  |
  | posted by
  v
Recruiter
```

---

## 7. Authentication & Authorization

The project uses Django's built-in authentication system with a custom user model.

### Custom User Model

The project configures:

```python
AUTH_USER_MODEL = 'portal.UserModel'
```

`UserModel` inherits from:

```python
AbstractUser
```

This keeps Django's built-in authentication functionality while allowing custom fields such as:

```python
display_name
user_type
```

### Registration

Registration is handled by:

```python
RegisterForm(UserCreationForm)
```

The form collects:

- Display name
- Username
- Email
- User type
- Password
- Password confirmation

### Login

Login uses:

```python
LoginForm(AuthenticationForm)
```

After successful authentication:

```python
login(request, user)
```

### Logout

Logout uses Django's:

```python
logout(request)
```

### Login protection

Some views use:

```python
@login_required
```

For example:

```python
@login_required
def logout_page(request):
    ...
```

### Role-based behavior

The application checks:

```python
request.user.user_type
```

For example:

```python
if request.user.user_type == 'Recruiter':
```

and:

```python
if request.user.user_type == 'Seeker':
```

This allows the interface and query behavior to differ between recruiters and seekers.

> **Important:** The current implementation uses role checks in views/templates, but production authorization should be strengthened with centralized decorators/mixins and ownership checks for every sensitive operation.

---

## 8. Security Considerations

Django provides several built-in security protections, and the project already benefits from some of them.

### CSRF protection

Forms use:

```django
{% csrf_token %}
```

This helps protect POST requests against Cross-Site Request Forgery.

### Password hashing

Passwords are handled through Django's authentication system rather than being stored as plain text.

### Authentication

Django session authentication is used for logged-in users.

### Production security requirements

The current development configuration should **not** be deployed directly to production.

Before production deployment:

- Move `SECRET_KEY` to an environment variable.
- Set `DEBUG=False`.
- Configure `ALLOWED_HOSTS`.
- Configure HTTPS.
- Configure secure cookies.
- Configure `CSRF_TRUSTED_ORIGINS` when needed.
- Enable Django password validators.
- Configure `STATIC_ROOT`.
- Configure `MEDIA_ROOT` and `MEDIA_URL`.
- Validate uploaded resume/file types and sizes.
- Store user-uploaded files safely.
- Avoid exposing sensitive uploaded files publicly.
- Add authorization checks to recruiter-only and seeker-only actions.
- Prevent users from viewing another recruiter's candidates.
- Prevent duplicate job applications where appropriate.
- Validate job deadlines and salary/opening values.
- Add automated security tests.
- Run Django's deployment checks:

```bash
python manage.py check --deploy
```

### File upload security

The project accepts:

```text
resume
profile image
company logo
```

File uploads require additional production controls such as:

- Extension validation
- MIME/content validation
- File size limits
- Safe storage
- Randomized filenames where appropriate
- Access control
- Malware scanning if required by the deployment environment

---

## 9. Job Posting / Application Workflow

### Recruiter workflow

```text
Register
   |
   v
Choose Recruiter
   |
   v
Login
   |
   v
Update Recruiter Profile
   |
   v
Create Job Post
   |
   v
Job appears in recruiter job list
   |
   v
Open Candidate list
   |
   v
Review applicant information / resume
```

### Job seeker workflow

```text
Register
   |
   v
Choose Seeker
   |
   v
Login
   |
   v
Update Seeker Profile
   |
   v
Browse Jobs
   |
   v
Filter by Category
   |
   v
Select a Job
   |
   v
Upload Resume
   |
   v
Submit Application
   |
   v
Application stored in database
   |
   v
View My Applied Jobs
```

### Application database flow

When a seeker submits an application, the application connects:

```python
apply.jb_applyer = request.user.seeker_profile
apply.applied_by = jb_apl
```

Therefore, the system knows:

1. Which seeker applied.
2. Which job they applied to.
3. Which resume they uploaded.
4. When the application was submitted.

---

## 10. Challenges & Solutions

### Challenge 1 — Custom user roles

**Problem:** A job portal needs different behavior for recruiters and seekers.

**Solution:** Extend Django's `AbstractUser` and add:

```python
user_type
```

with:

```text
Recruiter
Seeker
```

---

### Challenge 2 — Different profile information

**Problem:** Recruiters and seekers need different profile fields.

**Solution:** Create separate profile models:

```text
RecruiterProfileModel
SeekerProfileModel
```

and connect each to `UserModel` with `OneToOneField`.

---

### Challenge 3 — Connecting jobs to recruiters

**Problem:** A job needs to remember which recruiter/company posted it.

**Solution:** `JobPostModel` contains a foreign key to:

```python
RecruiterProfileModel
```

using:

```python
posted_by
```

---

### Challenge 4 — Connecting applications to both job and seeker

**Problem:** An application must identify both the applicant and the job.

**Solution:** `JobApplyModel` contains two foreign keys:

```python
jb_applyer
applied_by
```

---

### Challenge 5 — File uploads

**Problem:** Seekers need to submit resumes and users need profile/company images.

**Solution:** Django `FileField` and `ImageField` are used with upload directories.

Examples:

```text
se_resume/
company_logo/
seekerImage/
```

---

### Challenge 6 — Category filtering

**Problem:** Users need to browse jobs by category.

**Solution:** The job list reads a category ID from the query string:

```text
/job-list/?cate_id=<id>
```

and filters jobs through the Django ORM.

---

### Challenge 7 — Maintaining authentication state after password change

**Problem:** Changing a password can invalidate a user's existing session.

**Solution:** The project uses:

```python
update_session_auth_hash(request, data)
```

after changing the password.

---

## 11. What I Learned

This project helped demonstrate practical Django development concepts.

### Django fundamentals

- Creating a Django project
- Creating Django apps
- URL routing
- Views
- Templates
- Template inheritance
- Static/media concepts

### Database

- Creating models
- Primary keys
- Foreign keys
- One-to-one relationships
- Django migrations
- QuerySets
- Filtering records
- Object retrieval

### Authentication

- Custom user models
- `AbstractUser`
- Registration
- Login
- Logout
- Sessions
- Password change
- `login_required`

### Forms

- `ModelForm`
- `UserCreationForm`
- `AuthenticationForm`
- Form validation
- File uploads
- Custom widgets

### Frontend

- Bootstrap
- Responsive cards
- Navbar
- Forms
- Alerts/messages
- Template inheritance
- Basic CSS animations

### Software development

- Structuring a Django application
- Connecting models and views
- Designing user workflows
- Thinking about authorization
- Handling uploaded files
- Planning production security improvements

---

## 12. Installation & Setup

### Prerequisites

Install:

- Python 3.12+ recommended
- pip
- Git
- Virtual environment support

Verify Python:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

---

### Step 1 — Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_DIRECTORY>
```

---

### Step 2 — Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3 — Install dependencies

If the repository contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

For the current project, Django 6.0.4 is the framework version shown in the project settings.

If dependencies are not yet listed, install Django and Pillow:

```bash
pip install django==6.0.4 pillow
```

`Pillow` is required for Django `ImageField`.

---

### Step 4 — Configure environment variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=replace-with-a-secure-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

See the **Environment Variables** section below.

> The current source code contains a hard-coded development `SECRET_KEY`. For a real GitHub repository, replace that approach with environment-based configuration before publishing/deploying.

---

### Step 5 — Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 6 — Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts.

---

### Step 7 — Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## 13. Environment Variables

For production-ready configuration, use environment variables rather than hard-coding secrets.

Recommended variables:

| Variable | Purpose | Example |
|---|---|---|
| `SECRET_KEY` | Django cryptographic secret | `your-secret-key` |
| `DEBUG` | Development/debug mode | `True` / `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `CSRF_TRUSTED_ORIGINS` | Trusted HTTPS origins | `https://example.com` |
| `DATABASE_URL` | Optional production DB URL | `postgresql://...` |

### Example `.env`

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=example.com,www.example.com
CSRF_TRUSTED_ORIGINS=https://example.com,https://www.example.com
```

### `.gitignore`

Do not commit secrets or local development files.

Recommended:

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual environment
venv/
.env

# Django
db.sqlite3
staticfiles/

# User uploads
media/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

> If you intentionally want to distribute a sample SQLite database, keep `db.sqlite3` only if that is part of your repository strategy. Otherwise, let users create it with migrations.

---



## 14. Future Improvements

The current project provides a solid Django learning foundation. Possible improvements include:

### Job management

- Job detail page
- Job edit functionality
- Job delete functionality
- Job expiration based on deadline
- Featured jobs
- Search functionality
- Pagination
- Advanced filtering
- Salary range filtering
- Location filtering

### Applications

- Prevent duplicate applications
- Application status:
  - Pending
  - Shortlisted
  - Interview
  - Rejected
  - Hired
- Recruiter-side application management
- Applicant notification system
- Resume preview/download permissions

### User experience

- Better dashboard for recruiters
- Better dashboard for seekers
- Saved/bookmarked jobs
- Email notifications
- Job alerts
- Profile completion indicator
- Better validation messages
- Improved mobile UI

### Security

- Stronger role-based authorization
- Object ownership checks
- File type/size validation
- Secure media handling
- Rate limiting
- Email verification
- Password reset
- Two-factor authentication
- Security headers
- HTTPS-only production configuration

### Architecture

- Introduce class-based views where appropriate
- Add service/helper layers for complex business logic
- Add reusable permission decorators/mixins
- Add automated tests
- Add API endpoints with Django REST Framework
- Separate development and production settings
- Add proper dependency management

### Deployment

Possible production stack:

```text
Django
   |
Gunicorn / ASGI server
   |
Nginx
   |
PostgreSQL
   |
Cloud/Object Storage for media
```

Potential deployment platforms include:

- Render
- Railway
- PythonAnywhere
- AWS
- DigitalOcean
- VPS-based deployment

---

## 15. GitHub-Ready Formatting

Recommended repository structure:

```text
job-portal/
│
├── README.md
├── .gitignore
├── requirements.txt
├── manage.py
│
├── Riyad_NSDA_0001_portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── portal/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── docs/
│   └── screenshots/
│       ├── home.png
│       ├── register.png
│       ├── login.png
│       ├── job-list.png
│       ├── job-post.png
│       ├── job-apply.png
│       ├── candidates.png
│       └── profile.png
│
└── media/
```

### Recommended `requirements.txt`

At minimum, generate it from the development environment:

```bash
pip freeze > requirements.txt
```

This makes it easier for other developers to reproduce the environment.

### Recommended Git workflow

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

### Repository description

Suggested GitHub description:

> A Django-based job portal with recruiter and job seeker roles, job posting, category filtering, resume uploads, applications, profiles, and candidate management.

### Suggested GitHub topics

```text
django
python
job-portal
job-board
web-development
django-project
authentication
sqlite
bootstrap
crud
```

---

## Project Notes

### Current implementation details

The uploaded project currently uses:

- Django `6.0.4`
- SQLite database
- Custom `UserModel`
- Function-Based Views
- Bootstrap `5.3.8`
- Django authentication
- `ImageField` for profile/company images
- `FileField` for resumes

### Known areas to improve before production

The current source contains development-oriented settings such as:

```python
DEBUG = True
```

and a hard-coded `SECRET_KEY`.

It also currently has limited automated testing and some views rely on template/view role checks rather than a centralized authorization layer.

The repository should therefore be treated as a **Django learning/project portfolio application**, not as a production-hardened job platform.

---

## Author

**Riyad**

Django / Python Project

---

## Acknowledgements

Built as a Django learning project to practice:

- Django MVT architecture
- Authentication
- Custom user models
- Database relationships
- Forms
- File uploads
- Role-based application workflows
- Bootstrap-based frontend development