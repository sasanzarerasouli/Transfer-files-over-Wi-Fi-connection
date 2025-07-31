import sys
import os
import socket
import threading
from flask import Flask, request, send_from_directory
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt, QTimer

# Flask App
app = Flask(__name__)
upload_folder = None

# File upload methode
@app.route("/", methods=["GET", "POST"])
def upload_file():
    global upload_folder
    if not upload_folder:
        return "<h3>Folder is not selected</h3>"

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            file.save(os.path.join(upload_folder, file.filename))

    files = os.listdir(upload_folder) if os.path.exists(upload_folder) else []
    file_list_html = "<ul>" + "".join(f"<li>{f}</li>" for f in files) + "</ul>"
    
    #  Html code for uloading page
    return f"""
    <!doctype html>
    <html lang="en">
    <head>
    <title>↑ Upload File</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #eef2f7, #cfd9e6);
        padding: 20px;
        text-align: center;
        }}
        form {{
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        display: inline-block;
        width: 90%;
        max-width: 400px;
        }}
        h2 {{
        color: #2e3a59;
        }}
        input[type="file"] {{
        margin: 15px 0;
        }}
        input[type="submit"] {{
        background-color: #007BFF;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 16px;
        }}
        input[type="submit"]:hover {{
        background-color: #0056b3;
        }}
        progress {{
        width: 90%;
        max-width: 400px;
        height: 20px;
        border-radius: 10px;
        background: #eee;
        margin-top: 10px;
        }}
        #status {{
        font-weight: bold;
        margin-top: 10px;
        color: #333;
        }}
        @media (max-width: 600px) {{
        body {{
            background: linear-gradient(to bottom, #fefefe, #e2ebf3);
        }}
        h2 {{
            font-size: 20px;
        }}
        }}
        footer {{
        margin-top: 40px;
        font-size: 13px;
        color: #777;
        }}
        a {{
        color: #007BFF;
        }}
    </style>
    <script>
        function uploadFile(event) {{
        event.preventDefault();
        var fileInput = document.querySelector('input[name="file"]');
        var file = fileInput.files[0];
        if (!file) return;

        var formData = new FormData();
        formData.append("file", file);

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/", true);

        xhr.upload.onprogress = function(e) {{
            if (e.lengthComputable) {{
            var percent = Math.round((e.loaded / e.total) * 100);
            document.getElementById("progress").value = percent;
            document.getElementById("status").innerText = percent + "% uploaded";
            }}
        }};

        xhr.onload = function() {{
            document.getElementById("status").innerText = "Upload completed";
            setTimeout(() => {{
            window.location.reload();
            }}, 1000);
        }};

        xhr.send(formData);
        }}
    </script>
    </head>
    <body>
    <h2>Transfer files over Wi-Fi connection</h2>
    <form onsubmit="uploadFile(event)">
        <input type="file" name="file" accept="*/*"><br>
        <input type="submit" value="↑ Upload NOW ↑">
    </form>
    <p>&nbsp;</p>
    <progress id="progress" value="0" max="100"></progress>
    <p id="status"></p>
    <hr>
    <h3>Availabe Files in shared FOLDER:</h3>
    {file_list_html}
    <hr>
    <p>Access your downloads via <a href="/browse"><b>browse</b></a></p>
    <footer>Powered by: <b>Sasan Zare</b></footer>
    </body>
    </html>
    """

# File download list methode
@app.route("/browse")
def browse_files():
    global upload_folder
    if not upload_folder or not os.path.exists(upload_folder):
        return "<h3>Folder not found</h3>"

    files = os.listdir(upload_folder)
    links = "".join(f'<li><a href="/download/{f}" style="color:cyan">{f}</a></li>' for f in files)
    
    # Html code for download page
    return f"""
    <!doctype html>
    <html lang="en">
    <head>
    <title>Available Files For Downloads</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #f0f4f8, #dbe4ee);
        padding: 20px;
        text-align: center;
        }}
        h2 {{
        color: #2e3a59;
        margin-bottom: 20px;
        }}
        ul {{
        list-style: none;
        padding: 0;
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: center;
        }}
        li {{
        background: white;
        padding: 12px 16px;
        border-radius: 8px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.1);
        width: 90%;
        max-width: 400px;
        transition: transform 0.2s ease;
        }}
        li:hover {{
        transform: scale(1.02);
        }}
        a {{
        text-decoration: none;
        color: #007BFF;
        font-weight: bold;
        }}
        a:hover {{
        text-decoration: underline;
        }}
        footer {{
        margin-top: 40px;
        font-size: 13px;
        color: #777;
        }}
        @media (max-width: 600px) {{
        h2 {{
            font-size: 20px;
        }}
        li {{
            font-size: 14px;
        }}
        }}
    </style>
    </head>
        <body>
            <h2>Files Ready to Download</h2>
            <p>To download, simply click on the desired file.</p>
            <ul>{links}</ul>
            <p>Access your Uploads via <a href="/"><b>back</b></a></p>

            <p style="margin-top: 40px; font-size: 0.95em; color: #555;">
                You can only download individual files. Folder downloads are not supported.
                To download a folder, please compress it into a ZIP or RAR archive.
            </p>

            <footer>Powered by: <b>Sasan Zare</b></footer>
        </body>
    </html>

    """

# File download methode
@app.route("/download/<filename>")
def download_file(filename):
    global upload_folder
    return send_from_directory(upload_folder, filename, as_attachment=True)

# Start flask sserver
def start_flask():
    app.run(host="0.0.0.0", port=8000)

# Get ip addres
def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "You have not active IP address"

# Main GUI class
class DarkModernApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transfer files over Wi-Fi connection")
        self.setFixedSize(600, 400)
        self.init_ui()
        self.server_running = False

    # UI def
    def init_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #f0f0f0;
                font-family: Segoe UI;
                font-size: 14px;
            }
            QPushButton {
                background-color: #1e88e5;
                border: none;
                padding: 10px;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
            QLabel#statusLabel {
                font-weight: bold;
                color: #00e676;
            }
            QFrame#card {
                background-color: #1f1f1f;
                border-radius: 12px;
                padding: 20px;
            }
        """)

        layout = QVBoxLayout(self)

        # Folder selection
        self.folder_label = QLabel("⨉⨉ Folder not selected, In first time you need to select a folder for sharing files", self)
        self.folder_label.setStyleSheet("color: red; font-weight: bold;")
        layout.addWidget(self.folder_label)

        select_button = QPushButton("Select Folder")
        select_button.clicked.connect(self.choose_folder)
        layout.addWidget(select_button)

        # Server control buttons
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Server")
        self.start_btn.clicked.connect(self.start_server)
        self.stop_btn = QPushButton("Stop Server")
        self.stop_btn.clicked.connect(self.stop_server)
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        layout.addLayout(btn_layout)

        # Status card
        self.status_card = QFrame(self)
        self.status_card.setObjectName("card")
        self.status_layout = QVBoxLayout(self.status_card)
        self.status_label = QLabel("", self)
        self.status_label.setObjectName("statusLabel")
        self.status_label.setWordWrap(True)
        self.status_layout.addWidget(self.status_label)
        layout.addWidget(self.status_card)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Creator information (powered)
        powered = QLabel("Powered by: <b>Sasan Zare<\b>", self)
        powered.setAlignment(Qt.AlignmentFlag.AlignRight)
        powered.setStyleSheet("color: gray; font-size: 9px;")
        layout.addWidget(powered)
        
        # version information
        version = QLabel("<b>VERSION 2.0<\b>", self)
        version.setAlignment(Qt.AlignmentFlag.AlignRight)
        version.setStyleSheet("color: gray; font-size: 8px;")
        layout.addWidget(version)

    # Choose folder 
    def choose_folder(self):
        global upload_folder
        selected = QFileDialog.getExistingDirectory(self, "Select Save Folder")
        if selected:
            upload_folder = selected
            self.folder_label.setText(f"▷Folder: {selected}")
            self.folder_label.setStyleSheet("font: segoe UI; font-size:12; color: lightgreen; font-weight: bold;")

    # Start server def
    def start_server(self):
        if not upload_folder:
            self.status_label.setText("⨉⨉ Please select a folder first.")
            self.status_label.setStyleSheet("color: red")
            return
        if not self.server_running:
            threading.Thread(target=start_flask, daemon=True).start()
            ip = get_ip()
            self.status_label.setText(f"""
            Server running on this Address...
            you can search this address on your own browser:
            ↑ Upload→ {ip}:8000
            ↓ Download→ {ip}:8000/browse
            """)
            self.status_label.setStyleSheet("color: white")
            self.server_running = True

    # Stop server def
    def stop_server(self):
        self.status_label.setText("""
        ■   Server shutdown is currently in progress...
              Thank you for using this application.
              We hope you found it helpful and enjoyable.
              We look forward to having you back again soon.
              The application will close automatically in a moment.
              """)
        
        # After click on stop server, the application close after 5 sec 
        QTimer.singleShot(5000, lambda: (QApplication.quit(), sys.exit(0)))

#  Main def
def main():
    app = QApplication(sys.argv)
    window = DarkModernApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
