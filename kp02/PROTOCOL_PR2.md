# Practical Work #2 Protocol

## Student
- Full name: Stepan Potiienko
- Group: <add group>
- Date: <add date>

## Goal
Implement a Django web application with:
- home page `/`
- text page `/text/`
- resume page `/resume/`
- work in a separate git branch `kp02`

## 1. Git Branching
1. Created branch `kp02`.
2. Switched to branch `kp02`.

Screenshot placeholders:
- [ ] Branch creation/switch output
- [ ] `git branch` output

## 2. Django Project Setup
1. Created directory `kp02`.
2. Created project `proj_step_pot`.
3. Verified project with `python3 manage.py check`.

Screenshot placeholders:
- [ ] Project tree
- [ ] `manage.py check` output

## 3. App `app01`
1. Created app: `python3 manage.py startapp app01`.
2. Added `app01.apps.App01Config` to `INSTALLED_APPS`.
3. Implemented views in `app01/views.py`:
   - `response` for `/`
   - `response2` for `/text/`
4. Added routes in `app01/urls.py`.
5. Connected `app01.urls` in `proj_step_pot/urls.py`.

Screenshot placeholders:
- [ ] `settings.py` with `app01`
- [ ] `app01/views.py`
- [ ] `app01/urls.py`
- [ ] Browser page `/`
- [ ] Browser page `/text/`

## 4. App `resume`
1. Created app: `python3 manage.py startapp resume`.
2. Added `resume.apps.ResumeConfig` to `INSTALLED_APPS`.
3. Implemented `resume_view` in `resume/views.py`.
4. Added `resume/urls.py`.
5. Added template `resume/templates/resume/index.html`.
6. Connected `resume.urls` via route `/resume/`.

Screenshot placeholders:
- [ ] `settings.py` with `resume`
- [ ] `resume/views.py`
- [ ] Template `index.html`
- [ ] Browser page `/resume/`

## 5. Validation
Commands executed:
- `python3 manage.py check`
- `python3 manage.py test`
- `python3 manage.py migrate`
- `python3 manage.py runserver`

Screenshot placeholders:
- [ ] `manage.py test` output
- [ ] `runserver` output

## 6. Archive
Archive created from git commit:
- `kp02_code.zip`

Screenshot placeholders:
- [ ] Archive file in file manager/terminal
- [ ] Archive content list

## 7. Conclusion
All required routes are implemented and work:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/text/`
- `http://127.0.0.1:8000/resume/`
