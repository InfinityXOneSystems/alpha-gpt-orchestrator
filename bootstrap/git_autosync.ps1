git status
git add .
git commit -m 'auto-sync: system update' 2>
git pull origin main --rebase
git push origin main
