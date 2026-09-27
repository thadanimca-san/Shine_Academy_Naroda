import os
import subprocess

def test_pdfs(directory):
    unreadable_pdfs = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                path = os.path.join(root, file)
                try:
                    result = subprocess.run(['pdftotext', '-q', path, '-'], capture_output=True, text=True, timeout=10)
                    text = result.stdout.strip()
                    if not text or len(text) < 50:
                        unreadable_pdfs.append(path)
                except Exception as e:
                    unreadable_pdfs.append(path)
    return unreadable_pdfs

if __name__ == '__main__':
    unreadable = test_pdfs('/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12')
    print("UNREADABLE_PDFS_START")
    for pdf in unreadable:
        print(pdf)
    print("UNREADABLE_PDFS_END")
