# Dhar Hobe - A Bangladeshi Product Renting System
## Team Name: JU_High_Fives

Batch 48, Department of Computer Science & Engineering, Jahangirnagar University, Bangladesh

## Team Members:

1. Iffat Ara Sanzida (IA) - 344
2. Jannatul Ferdoush Jannati (JF) - 349
3. Sumaita Binte Shorif (SB) - 357
4. Amena Akter Sathi (AA)- 351
5. Fariha Rahman Saba (FR) - 347

# How to Use
## 1. Clone the project
- Install git bash
- Open your local directory's git bash terminal
- Configure git:
    
  `git config --global user.name <github_username>`
  
  `git config --global user.email <github_email>`
    
- Run command:
  `git clone https://github.com/JU-High-Fives/Dhar-Hobe.git`

## 2. Navigate to the project directory commands
- Navigate:
  `cd BharaHobe`
- Open VS Code:
  `code .`
- Open terminal:
  `Ctrl + J`
  
## 3. Run the Project:
- Check Python:
  `python --version`

  If python not found, [install](https://youtu.be/Gznz5Slw2Qg?si=PC2ZsaJLipd_8ERQ) python.
  
- Check Django:
  `python -m django --version`

  If Django is not found, install by running:
  `pip install django`
  
- See branch list:
  `git branch -a`
- Checkout to specific branch:
  `git checkout <branch_name>`
- Run the project:
   `python manage.py runserver`
  
- Click and Follow: `http://127.0.0.1:8000/`

# How to Develop
## 1. Create a new branch:
- Run command:
  `git checkout -b <new_branch_name>`
## 2. Make Changes:
- Create an app:
  `python manage.py startapp <app_name>`
  
- After making changes in databases:
  
  `python manage.py makemigrations`
  
  `python manage.py migrate`

- Run test cases to ensure everything is working as expected:
  `python manage.py test`

## 3. Commit and Push Changes:
- Commit changes to the local repository:
  
  `git add .`

  `git commit -m "Description of changes made"`

- Push changes to the remote repository:
  `git push origin <new_branch_name>`

## 4. Create a Pull Request:
- Create a Pull Request from new branch to the main development branch.
- [Watch this](https://youtu.be/8lGpZkjnkt4?si=wWhlt5uIpKkMVsMT)

## 5. Review and Merge:
- Collaborators will review changes in the Pull Request.
- If approved, merge changes into the main branch.
- [Watch this](https://youtu.be/OVQK2zzb6U8?si=5dcqy_z1v0TbbdLS)

## 6. Update Local Repository:
- Switch back to the main branch:
  `git checkout main`

- Pull the latest changes from the remote repository:
  `git pull origin main`

- Delete the local feature branch (optional):
  `git branch -d <new_branch_name>`

- Delete the remote feature branch (if merged and no longer needed):
  `git push origin --delete <new_branch_name>`

