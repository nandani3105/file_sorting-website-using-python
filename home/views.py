from django.shortcuts import render
from django.http import JsonResponse
import os
import shutil

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar']
}

def home(request):
    return render(request, 'index.html')

def sort_files(request):
    if request.method == 'POST':
        path = request.POST.get('folder_path')
        if not path or not os.path.exists(path):
            return JsonResponse({'error': 'Invalid folder path'})
        
        file_list = os.listdir(path)
        file_counts = {category: 0 for category in FILE_TYPES.keys()}
        total_files = 0
        
        for file in file_list:
            for category, extensions in FILE_TYPES.items():
                if file.endswith(tuple(extensions)):
                    file_counts[category] += 1
                    total_files += 1
                    break
        
        for category, count in file_counts.items():
            if count > 0:
                folder_path = os.path.join(path, category)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                if category == 'Documents':
                    for ext in FILE_TYPES['Documents']:
                        subfolder_path = os.path.join(folder_path, ext.strip('.'))
                        if not os.path.exists(subfolder_path):
                            os.makedirs(subfolder_path)
                
                for file in file_list:
                    if file.endswith(tuple(FILE_TYPES[category])):
                        src = os.path.join(path, file)
                        
                        if category == 'Documents':
                            for ext in FILE_TYPES['Documents']:
                                if file.endswith(ext):
                                    dst = os.path.join(folder_path, ext.strip('.'), file)
                                    break
                        else:
                            dst = os.path.join(folder_path, file)
                        
                        if not os.path.exists(dst):
                            shutil.move(src, dst)
        
        return JsonResponse({'message': 'Files sorted successfully', 'total_files': total_files, 'file_counts': file_counts})

