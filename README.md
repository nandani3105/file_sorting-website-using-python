
# 🗂️ File Sorting Web Application
A Django-based web application that automatically organizes files in a selected folder into categorized directories like Images, Documents, Videos, Audio, Archives, etc. Built with a clean and modern UI, it enhances productivity by saving time spent manually sorting files.

# 🚀 Features
📁 Upload or enter any folder path on your system

🔍 Automatically detects file types based on extensions

🧠 Organizes files into categories:
Images, Documents, Videos, Music, Archives

📊 Displays real-time counts of sorted files

✨ Smooth and responsive UI with animations

📱 Mobile-friendly interface


# 🛠️ Tech Stack
Backend: Django (Python)

Frontend: HTML5, CSS3, JavaScript

Libraries: Font Awesome (Icons), GSAP (optional for animations)


# 📁 file_sorter_project/
├── file_sorter_app/
│   ├── templates/
│   │   └── home.html
│   ├── static/
│   │   ├── style.css (optional)
│   ├── views.py
│   ├── urls.py
├── file_sorter_project/
│   ├── settings.py
│   ├── urls.py
├── manage.py
🧪 How It Works
Enter or browse the folder path using the web UI

Click Start to sort files

The app checks file extensions and moves them into their respective folders

Shows summary: Total files, Images, Audio, etc.

Clean UI with instant feedback and visual updates


# 💡 Setup Instructions

# Install Django
pip install django

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
Then open your browser and go to:
http://127.0.0.1:8000/

📸 Screenshots
  ![image alt](https://github.com/nandani3105/file_sorting-website-using-python/blob/main/image.png)


👨‍💻 Author
Nandani Kumari
